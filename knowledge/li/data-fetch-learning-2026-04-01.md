# 数据获取与网页解析工具学习报告（第二版）

**李元芳 · 都察院御史**
**日期：2026-04-01**

---

## 零、今天学到最重要的三件事

1. **bb-browser（OpenClaw原生浏览器）是最高效的提取方案** — 可以直接快照+截图，不需要额外API
2. **snapshot compact=true 返回结构化ARIA-ref** — 可以精准点击/导航，无需解析HTML
3. **Firecrawl skill文件不存在** — 可用的只有bb-browser + web_fetch + web_search

---

## 一、bb-browser（OpenClaw原生浏览器自动化）⭐ 推荐

### 核心定位
OpenClaw内置的浏览器控制工具，适合需要**交互**的网页数据提取场景。

### 工具链

| 工具 | 用途 |
|------|------|
| `browser action=status` | 检查浏览器状态 |
| `browser action=start` | 启动浏览器（Chrome） |
| `browser action=open url="..."` | 打开网页（新建标签页） |
| `browser action=navigate url="..."` | 在当前标签页导航 |
| `browser action=snapshot compact=true` | 获取页面结构（ARIA-ref格式） |
| `browser action=screenshot` | 截图 |
| `browser action=act kind=click ref="e12"` | 点击元素 |
| `browser action=act kind=type ref="..." text="..."` | 输入文本 |
| `browser action=wait` | 等待元素/URL加载 |
| `browser action=tabs` | 列出标签页 |
| `browser action=close targetId="..."` | 关闭标签页 |

### 实战演示（GitHub Trending）

**打开页面：**
```
browser action=open url="https://github.com/trending"
→ targetId: "749379384E23795E3533EE0350292440"
```

**获取快照：**
```
browser action=snapshot targetId="..." compact=true
```

返回示例（结构化数据）：
```
- article:
    - heading "microsoft / VibeVoice" [ref=e39] [level=2]:
      - link "microsoft / VibeVoice" [ref=e40]:
        - /url: /microsoft/VibeVoice
    - paragraph: Open-Source Frontier Voice AI
    - text: Python
    - link "star 33,171" [ref=e41]:
      - /url: /microsoft/VibeVoice/stargazers
      - text: 33,171
```

**精准提取的数据（2026-04-01 GitHub Trending）：**

| 仓库 | 语言 | Stars | 今日增长 |
|------|------|-------|---------|
| obra/superpowers | Shell | 128,213 | 2,620 |
| jwasham/coding-interview-university | - | 339,650 | 873 |
| microsoft/VibeVoice | Python | 33,171 | 3,863 |
| PaddlePaddle/PaddleOCR | Python | 74,206 | 439 |
| sherlock-project/sherlock | Python | 75,560 | 865 |
| neovim/neovim | Vim Script | 97,948 | 93 |

### 优点 vs 缺点

✅ 内置，无需API Key，不花钱  
✅ 支持JS渲染（真实浏览器）  
✅ 快照+截图一体化  
✅ ref系统精准定位元素，可点击/导航  
✅ headless可用  

❌ 速度比web_fetch慢（需要渲染）  
❌ 状态管理（需要start/close）  

---

## 二、web_fetch（轻量HTTP获取）

### 特点
- 简单：`web_fetch url="..." maxChars=3000`
- 返回Markdown格式
- 今天实测：news.ycombinator.com 连不上（fetch failed）
- 受网络/DNS/防火墙影响

### 使用场景
- 静态页面快速获取
- 不需要渲染的页面
- API接口调用

---

## 三、web_search（Tavily搜索）

### 特点
- 结构化搜索结果
- 今天的错误：`Tavily Search API error (432)` — 额度用尽
- 每5天刷新100次额度

---

## 四、Firecrawl工具（现状）

### 发现
**Firecrawl skill文件不存在。** `~/.openclaw/skills/firecrawl-*` 目录存在但无内容。

可用的是 `bb-browser`（浏览器自动化），原理等同于Firecrawl的`scrape`+`interact`能力。

### 如果未来要启用Firecrawl
需要：
1. 申请API Key（firecrawl.dev）
2. 通过MCP或CLI接入
3. 注意Credit消耗（$0.005-0.0007/页）

---

## 五、工具选择决策树

```
任务类型
├── 静态页面/无需交互
│   ├── 快速预览 → web_fetch（免费）
│   └── 批量提取 → Jina Reader / Firecrawl（需Key）
│
├── 需要浏览器渲染
│   ├── 单页/需交互 → bb-browser（内置，无需Key）✅
│   └── 批量/深度 → Firecrawl（需API Key）
│
└── 搜索
    └── Tavily web_search（有额度时）
```

---

## 六、最佳实践总结

### 李元芳的标准工作流

**Step 1：评估页面复杂度**
- 静态内容 → `web_fetch`
- JS渲染/交互 → `bb-browser`

**Step 2：bb-browser标准操作**
```
1. browser action=start
2. browser action=open url="目标URL"
3. browser action=snapshot compact=true  → 分析结构
4. 根据需要 browser action=act 点击/输入
5. browser action=screenshot  → 保存证据
6. browser action=close  → 关闭
```

**Step 3：提取数据后**
- 写入knowledge/li/目录
- 格式：`主题-YYYY-MM-DD.md`

---

## 七、发现的问题

1. **Firecrawl skill文件缺失** → 建议找魏征部署或删除占位目录
2. **Tavily搜索额度耗尽** → 等5天后自动刷新，或换搜索方案
3. **web_fetch今天失败** → 可能是目标站点的反爬/网络问题

---

*学习日期：2026-04-01 09:30 | 实操：GitHub Trending 页面提取*
