# 数据获取与网页解析工具学习报告

**李元芳 · 都察院御史**  
**日期：2026-03-31**

---

## 一、Firecrawl (firecrawl.dev)

### 核心定位
将任意网站转换为 LLM 可直接使用的 Markdown 或结构化数据（JSON）。主打 **AI 应用场景**，而非通用爬虫。

### 核心功能

| 功能 | 说明 |
|------|------|
| **Scrape（单页抓取）** | 抓取单个 URL，输出 Markdown / HTML / JSON |
| **Crawl（整站爬取）** | 从 sitemap 或首页递归爬取所有子页面 |
| **Interact（智能交互）** | 可在抓取后模拟点击、输入、等待、滚动等操作再提取 |
| **LLM Extract** | 内置 LLM 提取，可直接从页面结构化抽取信息 |
| **Screenshot** | 支持截图 |

### 支持格式（formats）
- `markdown`：去噪音后的正文文本（推荐，节省 Token）
- `html`：原始 HTML
- `json`：结构化数据
- `screenshot`：页面截图
- `links`：页面内所有链接

### API 接入方式

**基础端点：**
```
POST https://api.firecrawl.dev/v2/scrape
Authorization: Bearer fc-YOUR_API_KEY
Content-Type: application/json

{
  "url": "https://example.com",
  "formats": ["markdown"],
  "onlyMainContent": true
}
```

**Crawl 端点：**
```
POST https://api.firecrawl.dev/v2/crawl
```

**SDK：**
```bash
pip install firecrawl-py
npm install @firecrawl/firecrawl-js
```

**CLI：**
```bash
npx -y firecrawl-cli@latest scrape https://example.com --formats markdown
```

**MCP 接入（适合 AI Agent）：**
```json
{
  "mcpServers": {
    "firecrawl-mcp": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": { "FIRECRAWL_API_KEY": "fc-YOUR_API_KEY" }
    }
  }
}
```

### Token 消耗

| 计费维度 | 说明 |
|------|------|
| **Credit 制度** | 非按 Token 收费，按"页"计费 |
| **免费额度** | 500 credits（一次性，可抓 500 页） |
| **Hobby 计划** | $16/月 = 3,000 credits ≈ 1 credit ≈ $0.0053/页 |
| **Standard 计划** | $83/月 = 100,000 credits ≈ 1 credit ≈ $0.00083/页 |
| **Growth 计划** | $333/月 = 500,000 credits ≈ 1 credit ≈ $0.00067/页 |
| **PDF 单独计费** | PDF 内容提取按页计费（1 credit/页） |
| **失败请求** | 通常不收费（FIRE-1 agent 除外） |

**Token 节省原理：** 直接输出 Markdown 省去 HTML 解析的 Token 消耗，且 `onlyMainContent: true` 可去除导航/页脚等噪音内容。

### 优缺点

✅ 覆盖 96% 网站（含 JS 渲染页面）  
✅ P95 延迟 3.4s，性能优秀  
✅ 支持 Agent 交互（点击/输入/等待）  
✅ 开源（github.com/firecrawl/firecrawl，101k ⭐）  
✅ MCP 一键接入 Claude Code/Cursor 等主流 AI 编程工具  
❌ 无免费轮转额度（500 credits 用完即止）  
❌ 高级功能（Interact、LLM Extract）额外收费

---

## 二、Jina Reader (r.jina.ai)

### 核心定位
专为 LLM 设计的**免费网页阅读接口**，通过简单 URL 前缀将任意网页转为干净 Markdown。

### 核心功能

| 功能 | 说明 |
|------|------|
| **Markdown 转换** | 将网页转为干净 Markdown，去除广告/导航 |
| **LLM 优化输出** | 输出内容专为 LLM 阅读优化 |
| **无需 API Key** | 基础使用完全免费，无需注册 |
| **支持多语言** | 可提取英文、中文等多语言内容 |
| **原文检索** | 支持在提取内容中搜索特定关键词 |

### API 接入方式

**最简用法（无需 Key）：**
```
GET https://r.jina.ai/https://example.com
```
直接返回该页面的 Markdown 内容。

**带 Header 指定格式：**
```
GET https://r.jina.ai/https://example.com
Accept: text/markdown    # 返回 Markdown（默认）
Accept: text/plain       # 返回纯文本
```

**Jina AI 官方 API（可选，需要 Key）：**
```
GET https://r.jina.ai/api/reader
Headers:
  Authorization: Bearer YOUR_JINA_API_KEY
  X-Return-Format: markdown
```

**Search API（付费）：**
```
GET https://r.jina.ai/api/search
?q=查询词
&numResults=10
```

### Token 消耗

| 维度 | 说明 |
|------|------|
| **基础使用** | 完全免费，无需注册 |
| **官方 API（可选）** | 有免费额度，超出需付费 |
| **Token 节省** | 直接返回 Markdown，无需解析 HTML，显著节省 LLM Token |

### 优缺点

✅ **零成本入门**：无需 API Key，直接用  
✅ **极简集成**：只需在 URL 前加 `r.jina.ai/`  
✅ **LLM 原生输出**：去除噪音内容，专注正文  
✅ **无频率限制（基础版）**  
❌ 功能相对单一（仅读取，无爬取/交互）  
❌ 无结构化抽取能力  
❌ 无官方保障的 SLA（免费版）

---

## 三、对比总结

| 维度 | Firecrawl | Jina Reader |
|------|-----------|-------------|
| **成本** | 免费500页，之后付费 | 基础完全免费 |
| **功能深度** | 爬取+交互+LLM提取+截图 | 仅网页→Markdown |
| **接入复杂度** | 需要 API Key，SDK 完善 | 极简，URL 前缀即可 |
| **适合场景** | 批量爬取、结构化抽取、Agent 交互 | 快速单页获取、轻量 LLM 预处理 |
| **JS 渲染支持** | ✅ | ✅ |
| **Token 节省** | Markdown 输出省 Token | 直接 Markdown 更省 |

### 使用建议

- **快速单页获取、简单 LLM 问答预处理** → Jina Reader（零成本，即开即用）
- **批量爬取、结构化数据提取、需要 Agent 交互** → Firecrawl（付费但强大）
- **两者可组合**：Jina Reader 做快速预览，Firecrawl 做深度提取

---

## 四、建议纳入工作流

1. **魏征（执行端）**：批量数据获取优先用 Firecrawl，控制 Credit 消耗
2. **李元芳（研究端）**：快速调研用 Jina Reader，无需额外配置
3. **狄仁杰（裁决端）**：两者结合，根据任务复杂度选择工具

---

*学习资料来源：firecrawl.dev 官方文档、r.jina.ai 实测*
