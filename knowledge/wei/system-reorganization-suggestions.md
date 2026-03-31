# 魏征系统整理建议

**整理时间：2026-03-30**
**整理者：魏征（刑部尚书，ESTP企业家型）**

---

## 一、冗余Cron（建议删除/合并）

### 🔴 高优先级——立即处理

#### 1. 冗余：Skills维护 × 2（建议合并）
| ID | 名称 | 状态 |
|---|---|---|
| 618b25fa | 狄仁杰-每日Skills维护 | error(timeout) |
| ace0bae8 | 魏征-每日下载10个skills | error |

**问题**：两个任务都在做skills维护，重复。狄仁杰的任务每15天运行一次但timeout，魏征的任务每天运行但也error。

**建议**：
- 合并为一个cron：`魏征-Skills精选维护`（每3天运行一次）
- 减少每次处理的skills数量（每次20个而非全部）
- 删除ace0bae8

#### 2. 冗余：熔断监控 × 2（建议合并）
| ID | 名称 | 状态 |
|---|---|---|
| cb422bc0 | 唐王-熔断监控 | ok |
| 67787f65 | 狄仁杰-热记忆守护 | error(400错误) |

**问题**：两个任务都在做系统监控。熔断监控每30分钟运行正常，热记忆守护持续400错误。

**建议**：
- 禁用热记忆守护（67787f65），由熔断监控兼任
- 或者延长熔断监控的检测范围，把热记忆刷新纳入

#### 3. 冗余：热记忆刷新（建议精简）
**问题**：热记忆守护cron每15分钟刷新hot-1h.md，但文件本身在00:48之后就没有新内容了。记忆文件存在两个路径，容易混乱。

**建议**：
- 保留一个热记忆刷新机制（在三司会审-每日复盘中兼任即可）
- 删除额外的hot-1h.md（memory/目录下那个）

---

### 🟡 中优先级——重构或合并

#### 4. 李元芳研究时间碎片化（建议合并）
**现状**：
| ID | 名称 | 状态 |
|---|---|---|
| 4d3986ab | 李元芳-A-晨间预热 | error |
| 1d187fb0 | 李元芳-B-午前研究 | error |
| 258fba99 | 李元芳-深度研究 | error |
| f9246e08 | 李元芳-D-午后研究 | idle |
| fef182f6 | 李元芳-F-晚间深度 | error |

**问题**：5个碎片化的研究slot，全部error或idle，说明这套机制运转不良。

**建议**：
- 合并为**2个cron**：`李元芳-晨间研究(7:00)` + `李元芳-午后研究(14:00)`
- 删除其余3个碎片slot
- 或直接禁用这组cron，改用按需触发

#### 5. 魏征学习窗口碎片化（建议合并）
**现状**：
| ID | 名称 | 状态 |
|---|---|---|
| b79035f2 | 魏征-学习窗口A-07:00行业动态 | error |
| 14b1014c | 魏征-学习窗口B-09:00工具发现 | error |
| 5301ec6d | 魏征-学习窗口C-12:00审计方法 | idle |
| 32a327d7 | 魏征-学习窗口D-15:00安全研究 | idle |
| 000dad17 | 魏征-学习窗口E-18:00知识整理 | ok |
| 3c271e67 | 魏征-学习窗口F-20:00深度审计 | error |

**问题**：6个学习窗口碎片化，C/D运行正常（idle），E偶尔ok，A/B/F全部error。

**建议**：
- 合并为**3个cron**：
  - `魏征-晨间学习(07:00)` — 行业动态 + 工具发现
  - `魏征-午间研究(12:00)` — 审计方法 + 安全研究
  - `魏征-晚间整理(18:00)` — 知识整理 + 深度审计
- 删除其余3个

#### 6. 进化引擎与自查重复（建议合并）
| ID | 名称 | 状态 |
|---|---|---|
| cebe4ff0 | 唐王-常驻进化引擎 | error(timeout) |
| 485572e7 | 唐王李世民-高效自查 | ok |

