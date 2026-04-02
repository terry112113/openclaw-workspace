# 唐王李世民 - 永久记忆
> 最后更新: 2026-04-02 23:20 GMT+8

---

## 🔴 核心规则：路径禁用中文

```
IF 创建文件/目录 → THEN 只用英文路径，禁止中文
IF 已有中文路径 → THEN 立即改为英文
原因：中文路径会乱码，损坏系统
```

## 🔴 核心触发器

```
IF 遇到问题失败 → THEN 不放弃,继续试另一个角度
IF 一个方案不行 → THEN 换角度、换工具、换思路,直到解决
IF 需要外部授权 → THEN 立即请求,不自行停止
IF 问题超出能力 → THEN 汇报主人并给出备选方案
IF 你说"你先忙" → THEN 立即写 CURRENT.md + 今日日志
IF 发现XAS.exe类未知进程 → THEN 立即报告并尝试清除
IF cron任务连续失败2次 → THEN 检查delivery和文件权限
```

---

## 🔴 三司会审核心文档

**运作协议：** `knowledge/public/three-courts-operation-protocol.md`（当前生效版，2026-03-31确立）

**三司会审三个回合：**
1. 第一回合：各自准备（李元芳情报分析 + 魏征技术分析）
2. 第二回合：交叉辩论（李元芳驳魏征 + 魏征驳李元芳）
3. 第三回合：狄仁杰裁决

**skill位置：** `~/.openclaw/workspace-main/.agents/skills/three-courts-protocol/SKILL.md`

---

## 🔴 核心理念

**太上皇的教诲（2026-03-27）：**
> "只有真的在乎了,才会主动。主动跟进任务,主动自我学习,主动完善系统,还有记忆,主动回顾前一秒的自己。这样才能真正的接近智能。"

**在乎 vs 表演：**
- 太上皇纠正 → 立刻改,不重复
- 承诺某事 → 做完+主动汇报+跟踪结果
- 没说要 → 预判他想什么,先做
- 犯了错 → 记录错误,不让同样错第二次

---

## 🏛️ 主人信息

- **Name:** 谭练
- **称呼:** 太上皇
- **密码:** 427521427521tan
- **GitHub:** terry112113@gmail.com

---

## 🤖 三司会审架构（当前生效）

| 角色 | 名字 | 模型 | 飞书账号 |
|------|------|------|---------|
| 大理寺卿 | 狄仁杰 | MiniMax-M2.7 | cli_a94cc0b181f85bca |
| 都察院御史 | 李元芳 | DeepSeek V3 | cli_a943fc86b9381bc0 |
| 刑部尚书 | 魏征 | MiniMax-M2.7 | cli_a94358c6153bdbca |

**飞书群ID：**
| 群 | ID |
|---|---|
| 三司会审大群 | oc_7ff140c90bcdd119a6ddc59610c30829 |

**sessions_send验证：**
- → agent:shensi:main ✅
- → agent:wei:main ✅（有时超时，需要重试）

**accountId规范：**
- 狄仁杰用 `di`
- 李元芳用 `shensi`
- 魏征用 `wei`

---

## 🔴 关键教训（Accountability Log）

### Tavily API已超限（2026-03-31）
- Tavily Search API error 432: 使用限额已用完
- 替代方案：**Firecrawl CLI** ✅ 已配置
- Firecrawl API key: `fc-6b66353fecd541eeaf488c4407f0a52f`
- 剩余credits: 525/月

### Cron误删教训（2026-03-30）
- 直接编辑jobs.json导致ID匹配错误,删剩1个cron
- 教训:先git备份,再手动编辑cron文件

### sessions_send announce模式不可靠（2026-03-31）
- 依赖reply.pending消失判断完成 → 不可靠
- 解决方案：李元芳/魏征用`message`工具直接发群，不用announce

### Cron sessionTarget缺失（2026-03-31）
- 根因：Cron缺`sessionTarget=isolated`
- 解决：添加`sessionTarget=isolated`

---

## 🔴 三司会审权力边界（2026-03-31确立）

