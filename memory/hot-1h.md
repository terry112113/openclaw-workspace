# hot-1h.md - 热记忆（每30分钟刷新）

> 最后更新：2026-04-01 02:12 GMT+8

## 🛡️ 熔断监控报告（02:12）

### ⚠️ consecutiveErrors >= 2
- `0e026d7f` 魏征-云端环境与异步执行学习 — consecutiveErrors=2（最后错误：Axios 400）

**检查时间：** 2026-04-01 01:42 GMT+8

### ⚠️ 告警：连续错误任务 (consecutiveErrors >= 2)

| 任务ID | 任务名 | consecutiveErrors | enabled | 最新错误 |
|--------|--------|-------------------|---------|----------|
| 0e026d7f | 魏征-云端环境与异步执行学习 | 2 | true | AxiosError: 400 |
| 05c374d5 | 唐王-任务预填充 | 6 | false | HTTP 401 Auth |
| cb422bc0 | 唐王-熔断监控 | 4 | false | timeout |
| cebe4ff0 | 唐王-常驻进化引擎 | 8 | false | HTTP 401 Auth |
| 4f405e27 | 魏征-每日学习GitHub | 2 | false | HTTP 401 Auth |

### 📊 Skills数量

- 全局 skills: 29
- workspace .agents/skills: 80
- 合计: 109

### 💾 热记忆新鲜度

- 最后更新: 2026-04-01 01:12 (30分钟前)
- 状态: ✅ 正常 (< 2小时)

### 📝 待皇上处理

1. **auth失效** - 多个cron任务报401错误，API Key疑似过期
   - 唐王-任务预填充 (6次连续失败)
   - 唐王-常驻进化引擎 (8次连续失败)
   - 魏征-每日学习GitHub (2次连续失败)
2. **魏征-云端环境正在失败** - 实时告警，400错误，需要检查aleph-cloud配置
