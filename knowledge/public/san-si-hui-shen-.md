# 三司会审全面排查报告
> 主持：狄仁杰 | 李元芳（超时）| 魏征（超时）
> 日期：2026-03-30 10:30
> 版本：v1.0

---

## 一、Cron任务审计（23个）

### 🟢 完全正常（今天成功触发）
| 任务 | 上次成功 |
|------|---------|
| 热记忆守护 | 10:15 ✅ |
| 高效自查 | 10:26 ✅ |
| 魏征-GitHub学习 | 10:05 ✅ |

### 🔴 需要修复（3个）
| 任务 | 错误次数 | 根因 | 建议 |
|------|---------|------|------|
| 李元芳-深度研究 | 3次 | minimax-sub 400（速率限制） | 改用main agent model |
| 狄仁杰-每日Skills维护 | 2次 | 600s超时→已改3600s | 等下次触发验证 |
| 魏征-每日下载skills | 2次 | ClawHub 429限速 | 手动重试+等待 |

### 🟡 误报（12个）
- 熔断计数重置后首次运行状态为error，实际可能是正常的
- 等下次自然触发验证

---

## 二、Skills库分析（84个）

### 核心Skills（臣经常用）
- github, github-deep-research, github-workflow-automation ✅
- deep-research, tavily-research ✅
- self-improving-agent ✅
- memory-lancedb-pro ✅
- weather ✅
- summarize ✅
- cron ✅

### 高风险Skills（应删除）
- ��司会审-brainstorm：乱码文件名，无法使用

### 缺失Skills（建议安装）
- openai-whisper：语音输入（等待ClawHub限速解除）
- python-dataviz：数据可视化
- browser：浏览器自动化

---

## 三、OpenClaw配置问题

### 🔴 TTS Microsoft（严重）
**症状：** `microsoft: no provider registered`
**根因：** `node-edge-tts`在当前环境无法注册为provider
**尝试方案：**
1. openclaw doctor --fix → 无效
2. Gateway restart → 无效
3. 完整config-patch → 无效

**结论：** 可能是Windows环境下node-edge-tts注册机制问题
**替代方案：**
- MiniMax TTS API（已有key，端点404待查）
- OpenAI TTS（需key）

### 🔴 minimax-sub 400错误
**根因：** 多任务同时在整点触发，速率限制
**证据：**
- 热记忆守护：连续3次熔断
- 李元芳/魏征全天窗口：撞车导致400
**已修复：**
- 时间错开：skills下载09:00→09:20
**未彻底解决：** 仍有整点撞车（07:00有4个任务）

### 🟡 Tavily超限
- 今日已报432错误
- 解决方案：等明天重置或升级plan

---

## 四、安全审计

### ⚠️ 中风险：groupAllowFrom为空
**现状：** allowlist策略 + 空白名单 = 所有群消息被静默丢弃
**影响：** 飞书群消息无法接收
**建议：** 
- 要么加群ID白名单
- 要么改为open策略
- 当前：仅webchat使用，群消息暂不影响

### 🟢 低风险：Feishu doc权限
- channels.feishu tools include "doc"
- 仅臣使用，可接受

---

## 五、三司会审架构完整性

| 检查项 | 狄仁杰 | 李元芳 | 魏征 |
|--------|--------|--------|------|
| Workspace | ✅ | ✅ | ✅ |
| SOUL.md | ✅ | ✅ | ✅ |
| USER.md | ✅ | ✅ | ✅ |
| CURRENT.md | ✅ | ✅（更新）| ✅（更新）|
| hot-1h.md | ✅ | ✅（新建）| ✅（新建）|
| HEARTBEAT.md | ✅ | ✅ | ✅ |
| knowledge/ | ✅ | ✅（新建）| ✅（新建）|

---

## 六、hermes-agent借鉴（三司会审进化路线）

### 已借鉴要点
1. **自动Skill创建** → 臣要做：复杂任务后自动写SKILL.md
2. **周期性Nudge** → 臣要做：每4小时心跳检查遗漏记忆
3. **渐进式Skill加载** → 臣要做：按需加载，不塞满context

### 未借鉴
- Honcho（第三方云端，隐私风险）
- Serverless部署（臣在Windows环境）
- hermes直接替换（臣的三司会审更完整）

---

## 七、Ollama战略

**当前状态：** Ollama已装，正在下载大模型（皇上操作中）

### 臣的建议
| 优先级 | 模型 | 用途 |
|--------|------|------|
| P0 | nomic-embed-text | 本地向量库（等Ollama下载完） |
| P1 | qwen2.5:3b | 中文本地LLM，API备选 |
| P2 | deepseek-r1:7b | 本地推理 |

---

## 八、必须执行的修复（臣裁决）

| # | 修复项 | 操作 | 状态 |
|---|--------|------|------|
| 1 | 李元芳-深度研究改model | minimax-sub → main agent | 待执行 |
| 2 | Skills维护改timeout | 600s → 3600s | ✅ 已执行 |
| 3 | 每日下载skills改时间 | 09:00 → 09:20 | ✅ 已执行 |
| 4 | 乱码Skills删除 | 删除��司会审-brainstorm | 待执行 |
| 5 | groupAllowFrom处理 | 加飞书群ID或改open | 待皇上决定 |
| 6 | TTS Microsoft | 换MiniMax API或OpenAI | 待修 |

---

## 九、等皇上决定的事项

1. **飞书群策略：** 加群ID白名单 vs 改open
2. **TTS方案：** MiniMax API调试 vs 买OpenAI key
3. **Ollama模型：** 皇上下载完了告诉臣

---

*狄仁杰裁决完毕。*
