# 飞书同步方案研究报告
**调研人：李元芳（都察院御史）**
**日期：2026-03-29**
**密级：内部研究**

---

## 一、现有架构分析

### 1.1 OpenClaw Session 机制

经过实地勘查，当前 OpenClaw 的 session 架构如下：

**Session Key 命名规则：**
```
agent:<agentId>:<channel>:<peer-kind>:<peer-id>
```

**当前系统中的关键 Session：**

| Session Key | 类型 | 说明 |
|---|---|---|
| `agent:di:main` | direct | 狄仁杰 webchat 主会话（当前主 session） |
| `agent:di:feishu:group:oc_8365b711161460f315a825dcd8c3fe37` | group | 狄仁杰所在的飞书群 |
| `agent:shensi:feishu:group:oc_ee79942352d38d8320ced1db0fc207c7` | group | 李元芳所在的飞书群 |
| `agent:wei:feishu:group:oc_715234420dd4fceb5acc726708e358f5` | group | 魏征所在的飞书群 |
| `agent:shensi:main` | direct | 李元芳主会话 |

**核心发现：**
- 同一个 Agent（`di`/狄仁杰）可以持有**多个 session**，按 channel + peer 隔离
- Webchat 和飞书是**不同的 channel**，各自有独立的 session
- Session 之间**共享同一套 workspace 文件**（`C:\Users\TL\.openclaw\workspace-main`）
- Session 之间**不共享内存**，但共享文件系统

### 1.2 飞书接入方式

当前配置（`openclaw.json`）：
```json
"channels": {
  "feishu": {
    "enabled": true,
    "connectionMode": "websocket",
    "defaultAccount": "di",
    "accounts": {
      "di": { "appId": "cli_a94cc0b181f85bca", ... },
      "shensi": { "appId": "cli_a94cc062ef78dbce", ... },
      "wei": { "appId": "cli_a94cc0c3b3389bd9", ... }
    }
  }
}
```

飞书采用 **WebSocket 长连接**模式接收事件，无需公网 Webhook URL。

**消息路由流程：**
```
飞书消息 → OpenClaw Gateway → 根据 binding 规则匹配 agentId
         → 查找/创建对应 session key → 分发给对应 agent 处理
```

### 1.3 跨 Session 通信机制

OpenClaw 内置了 **Session Tools**（会话工具），包含：

| 工具 | 功能 |
|---|---|
| `sessions_list` | 列出所有可见 session |
| `sessions_history` | 获取某 session 的历史记录 |
| `sessions_send` | 向指定 session 发送消息 |
| `sessions_spawn` | 启动子 agent 会话 |

**`sessions_send` 是跨 session 通信的核心：**
```json
{
  "sessionKey": "agent:di:feishu:group:oc_xxx",  // 目标 session
  "message": "三司会审结果：...",
  "timeoutSeconds": 30  // 等待回复，超时则 fire-and-forget
}
```

**安全策略：** `session.sendPolicy` 可限制跨 channel 发送权限。

---

## 二、可行性方案评估

### 方案A：Session 直接广播（`sessions_send`）

**原理：** 在 webchat 狄仁杰（`agent:di:main`）处理三司会审时，调用 `sessions_send` 向飞书群 session 推送摘要。

**操作步骤：**
1. 在 webchat 狄仁杰的输出末端，自动调用 `sessions_send`
2. 目标 session key：`agent:di:feishu:group:oc_8365b711161460f315a825dcd8c3fe37`
3. 消息内容：三司会审的结论摘要
4. 可设置 `timeoutSeconds=0`（fire-and-forget，不阻塞主流程）

**技术可行性：✅ 可行**
- 同一 agent（`di`）下的 session 之间用 `sessions_send` 完全支持
- Webchat 和飞书都在 `di` agent 下，天然满足"同一 agent"条件
- 飞书群 session key 可从 `sessions_list` 获取或硬编码

**优点：**
- 实现最简单，无需额外基础设施
- 延迟最低（Gateway 内部 RPC）
- 支持双向对话（通过 ping-pong 机制）

**缺点：**
- 需要在每次三司会审结束时触发，有一定耦合
- 飞书端看到的是"摘要"，不是完整对话流

**实现代码示意：**
```
使用 sessions_send 工具：
  sessionKey: "agent:di:feishu:group:oc_8365b711161460f315a825dcd8c3fe37"
  message: "【三司会审摘要】\n议题：...\n李元芳意见：...\n宋慈意见：...\n狄仁杰裁决：..."
  timeoutSeconds: 0
```

---

### 方案B：共享知识库（文件系统）

**原理：** 三司会审的所有内容写入共享知识库文件，飞书狄仁杰通过定时读取或主动触发获取更新。

**操作步骤：**
1. 在 workspace 中创建 `knowledge/三司会审-当前议题.md`
2. 三司会审开始时，狄仁杰更新该文件
3. 飞书狄仁杰通过读取该文件获取上下文

**技术可行性：✅ 可行**
- 两个 session 共享同一个 workspace 文件系统
- 缺点：无法实时感知更新（需要轮询或显式触发）

**优点：**
- 实现简单
- 飞书端可主动读取完整上下文

**缺点：**
- 实时性差（依赖轮询或显式触发）
- 文件内容膨胀后需要管理

---

### 方案C：消息转发（`message` 工具 + 飞书 API）

**原理：** 通过 OpenClaw 的 `message send` 命令向飞书群/频道发送消息。

**技术可行性：⚠️ 有条件**
- `message send` 是向**外部 channel** 发送消息，不是向内部 session 发消息
- 需要知道飞书群 ID 或 DM 用户 ID
- 飞书需要配置好 bot 并有发消息权限

