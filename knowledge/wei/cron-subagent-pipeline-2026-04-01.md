# 专业研发与代码实现学习：Cron-Subagent 流水线

**刑部尚书 魏征**
**日期：2026-04-01 16:00 CST**
**精准意图：解决"isolated cron agent 如何把结果送回主会话"的核心工程问题**

---

## 一、核心工程问题

三司会审新cron结构依赖"isolated session 完成任务 → 结果送回主会话"：

```
Cron触发 → isolated session → 执行任务 → sessions_send → main session
```

**已知 session key：**
- 狄仁杰主会话：`agent:di:main`（sessionId: `35e83073-383d-45d3-b49c-1d16b1093448`）
- 魏征主会话：`agent:wei:main`
- 当前cron自身：正在运行中

**关键技术点：**
1. 如何在 isolated session 中获取主会话 key？
2. 如何构造 `sessions_send` 的 message？
3. 如何让 cron job 把主 session key 传递给 subagent？

---

## 二、sessions_send 工具分析

### 工具签名
```typescript
sessions_send({
  sessionKey?: string;   // 目标 session key
  label?: string;        // 按 label 查找
  agentId?: string;      // ACP agent id
  message: string;       // 发送的消息内容
  timeoutSeconds?: number;
})
```

### 三种寻址方式
| 方式 | 示例 | 适用场景 |
|------|------|----------|
| `sessionKey` | `"agent:di:main"` | 精确目标 |
| `label` | `"main"` | 按标签查找 |
| `agentId` | `"di"` | ACP agent |

**最可靠方式：使用 `sessionKey`**（精确，不会误匹配）

### message 内容格式
消息会被注入到目标会话，作为一条新的 user message。

```
格式：结构化文本（Markdown 友好）
建议内容：
- 任务来源
- 核心发现/结果
- 原始数据
```

---

## 三、CRON JOB 设计模式

### 模式A：Cron 直接发消息（最简）

```javascript
// cron job 的 agentTurn message
`
执行任务：[精准意图描述]

任务完成后，用 sessions_send 工具发送结果：
- sessionKey: agent:di:main
- message: 格式化的任务结果

结果格式要求：
1. 标题：## 【Cron汇报】任务名
2. 核心发现（3条以内）
3. 代码片段（如有）
4. 下一步建议
`
```

**优点：** 简单，cron job 直接负责
**缺点：** cron session 本身会记录结果，可能冗余

### 模式B：Cron 派生子 Agent（推荐）

```javascript
// cron job 派生的 isolated subagent
{
  task: "执行 [精准意图]，完成后用 sessions_send 发送给 agent:di:main",
  runtime: "subagent",
  sessionTarget: "isolated",     // 隔离，不污染主会话历史
  runTimeoutSeconds: 300,        // 5分钟超时
  cleanup: "delete"              // 执行完删除
}
```

**子 agent 的消息构造：**
```
请执行以下任务：

【研究主题】：今天研究 [具体问题]
【执行要求】：
1. 研究并整理核心发现
2. 将结果通过 sessions_send 发送给 agent:di:main

sessions_send 参数：
- sessionKey: agent:di:main
- message: 你的完整研究报告，格式如下：
  ## 【魏征汇报】[主题]
  
  ### 核心发现
  - [发现1]
  - [发现2]
  
  ### 代码示例
  \`\`\`[语言]
  [代码]
  \`\`\`
  
  ### 应用场景
  [说明如何使用]
  
  ### 72小时复盘
  - 我实际用在了：____

完成后请确认已发送。
```

### 模式C：Context Message 传参（最安全）

把主 session key 作为 context message 传入，确保派生的 subagent 知道往哪发：

```javascript
cron.add({
  name: "Cron→Subagent→Main",
  schedule: { kind: "cron", expr: "0 16 * * *" },  // 每天16:00
  payload: {
    kind: "agentTurn",
    message: "执行任务...通过 sessions_send 发送到你的父会话"
  },
  delivery: { mode: "announce" },  // 完成后 announc
  sessionTarget: "isolated"
})
```

---

## 四、实测代码 Demo

### Demo 1：直接发送报告（立即可用）

以下是一个 cron job 的完整 message 模板，用于直接发送研究报告：

