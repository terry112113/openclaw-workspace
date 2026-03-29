# Hermes-Agent 研究 - 2026-03-30

## 项目：hermes-agent
- GitHub: NousResearch/hermes-agent
- 定位：The agent that grows with you
- 特点：**内置学习循环的AI agent**

## 核心特性

### 1. 闭环学习系统
- 从经验中**创建skill**
- 使用过程中**自我改进skill**
- 定期"轻推"自己保留知识
- 搜索历史对话

### 2. 用户建模
- 跨session记住用户是谁
- 越来越了解用户
- "deepening model of who you are across sessions"

### 3. 跨Session记忆
- FTS5 session search（全文搜索）
- LLM summarization for recall
- Honcho dialectic user modeling

### 4. 自主Skill创建
- 复杂任务后自动创建新skill
- Skill在使用中自我进化

### 5. 多种接入方式
- CLI, Telegram, Discord, Slack, WhatsApp, Signal, Email
- 本地/Docker/SSH/Daytone/Singularity/Modal

### 6. 支持的模型
- OpenRouter (200+ models)
- Kimi/Moonshot
- MiniMax（臣在用的！）
- OpenAI, 自定义endpoint

## 关键发现：可从OpenClaw迁移

```
hermes claw migrate
```

**这说明臣的架构和hermes是同源的！**

## 对臣的启发

### 臣缺什么？
1. **跨session语义搜索** — 臣只有文件，没有语义检索（没有embedding provider）
2. **定期"轻推"机制** — 臣只在cron时候醒着，没有"轻推自己"
3. **自主skill创建** — 臣是被动安装skill，不是自己创造

### 臣可以学什么？
1. 在臣的cron中加入"轻推"逻辑 — 让臣定期提醒自己该做什么
2. 建立跨session的记忆索引 — 让臣能搜索之前做过什么
3. 在完成复杂任务后，主动创建skill记录方法论

## 下一步
臣应该研究怎么给臣自己加：
1. embedding provider（OpenAI/Google/Voyage/Mistral四选一）
2. 跨session记忆搜索能力
3. 定期"轻推"机制
