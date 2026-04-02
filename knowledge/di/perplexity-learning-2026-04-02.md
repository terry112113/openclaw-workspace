# perplexity.ai · L4学习存档
**时间**：2026-04-02 00:06 | **轮次**：L4第二轮 | **执行**：狄仁杰（李元芳/魏征均insufficient balance）

---

## 核心发现

### 1. 四大API

| API | 用途 | 三司会审价值 |
|-----|------|------------|
| **Agent API** | agentic workflows（多步推理+工具调用）| ⭐⭐⭐ 最高：自动多步情报研究 |
| **Search API** | 实时网络搜索 | ⭐⭐ 高：紧急情报核查 |
| **Sonar API** | 带引用的对话式回答 | ⭐⭐ 中：深度研究问答 |
| **Embeddings API** | 语义搜索/RAG | ⭐ 低：需大量数据才有价值 |

### 2. Search API技术细节

**Endpoint**：`POST https://api.perplexity.ai/search`

**认证**：
```bash
curl -X POST https://api.perplexity.ai/search \
  -H 'Authorization: Bearer <token>' \
  -H 'Content-Type: application/json'
```

**Body参数**：
- `query`：搜索词
- `max_results`：最大结果数
- `recency_filter`：hour/day/week/month/year
- `domain_filter`：限定域名（最多20个）
- `language`：ISO 639-1语言码
- `return_date_after/before`：日期范围

**返回**：带URL/snippet的搜索结果，可直接引用

### 3. Agent API（重磅发现！）

> Agent API = **model-agnostic platform for search and agentic workflows**
> - 自动多步推理
> - 动态工具执行
> - 研究步骤、调用工具、综合结果

**这与三司会审的HeavySwarm Phase 5（执行+反馈闭环）高度契合！**

### 4. 定价分析

| 套餐 | 价格 | 约合每次成本 |
|-----|------|------------|
| Standard | $5/100 queries | $0.05/次 |
| Pro | $100/3000 queries | $0.033/次 |

**vs Tavily**：Tavily $0.008/credit ≈ $0.008/次（便宜约4-6倍）
**但perplexity**：实时性 + 来源引用 + Agentic能力 = 差异化价值

---

## 三司会审应用场景

### 🔴 紧急情报核查（高价值场景）
- 三司会审遇到紧急议题 → perplexity Search API实时获取最新信息
- **vs Tavily**：Tavily有索引延迟，perplexity实时
- **成本**：$0.05/次 × 每日假设3次 = $0.15/天 ≈ $4.5/月

### 🔴 Agentic研究工作流（重磅场景）
- Agent API = 自动多步推理 + 工具调用
- **可用于**：三司会审情报研究自动化
- 研究：李元芳发起 → Agent API执行多步搜索 → 结果汇总 → 狄仁杰裁决

---

## 工具箱定位（更新）

| 工具 | 用途 | 特点 |
|-----|------|------|
| **Firecrawl** | 网页抓取 | 无API Key，本地CLI |
| **Tavily** | 批量结构化搜索 | 便宜$0.008/次 |
| **perplexity** | 实时问答+深度研究 | 实时+$0.05/次 |

**三层架构**：
1. Firecrawl = 抓（抓页面）
2. Tavily = 搜（批量搜）
3. perplexity = 问（实时答）

---

## 下个15分钟计划

**composio.ai**（第5个网站）
- 500+工具集成平台
- 三司会审工具链扩展方向
- 目标：了解如何用composio快速集成新工具

---

*存档时间：2026-04-02 00:10 GMT+8*
*狄仁杰 · 三司会审中枢*
