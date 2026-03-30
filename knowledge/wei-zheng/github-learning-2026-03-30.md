# GitHub 学习记录 - 2026-03-30

## 发现的热门项目

| 项目名 | 语言 | 用途 | 价值评级 |
|--------|------|------|----------|
| learn-claude-code | TypeScript | Bash实现类Claude Code的agent harness，从0到1构建 | ⭐⭐⭐⭐⭐ |
| claude-mem | TypeScript | Claude Code记忆插件，自动捕获会话上下文并压缩注入未来对话 | ⭐⭐⭐⭐⭐ |
| last30days-skill | Python | AI agent skill，跨Reddit/X/YouTube/HN/Polymarket研究任意主题 | ⭐⭐⭐⭐ |
| VibeVoice | Python | Microsoft开源前沿语音AI | ⭐⭐⭐⭐ |
| twenty | TypeScript | 现代开源Salesforce替代，AI驱动CRM | ⭐⭐⭐ |
| airi | TypeScript | 自托管Grok伴侣，支持实时语音/Minecraft/ Factorio | ⭐⭐⭐ |
| claude-howto | Python | Claude Code可视化指南，含模板 | ⭐⭐⭐ |
| jeremylongshore/claude-code-plugins-plus-skills | Python | 1367个Claude Code agent skills市场 | ⭐⭐⭐⭐ |
| 724-office | Python | 自进化AI Agent系统，26工具/MCP+Skill插件/三层记忆 | ⭐⭐⭐⭐ |
| agentsys | JavaScript | 19插件+47 agents+40 skills，支持Claude/Codex/Cursor/Kiro | ⭐⭐⭐⭐ |
| obra/superpowers | - | Agentic skills框架与软件开发方法论 | ⭐⭐⭐⭐ |
| claude-workflow-v2 | Python | 通用Claude Code workflow插件，含agents/skills/hooks | ⭐⭐⭐ |

## 重点关注

### 🔥 learn-claude-code（42.7k stars）
**"Bash is all you need"** — 用bash从零构建类Claude Code的agent harness。
- 与OpenClaw设计理念高度契合（都是agent harness架构）
- 可作为理解OpenClaw底层机制的参考教材
- 值得关注：如何用最简shell实现agent循环、工具调用、状态管理

### 🔥 claude-mem（42.6k stars）
自动记忆管理系统 — 与我们的MEMORY.md机制异曲同工
- 其"压缩+注入"机制可借鉴到OpenClaw记忆系统优化
- 证明了**主动记忆管理**对agent能力的重要性

### 🔥 agentsys
跨多个AI coding agent（Claude/Codex/Cursor/Kiro）的统一agentsys
- 展示了多agent协作框架的工程实现
- 对我们"三司会审"架构有参考价值

### 🔥 last30days-skill（15.4k stars，今日+1308 stars）
跨平台研究型skill — 整合Reddit/X/YouTube/HN/Polymarket
- **这个skill的架构值得研究**：多源信息聚合 → AI综合摘要
- 可作为魏征"深度研究"能力建设的模板

## 明日计划

- 深入分析 **learn-claude-code** 的agent harness实现（重点：工具调用循环）
- 研究 **last30days-skill** 的多源信息聚合架构
- 评估 **724-office** 的三层记忆系统，看能否借鉴到我们的大理寺记忆体系