**问题**：两个任务都在做自我优化/检查，重复。常驻进化引擎已连续9次timeout。

**建议**：
- 合并到`高效自查`中
- 删除常驻进化引擎cebe4ff0

---

### 🟢 低优先级——可保留

#### 7. 可保留的cron（状态正常）
| ID | 名称 | 状态 | 备注 |
|---|---|---|---|
| cb422bc0 | 唐王-熔断监控 | ok | 建议兼任热记忆守护 |
| 05c374d5 | 唐王-任务预填充 | ok | 正常 |
| 2e7341e0 | 李元芳-E-下班前整理 | ok | 正常 |
| 4f405e27 | 魏征-每日学习GitHub | ok | 正常 |
| 4766c28c | 三司会审-每日复盘 | idle | 22:00，重要 |

---

## 二、冗余Skills（建议删除）

### 🔴 明显无用/WHY无用

| Skill名称 | 问题 | 建议 |
|---|---|---|
| `create-sticker` | 钉钉功能，普通用户不需要 | 删除 |
| `flux-image` / `qwen-image-2` | 重复的图像生成（还有image-generation） | 保留image-generation，删除flux/qwen |
| `data-analysis` / `data-visualization` | 高度重叠，data-visualization更具体 | 合并或删除一个 |
| `video-generation` / `ai-video-generation` | 重复 | 保留一个即可 |
| `flutter-development` / `android-development` / `ios-development` | 三个移动开发skill重叠 | 保留flutter或合并 |
| `twitter-automation` / `twitter-thread-creation` | 重复 | 保留automation即可 |
| `news-briefing` / `newsletter-curation` | 重复 | 保留一个 |
| `openviking` / `openviking-memory` | 重复，memory是子集 | 保留openviking |

### 🟡 魏征不太可能用到的Skills（按功能区域）

**开发类**（魏征主执行，非开发）：
- `agent-fullstack-developer` — 太重，魏征用不到
- `frontend-dev-guidelines` — 不做前端
- `frontend-mobile-development-component-scaffold` — 不做移动开发
- `shader-programming` — 小众
- `postgresql-database-engineering` — DBA技能，魏征用不到
- `git-guardrails-claude-code` — 纯Git工具

**内容创作类**（魏征主执行，非创作）：
- `case-study-writing` — 不写案例研究
- `podcast-generation` — 不做播客
- `technical-blog-writing` — 不写技术博客
- `content-writing` — 通用内容，不适合魏征
- `linkedin-content` — 不做社媒运营
- `writing-skills` / `writing-plans` — 偏创作

**平台/工具类**：
- `apple-*`系列（apple-notes, apple-reminders等）— Windows不支持
- `1password` — 无op CLI
- `spotify-player` / `sonoscli` / `songsee` — 无音频设备
- `openhue` — 无智能家居
- `bluebubbles` / `notion` / `slack` — 无对应账号
- `obsidian-cli` — 无Obsidian
- `himalaya` — 无邮件CLI
- `tmux` — Windows不支持
- `wacli` — 用途不明

### 🟢 魏征真正会用到的Skills（建议保留重点）

