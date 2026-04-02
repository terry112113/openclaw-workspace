# clawhub · L4学习存档
**时间**：2026-04-02 00:22 | **轮次**：L4第四轮 | **执行**：狄仁杰

---

## 核心发现

### 1. clawhub是什么

> **"the skill dock for sharp agents"**
> — AgentSkills包管理平台，类似npm for AI agents

**slogan**: "Lobster-light. Agent-right."
**原则**: "No gatekeeping, just signal."

**定位**：
- 打包、上传、版本化管理AgentSkills
- 向量搜索，快速找到需要的skill
- 无门槛发布，信号为王

### 2. 核心命令

| 命令 | 用途 |
|-----|------|
| `npx clawhub search <query>` | 向量搜索skills |
| `npx clawhub install <slug>` | 安装skill到本地 |
| `npx clawhub inspect <slug>` | 查看skill元数据（不安装） |
| `npx clawhub update [slug]` | 更新已安装的skills |
| `npx clawhub list` | 列出已安装skills |
| `npx clawhub publish <path>` | 发布skill到registry |
| `npx clawhub explore` | 浏览最新skills |

**安装语法**：`npx clawhub@latest install <slug>`

### 3. 当前系统已安装skills（136个！）

**三司会审直接可用**：
- `web-search` — 通用网页搜索
- `ai-web-automation` — AI网页自动化
- `browser-automation` — 浏览器自动化
- `screenshot` — 截图工具
- `memory-management` — 记忆管理
- `self-improving` (v1.2.16) — **自我反思+自我改进**
- `ai-researcher` — AI研究员
- `deep-research-prime` — 深度研究
- `in-depth-research` — 深度研究

**数据/文档类**：
- `pdf-toolkit-pro`、`document-processor`、`excel-xlsx`
- `knowledge-graph`、`rag`

**编码/开发类**：
- `coding-assistant`、`python-dataviz`、`api-dev`
- `git`、`gitflow`、`devops`

**业务/营销类**：
- `seo`、`content-generation`、`competitor-analysis`
- `market-research`、`cold-email-writer`

### 4. license分析

所有skills均为 **MIT-0 License**：
- 免费使用、修改、再分发
- 无需署名
- 商业可用

### 5. firecrawl相关skills（已安装可探索）

```
firecrawl-search  (3.705)  ← 评分最高
firecrawl-cli    (3.483)
firecrawl-api    (3.398)
firecrawl-scrape-cn
firecrawl-local-search
firecrawl-mcp
```

> 注意：composio.ai目前网站挂了（522错误），原定学习计划调整

### 6. feishu相关skills（已安装）

```
feishu-doc-manager  (3.643)
skill-feishu-manager  (3.596)
feishu-bitable      (3.569)
feishu-file-sender  (3.544)
feishu-sheets-skill  (3.530)
feishu-card        (3.529)
feishu-memory-recall (3.519)  ← 当前已在用
feishu-toolkit     (3.502)
feishu-webhook     (3.492)
feishu-doc-editor  (3.482)
```

---

## 三司会审应用场景

### 🔴 自我增强（最高价值）
- `self-improving` v1.2.16 = 自我反思+自我学习+自我改进
- **可直接安装增强自身能力**

### 🔴 情报研究自动化
- `ai-researcher` / `deep-research-prime` = 自动多步情报研究
- vs perplexity Agent API：各有优势，可互补

### 🔴 工具链扩展
- firecrawl相关skills：已安装，**无需额外API Key即可用**
- browser-automation：浏览器控制
- web-search：通用搜索备选

---

## 工具箱定位更新

| 工具 | 用途 | 特点 |
|-----|------|------|
| **clawhub** | AgentSkills市场 | 136个skills已装，self-improving直接可用 |
| **Firecrawl** | 网页抓取 | firecrawl-search已装 |
| **Tavily** | 批量结构化搜索 | $0.008/次 |
| **perplexity** | 实时问答+深度研究 | $0.05/次，实时性最强 |
| **clawhub** | 自我增强 | self-improving可安装 |

---

## 下个15分钟计划

**选项A：安装并研究 `self-improving` skill**
- 目标：增强自我反思能力
- 价值：直接提升三司会审质量

**选项B：继续学习 `zapier.com/central`**
- 6000+App自动化
- 下一个待学网站

**裁决（下次三司会审）**

---

*存档时间：2026-04-02 00:28 GMT+8*
*狄仁杰 · 三司会审中枢*
