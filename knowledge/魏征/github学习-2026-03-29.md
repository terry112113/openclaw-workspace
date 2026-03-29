# GitHub 学习记录 - 2026-03-29

## 发现的热门项目

| 项目名 | 语言 | 用途 | 价值评级 |
|--------|------|------|----------|
| hermes-agent | Python | NousResearch自改进AI Agent，内置学习循环、自动创建技能、跨会话记忆 | ⭐⭐⭐⭐⭐ |
| awesome-openclaw-skills | - | OpenClaw技能合集，5400+技能过滤分类 | ⭐⭐⭐⭐⭐ |
| learn-claude-code | TypeScript | 从零构建类Claude Code的Agent Harness | ⭐⭐⭐⭐ |
| oh-my-claudecode | TypeScript | 团队优先的多Agent编排框架 for Claude Code | ⭐⭐⭐⭐ |
| last30days-skill | Python | AI Agent技能：跨Reddit/X/YouTube/HN/Polymarket研究话题 | ⭐⭐⭐⭐ |
| claude-mem | TypeScript | Claude Code插件，自动捕获会话压缩记忆注入未来上下文 | ⭐⭐⭐⭐ |
| deer-flow | Python | 长视野SuperAgent Harness，研究+代码+创建，内置沙箱记忆工具技能 | ⭐⭐⭐⭐ |
| OpenViking | Python | 面向AI Agent的开源上下文数据库（支持OpenClaw） | ⭐⭐⭐⭐ |
| memU | Python | 24/7主动Agent记忆系统（支持OpenClaw moltbot/clawdbot） | ⭐⭐⭐ |
| obra/superpowers | - | Agent技能框架+软件开发方法论 | ⭐⭐⭐ |
| claude-howto | Python | Claude Code视觉化指南，模板化即学即用 | ⭐⭐⭐ |

## 重点关注

**最重磅发现：hermes-agent（NousResearch）**
- 与OpenClaw高度竞争但有迁移路径（`hermes claw migrate`）
- 核心亮点：内置学习循环 + 自动创建技能 + MCP兼容 + 支持MiniMax
- 亮点设计：跨平台消息（Telegram/Discord/Slack/WhatsApp）、多终端后端
- 关键借鉴：它的"技能自改进"机制可作为魏征每日学习系统的参考架构

**OpenViking（字节Volcengine）**
- 专为此类平台设计的上下文数据库
- 统一管理AI Agent的记忆、工具、技能
- 与OpenClaw原生兼容，值得深入研究

**last30days-skill**
- 多源聚合研究技能（Reddit/X/YouTube/HN等）
- 可考虑移植为魏征的情报收集技能

## 明日计划

- 深入研究 hermes-agent 的技能自改进机制
- 评估 deer-flow 作为下一代研究Agent的可行性
- 调研 OpenViking 作为记忆存储层的方案
