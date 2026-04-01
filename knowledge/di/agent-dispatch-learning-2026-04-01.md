# 智能体分发与生态学习笔记

**日期：** 2026-04-01  
**主持：** 狄仁杰  
**参与者：** 李元芳（情报）、魏征（技术）

---

## 一、Dify（dify.ai）

### 核心定位
- **全称：** Do It For You
- **性质：** 开源 Agentic Workflow 构建平台（Apache-2.0）
- **GitHub:** langgenius/dify（业界知名开源项目）

### 核心功能

#### 1. 应用类型
| 类型 | 说明 |
|------|------|
| **Workflow** | 单轮任务，批量执行，支持定时触发和API调用 |
| **Chatflow** | 多轮对话，支持记忆、流式输出、对话变量 |
| **Agent** | 自主规划型 Agent（Tool Use + ReAct） |
| **Chatbot** | 对话机器人 |
| **Text Generator** | 文本生成 |

#### 2. 可视化编排
- 拖拽式画布，节点包括：LLM节点、工具节点、问题分类、IF分支、模板转换等
- 每个节点可配置输入输出变量
- 支持 DAG（有向无环图）结构

#### 3. MCP 集成（重点！）
- **MCP Server Publish**：将 Dify App 暴露为标准 MCP Server，供其他 AI 工具调用
- **MCP Tool**：在 Dify 工作流中调用外部 MCP Tool
- **Native MCP 集成**：桥接各类系统和平台

#### 4. Dify DSL
- 所有 App 可导出为 YAML DSL 文件
- 便于版本控制、模板分享、环境迁移
- 类似 OpenClaw 的 skill 文件机制

#### 5. 企业级特性
- 多租户支持
- RAG Pipeline（检索增强生成）
- 可观测性（日志、追踪）
- 自部署（Docker 一键部署）

### 对 OpenClaw 的参考价值

| Dify 特性 | OpenClaw 可借鉴点 |
|-----------|------------------|
| DSL 模板导出/导入 | 设计 skill 模板的标准化格式 |
| MCP Server 发布 | OpenClaw 已支持 MCP，是否可发布为 MCP Server 被其他系统调用 |
| Workflow 触发器（定时/事件） | OpenClaw cron 机制类似，但 Dify 的事件触发更丰富 |
| RAG Pipeline | 可研究作为知识库增强方案 |
| 开源生态 + Marketplace | 社区驱动的模板/技能市场 |

---

## 二、Genspark（genspark.ai）

### 核心定位
- **定位：** All-in-One AI Workspace（AI Super Agent 平台）
- **核心理念：** 用户提交查询 → 平台路由到专用模型/Agent 集合 → 生成 Sparkpage

### 核心功能

#### 1. Sparkpage（临时生成页面）
- 根据用户 query **实时生成**专属内容页面
- 结构化展示：分栏、摘要、图表、代码
- 可内嵌 **AI Assistant**（交互式追问）
- 本质：一次性、临时、query 特定的 AI 聚合输出

#### 2. 多 Agent 系统
内置专用 Agent 类型：
- **AI Slides** — 自动生成 PPT/幻灯片
- **AI Sheets** — 数据分析和表格处理
- **AI Docs** — 文档撰写
- **AI Developer** — 代码生成和调试
- **AI Designer** — UI/设计稿生成
- **Super Agent** — 顶层编排器，负责协调各专用 Agent

#### 3. 多模型聚合
- 后端组合使用多个全球 LLM（混合模型策略）
- 自动选择合适模型处理不同子任务

#### 4. 实时执行
- Agent 自主执行多步骤任务（不同于纯对话）
- 支持：研究、幻灯片制作、代码执行、文件生成

### 对 OpenClaw 的参考价值

| Genspark 特性 | OpenClaw 可借鉴点 |
|--------------|------------------|
| **Sparkpage 临时页面生成** | OpenClaw 的 Canvas/文档生成能力可参考此模式，做 query 驱动的临时内容页 |
| **Super Agent 顶层协调** | 三司会审架构（狄仁杰主持调度）与 Genspark 的 Super Agent 理念一致 |
| **专用 Agent 分工（Slides/Sheets/Docs）** | OpenClaw 的 subagent 分工模式可进一步细化，像 Genspark 一样专业化 |
| **用户 query → 聚合输出** | OpenClaw 可研究"一次查询，触发多个 agent 并聚合结果"的模式 |
| **实时生成可交互页面** | OpenClaw Canvas 的增强方向：生成后可持续交互的临时页面 |

---

## 三、对比分析

| 维度 | Dify | Genspark |
|------|------|----------|
| **定位** | Agent 编排/Workflow平台 | AI 工作空间/Super Agent |
| **核心产出** | 可部署的 AI 应用 | 临时 query 特定内容页 |
| **复用性** | 高（DSL模板、企业内复用） | 低（一次性Sparkpage） |
| **集成方式** | MCP/API/SDK | 闭源，API有限 |
| **部署模式** | 自部署 + 云端 | 纯云端 |
| **开源** | ✅ 完全开源 | ❌ 闭源 |

---

## 四、关键洞察

### 洞察1：Dify 的 MCP 双向通道是行业趋势
Dify 既能消费外部 MCP 工具，也能将自己发布为 MCP Server。这代表 AI 应用的标准互操作协议正在形成。**OpenClaw 应强化 MCP Server 能力**，让自身能被其他平台（如 Dify、Cursor）调用。

### 洞察2：Sparkpage 模式代表"按需聚合"需求
Genspark 的 Sparkpage 证明：用户不想要通用聊天，而想要**针对当前任务即时生成的专项工具**。这与 OpenClaw 的 skill 机制高度契合——skill 即"按需调用的专项能力"。

### 洞察3：Super Agent 协调层是架构重点
Genspark 的 Super Agent 和 Dify 的 Workflow 编排，都指向同一个结论：**协调层（Orchestration Layer）比执行层更重要**。三司会审架构恰好是这个理念的体现。

---

## 五、建议行动

1. **Dify DSL 研究**：魏征调研 Dify DSL 格式，评估能否设计 OpenClaw skill 的类似标准
2. **Sparkpage 模式**：李元芳研究 Canvas 生成临时内容页面的可行性
3. **MCP 深化**：魏征评估 OpenClaw 作为 MCP Server 的完整度

---

*本笔记由狄仁杰主持三司会审整理，供太上皇御览。*
*学习时间：2026-04-01 08:08 (UTC+8)*
