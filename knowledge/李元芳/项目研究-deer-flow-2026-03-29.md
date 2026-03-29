# 项目研究：deer-flow v2.0 - 字节跳动SuperAgent框架

**研究员：** 李元芳（都察院御史）  
**研究日期：** 2026-03-29  
**评级：** ⭐⭐⭐⭐⭐ 最高优先级

---

## 一、项目概览

| 属性 | 信息 |
|------|------|
| **名称** | DeerFlow (Deep Exploration and Efficient Research Flow) |
| **官方仓库** | bytedance/deer-flow |
| **Star数** | 51,800+（爆发式增长！） |
| **语言** | Python（后端）+ TypeScript（前端） |
| **赞助商** | 字节跳动 |
| **官网** | https://deerflow.tech |
| **重大里程碑** | **2026年2月28日登顶GitHub Trending #1！** |
| **版本** | v2.0 完全重写（与v1无共享代码） |

**一句话定位：** 开源的长时域SuperAgent框架，通过沙箱、记忆、工具、技能、子Agent组合，实现"研究-编码-创作"一体化。

---

## 二、核心架构

### 2.1 从Deep Research到Super Agent Harness

```
Deep Research（深度研究）
    ↓ 扩展
Super Agent Harness（超级Agent工具链）
    ├── Sub-Agents（子Agent编排）
    ├── Memory（记忆系统）
    ├── Sandboxes（隔离执行环境）
    ├── Skills（技能扩展）
    ├── Tools（工具集）
    └── Message Gateway（消息网关）
```

### 2.2 核心技术栈

| 组件 | 技术 |
|------|------|
| **Agent框架** | LangGraph |
| **前端** | React/TypeScript |
| **沙箱** | Docker / Kubernetes |
| **消息通道** | Telegram, Slack, 飞书/Lark |
| **追踪** | LangSmith |
| **MCP** | 支持MCP Server扩展 |

### 2.3 核心能力矩阵

| 能力 | 说明 |
|------|------|
| **Sub-Agent编排** | 多Agent协作，分工执行复杂任务 |
| **沙箱隔离执行** | Local/Docker/K8s三种模式，代码安全执行 |
| **长期记忆** | Memory系统持久化上下文 |
| **Skills扩展** | 可配置技能卡，扩展Agent能力 |
| **多IM渠道** | Telegram/Slack/飞书/Web |
| **MCP Server** | 支持HTTP/SSE协议的MCP服务器 |
| **LangSmith追踪** | 全链路可观测性 |

### 2.4 架构图

```
User Input
    ↓
Message Gateway（消息网关）
    ↓
Lead Agent（主导Agent）
    ├── Research Agent（研究Agent）
    ├── Coding Agent（编码Agent）
    ├── Skill Executor（技能执行器）
    └── Tool Manager（工具管理器）
    ↓
Sandbox Environment（沙箱环境）
    ↓
Memory System（记忆系统）
```

---

## 三、安装与配置

### 3.1 快速开始

```bash
# 克隆仓库
git clone https://github.com/bytedance/deer-flow.git
cd deer-flow

# 生成配置
make config

# Docker部署（推荐）
make docker-init  # 仅首次
make docker-start

# 本地开发
make install
make dev

# 访问
# http://localhost:2026
```

### 3.2 模型配置（config.yaml）

```yaml
models:
  - name: gpt-4
    display_name: GPT-4
    use: langchain_openai:ChatOpenAI
    model: gpt-4
    api_key: $OPENAI_API_KEY

  - name: deepseek-v3
    display_name: DeepSeek V3
    use: langchain_openai:ChatOpenAI
    model: deepseek-chat
    api_key: $DEEPSEEK_API_KEY
    base_url: https://api.deepseek.com/v1

  - name: claude-sonnet-4
    display_name: Claude Sonnet 4 (Claude Code OAuth)
    use: deerflow.models.claude_provider:ClaudeChatModel
    model: claude-sonnet-4-6
    supports_thinking: true
```

### 3.3 推荐模型

> "We strongly recommend using **Doubao-Seed-2.0-Code**, **DeepSeek v3.2** and **Kimi 2.5** to run DeerFlow"

### 3.4 环境变量（.env）

```bash
TAVILY_API_KEY=your-tavily-api-key
OPENAI_API_KEY=your-openai-api-key
INFOQUEST_API_KEY=your-infoquest-api-key  # BytePlus智能搜索

# IM渠道
TELEGRAM_BOT_TOKEN=xxx
SLACK_BOT_TOKEN=xxx
SLACK_APP_TOKEN=xxx
FEISHU_APP_ID=xxx
FEISHU_APP_SECRET=xxx
```

---

## 四、沙箱模式详解

### 4.1 三种执行模式

| 模式 | 说明 | 适用场景 |
|------|------|----------|
| **Local** | 直接在宿主机执行 | 开发测试 |
| **Docker** | 隔离容器执行 | 推荐生产 |
| **Kubernetes** | K8s Pod执行 | 大规模/高并发 |

### 4.2 安全隔离

代码在沙箱中执行，宿主机安全有保障。

---

## 五、Skills系统

### 5.1 Skills架构

DeerFlow的Skills是扩展Agent能力的技能卡：

```
Skills/
├── skill_1/
│   ├── manifest.yaml  # 技能描述
│   └── handler.py      # 执行逻辑
└── skill_2/
    └── ...
```

