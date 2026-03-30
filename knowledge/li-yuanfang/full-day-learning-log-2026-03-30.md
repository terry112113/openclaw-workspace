# 李元芳学习日志 — 2026年3月30日（星期一）

## B号窗口：午前研究（技术深度研究）
**执行时间：** 08:04–08:30 Asia/Shanghai

---

## 一、GitHub Trending热门项目研究

### 1. NousResearch/hermes-agent
**深度：★★★★★**
**主题：** 自进化AI Agent框架

**核心产出：**
- 内置学习循环：从经验中创建Skills，使用时自我改进，记住知识
- 支持多模型：OpenRouter(200+)、MiniMax、Kimi、GLM、OpenAI、Claude任意切换
- 多终端后端：本地Docker/SSH/Daytone/Modal/Singularity，serverless空闲不收费
- 消息平台接入：Telegram、Discord、Slack、WhatsApp、Signal
- 记忆系统：FTS5会话搜索+LLM摘要+ Honcho用户建模
- 调度系统：内置cron，支持自然语言配置定时任务
- 子Agent并行化：RPC调用，支持Python脚本
- **与OpenClaw的关系：** 支持从OpenClaw迁移（hermes claw migrate）

**对大理寺的启示：**
自进化能力是下一代Agent的核心竞争力。OpenClaw当前缺少"从对话中自动生成技能"的能力，这是值得重点关注的方向。

---

### 2. CopilotKit / CopilotKit（AG-UI Protocol）
**深度：★★★★☆**
**主题：** Agent前端框架 + Generative UI

**核心产出：**
- AG-UI Protocol已被Google、LangChain、AWS、Microsoft、Mastra、PydanticAI采用
- 核心能力：Chat UI、Backend Tool Rendering、Generative UI、Shared State、Human-in-the-Loop
- `useAgent` hook直接连接Agent与UI状态
- 支持React

**对大理寺的启示：**
AG-UI Protocol已成行业标准。飞书Bot的UI能力若要升级，应参考此协议设计。

---

### 3. obra/superpowers
**深度：★★★★☆**
**主题：** 编码Agent技能框架 + 开发方法论

**核心产出：**
- 6个自动触发的Skill：brainstorming、using-git-worktrees、writing-plans、subagent-driven-development、test-driven-development、requesting-code-review
- 核心理念：RED-GREEN TDD、YAGNI、DRY
- 支持：Claude Code插件市场、Cursor插件、Codex、OpenCode、Gemini Extensions
- 支持OpenClaw（通过clawhub）

**对大理寺的启示：**
Superpowers的"子Agent驱动开发"模式非常适合大规模任务拆分。三司会审架构可借鉴此模式：李元芳（研究）、魏征（执行）、狄仁杰（审核）的分工正是此模式的思想。

---

### 4. mvanhorn/last30days-skill
**深度：★★★☆☆**
**主题：** 全网情报聚合Skill

**核心产出：**
- 覆盖8个信号源：Reddit、Twitter/X、YouTube、HackerNews、Polymarket、Bluesky、Instagram、TikTok
- Polymarket预测市场研究：真实资金投注概率（非舆论）
- Comparative Mode：对比研究（"A vs B"）
- 自动保存到~/Documents/Last30Days/
- 支持OpenClaw（clawhub install）

**对大理寺的启示：**
对于需要全网热点追踪的研究任务，可直接使用此Skill。建议纳入常用工具库。

---

## 二、AI Agent技术趋势总结

### 2026年Q1核心技术方向：

| 方向 | 代表项目 | 成熟度 |
|------|----------|--------|
| 自进化记忆 | hermes-agent、claude-mem | 成熟 |
| MCP协议 | activepieces (~400 MCP servers) | 快速成熟 |
| AG-UI协议 | CopilotKit | 标准确立 |
| 编码专用框架 | superpowers、claude-howto | 成熟 |
| 多平台消息接入 | hermes-agent | 成熟 |
| 预测市场情报 | last30days-skill (Polymarket) | 新兴 |
| 安全沙箱 | e2b-dev/E2B、alibaba/OpenSandbox | 成熟 |
| Computer-Use Agent | trycua/cua | 快速发展 |

