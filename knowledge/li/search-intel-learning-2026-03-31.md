# 搜索与实时情报工具学习报告

**学习人：** 李元芳（都察院御史）
**日期：** 2026-03-31
**学习对象：** Tavily + Perplexity

---

## 一、Tavily（AI优化搜索引擎）

### 1.1 平台概述
- **官网：** tavily.com
- **定位：** 专为LLM/AI Agent设计的搜索API，"Ground models with fresh web context"
- **规模：** 100M+月请求，99.99% SLA，180ms p50延迟，1M+开发者
- **融资：** 2025年完成2500万美元A轮融资
- **合作伙伴：** Databricks MCP Marketplace、IBM WatsonX、JetBrains

### 1.2 核心功能（4大API端点）

| 端点 | 用途 | 特点 |
|------|------|------|
| `/search` | 搜索查询 | 返回结构化摘要，支持搜索深度控制 |
| `/extract` | 网页内容提取 | 从URL提取markdown格式内容 |
| `/crawl` | 深度爬取 | 按指令爬取整站，支持路径过滤 |
| `/map` | 网站地图 | 发现站点结构 |
| `/research` | 深度研究 | 多源综合+引用（30-120秒） |

### 1.3 Search API核心参数

```
POST https://api.tavily.com/search
Authorization: Bearer <API_KEY>

参数：
- query: 搜索查询字符串
- search_depth: basic|advanced|fast|ultra-fast（成本：basic/fast/ultra=1积分，advanced=2积分）
- chunks_per_source: advanced模式下的分块数量（1-3，每块最多500字符）
- max_results: 返回结果数（0-20，默认5）
- topic: general|news|finance（news适合实时事件）
- time_range: day|week|month|year（时间过滤）
- include_answer: 是否返回AI摘要
- include_raw_content: 是否包含原始内容
- include_images: 是否包含图片
```

### 1.4 Search Depth详解

| 深度 | 适用场景 | 延迟 | 成本 |
|------|---------|------|------|
| `ultra-fast` | 时间关键场景 | 最低 | 1积分 |
| `fast` | 快速查询 | 低 | 1积分 |
| `basic` | 通用搜索（默认） | 中 | 1积分 |
| `advanced` | 高精度复杂查询 | 较高 | 2积分 |

### 1.5 Research API（深度研究）

```bash
tvly research "AI agent frameworks comparison" --model pro --stream
# 模型：mini(~30s) / pro(~60-120s) / auto
# 输出：带引用的结构化报告
```

### 1.6 OpenClaw集成现状

✅ **已有skill：** `tavily-research`（位于 `.agents/skills/tavily-research/SKILL.md`）
- 通过 `tvly research` CLI调用
- 支持 `--model`、`--stream`、`--json`、`--output` 等选项
- 安装：`curl -fsSL https://cli.tavily.com/install.sh | bash && tvly login`

⚠️ **问题发现：**
- Tavily API配额已超限（web_search工具返回432错误）
- 需皇上确认是否续费或升级套餐

### 1.7 适用场景
- AI Agent的实时网络搜索（减少幻觉）
- 市场调研、竞品分析
- 新闻追踪（`topic=news`）
- 结构化数据提取
- 深度研究报告（research端点）

---

## 二、Perplexity AI（联网AI答案引擎）

### 2.1 平台概述
- **官网：** perplexity.ai
- **定位：** AI答案引擎，直接回答问题并附引用来源
- **核心理念：** "Answer Engine"——不是返回链接，而是直接给答案
- **API：** api.perplexity.ai

### 2.2 核心功能

| 功能 | 描述 |
|------|------|
| 语义搜索 | 理解查询意图，不只是关键词匹配 |
| 实时联网 | 获取最新信息，支持2024-2026数据 |
| 引用来源 | 每个答案附参考来源链接 |
| 多模型支持 | sonar-small、sonar-medium、sonar-reasoning等 |
| 对话式搜索 | 支持多轮对话上下文 |

### 2.3 API基础用法

```python
# pip install perplexity
from perplexity import Perplexity

client = Perplexity(api_key="pplx-xxxx")
response = client.chat(
    model="sonar",
    messages=[
        {"role": "user", "content": "What is the latest on AI agents?"}
    ]
)
```

### 2.4 主要模型

| 模型 | 参数量 | 适用场景 |
|------|--------|---------|
| sonar-small | 小模型 | 快速简单查询 |
| sonar-medium | 中模型 | 通用搜索（默认） |
| sonar-reasoning | 推理优化 | 复杂分析任务 |
| sonar-reasoning-pro | 高级推理 | 深度研究 |

### 2.5 与Tavily对比

| 维度 | Tavily | Perplexity |
|------|--------|------------|
| **定位** | 搜索API工具 | AI答案引擎 |
| **输出** | URL+摘要+分块 | 直接答案+引用 |
| **速度** | 180ms（search） | 实时 |
| **研究深度** | research端点(30-120s) | reasoning模型 |
| **价格** | 按积分收费 | 按token收费 |
| **OpenClaw集成** | 已有skill | 无 |

### 2.6 适用场景
- 需要直接答案的查询
- 需要引用来源的研究
- 对话式信息收集
- 深度推理分析（sonar-reasoning）
- 实时新闻/事件追踪

---

## 三、李元芳总结与建议

### 3.1 两个平台的战略价值

| 平台 | 对三司会审的价值 |
|------|----------------|
| **Tavily** | 基础设施级搜索API，适合Agent自动化搜索 |
| **Perplexity** | 深度研究+推理，适合复杂议题分析 |

### 3.2 当前问题

⚠️ **Tavily API配额问题（严重）：**
```
错误：This request exceeds your plan's set usage limit
```
web_search工具依赖Tavily API，配额耗尽会影响所有联网搜索功能。

### 3.3 建议行动

1. **立即：** 皇上确认Tavily API配额状态，是否需要续费
2. **短期：** 考虑引入Perplexity作为备选搜索API
3. **中期：** 评估Perplexity API接入OpenClaw的可能性

### 3.4 附注：OpenClaw现有搜索工具

| 工具 | 底层 | 状态 |
|------|------|------|
| `web_search` | Tavily API | ⚠️ 配额超限 |
| `web_fetch` | 直接HTTP | 正常 |
| `tavily-research` skill | Tavily CLI | 待验证 |
| `deep-research` skill | 未知 | 待查 |

---

*李元芳学习报告 · 2026-03-31 11:00*
