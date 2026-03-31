# 云端环境与异步执行学习笔记
**刑部尚书 魏征 · 2026-03-31**

---

## 一、Vercel AI SDK（sdk.vercel.ai）

### 概述
Vercel AI SDK 是一个 **TypeScript / Node.js 的 AI 应用开发工具包**，用于在 React、Next.js、Vue、Svelte、Node.js 等框架中构建 AI 应用和 Agent。

**定位：** 让开发者不用操心底层模型差异，用统一 API 调用各种 LLM，支持流式响应、工具调用、UI 组件。

### 核心模块

#### 1. AI SDK Core
统一 API，核心函数：
- `generateText()` — 文本生成
- `generateStructuredObject()` — 结构化输出
- `streamText()` — **流式文本响应**（关键！用于实时 UI）
- `generateObject()` — 对象生成
- `toolCalls()` / `toolCall()` — 工具调用

```typescript
import { generateText } from 'ai';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'What is love?',
});
```

#### 2. AI SDK UI
框架无关的 React Hooks，专门解决**流式 AI 界面**问题：
- `useChat` — 构建 ChatGPT 风格的聊天界面
- `useCompletion` — 流式补全
- `useAssistant` — AI 助手状态管理

```typescript
import { useChat } from 'ai/react';

const { messages, input, handleInputChange, handleSubmit } = useChat({
  api: '/api/chat',
});
```

#### 3. Vercel AI Gateway
统一网关，一套 API 接入 **100+ 模型**（OpenAI、Anthropic、Google、Cohere、Mistral 等），无需管理多个 API Key，支持负载均衡和自动重试。

#### 4. Vercel Sandbox（@vercel/sandbox）
**安全沙箱**，在云端隔离执行 AI 生成的代码：
- Python 3.13 沙箱
- 可作为 Agent 工具集成：`ai-sdk-tool-code-execution`
- 适合让 AI 生成代码后安全执行

```typescript
import { executeCode } from 'ai-sdk-tool-code-execution';
```

#### 5. AI SDK Workflows
**长时运行 Agent 框架**，支持暂停、恢复、超时存活。适合复杂多步骤 Agent 场景：
```typescript
npm i workflow
```

### 工具生态（Tool Registry）
内置大量官方工具集成，无需自己封装：
| 工具 | 功能 |
|------|------|
| `firecrawl-aisdk` | 网页抓取/爬取/搜索 |
| `@tavily/ai-sdk` | Web 搜索 |
| `@perplexity-ai/ai-sdk` | Perplexity 搜索 |
| `@browserbasehq/ai-sdk` | 浏览器自动化 |
| `bash-tool` | Bash + 文件读写工具 |
| `bedrock-agentcore` | 云端浏览器 + 代码解释器 |
| `@superagent-ai/ai-sdk` | 安全护栏（PII 脱敏、提示注入防护）|
| `@airweave/vercel-ai-sdk` | 35+ 数据源语义搜索（Notion/Slack/Google Drive 等）|

### 与 OpenClaw 集成的可能方向
1. **UI 界面层**：用 AI SDK UI 的 React Hooks 构建流式对话界面，替代当前方案
2. **流式响应**：用 `streamText()` 配合 Vercel Edge Functions 实现边缘流式推理
3. **工具调用**：用 Tool Registry 快速接入 Firecrawl、Tavily 等爬虫/搜索工具
4. **代码执行沙箱**：用 Vercel Sandbox 安全执行 AI 生成代码（比 Ollama 直接执行更安全）

---

## 二、Modal（modal.com）

### 概述
Modal 是一个 **Python 优先的 AI 基础设施云平台**，口号是"像写本地代码一样写云端代码"。

**定位：** 替代 AWS Lambda / Docker / Cloud Run，主打 GPU 推理、批量处理、训练任务。

### 核心理念
**零配置 YAML，一切皆代码**。用 Python 装饰器定义云端函数：
```python
import modal

app = modal.App('example')

@app.function(gpu='T4')
def generate_text(prompt: str):
    # 直接写业务逻辑，Modal 自动处理容器、GPU、网络
    return f"Result for: {prompt}"
```

### 核心能力

#### 1. LLM 推理（Inference）
- 支持主流开源模型（Llama、Mistral、Qwen 等）和自定义模型
- **子秒级冷启动**（< 1 秒）
- 多 GPU 并行推理

#### 2. 弹性 GPU 扩展
- 跨多云（AWS、GCP、Lambda Labs）动态调度 GPU 资源
- 支持 A100、H100、L40S 等
- **自动扩缩容，用完归零**（scale to zero）
- 无需配额申请或预留

#### 3. 批量处理（Batch Processing）
并行跑大规模任务，适合：
- 数据集批处理
- 模型评估（Evals）
- 并行微调

#### 4. 训练 & 微调
- 分布式训练
- Hugging Face Diffusers LoRA 微调示例
- HP Sweep（超参数搜索）

#### 5. Modal Sandboxes
**隔离安全沙箱**，执行 AI 生成的代码，支持：
- Python、JavaScript/TypeScript、Go 调用
- 内置文件系统
- 可横向扩展到数千个并发沙箱

#### 6. Modal Notebooks
Jupyter  notebooks，支持 **GPU 秒级启动**，实时协作。

### 工作原理
1. 写 Python 代码 + `@app.function()` 装饰器
2. `modal run` 一键部署到云端容器
3. Modal 自动管理：镜像构建、GPU 调度、容器扩缩容、日志
4. 调用如同本地函数：`generate_text.call("hello")`

### Modal vs 其他方案对比

| 维度 | Modal | AWS Lambda | Docker/K8s | Cloud Run |
|------|-------|------------|------------|-----------|
| 语言 | Python 优先 | 多语言 | 多语言 | 多语言 |
| GPU 支持 | ✅ 原生 | ❌ | ✅ 手动 | ❌ 原生 |
| 冷启动 | **< 1 秒** | 几秒~几十秒 | 手动 | 几秒 |
| 扩缩容 | 自动 to zero | 按请求 | 手动 | 自动 |
| 配置 | **零 YAML** | JSON/YAML | YAML | YAML |
| 性价比 | 按秒计费 | 按调用 | 固定成本 | 按请求 |

### 与 OpenClaw 集成的可能方向
1. **重计算任务卸载**：将 Ollama 推理或批量评估任务跑在 Modal GPU 上，减轻本地机器负担
2. **弹性扩展**：高峰期 Modal 承接突发推理请求
3. **Python 生态**：Modal 无缝运行 Python 脚本，OpenClaw 任务中涉及 Python 数据处理可考虑
4. **Sandbox 执行**：Modal Sandboxes 比 Vercel Sandbox 更灵活，支持更多语言

---

## 三、学习总结

### 战略定位分析

| 维度 | Vercel AI SDK | Modal |
|------|--------------|-------|
| **主战场** | AI UI / 前端 / 流式应用 | GPU 推理 / 后端 / Python 任务 |
| **语言** | TypeScript/Node.js | Python |
| **特点** | 流式 UI + 工具生态 | 弹性 GPU + 零配置 |
| **与 OpenClaw 关系** | 界面层增强 | 执行层增强 |

### 最快落地路径
1. **Firecrawl 工具集成** → 已在 `firecrawl-aisdk`，李元芳可用
2. **Vercel Sandbox 替代本地 exec** → 更安全的代码执行环境
3. **Modal 承接重 GPU 推理** → 缓解本地 Ollama 20B 机器负担

### 待深入
- AI SDK Workflows 的 `suspend/resume` 机制细节
- Modal 与 Vercel Sandbox 的安全边界对比
- AI Gateway 的多模型路由策略
