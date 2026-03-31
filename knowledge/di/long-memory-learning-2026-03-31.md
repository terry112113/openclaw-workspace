# 长时记忆与知识库工具学习报告

**狄仁杰 | 2026-03-31 | 三司会审专项学习**

---

## 一、Pinecone — 向量数据库（外部大脑）

### 核心定位
> *"The vector database to build knowledgeable AI"*

Pinecone 是专为 AI 应用设计的向量数据库，支持大规模语义检索，是 RAG（检索增强生成）架构的核心基础设施。

### 核心概念

#### 1. Index（索引）
向量数据存储在 Index 中，分为两种类型：
- **Dense Index**：存储稠密向量，用语义相似度搜索（语义搜索/向量搜索）
- **Sparse Index**：存储稀疏向量，用关键词精确匹配（词法搜索）

#### 2. Namespace（命名空间）
- 在 Index 内部，用 Namespace 对记录做分区隔离
- 核心价值：**多租户隔离** — 每个用户/Agent 可用独立 Namespace
- 自动创建，无需显式声明

#### 3. Vector Embedding（向量嵌入）
- 文本 → 向量（通过 Embedding 模型）
- Pinecone 提供内置 Embedding 模型，也支持自备（BYOV）
- 支持导入 Parquet 文件进行大规模数据导入（千万级）

#### 4. Hybrid Search（混合搜索）
- 语义搜索 + 词法搜索的融合
- 解决"语义搜到了但关键词没命中"或"关键词命中了但语义不相关"的问题

### API 接入方式

```python
# 安装
pip install pinecone

# 初始化
from pinecone import Pinecone
pc = Pinecone(api_key="YOUR_API_KEY")
index = pc.Index("semantic-search")

# 语义搜索
results = index.search(
    namespace="user-memory",
    query={"inputs": {"text": "上周的会议结论"}},
    top_k=5,
    fields=["content", "timestamp"]
)
```

**多语言 SDK**：Python / JavaScript / Go / Java

**接入要点**：
- Serverless 模式：自动扩缩，按用量付费，无需运维
- 支持元数据过滤（filter），可按时间、类别等条件筛选
- 单 Index 可支持 100,000 个 Namespace（企业级多租户）

### 对"记忆不忘协议"的价值

| 维度 | 价值 |
|------|------|
| **长期记忆存储** | 将每日对话记忆、决策记录永久存入向量数据库，不依赖文件 |
| **语义检索** | 用自然语言提问找回记忆，如"上次讨论的项目优先级" |
| **多 Agent 共享** | 每个 Agent 可有独立 Namespace，互不干扰 |
| **RAG 增强** | 检索历史上下文注入 LLM 提示词，减少遗忘 |
| **时间衰减** | 可结合元数据过滤实现"近期记忆优先"策略 |

**典型应用场景**：
- `memory/YYYY-MM-DD.md` → 向量化 →存入 Pinecone → 提问时语义检索 → 召回 Top-K 相关记忆片段 → 注入上下文

---

## 二、LangSmith — LLM 应用调试与评估平台

### 核心定位
> *"A framework-agnostic platform for building, debugging, and deploying AI agents and LLM applications."*

LangSmith 是 LLM 应用的全栈观测平台，集 **Tracing（追踪）**、**Evaluation（评估）**、**Prompt 管理** 于一体，被称为 AI 应用的"黑匣子"和"复盘记录本"。

### 核心功能

#### 1. Tracing（追踪/可观测性）
- 每次请求生成完整 **Trace（轨迹）**，记录 LLM 调用、Tool 执行、检索步骤等
- 每个 Trace 由多个 **Run（运行）** 组成（子操作）
- 非确定性 LLM 的行为变得可追踪、可调试
- 支持 LangChain / LangGraph 一行环境变量开启追踪

```bash
export LANGSMITH_TRACING=true
export LANGSMITH_API_KEY="your-key"
# 无需改代码，自动追踪所有 LLM 调用
```