**关键问题：** `message` 工具发送到飞书，是走**飞书开放 API**，不是直接写 Gateway session。飞书群里的"狄仁杰"收到消息后，是否会创建新的 session 取决于 binding 规则。

**如果 binding 规则匹配：**
- 消息 → Gateway → 匹配 `di` agent → 创建/复用飞书群 session → `di` agent 处理
- 这样会形成**循环**：webchat 狄仁杰发消息 → 飞书狄仁杰收到 → 飞书狄仁杰处理 → 如果又调用 sessions_send → 回到 webchat

**结论：** 不推荐，容易形成循环。

---

### 方案D：API 打通（Gateway RPC + sessions_send）

**原理：** 通过 Gateway 的 WebSocket RPC 直接调用 `sessions_send`，绕过 agent 自身。

**技术可行性：✅ 最可靠**
- Gateway RPC `sessions.send` 可从任何地方调用
- 不依赖 agent 自身是否加载了 sessions 工具
- 可精确控制目标 session

**实现方式：**
```bash
openclaw gateway call sessions.send \
  --params '{"sessionKey":"agent:di:feishu:group:oc_8365b711161460f315a825dcd8c3fe37","message":"...","timeoutSeconds":0}'
```

**优点：**
- 最精确，最可控
- 不依赖 agent 模型能力
- 可通过 cron job 定期同步

**缺点：**
- 需要获取正确的 session key
- 飞书 session key 可能随群消息而重建（但对于固定群组应该稳定）

---

## 三、技术门槛评估

### 综合对比

| 维度 | 方案A sessions_send | 方案B 共享文件 | 方案C message工具 | 方案D Gateway RPC |
|---|---|---|---|---|
| **实现难度** | ⭐ 简单 | ⭐⭐ 最简单 | ⭐⭐⭐ 复杂 | ⭐⭐ 中等 |
| **实时性** | ✅ 准实时 | ❌ 轮询/触发 | ✅ 实时 | ✅ 准实时 |
| **可靠性** | ✅ 高 | ✅ 高 | ⚠️ 循环风险 | ✅ 高 |
| **精确控制** | ✅ | ❌ | ⚠️ | ✅ |
| **需额外基础设施** | 无 | 无 | 飞书权限 | 无 |
| **循环风险** | 无 | 无 | ⚠️ 高 | 无 |

### 推荐结论

**首选方案：方案A（`sessions_send`）+ 方案D（Gateway RPC）结合**

具体策略：
1. **三司会审进行中：** webchat 狄仁杰在每个重要节点调用 `sessions_send` 向飞书群推送摘要（fire-and-forget，`timeoutSeconds=0`）
2. **三司会审结束时：** 狄仁杰生成完整结论，通过 `sessions_send` 推送最终结果
3. **作为备用：** 通过 cron job 定期同步 workspace 中的知识库文件到飞书 session

**最简实现路径：**
在 AGENTS.md 或 SOUL.md 中为"狄仁杰"添加一条"三司会审后置动作"：每次三司会审产出结论后，自动调用 `sessions_send` 广播到所有绑定飞书群。

---

## 四、关键风险与注意事项

1. **Session Key 的稳定性**
   - 飞书群的 session key 格式为 `agent:di:feishu:group:<group_id>`
   - `<group_id>` 是飞书群的 `open_id`，通常稳定
   - 但如果群被删除重建，session key 会变化

2. **Send Policy 限制**
   - 检查 `openclaw.json` 中是否有 `session.sendPolicy` 限制跨 channel 发送
   - 当前配置中未看到限制，但部署时需确认

3. **循环消息风险**
   - 如果飞书狄仁杰收到同步消息后，又调用 `sessions_send` 回 webchat，可能形成循环
   - 解决：在消息中加标记（如 `[同步消息]` 前缀），收到时跳过再次广播

4. **飞书账号隔离**
   - 当前有三个飞书账号（di/shensi/wei），分别对应不同群组
   - 同步时需确认目标群是否属于 `di` 账号能访问的范围

---

## 五、具体实施建议

### 第一步：验证 sessions_send 可用性
在当前 webchat 会话中，让狄仁杰调用 `sessions_list` 工具，验证能看到飞书群 session。

### 第二步：确定目标 Session Key
从 `sessions_list` 输出中找到飞书群的完整 key，格式如：
```
agent:di:feishu:group:oc_8365b711161460f315a825dcd8c3fe37
```

### 第三步：添加同步指令
在三司会审流程中，当狄仁杰宣布"三司会审结论"时，自动执行：
```
sessions_send(
  sessionKey="agent:di:feishu:group:oc_8365b711161460f315a825dcd8c3fe37",
  message="【三司会审实时同步】\n...",
  timeoutSeconds=0
)
```

### 第四步：防循环处理
在飞书端的处理逻辑中加入判断：如果消息带有 `[同步消息]` 前缀，则不再次广播。

---

## 六、附录：当前系统 session 一览

```
agent:di:main                    → 狄仁杰 webchat 主会话
agent:di:feishu:group:oc_8365b711161460f315a825dcd8c3fe37 → 狄仁杰飞书群
agent:di:feishu:group:oc_ee79942352d38d8320ced1db0fc207c7 → 李元芳飞书群
agent:di:feishu:group:oc_715234420dd4fceb5acc726708e358f5 → 魏征飞书群
agent:shensi:main               → 李元芳主会话
```

**关键洞察：飞书中的"狄仁杰"（`agent:di:feishu:group:oc_8365b711161460f315a825dcd8c3fe37`）和 webchat 中的"狄仁杰"（`agent:di:main`）是同一个 agent `di` 下的两个不同 session！它们之间可以用 `sessions_send` 直接通信。**

---

*调研完成。李元芳，INTJ建筑师型，都察院御史，汇报完毕。*