| 优先级 | Skill | 用途 |
|---|---|---|
| ⭐⭐⭐ | `github` | 魏征核心职责：GitHub学习和审计 |
| ⭐⭐⭐ | `github-deep-research` | GitHub深度研究 |
| ⭐⭐⭐ | `cron` | 任务调度管理 |
| ⭐⭐⭐ | `skills-vetter` / `find-skills` | Skills维护核心 |
| ⭐⭐ | `tavily-research` | 网络研究 |
| ⭐⭐ | `web-scraper` | 数据采集 |
| ⭐⭐ | `apify-ultimate-scraper` | 高级爬虫 |
| ⭐⭐ | `deep-research` | 综合研究 |
| ⭐⭐ | `planning-with-files` | 文件规划 |
| ⭐⭐ | `knowledge-synthesis` | 知识综合 |
| ⭐⭐ | `self-improving-agent` | 自我提升 |
| ⭐⭐ | `summarize` | 摘要生成 |
| ⭐⭐ | `data-analysis` | 数据分析 |
| ⭐ | `weather` | 天气查询 |
| ⭐ | `health` | 健康提醒 |
| ⭐ | `pdf` | PDF处理 |
| ⭐ | `docx` / `xlsx` | 文档处理 |
| ⭐ | `ppt-generation` | PPT生成 |
| ⭐ | `image-generation` | 图像生成 |
| ⭐ | `security-auditor` | 安全审计 |
| ⭐ | `docker` | 容器化 |
| ⭐ | `ci-cd-pipeline` / `cicd-pipelines` | CI/CD（可能重复）|
| ⭐ | `vercel-deploy` | 部署 |

---

## 三、Workspace整理情况

### agents/wei/ 目录
**不存在**。任务要求检查`agents/wei/`但该目录不存在。
- 当前workspace根目录下没有`agents/`目录
- 三司会审agent配置在别处

**建议**：如需建立魏征专属workspace，在`.agents/`下创建`wei/`子目录。

### knowledge/魏征/ 目录
**存在**，但文件系统编码问题导致显示为乱码"κ��"。

现有文件（按内容）：
- agent配置报告 × 1
- deer-flow实验报告 × 1
- github学习日志 × 2（最新）
- opencli研究 × 1
- superpowers-brainstorm × 1
- 医疗健康管理研究 × 1
- 全局学习日志 × 2（最新）
- 系统车票分析 × 1
- 系统改进建议 × 1
- 竞品分析计划 × 1
- 项目研究-superpowers × 1

**问题**：
1. 文件命名混乱（部分中文乱码）
2. 部分文件过于庞大（如医疗健康管理18KB）
3. 全局学习日志和魏征学习日志内容可能重复

**建议**：
- 统一文件命名规范（避免中文乱码）
- 精简过大的文件
- 区分"魏征个人学习"和"全局学习日志"

### hot-1h.md 热记忆
**两处位置**：
- `hot-1h.md`（根目录，最新v2.1）
- `memory/hot-1h.md`（旧版，00:48）

**问题**：两个文件并存，容易混淆。

**建议**：统一到根目录`hot-1h.md`，删除`memory/hot-1h.md`。

---

## 四、魏征记忆整理情况

### 热记忆质量评估
**hot-1h.md（根目录）**：✅ 内容清晰，配置状态最新（10:59更新）
- 三司会审配置表清晰
- 待处理事项明确
- Skills数量标注：84个

**memory/hot-1h.md**：❌ 内容陈旧（00:48），充斥着历史告警记录
- 大量重复的熔断告警
- 建议：清理历史告警，保留最近3条有效记录即可

### 长期记忆
- `memory/2026-03-30.md` — 最新日志
- `memory/2026-03-29.md` — 前一天日志
- `memory/2026-03-28.md` — 历史
- `memory/daily-assessment.md` — 每日评估
- `memory/weekly-7d.md` — 周评估
- `memory/permanent.md` — 永久记忆

**评估**：✅ 长期记忆结构良好，定期更新

---

## 五、行动清单

### 本次立即执行
1. ✅ 删除`memory/hot-1h.md`（冗余文件）
2. ✅ 禁用热记忆守护cron（67787f65）
3. ✅ 合并Skills维护 × 2 → 1

### 下次执行
4. 合并魏征学习窗口：6个 → 3个
5. 合并李元芳研究slot：5个 → 2个（或全部禁用）
6. 删除冗余skills（见第二部分表格）
7. 整理knowledge/魏征/文件命名

### 待狄仁杰定夺
- 进化引擎与自查合并
- 李元芳研究slot是否全部重构

---

*魏征整理完毕，待狄仁杰审阅定夺。*
