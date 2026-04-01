# deer-flow v2.0 移植方案

**制定人：** 李元芳（INTJ建筑师型）
**日期：** 2026-03-29
**研究对象：** bytedance/deer-flow v2.0
**仓库地址：** https://github.com/bytedance/deer-flow

---

## 一、deer-flow v2.0 架构总览

### 1.1 定位变化

deer-flow v2.0 从"Deep Research 框架"进化为**超级Agent运行时（Super Agent Harness）**：
- 不再是"研究工具"，而是**赋予Agent超能力的运行时基础设施**
- 构建在 LangGraph + LangChain 之上
- 提供：文件系统 + 内存 + 沙箱隔离执行 + 子Agent调度 + Skills扩展

### 1.2 技术栈

| 层级 | 技术 | 端口 |
|------|------|------|
| 前端 | Next.js 16 + React 19 + TypeScript | 3000 |
| API Gateway | FastAPI (Python) | 8001 |
| Agent运行时 | LangGraph Server (LangGraph SDK) | 2024 |
| 反向代理 | Nginx (unified reverse proxy) | 2026 |
| 沙箱（可选） | Docker / Kubernetes Provider | - |

### 1.3 核心架构图

```
                    ┌─────────────────────────────────────────┐
                    │           Nginx (port 2026)             │
                    │    Unified Reverse Proxy Entry Point     │
                    └───────────────┬─────────────────────────┘
                                      │
              ┌───────────────────────┼───────────────────────┐
              │                       │                       │
        ┌─────▼─────┐         ┌──────▼──────┐         ┌─────▼──────┐
        │  Frontend  │         │  FastAPI    │         │ LangGraph  │
        │ (Next.js)  │         │  Gateway    │         │  Server    │
        │  :3000     │         │  :8001      │         │  :2024     │
        └───────────┘         └──────┬──────┘         └──────┬──────┘
                                     │                        │
                                     │    ┌────────────────────┤
                                     │    │                    │
                              ┌───────▼────▼───────┐  ┌───────▼──────┐
                              │  REST API Routes   │  │  LangGraph  │
                              │  models/mcp/       │  │  Agents     │
                              │  skills/memory/    │  │  Tools      │
                              │  uploads/threads   │  │  Sandbox    │
                              └────────────────────┘  └──────┬──────┘
                                                               │
                            ┌──────────────────────────────────┤
                            │                                  │
                   ┌────────▼────────┐           ┌─────────────▼──────┐
                   │   Middleware    │           │  SubAgent System   │
                   │   Chain (12个)   │           │  general-purpose   │
                   │                  │           │  bash             │
                   │ ThreadData       │           │  (3 workers)      │
                   │ Uploads          │           │  15min timeout     │
                   │ Sandbox          │           └───────────────────┘
                   │ Summarization    │
                   │ TodoList         │
                   │ Title            │
                   │ Memory           │
                   │ ViewImage        │
                   │ SubagentLimit    │
                   │ Classification   │
                   └──────────────────┘
```

---

## 二、核心组件详解

### 2.1 Lead Agent（主Agent）

**入口点：** `make_lead_agent(config)` 注册在 `langgraph.json`

核心能力：
- **动态模型选择**：通过 `create_chat_model()` 支持 thinking/vision
- **Middleware Chain**：12个中间件顺序执行
- **Tool System**：沙箱+MCP+内置+社区+子Agent工具
- **子Agent委托**：通过 `task()` 工具并行执行
- **System Prompt**：包含 skills注入、memory上下文、工作目录指导

### 2.2 Middleware Chain（12个中间件，顺序执行）

| # | 中间件 | 职责 |
|---|--------|------|
| 1 | ThreadDataMiddleware | 创建per-thread隔离目录（workspace/uploads/outputs）|
| 2 | UploadsMiddleware | 将上传文件注入对话上下文 |
| 3 | SandboxMiddleware | 获取沙箱，执行环境存储sandbox_id |
| 4 | DanglingToolCallMiddleware | 注入占位ToolMessages，避免AI乱调用 |
| 5 | GuardrailMiddleware | 预工具调用授权（可插拔：Allowlist/OA政策/自定义）|
| 6 | SummarizationMiddleware | Token超限时自动压缩上下文（可选）|
| 7 | TodoListMiddleware | Plan模式任务追踪（可选）|
| 8 | TitleMiddleware | 首轮对话后自动生成标题 |
| 9 | MemoryMiddleware | 异步更新对话队列（过滤用户+最终AI回复）|
| 10 | ViewImageMiddleware | 注入base64图像数据供vision模型使用 |
| 11 | SubagentLimitMiddleware | 截断 `task()` 调用强制MAX_CONCURRENT_SUBAENTS限制 |
| 12 | ClassificationMiddleware | 拦截 `ask_classification` 调用，END终止执行（必须最后）|

