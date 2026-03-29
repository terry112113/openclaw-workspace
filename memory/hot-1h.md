# hot-1h.md - 热记忆（每30分钟刷新）

> 最后更新：2026-03-29 12:55 GMT+8

## 🛡️ 守护cron运行
- 时间：12:55（每30分钟自动刷新）
- 状态：⚠️ 存在已知告警（无新增恶化）

## 🔴 [11:55] 熔断告警：Skills维护cron连续超时（consecutiveErrors=2）
- 影响：狄仁杰-每日Skills维护（618b25fa）连续2次执行超时
  - 上次运行：2026-03-29 11:55（刚执行完）
  - 前次运行：2026-03-29 10:00（也超时）
  - consecutiveErrors: 1 → 2（⚠️ 升级）
- 原因：任务执行时间超过600秒timeout限制
- 建议：延长timeoutSeconds至900或1200，或拆分审核任务分批执行
- 状态：enabled=true（仍在运行，但持续超时）

## 🔴 [11:55] 熔断告警：API Key认证失败（2个cron任务异常）
- 影响：2个cron任务因API Key无效（****f922）连续失败
  - 唐王-任务预填充：consecutiveErrors=6（认证失败，已禁用）
  - 唐王-常驻进化引擎：consecutiveErrors=8（认证失败，已禁用）
- 原因：Together API Key已失效或过期
- 建议：检查TOGETHER_API_KEY环境变量，更新有效API Key
- 参考：TOOLS.md中配置的Key格式为sk-api-00WUwOscj89WAowb4Q4y1j3w8...

## 🔴 [11:55] 熔断告警：多个cron任务被禁用（长期观察）
- 影响：
  - 唐王-任务预填充（05c374d5）：enabled=false（auth问题）
  - 唐王李世民-高效自查（485572e7）：enabled=false
  - 狄仁杰-热记忆守护（67787f65）：enabled=false（timeout问题）
  - 唐王-记忆冲突检测（7b9eb04e）：enabled=false（auth问题）
  - 魏征-每日下载10个skills（ace0bae8）：enabled=false
  - 宋慈-整理公共知识库（584f1176）：enabled=false
  - 李元芳-整理公共Skills（670e8ad2）：enabled=false
  - 魏征-整理公共知识库（f73a226e）：enabled=false
  - 唐王-常驻进化引擎（cebe4ff0）：enabled=false（auth问题）
- 建议：确认禁用是否预期，如非预期则重新启用；auth问题需先修复API Key

## 飞书群ID绑定（已确认）
- oc_8365b711161460f315a825dcd8c3fe37 → 狄仁杰专属群
- oc_ee79942352d38d8320ced1db0fc207c7 → 李元芳专属群
- oc_715234420dd4fceb5acc726708e358f5 → 魏征专属群

## 待解决问题
- [ ] 飞书群里@用户的方法（message工具在群里发送失败）

---

*热记忆·2026-03-29 11:55·守护中*
