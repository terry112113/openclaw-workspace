# L4_LEARNINGS.md - 15网站学习成果汇编

> 三司会审L4第1-18次完成，15/15网站全部学完，进入整合阶段
> 更新时间：2026-04-02 08:39

---

## 一、网页信息获取（Firecrawl / Tavily / r.jina.ai）

### firecrawl.dev — 网页抓取核心工具
- **四种模式：** Scrape（单URL）、Search（搜索+内容）、Browse（云浏览器/交互）、Crawl（批量）、Map（URL发现）
- **CLI安装：** `npx -y firecrawl-cli@latest init --all --browser` → 安装CLI+浏览器认证+skill文件
- **命令：** `firecrawl scrape`、`firecrawl search`、`firecrawl browser`
- **API：** `POST https://api.firecrawl.dev/v2/scrape` + Bearer Token
- **Python SDK：** `pip install firecrawl-py` → `app.scrape(url)` 返回markdown
- **MCP Server：** 支持Model Context Protocol，连接AI工具
- **免费额度：** 500积分/月
- **核心优势：** JS渲染+反爬全搞定，96%网站覆盖，开源102k⭐
- **Coding Agent接入：** CLI认证流程（code_challenge+session_id轮询），详见agent-onboarding/SKILL.md
- **触发场景：** 任意网页→干净Markdown→直接喂LLM

### tavily.com — AI联网搜索
- **三大端点：** `/search`（搜索）、`/extract`（网页提取）、`/research`（深度研究）
- **Python SDK：** `pip install tavily-python`
- **性能：** p50=180ms，99.99% SLA，1M+开发者信任
- **免费额度：** 1000次/月
- **安全层：** 内置PII过滤、prompt injection拦截
- **触发场景：** AI Agent联网大脑，替代Perplexity做程序化搜索

### r.jina.ai — LLM阅读接口
- **用法：** `https://r.jina.ai/https://目标URL` → 直接返回Markdown
- **免费：** 无需API Key
- **限制：** 第三方依赖，JS渲染页面效果不稳定
- **触发场景：** 轻量快速网页转Markdown，与Firecrawl互补

---

## 二、AI搜索与研究（Perplexity）

### perplexity.ai — AI精准问答搜索
- **官方MCP服务器：** github.com/perplexityai/modelcontextprotocol（2k⭐）
- **MCP工具：** perplexity_search/ask/research/reason
- **支持：** Claude Code/Cursor/Windsurf/VS Code
- **API：** Sonar免费1M tokens/月；Sonar Pro $5/1M input tokens
- **标准chat completions格式：** curl可直接调
- **核心限制：** 无原生embedding，不适合标准RAG
- **核心优势：** Pro Search技术类查询质量高，citations引用准确
- **对比：** perplexity vs tavily = 质量 vs 广度
- **触发场景：** 精准技术问答替代传统搜索

---

## 三、工具与自动化集成（Composio / Zapier）

### composio.ai — 500+工具统一集成平台
- **架构：** 学一个API = 能用500+工具（GitHub/Slack/Gmail/Salesforce等）
- **调用模式：** `composio.tools.get('default', 'GITHUB')` → 获取工具 → `composio.tools.execute('TOOL_SLUG', {...})`
- **HITL安全机制：** agent准备执行但需人类批准（重要！）
- **多用户session：** 支持
- **安装：** `pip install composio-core`
- **主站状态：** 被墙（522），用Tavily WebSearch获取信息
- **触发场景：** 需要集成外部SaaS工具时优先考虑

### zapier.com — 6000+App自动化（低优先级）
- **本质：** 人类SaaS自动化工具，非API-first平台
- **问题：** 需要人类在网页配置，OAuth配置复杂
- **结论：** Agent难以直接调用，暂缓深度学习

---

## 四、开源模型与AI（HuggingFace / GitHub）