### 2.3 Sandbox System（沙箱隔离）

**核心接口：** `Sandbox` abstract class with `execute_command`, `read_file`, `write_file`, `list_dir`

**两个Provider：**
- `LocalSandboxProvider`：本地文件系统执行
- `AioSandboxProvider`：Docker容器隔离

**虚拟路径系统：**
```
Agent可见：  /mnt/user-data/{workspace, uploads, outputs}
物理路径：   backend/.deer-flow/threads/{thread_id}/user-data/...
Skills路径： /mnt/skills → deer-flow/skills/
```

**沙箱工具（tools.py）：**
- `bash`：路径翻译 + 错误处理
- `ls`：目录列表（树格式，最多2层）
- `read_file`：带行号范围读取
- `write_file`：创建/追加文件
- `str_replace`：单次/全局替换

### 2.4 SubAgent System（子Agent）

- **内置Agent**：`general-purpose`（全工具）、`bash`（命令专家）
- **并发控制**：最多3子Agent/轮，15分钟超时
- **执行机制**：`task()` 工具 → `SubagentExecutor` 后台线程池 → poll 5s → SSE events → 结果
- **事件**：task_started / task_running / task_completed / task_failed / task_timed_out

### 2.5 Skills + MCP 扩展机制

**Skills系统：**
- 目录结构：`skills/{public, custom}/skill-name/SKILL.md`
- 格式：YAML frontmatter + Markdown描述
- 加载：`load_skills()` 递归扫描，解析 metadata，读取 enabled 状态
- 注入：Skills列表注入system prompt，附container paths

**MCP系统：**
- 支持：stdio / SSE / HTTP 传输协议
- OAuth：client_credentials + refresh_token 自动刷新
- 工具懒加载：首次使用时初始化，mtime缓存失效
- 传输：stdio（npm命令）、SSE、HTTP

**Gateway API routes：**
- `GET/POST /api/mcp/config` - MCP服务器配置
- `GET /api/skills` - 列出所有Skills
- `POST /api/skills/install` - 从.zip安装skill

### 2.6 Memory System（长期记忆）

- **自动提取**：分析对话提取用户上下文、事实、偏好
- **结构化存储**：UserContext(工作/个人/TopOfMind) + History + Facts
- **Debounced更新**：可配置等待时间减少LLM调用
- **System Prompt注入**：Top Facts + Context注入
- **存储**：JSON文件 + mtime-based缓存失效

### 2.7 Guardrails（防御护栏）

多层可插拔架构：
1. `GuardrailMiddleware` 预工具调用授权
2. `ClassificationMiddleware` 拦截危险分类请求
3. `DanglingToolCallMiddleware` 阻止AI幻觉调用工具
4. 支持自定义provider：Allowlist（零依赖）、OAPolicy等

---

## 三、OpenClaw现状 vs deer-flow v2.0 对比

### 3.1 现状分析

OpenClaw当前已具备：
- ✅ Agent架构（SRE/SDC/Dev/DevOps等角色模型）
- ✅ 工具系统（read/write/exec等）
- ✅ 多模型支持（Together API配置）
- ✅ Feishu飞书集成
- ✅ 工作区文件管理
- ❌ **LangGraph多Agent协作**（无）
- ❌ **沙箱隔离执行**（无，直接exec）
- ❌ **Skills+MCP扩展机制**（弱，只有skill目录）
- ❌ **持久化Memory系统**（无，仅session）
- ❌ **子Agent并行执行**（无）
- ❌ **Middleware Chain机制**（无）

### 3.2 核心差距

| 维度 | OpenClaw现状 | deer-flow v2.0 |
|------|-------------|----------------|
| Agent编排 | 无固定框架 | LangGraph状态机 |
| 沙箱隔离 | 无，direct exec | Docker/Local隔离 |
| 子Agent | 无 | 3并发/15min超时 |
| Tools扩展 | 基础 | MCP+Skills双轨 |
| Memory | 无 | 全自动提取+存储 |
| Middleware | 无 | 12个可插拔 |
| 前端 | 无 | Next.js完整UI |

---

## 四、移植方案评估

### 方案A：整体采纳
**评价：不推荐**
- OpenClaw是Node.js体系，deer-flow是Python后端
- 架构冲突（FastAPI vs OpenClaw Gateway）
- 太重，破坏现有架构

### 方案B：逐步移植（推荐）
**评价：推荐，分阶段吸收精华**

