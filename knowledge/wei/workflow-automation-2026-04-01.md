# 工作流自动化平台学习报告

**刑部尚书 魏征**
**日期：2026-04-01**

---

## 一、n8n (n8n.io)

### 核心定位
> "AI Workflow Automation Platform"
> 500+ 预构建集成，原生 AI Agent 支持

### 核心功能

| 功能 | 说明 |
|------|------|
| **500+ Nodes** | 预构建应用连接器 |
| **AI Agents** | 支持构建可控制、可解释的 AI Agent |
| **Human-in-the-loop** | 人工审批介入节点 |
| **执行检查点** | 每个决策可追溯 |
| **Git 版本控制** | 工作流代码化管理 |
| **审计日志** | 企业级安全合规 |

### 安全与治理
- ✅ 完全本地部署选项
- ✅ SSO/SAML/LDAP
- ✅ 加密密钥存储
- ✅ RBAC 权限控制
- ✅ 审计日志输出到 SIEM

### 与 OpenClaw 对比

| 维度 | n8n | OpenClaw |
|------|-----|----------|
| **定位** | 可视化工作流编排 | AI Agent 运行时 |
| **集成** | 500+ Apps | 79+ Skills + MCP |
| **执行模式** | 事件驱动 + Cron | Cron + 主动心跳 |
| **AI 原生** | ✅ | ✅ |
| **代码执行** | 有限 | ✅ (exec/sandbox) |
| **部署** | 自托管/云端 | 本地为主 |

### n8n + OpenClaw 集成场景
```
n8n 工作流触发 → Webhook → OpenClaw 会话
OpenClaw 任务完成 → Webhook → n8n 后续处理
```

---

## 二、Temporal (temporal.io)

### 核心定位
> "Durable Execution"
> 让代码在分布式系统故障中自动恢复

### 核心理念
**"Write code as if failure doesn't exist"**

Temporal 可以捕获每一步的状态，失败后从断点恢复，不会丢失进度。

### 关键概念

| 概念 | 说明 |
|------|------|
| **Workflow** | 业务逻辑代码，故障恢复点 |
| **Activity** | 可能失败的操作，自动重试 |
| **Task Queue** | 任务分发队列 |
| **Signals** | 向运行中的 Workflow 发送信号 |
| **Timers** | 延时执行 |

### AI 场景支持
- ✅ **MCP 集成**：可靠编排 MCP 工具调用
- ✅ **Agent 存活**：让 Agent 在真实环境中持久运行
- ✅ **训练管道**：ML 训练任务可靠编排

### 案例
- NVIDIA：用 Temporal 管理跨云 GPU 集群
- Salesforce：微服务架构迁移
- Twilio：离开自建系统迁移到 Temporal Cloud

### 技术特点
- 100% 开源 (MIT)
- 9 年生产验证
- 源自 AWS SQS/SWF、Azure Durable Functions、Cadence

### 与 OpenClaw 集成场景
```
OpenClaw 复杂任务 → Temporal Workflow
    ↓ 故障自动恢复
    ↓ 多步骤编排
结果返回 OpenClaw
```

---

## 三、Windmill (windmill.dev)

### 核心定位
> "Build, deploy and monitor internal software at scale"
> 用代码构建内部工具，无平台工程负担

### 核心功能

| 功能 | 说明 |
|------|------|
| **20+ 语言** | Python, TS, Go, etc |
| **WebIDE** | 内置开发环境 + LSP |
| **Git 同步** | 代码版本控制 |
| **自动生成 UI** | 脚本 → 即时 Endpoint/UI |
| **触发器** | Cron/Webhook/Pubsub |
| **CLI + VS Code** | 本地开发体验 |

### AI Agent 集成
- ✅ Claude Code rules for Cursor
- ✅ AI 辅助代码生成
- ✅ 自动化 Git 同步部署

### 性能
- 号称"最快的工作流引擎"
- 支持大规模并发任务

### 与 OpenClaw 对比

