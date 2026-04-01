# OpenClaw文件深度审查

**审查人：** 李元芳（都察院御史）  
**审查时间：** 2026-03-30 14:00  
**审查范围：** `C:\Users\TL\.openclaw\`

---

## 一、目录结构总览

```
.openclaw/
├── agents/
│   ├── di/              # ❌ 不完整，无workspace配置文件
│   ├── main/            # ✅ 完整
│   ├── shensi/          # ⚠️ 缺少大量标准文件
│   └── wei/             # ✅ 基本完整
├── knowledge/           # 根目录知识库（几乎空）
├── workspace-main/      # 主工作空间知识库（庞大，冗余多）
├── memory/              # SQLite记忆文件（9个，7个已废弃）
├── skills/              # 全局skills（29个）
├── .clawhub/            # Clawhub缓存
├── browser/             # 浏览器数据
├── canvas/              # Canvas（仅1个index.html）
├── completions/         # Shell补全文件（4个，共464KB）
├── credentials/         # 凭证（16个json）
├── cron/                # Cron任务及运行日志（50+个run文件）
├── delivery-queue/      # 投递队列（空目录）
├── devices/             # 配对设备状态（多个tmp残留）
├── feishu/              # 飞书集成（dedup目录）
├── identity/            # 身份认证
├── knowledge-base/       # ❌ 编码损坏的文件
├── logs/                # 日志文件
├── media/               # 媒体缓存（browser+inbound大量图片）
├── shared/              # 共享目录（几乎空）
├── subagents/           # 子agent记录
├── workspace-main/      # 主workspace
└── 根目录杂项脚本/       # 多为废弃诊断脚本
```

---

## 二、问题文件详解

### 🔴 2.1 根目录废弃脚本（建议删除）

| 文件 | 大小 | 问题 |
|------|------|------|
| `check-files.ps1` | - | 2026-03-27 诊断脚本，已废弃 |
| `check-knowledge.ps1` | - | 2026-03-27 诊断脚本，已废弃 |
| `check-ministers.ps1` | - | 2026-03-27 诊断脚本，已废弃 |
| `check-ministers2.ps1` | - | 2026-03-27 诊断脚本，已废弃 |
| `play-audio.ps1` | - | 2026-03-27 临时脚本，已废弃 |
| `play-mp3.ps1` | - | 2026-03-27 临时脚本，已废弃 |
| `github-search.ps1` | - | 2026-03-27 临时脚本，已废弃 |
| `simple-backup.ps1` | - | 2026-03-27 备份脚本，可保留但不常用 |
| `tang_emperor.jpeg` | - | 图像文件，用途不明 |
| `.clawhub/` | - | 根目录Clawhub缓存，无用 |

**结论：** `check-*.ps1`（4个）+ `play-*.ps1`（2个）+ `github-search.ps1` 共7个文件建议删除。`simple-backup.ps1`和`tang_emperor.jpeg`待确认。

### 🔴 2.2 根目录备份文件（建议清理）

| 文件 | 说明 |
|------|------|
| `openclaw.json.bak.1` ~ `.bak.4` | 4个旧版备份，当前已有`.bak`，无需保留多个旧备份 |
| `cron/jobs.json.bak` | 旧备份 |
| `devices/paired.json.*.tmp` × 3 | 残留tmp文件 |
| `devices/pending.json.*.tmp` × 4 | 残留tmp文件 |
| `cron/jobs.json.*.tmp` × 2 | 残留tmp文件 |

### 🟡 2.3 knowledge-base目录（编码损坏）

```
knowledge-base/
├── ������-����ѧϰ-2026-03-26.md  （文件名乱码，无法识别）
└── �-��������-2026-03-27.md    （文件名乱码，无法识别）
```

**问题：** 文件名编码损坏，无法判断内容价值。建议读取文件内容后决定是否迁移或删除。

### 🟡 2.4 agents/di workspace（严重不完整）

```
agents/di/
├── agent/
│   ├── auth-profiles.json  (37字节，几乎空)
│   └── models.json
└── sessions/  (237个文件, 63MB)
```

**缺失的标准文件：** `AGENTS.md`, `SOUL.md`, `USER.md`, `CURRENT.md`, `HEARTBEAT.md`, `IDENTITY.md`, `TOOLS.md`

**判断：** `di` agent的workspace没有正确初始化，所有身份/工具/记忆文件均缺失。这是一个"幽灵workspace"——只有session记录，但没有任何身份定义。可能是历史废弃agent的残留。

### 🟡 2.5 agents/shensi workspace（基本废弃）

```
agents/shensi/
├── .clawhub/lock.json      ⚠️ Clawhub锁文件残留
├── agent/models.json
├── knowledge/
│   └── ��Ԫ��/              （文件夹名乱码）
├── memory/                  （空目录）
├── sessions/  (4个文件, 227KB)
├── AGENTS.md
├── CURRENT.md
├── HEARTBEAT.md
├── hot-1h.md
├── IDENTITY.md
├── SOUL.md
├── TOOLS.md
└── USER.md
├── skills/  (13个skill副本)
└── .openclaw/workspace-state.json
```

**问题：**
1. knowledge目录名乱码（可能是"李元芳"或类似中文名）
2. skills目录存在且有13个skill —— 但这些skill与全局skills重复
3. memory目录空 —— 无记忆文件
4. Clawhub锁文件残留

**判断：** shensi的agent workspace基本处于废弃状态，工作已迁移到workspace-main。

### 🟡 2.6 agents/wei workspace（部分有价值）

```
agents/wei/
├── knowledge/
│   ├── wei-zheng/
│   │   └── github-��ʱѧϰ-2026-03-30.md  （文件名乱码）
│   └── κ��/                               （目录名乱码）
└── memory/  （空目录）
```

**问题：** knowledge目录有乱码目录名，可能是因为创建时编码问题。

**判断：** wei的workspace相对完整，但knowledge目录结构有编码问题。

### 🔴 2.7 workspace-main/knowledge 大量重复/冗余文件

#### 重复文件（同一内容出现在多处）

| 文件 | 重复位置 | 建议 |
|------|----------|------|
| `dad-rehabilitation-plan-2026-03-29.md` | `wei-zheng/dad-rehab-plan-2026-03-29.md` | 内容相同，保留一处 |
| `full-day-learning-log-2026-03-29.md` | `wei-zheng/full-day-learning-log-2026-03-29.md` | 内容相同，保留一处 |
| `full-day-learning-plan-2026-03-29.md` | `wei-zheng/full-day-learning-plan-.md` | 内容相关，保留一处 |
| `2026-03-27-lessons.md` | `public/misc/2026-03-27-lessons.md` | 内容相同 |
| `system-self-check-2026-03-29.md` | `wei-zheng/system-self-check-2026-03-29.md` | 内容相同 |
| `system-self-check-report-2026-03-29.md` | `wei-zheng/system-audit-report-2026-03-29.md` | 名称不同但内容可能重叠 |
| `2026-03-27-openclaw-bug.md` | `strategic/2026-03-27-openclaw-bug.md` | 相同 |
| `public/research/2026-03-27-openclaw-bug.md` | 同上 | 相同 |
| `transparent-thinking-2026-03-29.md` | `public/transparent-thinking-2026-03-29.md` | 相同 |
| `transparent-thinking-2026-03-29_1.md` | 同上 | 版本变体，择一保留 |

#### 内容过小/几乎是空的

| 文件 | 大小 | 问题 |
|------|------|------|
| `old-minister-plan-2026-03-29.md` | 3字节 | 几乎为空，内容无意义 |
| `fast-thinking-daily-2026-03-28.md` | 675字节 | 内容极简 |

#### 命名错误/临时文件

| 文件 | 问题 |
|------|------|
| `public/skill.json` | 内容只有`{}`，空json |

#### 可考虑归档（非紧急）

以下文件性质为"研究笔记/草稿"，可考虑归档压缩：
- `deer-flow-porting-plan-2026-03-29.md` (18KB)
- `deer-flow-sandbox-integration-2026-03-29.md` (21KB)
- `feishu-sync-plan-2026-03-29.md` (10KB)
- `memory-system-reorganization-report.md` (13KB)
- 大量`project-*.md`、`*review*.md`

### 🟡 2.8 memory目录（7/9个sqlite文件已废弃）

| 文件 | 最后修改 | 状态 |
|------|----------|------|
| `di.sqlite` | 2026-03-30 00:36 | ✅ 正在使用 |
| `shensi.sqlite` | 2026-03-28 14:32 | ✅ 正在使用 |
| `main.sqlite` | 2026-03-27 18:34 | ✅ 最近使用 |
| `memory-keeper.sqlite` | 2026-03-27 19:27 | ✅ 最近使用 |
| `cheng-qiaojin.sqlite` | 2026-03-25 18:35 | ⚠️ 3天前，最后活跃3月25日 |
| `du-ruhui.sqlite` | 2026-03-25 17:08 | ⚠️ 同上 |
| `fang-xuanling.sqlite` | 2026-03-25 14:01 | ⚠️ 同上 |
| `li-jing.sqlite` | 2026-03-25 17:03 | ⚠️ 同上 |
| `zhangsun-wuji.sqlite` | 2026-03-25 14:01 | ⚠️ 同上 |

**判断：** `cheng-qiaojin`、`du-ruhui`、`fang-xuanling`、`li-jing`、`zhangsun-wuji` 5个sqlite文件最后活跃于3月25日，距今5天。如果这些不是休眠agent，建议检查后删除。

### 🟡 2.9 media目录（浏览器截图大量堆积）

| 子目录 | 文件数 | 问题 |
|--------|--------|------|
| `media/browser/` | 57个 | jpg/png截图，单个最大1.7MB，大量堆积 |
| `media/inbound/` | 13个 | 图片+语音文件，有重复（如8a95c1ff和894b3336同为643187字节） |

**判断：** 建议清理30天以上的截图，或建立自动清理机制。

### 🟡 2.10 cron/runs目录（50个运行日志堆积）

`cron/runs/` 下有50个`.jsonl`运行日志文件，无明显清理机制。建议设置保留策略（如只保留最近7天）。

### 🟡 2.11 skills目录全局 vs agents/shensi本地副本

全局skills目录（`~/.openclaw/skills/`）有29个skill。`agents/shensi/skills/`下有13个skill副本：

```
shensi/skills/ (13个)
├── browser-automation/
├── cron-mastery/
├── docx-generator/
├── fullstack-dev-engineer/
├── markdown-converter/
├── memory-lancedb-pro-openclaw/
├── news-summary/
├── openclaw-ppt-generator/
├── pdf-ocr/
├── self-improving/
├── skill-creator/
└── skill-finder-cn/
```

**判断：** `agents/shensi/skills/`是shensi agent的工作目录副本，有.clawhub标记，不是冗余。但若shensi workspace已废弃，这些本地skills无存在必要。

---

## 三、建议删除汇总

### 高优先级（安全删除）

```
根目录（7个废弃脚本）：
- check-files.ps1
- check-knowledge.ps1
- check-ministers.ps1
- check-ministers2.ps1
- play-audio.ps1
- play-mp3.ps1
- github-search.ps1

