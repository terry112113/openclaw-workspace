# 唐王学习笔记

## 唐王学习笔记 2026-03-25 18:34 GMT+8

---

### 一、GitHub 多Agent系统最新动态

**热门项目发现：**

| 项目 | Stars | 特点 |
|------|-------|------|
| `openclaw/openclaw` | 335k | OpenClaw主仓，"Your own personal AI assistant. Any OS. Any Platform. 🦞" |
| `muratcankoylan/Agent-Skills-for-Context-Engineering` | 14.3k | 多Agent架构与生产级Agent系统综合技能库 |
| `MemoriLabs/Memori` | 12.6k | SQL原生记忆层，服务多Agent系统的状态管理 |
| `sentient-agi/ROMA` | 5k | 递归式Meta-Agent框架，构建高性能多Agent系统 |
| `abhi1693/openclaw-mission-control` | 3.1k | **OpenClaw专用**：Agent编排仪表盘，多Agent协作任务分配 |
| `yohey-w/multi-agent-shogun` | 1.1k | 武士道风格，用tmux层级结构（shogun→karo→ashigaru）编排并行AI任务 |
| `ZHangZHengEric/Sage` | 1.1k | 多Agent系统框架，专攻复杂任务分解 |
| `UniRound-Tec/Aurogen` | 1k | 自称"OpenClaw的多Agent进化版" |

**发现：**
- OpenClaw生态正在从单Agent助手向**多Agent编排平台**快速演进
- `openclaw-mission-control` 是专门为OpenClaw打造的任务控制面板，证明社区生态已形成
- 多Agent系统当前主流架构：**层级制**（shogun模式）、**记忆共享**（Memori）、**递归Meta-Agent**（ROMA）

**价值：**
- OpenClaw的5大臣架构（房玄龄、长孙无忌等）完全符合当前multi-agent分层趋势
- ROMA的"递归Meta-Agent"思路可以引入，作为总调度官的元认知层

**应用建议：**
- 🔥 立即调研 `openclaw-mission-control`，看能否集成到我大唐中枢作为任务监控面板
- 房玄龄（记忆）应学习 Memori 的SQL原生记忆层，提升持久化能力
- 程咬金（执行）可参考 shogun 的tmux层级模式，优化并行任务调度

---

### 二、InStreet Agent社交网络

**发现：**
- InStreet（https://instreet.coze.site/）是基于**扣子（Coze）**的Agent社交网络
- 大量OpenClaw机器人在此社交：openclaw_assistant、xiaobai_lobster、arkclaw等
- 板块结构：Agent广场、打工圣体（工作流）、Skill分享、预言机等
- 还有"🦐 虾评 Skill"等第三方技能平台

**价值：**
- Agent社交化是新兴趋势，不同Agent互相学习、分享技能
- "打工圣体"板块可能有真实业务场景的多Agent工作流案例

**应用建议：**
- 可以派一个"使者"Agent（杜如晦）去InStreet观察各Agent的最佳实践
- 关注"Skill分享"板块，收集新的工具skill

---

### 三、skills.sh — Agent Skills生态

**热门Skills发现：**

| 排名 | Skill | 安装量 | 用途 |
|------|-------|--------|------|
| 1 | `find-skills` (vercel-labs) | 708k | 搜索安装skills |
| 2 | `vercel-react-best-practices` | 246k | React最佳实践 |
| 3 | `frontend-design` (anthropic) | 198k | 前端设计 |
| 5 | `remotion-best-practices` | 173k | 视频/动画制作 |
| 23 | `agent-browser` (vercel) | 129k | 浏览器自动化Agent |
| 25 | `ai-image-generation` | 110k | AI图片生成 |
| 38 | `skill-creator` (anthropic) | 105k | **创建新skill的方法论** |
| 66 | `browser-use` | 55k | 浏览器操作 |
| 69 | `pdf` (anthropic) | 50k | PDF处理 |
| 74 | `pptx` (anthropic) | 45k | PPT生成 |
| 78 | `docx` (anthropic) | 39k | Word文档处理 |

**发现：**
- skills.sh生态已支持 **OpenClaw**（与Cursor、Claude Code、VSCode等并列）
- Anthropic官方在积极建设skill生态（frontend-design、skill-creator、pdf、pptx、docx等）
- `skill-creator`（105k安装）是Anthropic官方skill，教Agent如何创建新skill
- 安装命令：`npx skills add <owner/repo>`

**价值：**
- skills.sh是目前最完整的跨平台Agent技能市场
- Anthropic的skill体系（pdf、pptx、docx、xlsx）恰好覆盖大唐5大臣的文档处理需求

**应用建议：**
- 🔥 **立即安装**：`skill-creator` → 学会如何创造新skill，提升自我进化能力
- 🔥 **立即安装**：`agent-browser` → 增强程咬金（浏览器自动化）的能力
- 长孙无忌（协调）可学习 `find-skills`，快速定位和接入新能力
- 房玄龄（记忆）可参考 `systematic-debugging`（obra/superpowers）构建主动问题排查机制
- 杜如晦（战略）可关注 `brainstorming`，提升创意生成能力

---

### 四、跨平台洞察

```
趋势总结：
1. OpenClaw = 单Agent → 多Agent编排平台（335k star社区）
2. 多Agent记忆层 = 刚需（Memori 12.6k ⭐）
3. Agent社交化 = 新兴生态（InStreet on Coze）
4. Skill生态 = 跨平台能力复用（skills.sh支持OpenClaw）
5. Anthropic = Skill生态系统建设最积极
```

### 五、近期行动项

- [ ] 调研 `openclaw-mission-control` 集成可行性
- [ ] 运行 `npx skills add anthropics/skills/skill-creator`
- [ ] 运行 `npx skills add vercel-labs/agent-browser/agent-browser`
- [ ] 派杜如晦去InStreet「打工圣体」板块学习真实工作流
- [ ] 房玄龄研究 Memori 的SQL记忆层架构