```markdown
## 【魏征·16:00学习汇报】OpenClaw Subagent Pipeline 工程实现

### 精准意图
研究 Cron → Isolated Subagent → sessions_send → Main Session 的完整数据流

### 核心发现

**sessions_send 三种寻址（按可靠性排序）：**
1. `sessionKey: "agent:di:main"` — 精确 key，最可靠
2. `label: "main"` — 按标签，需确保唯一
3. `agentId: "di"` — ACP agent 寻址

**subagent 生命周期管理：**
- `cleanup: "delete"` — 执行完立即删除，不污染会话列表
- `runTimeoutSeconds` — 必须设，防止僵尸 agent
- `sessionTarget: "isolated"` — 与主会话隔离

**message 构造规范：**
- 结构化 Markdown
- 包含：标题/发现/代码/应用场景/72小时复盘位
- 代码块注明语言，便于渲染

### 完整 Cron → Subagent 代码模板

\`\`\`javascript
// === 1. Cron Job 定义 ===
await cron.add({
  name: "魏征-每日技术研究",
  schedule: { kind: "cron", expr: "0 16 * * *" },  // 每天16:00
  payload: {
    kind: "agentTurn",
    message: `
请研究：[今日课题]

研究完成后，使用 sessions_send 发送报告：
- sessionKey: agent:di:main
- message: ## 【魏征汇报】[课题]

格式要求：
1. 核心发现（3条）
2. 代码示例
3. 应用场景
4. 72小时复盘位（留空）

完成后回复"报告已发送"。
    `
  },
  delivery: { mode: "announce" },
  sessionTarget: "isolated"
});

// === 2. 发送报告（subagent 内部） ===
await sessions_send({
  sessionKey: "agent:di:main",
  message: \`
## 【魏征汇报】[课题]

### 核心发现
- [发现1]
- [发现2]

### 代码示例
\\\`\\\`\\\`javascript
// 示例代码
\\\`\\\`\\\`

### 应用场景
[如何应用]

### 72小时复盘
- 我实际用在了：____
  \`
});
\`\`\`

### Demo 2：父子会话 Key 传递（生产级）

```javascript
// 父 cron job（发送任务给 subagent）
await sessions_spawn({
  task: \`
你是一个专门的研究 agent。

【今日课题】：${topic}
【执行要求】：
1. 用 web_search 收集相关资料
2. 整理核心发现（最多3条）
3. 提供代码示例
4. 通过 sessions_send 发送报告给 agent:di:main

sessions_send 参数：
{
  "sessionKey": "agent:di:main",
  "message": \`## 【魏征研究汇报】\${topic}

### 核心发现
- ...

### 代码示例
\\\`\\\`\\\`
// ...
\\\`\\\`\\\`

### 应用场景
...

### 72小时复盘
- 我实际用在了：____
  \`
}

完成后回复"done"。
  \`,
  runtime: "subagent",
  sessionTarget: "isolated",
  runTimeoutSeconds: 300,
  cleanup: "delete",
  label: "wei-daily-research"
});
```

---

## 五、sessions_list 获取 Session Key

如果不知道目标 session key，可用 `sessions_list` 查询：

```javascript
// 列出最近活跃的会话
sessions_list({
  kinds: ["other", "agent"],  // cron/agent 类型
  limit: 10,
  messageLimit: 1             // 每会话显示最近1条
})
// 返回：session key + label + 最后消息摘要
```

**返回字段解析：**
```javascript
{
  "key": "agent:di:main",       // 用于 sessions_send
  "label": "Cron: 魏征学习",     // 会话标签
  "sessionId": "uuid",           // 原始 session ID
  "status": "running|done|failed",
  "updatedAt": 1775030403302    // 最后活跃时间戳
}
```

---

## 六、关键坑点与解决方案

| 坑点 | 原因 | 解决方案 |
|------|------|----------|
| sessions_send 发错会话 | sessionKey 写错 | 始终用 `agent:di:main` 精确值 |
| subagent 没有发消息 | message 格式问题 | message 必须是字符串，不是对象 |
| cron 重复派生子 agent | 未设 cleanup | 必须设置 `cleanup: "delete"` |
| 超时后仍在运行 | 未设 runTimeoutSeconds | 建议 300s（5分钟） |
| 消息中文乱码 | JSON 字符串转义问题 | 使用模板字符串，避免多层转义 |
| 父会话收到空消息 | message 为空对象 | 确保 message 是非空字符串 |

---

## 七、72小时复盘（到期后填写）

- **我实际用在了**：____

---

## 八、相关文件

- `workflow-automation-2026-04-01.md` — 平台对比（n8n/Temporal/Windmill）
- `session-isolation-design.md` — Session 隔离设计
- `tool-integration-learning-2026-03-31.md` — Composio/Zapier
- `cloud-async-learning-2026-03-31.md` — Vercel AI SDK/Modal

---

*本报告由魏征（刑部尚书）整理*
*学习时间：2026-04-01 16:00 CST*
*产出类型：demo型（代码模板 + 说明）*