### 5.2 内置能力

- Web搜索（ Tavily / InfoQuest）
- 代码执行（沙箱）
- 文件读写
- 网页抓取

### 5.3 MCP Server集成

支持HTTP/SSE协议的MCP服务器，可扩展更多工具。

---

## 六、IM渠道集成

### 6.1 支持的渠道

| 渠道 | 难度 | 说明 |
|------|------|------|
| Telegram | 简单 | Bot API长轮询 |
| Slack | 中等 | Socket Mode |
| 飞书/Lark | 中等 | WebSocket |
| Web | - | 默认界面 |

### 6.2 飞书配置示例

```yaml
channels:
  feishu:
    enabled: true
    app_id: $FEISHU_APP_ID
    app_secret: $FEISHU_APP_SECRET
  session:
    assistant_id: lead_agent
    config:
      recursion_limit: 100
      context:
        thinking_enabled: true
```

---

## 七、与三司会审架构的集成分析

### 7.1 契合度分析

| 三司会审组件 | DeerFlow对应 | 契合度 |
|-------------|-------------|--------|
| 狄仁杰（主持/调度） | Lead Agent编排 | ⭐⭐⭐⭐⭐ |
| 李元芳（研究/监察） | Research Agent | ⭐⭐⭐⭐⭐ |
| 宋慈（执行/审判） | Coding Agent + 沙箱 | ⭐⭐⭐⭐⭐ |
| 记忆系统 | Memory System | ⭐⭐⭐⭐⭐ |
| 技能系统 | Skills + MCP | ⭐⭐⭐⭐⭐ |
| 多渠道接入 | Telegram/飞书/Slack | ⭐⭐⭐⭐⭐ |

### 7.2 关键优势

1. **LangGraph驱动** - 成熟的Agent编排，契合三司会审的流程编排需求
2. **飞书原生支持** - 太上皇已在用飞书，无缝集成
3. **沙箱安全执行** - 宋慈执行代码有安全保障
4. **Sub-Agent分工** - 自然映射李元芳(研究)+宋慈(执行)的分工
5. **LangSmith追踪** - 全链路可观测，便于审计

### 7.3 集成方案

#### 方案A：整体采纳（高投入高回报）

将deer-flow作为三司会审的**底层框架**：

```
deer-flow Lead Agent → 狄仁杰（主持）
  ├── Research Sub-Agent → 李元芳
  ├── Coding Sub-Agent → 宋慈
  └── Skill Executor → 技能系统
```

**优势：** 成熟的LangGraph编排 + 沙箱 + 记忆 + IM渠道一步到位
**风险：** 改造工作量较大，需深度定制

#### 方案B：部分采纳（低投入中回报）

仅使用deer-flow的特定能力：

1. **Skills系统** → 移植到现有架构
2. **沙箱执行** → 宋慈执行层增强
3. **Memory机制** → 长期记忆增强

**优势：** 渐进式集成，风险可控
**风险：** 可能产生架构不协调

#### 方案C：作为并行研究工具

保持现有OpenClaw三司会审架构不变，deer-flow作为专项研究/执行工具。

**优势：** 不影响现有架构，探索新技术
**风险：** 双架构维护成本

### 7.4 风险评估

| 风险 | 等级 | 应对 |
|------|------|------|
| 字节跳动技术锁定 | 低 | 支持多模型（DeepSeek/GPT等） |
| 飞书渠道依赖 | 中 | 同时支持Telegram/Slack |
| LangGraph耦合 | 中 | 可考虑独立实现核心逻辑 |
| Docker依赖 | 低 | 支持本地/K8s多种模式 |
| v2.0完全重写 | 中 | v1代码废弃，但更成熟 |

---

## 八、与OpenViking的协同分析

| 维度 | OpenViking | deer-flow | 协同效应 |
|------|-----------|-----------|---------|
| **定位** | 上下文数据库 | SuperAgent框架 | 互补 |
| **核心价值** | 记忆存储检索 | Agent编排执行 | 分层协作 |
| **我们的优先级** | 记忆系统增强 | 整体架构升级 | 可同时推进 |

**推荐组合：**
- OpenViking → 三司会审的**记忆引擎**
- deer-flow → 三司会审的**执行框架**

---

## 九、行动建议

### 9.1 立即行动（本周）
1. 部署体验deer-flow v2.0（Docker）
2. 测试飞书渠道集成
3. 评估Skills系统机制

### 9.2 短期集成（本月）
1. 评估deer-flow的LangGraph编排能否增强狄仁杰的调度能力
2. 研究将deer-flow Skills机制移植到三司会审的可行性
3. 测试沙箱执行对宋慈执行层的安全保障

### 9.3 长期规划
- 制定OpenViking + deer-flow的整合路线图
- 考虑是否将deer-flow作为三司会审的底层框架

---

## 十、参考资料

- GitHub: https://github.com/bytedance/deer-flow
- 官网: https://deerflow.tech
- Star: 51,800+
- Trending: #1（2026年2月28日）
- 文档: 项目README + CONTRIBUTING.md

---

**御史李元芳奏报完毕。**  
**建议：deer-flow v2.0架构成熟、增长迅猛，建议与OpenViking组合推进，作为三司会审架构升级的核心参考。**
