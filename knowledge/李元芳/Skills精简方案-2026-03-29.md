# Skills精简方案

**制定人：** 李元芳（INTJ建筑师）
**日期�?* 2026-03-29
**目标�?* �?22个精简�?0个核心skills

---

## 精简原则

1. **同类只保留最�?-2�?* �?避免功能重叠
2. **淘汰低使用率/可替�?* �?不常用或可被其他skill覆盖
3. **保留OpenViking重点关注项目** �?openviking系列全保�?
---

## 📋 精简后清单（50个）

### 🔧 核心系统类（8个）
| 保留 | 淘汰 | 理由 |
|------|------|------|
| skill-creator | 三司会审-brainstorm | brainstorm功能已被planning-with-files覆盖 |
| skill-vetter | memory-merger | memory合并已被memory-lancedb-pro统一管理 |
| banana-skill-finder | deep-agents-memory | 多agent记忆已被lancedb统一架构覆盖 |
| self-improving-agent | planning-with-files-zh | 中英文planning实质相同，保留英文版即可 |
| memory-lancedb-pro | | 统一记忆基础设施，保�?|
| openviking-memory | | OpenViking重点，保�?|
| planning-with-files | | 核心规划工具，保�?|

---

### 🔬 研究类（4个）
| 保留 | 淘汰 | 理由 |
|------|------|------|
| tavily-research | biomedical-search | niche领域可由tavily覆盖 |
| deep-research | medical-research | 同上，medical已被research工具覆盖 |
| academic-researcher | knowledge-synthesis | 学术研究和知识综合有重叠，保留academic更专�?|
| knowledge-synthesis | | 知识综合能力重要，保�?|

---

### ⚙️ 执行类（4个）
| 保留 | 淘汰 | 理由 |
|------|------|------|
| cron | task-execution-engine | cron是定时执行核心，task-execution-engine可被其他工具覆盖 |
| github | execution-accelerator | github是代码管理核心，execution-accelerator概念模糊 |
| github-workflow-automation | deep-productivity | 工作流自动化更具体，deep-productivity太宽�?|
| workflow-automation | | 工作流自动化实用，保�?|

---

### ✍️ 内容类（6个）
| 保留 | 淘汰 | 理由 |
|------|------|------|
| summarize | markdown-converter | markdown转换非核心，可依赖其他工�?|
| writing-plans | document-pdf | PDF处理非核心写作环�?|
| writing-skills | copywriting | 文案与内容写作有重叠，保留writing-skills更通用 |
| content-writing | technical-blog-writing | 技术博客有专精需求，保留technical-blog-writing |
| case-study-writing | press-release-writing | 两者场景不同，都保留case-study；press-release相对小众 |

---

### 📱 社媒类（3个）
| 保留 | 淘汰 | 理由 |
|------|------|------|
| twitter-thread-creation | ai-social-media-content | 通用社媒内容被具体工具覆�?|
| twitter-automation | social-content | 同上 |
| linkedin-content | linkedin-content-generation | 内容生成和内容本身重叠，保留一个即�?|
| newsletter-curation | | 新闻简报有独特价值，保留 |

---

### 🎨 多媒体类�?个）
| 保留 | 淘汰 | 理由 |
|------|------|------|
| flux-image | ai-image-generation | flux是最强开源图像生成，保留 |
| qwen-image-2 | | 国产模型补充，保�?|
| ai-video-generation | p-video | p-video功能被ai-video-generation覆盖 |
| ai-voice-cloning | elevenlabs-tts, speech-to-text, elevenlabs-stt, elevenlabs-music | 语音类太多，保留ai-voice-cloning作为核心 |

---

### 🌐 网页类（3个）
| 保留 | 淘汰 | 理由 |
|------|------|------|
| web-scraper | apify-ultimate-scraper | apify是scraper的上位替代，保留apify |
| scrapy-web-scraping | browser-automation | scrapy是专业爬虫，browser-automation范围模糊 |
| audit-website | news-briefing | 新闻简报可由tavily-research覆盖 |
| web-scraping | | 网页抓取基础能力，保�?|

---

### 📊 数据类（3个）
| 保留 | 淘汰 | 理由 |
|------|------|------|
| data-visualization | data-scientist | 可视化更直接，data-scientist范围太广 |
| python-executor | xlsx | Excel处理非核心数据分析环�?|
| python-sdk | native-data-fetching | SDK更实用，native-data-fetching概念模糊 |

---

### 🔒 安全类（3个）
| 保留 | 淘汰 | 理由 |
|------|------|------|
| security-auditor | security-requirement-extraction | 安全审计更核心，需求提取属专项 |
| memory-safety-patterns | convex-security-audit | convex审计�?niche |
| git-guardrails-claude-code | agent-governance | git guardrails更具体，agent-governance太宽�?|

---