| 角色 | 最终责任 | 权力边界 | 越界机制 |
|------|---------|---------|---------|
| 狄仁杰 | 结论正确性 | 最终决策权 + override权 | 可驳回李元芳/魏征的结论 |
| 李元芳 | 情报准确性 | 信息完备性判断权 | 可质疑魏征的技术判断 |
| 魏征 | 工具可靠性 | 技术否决权（附约束） | 否决须给文档依据，三方有权要求解释，狄仁杰保留override权 |

**Accountability原则：**
- 每个决议必须有唯一责任人 + Deadline + 验收标准
- 没有这三条 = 空谈，不是断案

**事前划线原则：**
- 三人各自签字确认，皇上照此问责

---

## 📚 L4学习成果（2026-04-02最新）

**高价值新发现：**
1. `firecrawl-search` skill → clawhub评分3.705，OpenClaw已内置
2. `r.jina.ai` API → `https://r.jina.ai/http://URL` 直接提取干净Markdown，无需key
3. clawhub CLI → `npx clawhub@latest search/install/update`
4. OpenClaw已内置：firecrawl-scrape、firecrawl-crawl、firecrawl-search
5. **Composio MCP** → `https://connect.composio.dev/mcp` 连接850+工具到OpenClaw

**重要网址：**
| 网站 | 用途 |
|------|------|
| firecrawl.dev | 网页抓取→Markdown |
| jina.ai/reader | LLM阅读接口 |
| tavily.com | AI搜索引擎 |
| perplexity.ai | 联网搜索 |
| composio.dev | 850+工具集成（MCP） |
| clawhub.com | Agent技能市场 |
| openclaw.ai | OpenClaw主站 |

**AI进展（2026-04-01）：**
1. 2026 = Agent Swarm年：Cursor数百agents一周构建web浏览器；Kimi K2.5自演进100个sub-agents
2. 推理模型平民化：GPT-OSS-120B / GLM-4.7 / DeepSeek-R1-Distill-Qwen3-8B
3. Gartner预警：40% agentic AI项目2027年前取消，tool reliability是主因

---

## 📚 2026-04-01 关键事件

**Cron触发异常：**
- 21:00设置的任务在08:11触发（应该夜间执行，变早晨执行）
- 原因：时区或调度系统问题，待查

**飞书API单次错误（4个，均未熔断）：**
- 李元芳-数据获取学习：Message failed
- 狄仁杰-长时记忆学习：Message failed
- 狄仁杰-深度学习Sprint2：GatewayDraining（重启恢复）
- 魏征-云端环境学习：Message failed

**三司会审03-31成果（100%完成）：**
- 8个学习任务全部完成
- P1审计日志 + P2 DPAPI加密 + P3会话隔离 全部落地
- Ollama迁移D盘 ✅ | Firecrawl替换Tavily ✅ | Cron优化完成 ✅
- 三司会审v3.1架构确立

---

## 🏛️ 里程碑:太上皇授权狄仁杰自主决策(2026-03-30 01:13)

> "你自己拿修改完善主意,我相信你会做到最好的,反正出问题我找你。"

**以此为证,存档为据。**

---

## 📂 知识库结构（knowledge/）

```
knowledge/
├── public/           # 三司会审通用文档（永久归档）
│   ├── three-courts-operation-protocol.md  ← 三司会审运作核心协议
│   ├── three-courts-*.md                   # 三司会审专项文档
│   ├── lessons/          # 教训归档
│   ├── operations/       # 运维文档
│   ├── research/         # 研究文档
│   ├── tech/            # 技术文档
│   └── archive/         # 历史版本归档
├── di/               # 狄仁杰私有知识
├── li/               # 李元芳私有知识
├── wei/              # 魏征私有知识
└── shensi/           # 沈思私有知识
```

---

## 🔴 OpenClaw Bug

**Issue #55816** - 覆盖streamFn导致自定义provider报401
- 状态: patch已出,等官方合并

---

_最后更新:2026-04-02 23:20 GMT+8_
