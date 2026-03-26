# 唐王李世民 - 系统自检协议
> 创建：2026-03-26 09:25 GMT+8
> 触发器：IF → THEN

---

## 🔴 熔断触发器（任一满足立即告警）

```
IF 任何cron连续失败3次 → THEN 立即上报唐王
IF 唐王自查连续失败2次 → THEN 立即上报主人
IF hot-1h.md超过2小时未更新 → THEN 强制补写并上报
IF 磁盘使用率超过90% → THEN 立即告警
IF Gateway无响应超过5分钟 → THEN 通知主人重启
```

---

## 🔍 每日健康检查清单

| 检查项 | 正常状态 | 异常状态 |
|--------|---------|---------|
| cron jobs数量 | = 7 | ≠ 7 |
| jobs.json可读 | ✅ | ❌ 重建 |
| hot-1h.md最后更新 | < 1小时 | > 1小时 |
| git状态 | clean | dirty |
| 磁盘剩余空间 | > 10GB | < 10GB |
| 5大臣下次学习 | 有计划 | 全空 |
| error计数总和 | 0 | > 0 |

---

## ⚡ 紧急恢复步骤

### 热记忆失效
1. 主session直接读取最近git commit
2. 从decisions.md/todos.json重建上下文
3. 重新生成hot-1h.md

### 三层文件损坏
1. `git log` 找回最近commit
2. `git checkout` 恢复到稳定版本
3. 从decisions.md重建

### 全面崩溃
1. 读取MEMORY.md触发器
2. 读取decisions.md历史决策
3. 按priority顺序重建：
   - PROJECT.md → todos.json → hot-1h.md

---

## 📅 自检Cron（每30分钟）

```
IF 唐王自查运行 → THEN 验证hot-1h.md更新时间
IF 更新缺失 → THEN 主session强制补写
IF 发现error → THEN 立即上报
```

---

_最后更新：2026-03-26 09:25 GMT+8_