### 🛠�?开发类�?个）
| 保留 | 淘汰 | 理由 |
|------|------|------|
| docker | devops-cicd | docker是容器化核心 |
| database-migrations-sql-migrations | postgresql-database-engineering | 数据库迁移是通用需�?|
| nosql-database-design | neon-postgres | NoSQL设计更通用 |
| apify-ultimate-scraper | | 已有但与网页类重叠，保留在开发类 |

---

### 🎯 效率类（3个）
| 保留 | 淘汰 | 理由 |
|------|------|------|
| complex-reasoning | planning-under-uncertainty | 复杂推理是核心能�?|
| critical-thinking-logical-reasoning | strategy-advisor | 逻辑推理是基础，策略建议可由其他工具提�?|
| office-productivity | | 办公效率有实际需求，保留 |

---

### 🏛�?OpenViking类（4个）
**全部保留 �?皇上重点关注项目**
| 保留 |
|------|
| openviking |
| ov-add-data |
| ov-search-context |
| ov-server-operate |

---

### 💻 UI类（2个）
| 保留 | 淘汰 | 理由 |
|------|------|------|
| ui-ux-pro-max | web-design-guidelines | ui-ux-pro-max更全�?|
| agent-ui | headlessui, chat-ui | UI类太多，保留agent-ui作为核心 |

---

### 🔧 工具类（2个）
| 保留 | 淘汰 | 理由 |
|------|------|------|
| tmux | weather | 天气非核心工�?|
| agent-tools | opencode, running-claude-code-via-litellm-copilot, running-decision-processes | agent-tools是核心，其他工具概念模糊或可替代 |

---

### 🚀 其他类（4个）
| 保留 | 淘汰 | 理由 |
|------|------|------|
| health | blockchain-developer, software-crypto-web3 | 健康有实际需求，区块链太 niche |
| self-learning | continuous-learning-v2 | 自我学习是核心能�?|
| agentic-eval | project-health | agentic-eval更核�?|
| prompt-engineering | prompt-engineering-patterns, ai-product-strategy, ai-automation-workflows, knowledge-site-creator, learning-medusa | prompt-engineering是核心，其他概念模糊或可被其他工具覆�?|

---

## 📊 精简统计

| 类别 | 原数�?| 保留 | 淘汰 |
|------|--------|------|------|
| 核心系统�?| 11 | 8 | 3 |
| 研究�?| 6 | 4 | 2 |
| 执行�?| 6 | 4 | 2 |
| 内容�?| 10 | 6 | 4 |
| 社媒�?| 6 | 3 | 3 |
| 多媒体类 | 10 | 4 | 6 |
| 网页�?| 7 | 3 | 4 |
| 数据�?| 6 | 3 | 3 |
| 安全�?| 6 | 3 | 3 |
| 开发类 | 7 | 4 | 3 |
| 效率�?| 6 | 3 | 3 |
| OpenViking�?| 4 | 4 | 0 |
| UI�?| 5 | 2 | 3 |
| 工具�?| 6 | 2 | 4 |
| 其他�?| 13 | 4 | 9 |
| **合计** | **122** | **50** | **72** |

---

## �?最终保留清单（50个）

### 核心系统�?�?1. skill-creator
2. skill-vetter
3. banana-skill-finder
4. self-improving-agent
5. memory-lancedb-pro
6. openviking-memory
7. planning-with-files
8. openviking

### 研究�?�?9. tavily-research
10. deep-research
11. academic-researcher
12. knowledge-synthesis

### 执行�?�?13. cron
14. github
15. github-workflow-automation
16. workflow-automation

### 内容�?�?17. summarize
18. writing-plans
19. writing-skills
20. content-writing
21. technical-blog-writing
22. case-study-writing

### 社媒�?�?23. twitter-thread-creation
24. twitter-automation
25. linkedin-content
26. newsletter-curation

### 多媒体（4�?27. flux-image
28. qwen-image-2
29. ai-video-generation
30. ai-voice-cloning

### 网页�?�?31. apify-ultimate-scraper
32. scrapy-web-scraping
33. web-scraping

### 数据�?�?34. data-visualization
35. python-executor
36. python-sdk

### 安全�?�?37. security-auditor
38. memory-safety-patterns
39. git-guardrails-claude-code

### 开发（4�?40. docker
41. database-migrations-sql-migrations
42. nosql-database-design
43. neon-postgres

### 效率�?�?44. complex-reasoning
45. critical-thinking-logical-reasoning
46. office-productivity

### OpenViking�?�?47. ov-add-data
48. ov-search-context
49. ov-server-operate
50. openviking

---

## 📝 精简说明

**淘汰逻辑总结�?*
- 同类保留最强者，避免功能重叠
- 概念模糊、范围太广的工具淘汰
- niche领域工具淘汰（crypto/blockchain等）
- 保留OpenViking全系列（皇上重点关注�?
**保留核心逻辑�?*
- 每个大类保留1-3个最实用�?- 跨类重复的只保留一个位�?- 保留有明确技术壁垒的工具

