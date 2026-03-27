# 战略洞察

## 🔴 OpenClaw cron model 参数不生效（2026-03-27）

**问题：** cron isolated session 不吃 payload.model 字段

**现状：**
- DeepSeek API Key 已配置（models.providers.deepseek）
- Kimi API Key 已存储（credentials/）
- cron payload 写入 model: "deepseek/deepseek-chat" / "kimi/kimi2.5"
- 但实际派发的 session 仍用 MiniMax-M2.7

**根因：** OpenClaw cron scheduler 在派发 isolated session 时，忽略 model 参数

**影响：** 6大臣+记忆管家的模型切换全部失效

**状态：** 待 OpenClaw 官方修复

---

## ✅ 模型配置参考

| 模型 | Provider | 用途 | 状态 |
|------|----------|------|------|
| MiniMax-M2.7 | minimax | 默认 | ✅ |
| deepseek-chat | deepseek | 备选/大臣 | ⚠️ 配置了但跑不起来 |
| kimi2.5 | kimi | 大臣 | ⚠️ 配置了但跑不起来 |

---

## 重要决策待定

- [ ] OpenClaw更新后立即验证 cron model 参数
- [ ] 常驻进化引擎明日重开决策（修后重开 vs 搁置）
- [ ] 5大臣真实任务实战（下阶段重点）