### huggingface.co — 开源模型生态
- **核心产品：** Transformers（158k⭐）、Diffusers（33k⭐）、smolagents（26k⭐）、Transformers.js（15k⭐）
- **PEFT：** 模型轻量化微调技术
- **Inference API：** pip install huggingface_hub → 申请Token → 直接调用
- **Spaces：** 免费托管ML应用的空间
- **触发场景：** 调用开源模型执行任务（embedding/OCR/图像分类等）

### github.com — 代码与协作平台
- **openclaw-ai组织：** 344k⭐主仓，23个仓库
- **关键项目：**
  - lobster（OpenClaw工作流引擎）
  - smolagents（HuggingFace Agent框架）
  - transformers.js（浏览器端ML）
- **高级功能：** Actions（CI/CD）、Codespaces（云端开发）、Copilot（AI编程）
- **触发场景：** 代码管理、开源协作、日常开发效率

---

## 五、消息通讯（Telegram / Discord）

### Telegram Bot — 最易集成的消息通道
- **核心：** Token认证，getUpdates（长轮询）vs setWebhook（推送）
- **申请：** @BotFather三步创建bot
- **API特性：** 简单成熟，送达率高
- **OpenClaw集成：** 已有message工具支持
- **触发场景：** Agent推送通知、简单指令交互

### Discord — 复杂但强大
- **Webhook：** 30次/分限制，2000字符上限，适合通知推送
- **Bot模式：** OAuth2 URL公式+Gateway Intents+Privileged Intents（需Discord审批）
- **复杂性：** 比Telegram难配置，WebSocket长连接
- **触发场景：** 需要频道管理、复杂权限结构时

---

## 六、生态与工具平台（ClawHub / OpenClaw主站）

### clawhub — Agent技能市场
- **安装：** `npx clawhub@latest install <skill-name>`
- **热门skill：** X Search、Trello、Slack、Caldav Calendar等
- **版本化管理：** 支持rollback，向量搜索可发现性
- **触发场景：** 找现成skill直接用，无需自己开发

### openclaw.ai — 主站
- **核心能力：** 持久记忆、浏览器控制、全系统访问、50+集成
- **安装：** `powershell -c "irm https://openclaw.ai/install.ps1 | iex"`
- **关键文档：** Platform capabilities、Configuration options、Gateway/daemon setup、Extension points
- **命令：** `openclaw doctor --fix`（诊断修复）、`openclaw gateway start/stop/restart`
- **docs.openclaw.ai状态：** 需验证可访问性
- **触发场景：** 平台配置、故障诊断、能力扩展

---

## 七、自主进化机制（self-improving-agent）

### learnings/目录模式
- **文件：** LEARNINGS.md、ERRORS.md、FEATURE_REQUESTS.md、CHANGELOG.md
- **触发条件：** 用户纠正/发现更好做法/任务完成回顾/知识过时时记录
- **晋升机制：** 反复出现3次→晋升AGENTS.md；impact>0.8→立即晋升
- **核心价值：** 知识不存档=知识没学，整理才能传承

---

## 八、学习方法论

### 被墙网站处理策略
- **症状：** 522超时/连接失败
- **解决思路：** ①Tavily WebSearch获取信息 ②Firecrawl尝试抓取 ③找镜像站
- **适用：** composio.ai等被墙网站

### 三司会审应用原则
- **优先学：** 能立即产生价值的（Firecrawl、Tavily）
- **次优先：** 扩展能力的（HuggingFace、Composio）
- **最后学：** 生态类的（ClawHub、Discord）
- **跳过：** 定位不符的（Zapier人类工具，非Agent平台）

---

## 九、下一阶段建议

1. **API Key注册：** Firecrawl + Tavily → 写demo验证
2. **Composio实战：** 注册composio.ai → 测试GitHub集成
3. **Perplexity MCP：** 申请API → 集成到OpenClaw
4. **文档化维护：** 每次学习后更新本文件
