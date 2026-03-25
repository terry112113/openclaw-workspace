# BACKUP.md - 备份与故障恢复

## 核心原则
> "参数、决策、坑，要写进文件，不要写进脑子。"

## 每日自动快照
- 每3天心跳触发一次 `git add -A && git commit`
- 快照保留最近10次

## 各Agent备份清单

### 唐王李世民
- SOUL.md, MEMORY.md, USER.md, AGENTS.md
- 备份位置：workspace-main/
- 故障恢复：从git历史恢复

### 记忆管家
- SOUL.md, AGENTS.md
- memory/hot-1h.md, warm-12h.md, cold-1d.md, weekly-7d.md, permanent.md
- 备份位置：memory-keeper/
- 故障恢复：从文件恢复

### 5位大臣
- 各自 SOUL.md, AGENTS.md
- 各自 memory/self-learning.md
- 备份位置：ministers/{name}/

## 单点故障处理

| 故障场景 | 处理方式 |
|---------|---------|
| 唐王李世民挂 | 记忆管家接管调度，通知主人 |
| 记忆管家挂 | 主人人工顶替，等待自动恢复 |
| 某大臣挂 | 其他大臣临时接管，主人分配 |
| Gateway挂 | 自动重启，5分钟无恢复则通知主人 |

## 紧急联系人
- 主人：谭练
- 飞书：唐王李世民机器人
