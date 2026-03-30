# claude-mem 评估报告

> 刑部尚书魏征，奉命审计。日期：2026-03-30

---

## 是什么

**claude-mem** 是由 `thedotmack`（Plastic Labs）开发的一个 **Claude Code 专用记忆压缩系统**，并非 OpenClaw 的插件。

- **npm 包**：[https://npm.im/claude-mem](https://npm.im/claude-mem)，版本 10.6.3（2026-03-29 最新）
- **GitHub 仓库**：`plastic-labs/claude-mem` → **已 404**，可能已更名或私有
- **安装方式**：`curl -fsSL https://install.cmem.ai | bash`（Node.js >= 18）
- **核心关键词**：memory compression、knowledge-graph、transcript、MCP plugin、TypeScript/NodeJS

### ⚠️ 注意：cmem.ai 是另一个项目

`cmem.ai`（$CMEM）是 **Solana 区块链上的 Agent 经济代币**，与 claude-mem 软件是**两个独立事物**：
- $CMEM 代币用于 Agent 经济体的 memory services、bounties 等
- claude-mem 是记忆压缩工具软件本身

---

## 能解决什么问题

claude-mem 的设计目标（基于 npm 描述和关键词推断）：

1. **会话上下文压缩**：将长 transcript 压缩，突破 context 窗口限制
2. **跨会话记忆持久化**：下次启动时恢复之前的学习上下文
3. **知识图谱构建**：基于知识图谱的结构化记忆，而非纯文本
4. **MCP 插件生态**：有多个 OpenCode 适配器（@bloodf/opencode-claude-mem、claude-mem-opencode 等）

---

## 与现有记忆管家对比

| 维度 | claude-mem | OpenClaw 现有记忆体系 |
|------|-----------|---------------------|
| **定位** | Claude Code 的 MCP 插件 | 通用 Agent 框架内置 |
| **存储方式** | 知识图谱 + 压缩 transcript | 文件系统（MEMORY.md、CURRENT.md、memory/YYYY-MM-DD.md） |
| **上下文压缩** | ✅ 有（transcript compression） | ❌ 无，靠人工精简 |
| **跨会话学习** | ✅ 有 | ⚠️ 有，但依赖文件读写和人工维护 |
| **知识图谱** | ✅ 有 | ❌ 无（memory-lancedb 是向量数据库，非知识图谱） |
| **OpenClaw 适配** | ❌ **无直接适配**（只有 OpenCode 适配器） | — |
| **依赖要求** | Node.js >= 18，Claude Code SDK | OpenClaw 内置，无需额外依赖 |

### OpenClaw 现有记忆管家能力（AGENTS.md 定义）
- `MEMORY.md`：长期记忆精选
- `CURRENT.md`：当前会话状态
- `memory/YYYY-MM-DD.md`：每日原始日志
- `memory-lancedb-pro` skill：向量数据库检索

**结论**：claude-mem 在"知识图谱"和"自动压缩"上有优势，但它是 **Claude Code 专属**，无法直接用于 OpenClaw。

---

## 安装风险评估

### 🔴 高度风险：不兼容

1. **架构不兼容**
   - claude-mem 基于 `claude-agent-sdk` / Claude Code 的 MCP 协议
   - OpenClaw 使用自己的 Agent 架构和工具系统
   - 二者 SDK 底层完全不同

2. **GitHub 仓库已 404**
   - `plastic-labs/claude-mem` 无法访问
   - 项目是否还在维护存疑

3. **$CMEM 代币关联风险**
   - cmem.ai 域名与 Solana 代币经济绑定
   - 安装脚本 `install.cmem.ai` 来源不明，可能有供应链风险

4. **没有 OpenClaw 适配器**
   - npm 上有多个 OpenCode 适配器，但**没有 OpenClaw 适配器**
   - 要用必须自己写适配层

### 🟡 中等风险

- **Node.js >= 18**：太上皇环境 Node v24.14，满足要求
- **独立运行**：不修改 OpenClaw 核心文件，不会破坏现有架构
- **但**：可能与 OpenClaw 的记忆系统产生冲突（双重记忆层）

### 🟢 低风险（如果仅研究）

- 安装脚本是 bash（Windows 上需要 WSL/Git Bash）
- 不影响 OpenClaw 核心

---

## 结论

### 🚫 不建议安装到 OpenClaw

**核心理由**：

1. **血脉不通**：claude-mem 是 Claude Code（Anthropic 官方 CLI）的插件，嫁接不到 OpenClaw 身上
2. **没有适配层**：npm 上有 OpenCode 适配器，OpenClaw 适配器为零
3. **项目状态可疑**：GitHub 仓库 404，维护状态不明
4. **收益不确定**：太上皇已有文件型记忆系统 + memory-lancedb-pro，风险大于收益

### 💡 如果太上皇想要类似能力，建议

1. **知识图谱记忆** → 研究 OpenClaw 的 `memory-lancedb-pro` skill 能否扩展为知识图谱
2. **自动压缩** → 在 OpenClaw skill 中自己实现 transcript 压缩逻辑
3. **跨会话学习** → 增强 `MEMORY.md` 的自动更新机制

---

*魏征，刑部尚书，审计完毕。*