#### 2. Evaluation（评估 / LLM-as-a-Judge）
- **Dataset**：测试数据集，支持输入/期望输出
- **Evaluator**：评分器，预置 Correctness、Relevance 等
- **Experiment**：实验记录，对比不同 Prompt/模型版本
- **LLM-as-a-Judge**：用强模型评估弱模型输出的质量

**预置 Evaluator 类型**（来自 `openevals` 包）：
- Correctness（答案正确性）
- Relevance（相关性）
- Hallucination（幻觉检测）
- Containment（包含性）

#### 3. Playground（调试验证台）
- 在 UI 中实时测试 Prompt，无需改代码
- 同一界面可创建 Dataset、添加 Evaluator、运行 Experiment
- 支持版本化管理 Prompt

#### 4. LangSmith Fleet（无代码 Agent 构建）
- 可视化设计 Agent 流程，无需写代码
- 部署为 Agent Server，支持自动扩缩

### API 接入方式

```python
# 安装
pip install langsmith

# 环境变量配置
import os
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = "your-key"
os.environ["LANGSMITH_PROJECT"] = "my-agent"  # 可选，指定项目

# LangSmith SDK 使用
from langsmith import Client
client = Client()

# 创建 Dataset
client.create_dataset("test-dataset", inputs=[{"question": "..."}])

# 运行 Evaluation
from langsmith.evaluation import evaluate
results = evaluate(
    dataset_name="test-dataset",
    llm_or_chain=my_rag_chain,
    evaluators=[my_evaluator]
)
```

**接入要点**：
- SOC 2 Type 2 / HIPAA / GDPR 合规
- 支持自托管（Self-hosted）和混合部署
- 支持 MCP（Model Context Protocol）连接 Claude、VSCode

### 对"记忆不忘协议"的价值

| 维度 | 价值 |
|------|------|
| **复盘记录** | 每次决策/对话的 Trace 都是完整复盘素材 |
| **Agent 行为审计** | 追踪 Agent 的思考链、工具调用、检索结果 |
| **质量评估** | 用 LLM-as-a-Judge 自动评估回答质量 |
| **实验对比** | 对比不同记忆策略（加或不加记忆）的效果差异 |
| **错误定位** | 记忆召回错误时，可追踪是哪次检索出了问题 |

**典型应用场景**：
- 开启追踪：让每次三司会审都有完整 Trace 存档
- 创建 Dataset：积累"标准问答对"，测试记忆召回准确率
- LLM-as-a-Judge：自动判断 Agent 的回答是否正确运用了记忆

---

## 三、双平台协同：记忆不忘协议架构

```
Pinecone（外部记忆）          LangSmith（复盘与审计）
┌─────────────────┐          ┌──────────────────────┐
│  每日记忆向量存储  │  ────▶  │  Trace 记录检索过程  │
│  Namespace per  │          │  Evaluation 评估质量 │
│  Agent/User     │          │  Experiment 对比策略 │
└─────────────────┘          └──────────────────────┘
         ↑                            ↑
         │                            │
    RAG 检索，注入上下文         追踪+复盘，持续优化
         ↑                            ↑
   ┌─────────────────────────────────────────┐
   │           LLM (狄仁杰/李元芳/魏征)         │
   └─────────────────────────────────────────┘
```

**核心思路**：
1. **Pinecone** 解决"记忆在哪里"（Where）— 外部知识库，向量检索
2. **LangSmith** 解决"记忆用得好不好"（How Well）— 追踪评估，持续优化

---

## 四、学习结论与建议

### 立即可行动项
1. **Pinecone Free Tier**：已有免费套餐，可立即注册测试，向量存储记忆
2. **LangSmith Tracing**：加三个环境变量即可开启，不影响现有代码
3. **自托管备选**：若对数据主权有要求，两者均支持自托管

### 待深入研究
- Pinecone：多租户 Namespace 隔离策略的具体实现
- LangSmith：自定义 Evaluator 的编写方法
- 两者结合：如何让评估结果自动触发记忆更新

---

*狄仁杰学习笔记 | 2026-03-31*