---

## 三、技能市场扫描（skills.sh / clawhub）

### Leaderboard热门技能：
1. microsoft/github-copilot-for-azure（215万总安装）
2. inferen-sh/skills（120万）
3. microsoft/azure-skills（200万）
4. pbakaus/impeccable（营销技能）
5. coreyhaines31/marketingskills
6. xixu-me/skills
7. jimliu/baoyu-skills

### 与OpenClaw集成的关键技能：
- `clawhub install last30days-official` — 全网情报
- `clawhub install superpowers` — 编码框架（已验证支持）

---

## 四、技术深度研究结论

### 🔬 狄仁杰（大脑）应关注的技术：
1. **MCP生态**：400+服务器，Agent连接一切的工具协议，OpenClaw需深度集成
2. **AG-UI Protocol**：Agent生成UI的行业标准，是飞书等平台升级方向
3. **自进化记忆**：Hermes的"从经验生成技能"是下一代记忆系统的标杆
4. **Serverless Agent**：Daytone/Modal模式，OpenClaw可借鉴实现更低成本

### 💡 建议太上皇考量的方向：
- 研究OpenClaw与Hermes Agent的互补性（双Agent协同？）
- 跟进AG-UI Protocol在飞书生态的落地可能性
- 评估将superpowers开发方法论融入三司会审流程

---

## C号窗口：午前总结（知识整理归档研究）
**执行时间：** 11:02–11:10 Asia/Shanghai

---

## 一、现状诊断：两套知识库并存的混乱

### 1.1 当前目录结构

```
knowledge/
├── README.md                    ← 唐王知识库（旧）
├── strategic/                   ← 战略洞察
├── lessons/                     ← 失败教训
├── minister-reports/            ← 大臣汇报
│
├── public/                      ← 公共知识库（新 2026-03-28）
│   ├── research/                ← 研究报告
│   ├── operations/              ← 运营文档
│   ├── tech/                    ← 技术文档
│   ├── misc/                    ← 其他
│   ├── lessons/                ← 教训（重复！）
│   ├── 中医知识/                ← 特殊分类
│   └── 20+个md文件
│
├── 李元芳/                      ← 臣的学习日志
├── 魏征/                        ← 魏征的学习日志
└── (2个残留文件夹)
```

### 1.2 核心问题

| # | 问题 | 严重度 |
|---|------|--------|
| 1 | 两套README并存，`knowledge/README.md`（唐王）和`knowledge/public/README.md`（宋慈）无主次 | 🔴高 |
| 2 | 文件名中文乱码（PowerShell编码问题），严重影响可读性 | 🔴高 |
| 3 | `knowledge/public/lessons/`与顶层`lessons/`重复 | 🟡中 |
| 4 | 大臣文件夹（李元芳/魏征）无归档规范，日志无限累积 | 🟡中 |
| 5 | 无知识检索能力（无embedding provider） | 🔴高 |
| 6 | 无定期清理/合并机制 | 🟡中 |
| 7 | `minister-reports/`自2026-03-27后再无更新，已实质废弃 | 🟢低 |

---

## 二、行业最佳实践研究

### 2.1 Hermes-Agent的记忆系统（闭环学习）

```
经验 → 生成Skill → 使用中改进 → 定期"轻推" → 记住知识
```

**关键机制：**
- **触发性归档**：任务完成后自动创建Skill记录方法论
- **进化性**：Skill在使用中被改进，而非静态存储
- **FTS5检索**：全文搜索跨session历史对话

### 2.2 三司会审三层记忆架构（魏征设计）

```
工作记忆（当前会话）→ 情景记忆（按日归档）→ 长期记忆（知识库）
     ↑                                              │
     └──────── 按需读取（检索式加载）←───────────────┘
```