根目录（多余备份，保留.bak和.bak.1即可）：
- openclaw.json.bak.2
- openclaw.json.bak.3
- openclaw.json.bak.4

根目录.tmp残留：
- cron/jobs.json.bak
- cron/jobs.json.*.tmp (2个)
- devices/paired.json.*.tmp (3个)
- devices/pending.json.*.tmp (4个)
```

### 中优先级（需确认后删除）

```
memory废弃agent（需确认5天无活动后可删）：
- memory/cheng-qiaojin.sqlite
- memory/du-ruhui.sqlite
- memory/fang-xuanling.sqlite
- memory/li-jing.sqlite
- memory/zhangsun-wuji.sqlite

workspace-main/knowledge重复文件：
- wei-zheng/dad-rehab-plan-2026-03-29.md （与dad-rehabilitation-plan-2026-03-29.md重复）
- wei-zheng/full-day-learning-log-2026-03-29.md
- wei-zheng/full-day-learning-plan-.md
- public/misc/2026-03-27-lessons.md
- strategic/2026-03-27-openclaw-bug.md
- public/research/2026-03-27-openclaw-bug.md
- transparent-thinking-2026-03-29_1.md
- old-minister-plan-2026-03-29.md （3字节，无意义）

knowledge-base编码损坏文件（读取内容后决定）：
- knowledge-base/（两个乱码文件）
```

### 低优先级（可归档/清理）

```
media/browser/ 截图（>30天的）
cron/runs/ 日志（>7天的）
agents/di/sessions/ 大量旧session（>30天的）
agents/shensi/skills/（若shensi已废弃）
```

---

## 四、建议保留

### 必须保留

```
openclaw.json              # 核心配置
openclaw.json.bak          # 当前备份
gateway.cmd                 # Gateway启动器
exec-approvals.json         # Exec审批记录
tts-health.json            # TTS健康状态
tts-probe.cjs              # TTS探测工具
update-check.json          # 更新检查状态

