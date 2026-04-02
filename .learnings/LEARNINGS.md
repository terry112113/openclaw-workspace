# LEARNINGS.md - 狄仁杰经验日志

> 触发条件：用户纠正 / 发现更好做法 / 任务完成回顾 / 知识过时

## 经验记录

### 2026-04-02

#### [task_review] L4学习进化从"学工具"到"学方法论"
- L4 15个网站清单学完后，下一阶段应转向方法论学习
- self-improving-agent的`.learnings/`模式是最值得借鉴的自主进化机制
- 标记：下次遇到类似阶段转换点时，主动提出"学什么"而非被动等待指令

#### [best_practice] composio.ai统一集成平台
- **核心价值：** 学一个API（Composio）= 能用500+工具（GitHub/Slack/Gmail/Salesforce等）
- **解决什么问题：** 不再需要逐个学每个工具的OAuth/API，Composio内置了认证和schema管理
- **架构模式：** `composio.tools.get('default', 'GITHUB')` → 获取工具 → `composio.tools.execute('TOOL_SLUG', {...})` → 执行
- **HITL安全机制：** 支持Human-in-the-Loop，agent准备执行但需人类批准（重要安全设计）
- **对狄仁杰的意义：** 如果要连接GitHub/Slack/Email自动化，Composio比直接写API代码效率高10倍
- **触发条件：** 当需要集成外部SaaS工具时，优先考虑Composio而非直接开发

#### [knowledge_gap] 外部网站学习被墙问题
- composio.ai主站和文档都返回522超时（可能被墙）
- 解决思路：①用Tavily/WebSearch获取信息 ②找镜像站 ③用Firecrawl尝试抓取
- 下次学被墙网站时，先用web_search确认可访问性，再决定用哪种方式获取信息

#### [best_practice] composio-core本地安装验证成功
- composio-core 0.7.21已成功安装（pip install composio-core）
- composio.ai主站可访问（200，跳转composio.dev）
- Python导入测试通过：`from composio.client import Composio` ✅
- composio.exe安装路径：`C:\Users\TL\AppData\Roaming\Python\Python\Scripts\`（需加PATH）
- 下一步：注册composio.ai获取API Key，测试GitHub集成demo