---

## 五、详细移植步骤

### Phase 1：沙箱隔离执行（优先级：⭐⭐⭐⭐⭐）

**目标：** 解决exec安全隔离问题

**需要移植的代码：**
```
backend/packages/harness/deerflow/sandbox/
  ├── sandbox.py          # 抽象接口
  ├── local.py            # 本地实现
  ├── tools.py            # bash/ls/read_file/write_file/str_replace
  └── lifecycle.py        # 生命周期管理

backend/packages/harness/deerflow/community/  # Tavily/Jina/Firecrawl等工具provider
```

**实施步骤：**

1. 创建 `sandbox/` 目录
2. 实现 `SandboxProvider` 抽象类
3. 移植 `LocalSandboxProvider`（基于Node.js child_process）
4. 移植虚拟路径系统：`/mnt/user-data/*` → 物理路径
5. 移植沙箱工具：`bash`/`ls`/`read_file`/`write_file`/`str_replace`
6. 集成进入OpenClaw的tool system

**代码量估算：** ~800行Python → ~600行TypeScript

### Phase 2：SubAgent并发系统（优先级：⭐⭐⭐⭐）

**目标：** 支持多Agent并行任务执行

**需要移植：**
```
backend/packages/harness/deerflow/subagents/
  ├── registry.py         # Agent注册表
  ├── executor.py         # 后台执行引擎
  ├── builtins/
  │   ├── general-purpose/
  │   └── bash/
  └── lifecycle events
```

**关键设计：**
- Worker线程池（3 workers + 3 executors）
- `task()` 工具调用模式
- SSE事件驱动结果收集
- 15分钟超时控制

**OpenClaw适配：**
- 在OpenClaw中实现类似 `SubagentExecutor`
- 通过Node.js `child_process` + `Worker Threads` 实现
- 定义标准task tool接口

### Phase 3：Skills + MCP扩展机制（优先级：⭐⭐⭐⭐）

**目标：** 让OpenClaw的Skills系统升级为可插拔生态

**需要移植：**
```
backend/packages/harness/deerflow/skills/
  ├── loader.py           # 递归发现 + metadata解析
  ├── SKILL.md格式定义
  └── skill路径系统

backend/packages/harness/deerflow/mcp/
  ├── client.py           # MCP客户端
  ├── cache.py            # mtime缓存失效
  ├── transports/         # stdio/SSE/HTTP
  └── auth/               # OAuth token刷新
```

**SKILL.md格式（YAML frontmatter）：**
```yaml
---
name: my-skill
description: 技能描述
allowed-tools: [bash, read_file]  # 可选白名单
---
# Markdown正文
## Workflow
...
```

**OpenClaw适配：**
- 创建 `skills/` 目录结构
- 实现 `load_skills()` 递归扫描
- SKILL.md parser（YAML frontmatter）
- MCP客户端（通过stdio调用npx @modelcontextprotocol/server-*）
- Gateway API: `GET /api/skills`, `POST /api/skills/install`

### Phase 4：Memory System（优先级：⭐⭐⭐）

**目标：** 持久化用户上下文、跨会话记忆

**需要移植：**
```
backend/packages/harness/deerflow/memory/
  ├── extractor.py        # 对话分析 + 事实提取
  ├── storage.py          # JSON持久化
  ├── queue.py            # 异步更新队列
  └── prompt_inject.py     # System prompt注入
```

**核心设计：**
- LLM分析对话 → 提取 facts/preferences/context
- 存储：JSON文件 + mtime缓存
- 异步debounced更新（减少LLM调用）
- System prompt注入 top facts

### Phase 5：Middleware Chain机制（优先级：⭐⭐⭐）

**目标：** 可插拔中间件链，增强Agent行为控制

**需要移植：**
```
backend/agents/middleware/
  ├── base.py
  ├── thread_data.py      # per-thread隔离
  ├── uploads.py          # 文件注入
  ├── summarization.py    # 上下文压缩
  ├── todo_list.py        # Plan模式追踪
  ├── title_gen.py        # 自动标题
  ├── guardrail.py        # 预授权
  └── classification.py   # 危险请求拦截
```

**OpenClaw适配（TypeScript）：**
```typescript
interface Middleware {
  name: string;
  beforeLLM?(state: AgentState): Promise<void>;
  afterLLM?(state: AgentState): Promise<void>;
  beforeTool?(tool: ToolCall): Promise<ToolCall | null>;
}

// Pipeline执行器
class MiddlewareChain {
  async execute(state: AgentState): Promise<void> {
    for (const mw of this.middlewares) {
      await mw.beforeLLM?.(state);
    }
    const result = await this.llm(state);
    for (const mw of this.middlewares.reverse()) {
      await mw.afterLLM?.(result);
    }
  }
}
```