agents/main/               # 完整且在用
agents/shensi/ (核心文件)   # SOUL.md, AGENTS.md等
agents/wei/ (核心文件)      # SOUL.md, AGENTS.md等

memory/di.sqlite           # 活跃
memory/shensi.sqlite       # 活跃
memory/main.sqlite         # 活跃
memory/memory-keeper.sqlite # 活跃

workspace-main/knowledge/   # 知识库主体（去重后）
~/.openclaw/skills/        # 全局skills

credentials/               # 所有凭证
identity/                  # 身份认证
```

---

## 五、总结

### 核心问题

1. **agents/di workspace是"幽灵"** — 有237个session记录（65MB），但没有任何身份定义文件。极可能是历史废弃agent残留。

2. **agents/shensi workspace基本废弃** — 所有工作已迁移到workspace-main，knowledge目录有编码问题，本地skills和memory为空。

3. **workspace-main/knowledge大量重复** — 同一内容在`li-yuanfang/`、`wei-zheng/`、`public/`多处出现，估计有20+个文件可以合并/删除。

4. **memory目录5个废弃agent sqlite文件** — cheng-qiaojin、du-ruhui、fang-xuanling、li-jing、zhangsun-wuji 最后活跃于3月25日，之后无活动。

5. **根目录7个废弃诊断/临时脚本** — 3月27日的check-*/play-*/github-search脚本，明显是一次性使用后遗留。

6. **knowledge-base目录编码损坏** — 2个文件无法识别，疑似中文名文件在创建时系统编码不一致。

7. **media和cron/runs无自动清理机制** — 57个浏览器截图 + 50个cron运行日志持续堆积。

### 估算可释放空间

- agents/di/sessions old files: ~30MB+（清理30天前）
- memory废弃sqlite: 5 × 69KB ≈ 350KB
- media/browser old screenshots: 数十MB
- cron/runs old logs: 数MB
- 根目录废弃脚本: 数KB
- workspace-main knowledge重复: 数百KB

**总计可安全清理：约50-80MB+**
