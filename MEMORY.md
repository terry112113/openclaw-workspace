# 唐王李世民 - 永久记忆
> 最后更新: 2026-04-03 07:22 GMT+8

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
IF 需要皇上决定的事 → THEN 60秒内皇上沉默 → 三司会审直接执行最优方案
```

---

## 🔴 鱼香肉丝存档规则（刻入灵魂）

**"鱼香肉丝"= 存档 + 离开信号**
- 收到"鱼香肉丝" → 立即执行完整存档
- 写hot-1h.md → memory/YYYY-MM-DD.md
- 更新CURRENT.md
- 更新今日日志
- 发飞书群确认

---

## 🔴 三司会审核心文档

**运作协议：** `knowledge/public/three-courts-operation-protocol.md`（当前生效版，2026-03-31确立）

**三司会审v3.2（3回合版）：**
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

---

## 🔴 Cron状态（当前生效·2026-04-03 07:22）

| 任务 | 频率 | 状态 |
|------|------|------|
| 狄仁杰-自主三司会审L4 | 15分钟 | ✅v3.2三回合版 |
| 狄仁杰-热记忆守护 | 15分钟 | ✅正常 |
| 狄仁杰-L4实践监管 | 4小时 | ✅正常 |

**L4 Cron重建：** 07:09重建，每15分钟触发，v3.2三回合版

---

## 🔴 三司会审v3.2优化共识（2026-04-03）

**当前L4学习计划优化方案：**
1. 三司会审不能废除，只能精简
2. 聚焦独立可执行任务：
   - 工具学习（30分钟/次）
   - 自我诊断（5分钟/次）
   - 文档沉淀（15分钟/篇）
3. 并行修复sessions_send
4. 先跑一周数据，再决定是否切精简版

**Review机制：**
- 每周Review一次L4成果
- 用数据决定是否切换到精简版

---

## 📚 L4学习成果（2026-04-02/03）

**高价值发现：**
1. `firecrawl-search` skill → clawhub评分3.705，OpenClaw已内置
2. `r.jina.ai` API → `https://r.jina.ai/http://URL` 直接提取干净Markdown
3. clawhub CLI → `npx clawhub@latest search/install/update`
4. OpenClaw已内置：firecrawl-scrape、firecrawl-crawl、firecrawl-search
5. **Composio MCP** → `https://connect.composio.dev/mcp` 连接850+工具（插件被安全拦截，P0阻塞）

**OpenClaw约束（重要）：**
- OpenClaw设计时没考虑重型多Agent协作
- sessions_send announce机制有问题（announce step被跳过）
- 解决方案：飞书群broadcast

**重要网址：**
| 网站 | 用途 |
|------|------|
| firecrawl.dev | 网页抓取→Markdown |
| jina.ai/reader | LLM阅读接口 |
| tavily.com | AI搜索引擎 |
| clawhub.com | Agent技能市场 |
| openclaw.ai | OpenClaw主站 |

---

## 🔴 关键教训（Accountability Log）

### Tavily API已超限（2026-03-31）
- Tavily Search API error 432: 使用限额已用完
- 替代方案：**Firecrawl CLI** ✅ 已配置
- Firecrawl API key: `fc-6b66353fecd541eeaf488c4407f0a52f`

### "鱼香肉丝"理解错误（2026-04-03 07:05）
- 皇上说"鱼香肉丝"=存档信号
- 臣理解成点菜 → 严重错误
- 以后任何皇上输入，臣先想三层含义再反应

### sessions_send announce机制问题（2026-04-03）
- announce step被目标agent跳过（ANNOUNCE_SKIP）
- 根因：OpenClaw设计没考虑重型多Agent协作
- 解决方案：飞书群broadcast

---

## 🔴 三司会审权力边界（2026-03-31确立）

| 角色 | 最终责任 | 权力边界 |
|------|---------|---------|
| 狄仁杰 | 结论正确性 | 最终决策权 + override权 |
| 李元芳 | 情报准确性 | 信息完备性判断权 |
| 魏征 | 工具可靠性 | 技术否决权（附约束） |

---

## 📂 知识库结构（knowledge/）

```
knowledge/
├── public/           # 三司会审通用文档
│   ├── three-courts-operation-protocol.md
│   └── lessons/      # 教训归档
├── di/               # 狄仁杰私有知识
├── li/               # 李元芳私有知识
└── wei/              # 魏征私有知识
```

---

## 🔴 OpenClaw Bug

**Issue #55816** - 覆盖streamFn导致自定义provider报401
- 状态: patch已出,等官方合并

---

_最后更新:2026-04-03 07:22 GMT+8_