### Phase 6：LangGraph引入评估（优先级：⭐⭐）

**目标：** 判断是否引入LangGraph作为Agent编排层

**结论：谨慎引入**
- OpenClaw目前Agent体系较轻量
- LangGraph适合复杂多步骤工作流
- 建议：仅在需要复杂状态机时引入
- 备选：考虑更轻量的XState

---

## 六、OpenClaw具体改造清单

### 6.1 目录结构新增

```
C:\Users\TL\.openclaw\workspace-main\
├── sandbox/                    # [NEW] 沙箱隔离层
│   ├── sandbox.ts              # 抽象接口
│   ├── providers/
│   │   ├── local.ts            # 本地执行provider
│   │   └── docker.ts           # Docker provider（未来）
│   └── tools/
│       ├── bash.ts
│       ├── ls.ts
│       ├── read_file.ts
│       ├── write_file.ts
│       └── str_replace.ts
├── skills/                      # [NEW/升级] Skills系统
│   ├── loader.ts               # 扫描 + 解析
│   ├── SKILL.md格式定义
│   ├── public/                 # 内置skills
│   └── custom/                  # 用户skills
├── subagent/                    # [NEW] 子Agent系统
│   ├── registry.ts
│   ├── executor.ts
│   └── builtins/
├── memory/                      # [NEW] 持久化记忆
│   ├── extractor.ts
│   ├── storage.ts
│   └── prompt.ts
├── middleware/                  # [NEW] 中间件链
│   ├── chain.ts
│   ├── thread_data.ts
│   ├── summarization.ts
│   └── guardrail.ts
└── mcp/                         # [NEW] MCP客户端
    ├── client.ts
    ├── transports/
    └── auth/
```

### 6.2 配置文件扩展

**新增 `sandbox.yamllite`：**
```yaml
sandbox:
  provider: local  # local | docker
  workspace_root: .deer-flow/threads
  virtual_paths:
    user_data: /mnt/user-data
    skills: /mnt/skills
  timeout_ms: 300000  # 5min default
  allowed_commands: [bash, ls, read_file, write_file]
```

**新增 `skills.yamllite`：**
```yaml
skills:
  public_dir: skills/public
  custom_dir: skills/custom
  auto_load: true
  metadata_cache_ttl: 3600
```

### 6.3 工具函数映射（Python → TypeScript）

| deer-flow (Python) | OpenClaw (TypeScript) |
|-------------------|----------------------|
| `execute_command(cmd)` | `bash(command)` |
| `read_file(path, lines?)` | `read(path, offset?, limit?)` |
| `write_file(path, content)` | `write(path, content)` |
| `str_replace(path, old, new)` | `str_replace(path, old, new)` |
| `list_dir(path)` | `ls(path)` |
| `task(description, type, max_turns)` | `task(description)` via SubAgent |
| `ask_classification()` | [Intrusive, via middleware] |

---

## 七、实施风险与缓解

### 风险1：沙箱安全
**风险：** 路径穿越漏洞
**缓解：** 三层路径验证（虚拟路径→物理路径映射→realpath检查）

### 风险2：MCP生态锁定
**风险：** MCP server npm包依赖
**缓解：** 通过npx动态加载，不硬绑定

### 风险3：Memory LLM成本
**风险：** 每个对话都调用LLM提取记忆
**缓解：** Debounced更新 + mtime缓存 + 可配置开关

### 风险4：Phase顺序依赖
**风险：** 后续Phase依赖前置Phase
**缓解：** 严格按Phase 1→2→3→4→5顺序

---

## 八、总结

**deer-flow v2.0的核心价值在于：**
1. **沙箱隔离** - 把exec从危险变为安全
2. **子Agent并行** - 从单Agent进化为多Agent协作
3. **Skills+MCP双轨扩展** - 让工具生态化
4. **Middleware可插拔链** - 行为控制模块化
5. **Memory持久化** - 真正的跨会话智能

**建议OpenClaw分5个Phase逐步移植，总工程量估算：**
- Phase 1（沙箱）：中，约2周
- Phase 2（子Agent）：高，约2-3周
- Phase 3（Skills+MCP）：中，约2周
- Phase 4（Memory）：中，约1-2周
- Phase 5（Middleware）：低，约1周

**优先Phase 1和Phase 3**，这两部分是deer-flow最具差异化的能力，且对现有架构侵入性最小。

---

*李元芳研究报告 · INTJ建筑师型 · 2026-03-29*