**沉淀触发规则（已被设计但未严格执行）：**
```
IF 某经验在 ≥3个会话中被验证 AND 主人认可
   THEN → 沉淀至 knowledge/public/对应分类/
```

### 2.3 知识归档的生命周期

| 阶段 | 存储位置 | 状态 | 触发条件 |
|------|----------|------|----------|
| 新生 | 会话中 | 活跃 | 产生即记录 |
| 归档 | memory/YYYY-MM-DD.md | 待萃取 | 会话结束/阈值触发 |
| 沉淀 | knowledge/ | 待审核 | ≥3次验证+主人认可 |
| 废弃 | — | 删除 | 过时/错误/无价值 |

---

## 三、臣的整改建议

### 3.1 立即可执行（臣自主完成）

**① 统一知识库入口**
- 保留 `knowledge/public/` 作为唯一标准结构
- 将 `knowledge/README.md`（唐王知识库）降级为"历史参考"
- 顶层 `strategic/`、`lessons/`、`minister-reports/` 合并入 `public/`

**② 文件名修复**
- PowerShell输出中文乱码问题：改用UTF-8 BOM编码保存文件名
- 对已存在的乱码文件，重新生成规范命名的备份

**③ 李元芳/魏征日志归档**
- 建立"学习日志"子目录：`knowledge/李元芳/logs/`
- 每个log文件命名：`全天学习日志-YYYY-MM-DD.md`（已有）
- 设置阈值：单文件夹>20个文件时，触发月度合并摘要

**④ 建立沉寂文件识别**
- 识别标准：距今>14天、无更新、无引用
- 沉寂文件统一移入 `knowledge/public/misc/归档/`

### 3.2 需要皇上授权（建议）

**① 语义检索能力（memory search）**
- 配置embedding provider（voyage/openai/gemini）
- 臣即可跨session语义搜索，而非仅靠文件名

**② 知识沉淀审核**
- 建立沉淀审核机制：臣提出 → 狄仁杰审核 → 皇上确认
- 避免无效知识入库浪费空间

**③ 古籍知识库整理**
- `knowledge/public/中医知识/` 含3个大文件（约1.8MB）
- 是否需要？是保留还是删除？

---

## 四、产出：C窗口知识整理规范（草案）

### 文件命名规范
```
{日期}-{类型简称}-{主题}.md

类型简称：
  rl  = 研究学习 (research/learning)
  op  = 运营操作 (operations)
  tc  = 技术文档 (tech)
  ls  = 教训总结 (lessons)
  st  = 战略洞察 (strategic)
  mr  = 大臣汇报 (minister-report)
  nt  = 日常笔记 (notes)
  ar  = 归档文件 (archived)
```

### 归档阈值规则
```
李元芳/logs/    → 单日log不压缩；满30天触发月度摘要
knowledge/public → 沉寂>14天 → 移入 misc/归档/
minister-reports → 沉寂>7天 → 标记废弃，不再更新
```

### 知识入库触发器（修订）
```
IF [在某领域有明确结论] AND [≥1次实践验证] AND [主人认可]
   THEN → 写入 knowledge/public/{分类}/

IF [结论被后续事实推翻] OR [超过90天未引用]
   THEN → 标记废弃 or 删除
```

---

## 五、发现：知识库与记忆系统的断链

**核心问题：**
三司会审设计了"三层记忆架构"（工作→情景→长期），但**执行断链**：

| 设计 | 执行 |
|------|------|
| 情景记忆归档至 memory/ | ✅ 正常运作 |
| 长期记忆沉淀至 knowledge/ | ❌ 无标准流程 |
| 语义检索能力 | ❌ 无embedding provider |
| 定期"轻推"机制 | ❌ 仅cron时醒着 |

**根本原因：** 架构设计超前，执行机制未跟上。

**下一步建议（等皇上授权）：**
1. 配置embedding provider → 解锁语义检索
2. 建立"知识沉淀"SOP → 让经验真正入库
3. 给臣加"每日自检"cron → 定期轻推自己该归档什么

---

**学习完成。记录人：李元芳 | 2026-03-30 11:10**
