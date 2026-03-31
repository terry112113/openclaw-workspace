# hot-1h.md - 热记忆（每30分钟刷新）
> 最后更新：2026-03-31 14:12 GMT+8

## 状态: ⚠️ 熔断告警

### Cron Jobs (28个)
- ⚠️ 熔断监控(c7d511fe): enabled=true, consecutiveErrors=**2**, lastRunStatus=error(reason:timeout) **[自触发]**
- ⚠️ 李元芳-数据获取(2c9a4343): consecutiveErrors=1, lastRunStatus=error(Message failed)
- 李元芳-数据获取(2c9a4343): consecutiveErrors=1, lastRunStatus=error(Message failed)
- 其余enabled=true的jobs无异常
- 手动暂停的disabled jobs: 唐王-任务预填充(6次错误), 唐王-常驻进化引擎(8次错误), 魏征-每日Skills维护(2次错误,timeout), 狄仁杰-每日Skills维护(2次错误,timeout), 三司会审-每日复盘(1次错误,auth), 魏征-每日学习GitHub(2次错误,auth), 李元芳-每日学习skills.sh(1次错误,auth), 唐王-记忆冲突检测(1次错误,auth)
  ⚠️ 多个旧jobs因auth(401)失败，Together API key可能已失效（见TOOLS.md）

### Skills数量
- 当前: 108
- 热记忆记录: 95
- 差值: 13 (<20阈值，正常)
- 状态: ✅ 正常

### 熔断状态
- consecutiveErrors >= 2 的jobs: 无enabled态的（均已手动disabled）
- Skills数量变化: 13 < 20 ✅
- 热记忆新鲜度: 已刷新（13:42）
