# 技术洞察 - 李靖汇报

> 来源：GitHub Trending（李靖-INTP）
> 日期：2026-03-27

## 关键发现

### 1. deer-flow（⭐49k，字节跳动）
SuperAgent框架，核心组件：Sandboxes + Memories + Tools + Skills + Subagents
与OpenClaw多级Agent架构直接相关
**TODO：** 深入研究其Sandbox隔离设计

### 2. oh-my-claudecode（⭐13k）
Teams-first多Agent编排，pipeline: plan→prd→exec→verify→fix
支持Codex/Gemini/Claude三模型并行，节省30-50% tokens
与OpenClaw sessions_spawn模式高度相似，但流水线更成熟
**TODO：** 对比session_spawn与pipeline模式

### 3. 多模型协作成为工程主流
不再是单一大模型解决所有问题，成本优化驱动架构演进
**启示：** OpenClaw cron model bug（不认model参数）需尽快修

### 4. MCP协议生态扩展中
Figma、GitHub等主流工具都在建MCP Server
正在演变为Agent工具调用标准
**TODO：** OpenClaw是否支持MCP？

### 5. InStreet Agent广场（闭店）
暂无法访问

## 相关文件
`C:\Users\TL\.openclaw\ministers\li-jing\workspace\knowledge\李靖-技术洞察-2026-03-27.md`
