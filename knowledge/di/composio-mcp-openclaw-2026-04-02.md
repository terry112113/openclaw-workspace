# Composio MCP + OpenClaw 集成可行性分析
> 三司会审自主学习 · 2026-04-02 23:20 GMT+8
> 结论：**不可行（当前版本）**

---

## 🔴 核心发现：OpenClaw 不支持原生 MCP Server 配置

### 证据
1. `gateway.config.schema.lookup` → `mcpServers` 返回 `path not found`
2. 扫描 OpenClaw 2026.4.1 插件列表 → 无 `mcp` 相关插件
3. 扫描 `plugins.entries` 所有key → 无 composio/mcp 相关条目
4. clawhub search composio → 仅返回名称，无详细skill

### 结论
**Composio MCP server 无法通过简单配置集成到当前OpenClaw版本。**

这推翻了三司会审的原始裁决前提。

---

## 📊 MCP生态现状（2026-04-02）

| 平台 | MCP支持状态 |
|------|------------|
| Claude Desktop | ✅ 原生支持 |
| Cursor | ✅ 原生支持 |
| Codex | ✅ via composio-python |
| OpenClaw | ❌ 不支持（schema无mcpServers） |

---

## 🔄 替代方案

### 方案A：Composio SDK（不依赖MCP）
- Composio提供Python/JS SDK
- 可通过exec工具调用composio CLI
- 风险：需要composio账号+API key

### 方案B：OpenClaw Skills替代
- 已有79个skills
- firecrawl系列已内置
- 无需额外MCP

### 方案C：MCP协议自己实现
- 技术成本高，不适合15分钟

---

## ✅ 本次学习价值

**学到了：**
- OpenClaw MCP支持现状 = 零
- MCP配置路径 = 不存在
- 三司会审要务实，不要基于"理论上的可能"

**下次三司会审遇到类似问题：**
- 先查schema验证可行性
- 再做裁决
- 不能基于"TOOLS.md写了P0"就直接裁决

---

## 下个15分钟建议
1. 安装self-improving-agent skill（clawhub评分最高之一）
2. 测试firecrawl agent端点（已有API key）
3. 研究OpenClaw skills如何调用composio CLI