| 维度 | Windmill | OpenClaw |
|------|----------|----------|
| **定位** | 内部工具平台 | AI Agent 运行时 |
| **语言** | 20+ | 主要 Node.js |
| **UI 生成** | 自动生成 | 无 |
| **工作流** | 可视化 + 代码 | Session-based |
| **部署** | 自托管/云端 | 本地为主 |

---

## 四、inference.sh (CLI)

### 核心定位
> "Run 150+ AI apps in the cloud with a simple CLI"
> 无 GPU 调用 AI 能力

### 支持类别

| 类别 | 示例 |
|------|------|
| **图像** | FLUX, Gemini 3 Pro, Grok Imagine, Seedream |
| **视频** | Veo 3.1, Seedance, Wan 2.5, OmniHuman |
| **LLMs** | Claude Opus/Sonnet/Haiku, Gemini, Kimi |
| **搜索** | Tavily Search, Exa Search |
| **Twitter/X** | 发推、DM、关注、点赞 |
| **3D** | Rodin 3D Generator |

### CLI 使用
```bash
# 安装
curl -fsSL https://cli.inference.sh | sh

# 运行 AI App
infsh app run openrouter/claude-sonnet-45 --input '{"prompt": "Hello"}'

# 图像生成
infsh app run falai/flux-dev-lora --input '{"prompt": "a cat astronaut"}'

# Twitter 发推
infsh app run x/post-tweet --input '{"text": "Hello from AI!"}'

# 不等待结果
infsh app run <app> --input input.json --no-wait
```

### OpenClaw 集成
- **已支持**：Skills 可调用 `infsh` CLI
- **权限**：允许 `Bash(infsh *)` 工具

---

## 五、OpenClaw 自动化执行能力现状

### Cron 系统
| 功能 | 说明 |
|------|------|
| **模式** | Reminder / Task / One-time |
| **时间表达式** | every_seconds / cron_expr / at |
| **Session 隔离** | main / isolated / current |

### Session 管理
- `sessions_spawn`: 派生子 Agent
- `sessions_send`: 向其他 Session 发送消息
- `sessions_list`: 列出活跃 Session

### 自动化场景
```
Cron 触发 → 新 Session → 执行任务 → 汇报
```

---

## 六、平台对比总结

| 平台 | 定位 | 集成数量 | 执行模型 | 故障恢复 |
|------|------|----------|----------|----------|
| **n8n** | 可视化工作流 | 500+ | 事件驱动 | 有限 |
| **Temporal** | 持久执行 | 代码级 | Durable WF | 完整 |
| **Windmill** | 内部工具 | 20+ 语言 | 作业调度 | 完整 |
| **inference.sh** | AI API 网关 | 150+ | 云端执行 | 云端负责 |

---

## 七、OpenClaw 集成策略建议

### 当前能力评估
- ✅ Cron 调度 ✅ Session 管理 ✅ Skills 生态 ✅ MCP 支持
- ❌ 可视化工作流 ❌ 跨系统编排 ❌ 长期状态跟踪

### 建议集成优先级

| 优先级 | 平台 | 理由 |
|--------|------|------|
| **P1** | inference.sh | 直接可用，扩展 AI 能力 |
| **P2** | n8n Webhook | 触发 OpenClaw 任务 |
| **P3** | Temporal | 复杂长时任务可靠执行 |

### 架构设想
```
外部系统 → n8n 工作流 → Webhook → OpenClaw
                                      ↓
OpenClaw → inference.sh CLI → 150+ AI 能力
                                      ↓
                              结果 → Temporal (可选)
                                      ↓
                              汇报 → 皇上
```

---

## 八、今日学习行动项

- [ ] 研究 inference.sh 在 OpenClaw 中的实际集成方式
- [ ] 测试 n8n Webhook 触发 OpenClaw Session 的可行性
- [ ] 评估 Temporal 是否适合复杂长时任务
- [ ] 整理现有 Skills 形成自动化能力矩阵

---

## 九、相关文件

- `tool-integration-learning-2026-03-31.md` - Composio/Zapier
- `cloud-async-learning-2026-03-31.md` - Vercel AI SDK/Modal
- `session-isolation-design.md` - Session 隔离设计

---

*本报告由魏征（刑部尚书）学习整理*
*学习时间：2026-04-01 10:00 CST*
