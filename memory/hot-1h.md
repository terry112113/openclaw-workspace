# hot-1h.md - 热记忆（每30分钟刷新）

> 最后更新：2026-03-29 10:55 GMT+8

## 🛡️ 守护cron运行
- 时间：10:55（每30分钟自动刷新）
- 状态：⚠️ 存在告警

## 🔴 [10:55] 熔断告警：API Key认证失败（4个cron任务异常）
- 影响：4个cron任务因API Key无效（****f922）连续失败
  - 唐王-熔断监控：consecutiveErrors=6（认证失败）
  - 唐王-任务预填充：consecutiveErrors=6（认证失败）
  - 唐王-常驻进化引擎：consecutiveErrors=8（认证失败）
- 原因：Together API Key已失效或过期
- 建议：检查TOGETHER_API_KEY环境变量，更新有效API Key
- 参考：TOOLS.md中配置的Key格式为sk-api-00WUwOscj89WAowb4Q4y1j3w8...

## 🔴 [10:55] 熔断告警：2个cron任务被意外禁用
- 影响：
  - 唐王-任务预填充（05c374d5）：enabled=false
  - 唐王李世民-高效自查（485572e7）：enabled=false
- 建议：确认禁用是否预期，如非预期则重新启用

## ⚠️ [10:55] Skills维护cron运行异常
- 影响：狄仁杰-每日Skills维护今日10:00运行超时（consecutiveErrors=1）
- 建议：检查维护任务执行时间，若持续超时考虑延长timeoutSeconds

## 飞书群ID绑定（已确认）
- oc_8365b711161460f315a825dcd8c3fe37 → 狄仁杰专属群
- oc_ee79942352d38d8320ced1db0fc207c7 → 李元芳专属群
- oc_715234420dd4fceb5acc726708e358f5 → 魏征专属群

## 待解决问题
- [ ] 飞书群里@用户的方法（message工具在群里发送失败）

---

*热记忆·2026-03-29 10:15·守护中*
