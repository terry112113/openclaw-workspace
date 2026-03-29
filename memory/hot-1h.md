# hot-1h.md - 热记忆（每30分钟刷新）

> 最后更新：2026-03-29 21:30 GMT+8

## 🛡️ 守护cron运行
- 时间：21:30
- 状态：自动刷新

## 🔴 [21:25] 熔断告警：多个cron持续恶化（7个任务告警）
- 影响：7个cron任务告警，共中3个高危：
  - 熔断监控自身（cb422bc0）：consecutiveErrors=5，API Key ****63f8认证失败
  - 唐王李世民-高效自查（485572e7）：consecutiveErrors=5，timeout持续
  - 唐王-常驻进化引擎（cebe4ff0）：consecutiveErrors=7，timeout持续恶化
  - 李元芳-深度研究（258fba99）：consecutiveErrors=2，auth失败
  - 狄仁杰-每日Skills维护（618b25fa）：consecutiveErrors=2，timeout
  - 唐王-记忆冲突检测（7b9eb04e）：consecutiveErrors=2，auth失败
- 关键：Together API Key（****63f8）疑似失效或被吊销，多个使用该Key的任务auth持续失败
- 建议：检查TOOLS.md中的Together API Key有效性；考虑为timeout任务延长timeoutSeconds
- 状态：所有任务enabled=true（仍在调度，但持续失败）

## 🔴 [17:26] 熔断监控例行报告
- Skills维护cron：consecutiveErrors=2（持续timeout，lastRun=2026-03-29 07:22）
- 唐王-任务预填充：consecutiveErrors=7（timeout，持续恶化！）
- 唐王-常驻进化引擎：consecutiveErrors=9（timeout，持续恶化！）
- 结论：⚠️ 常驻进化引擎9次timeout，任务预填充升至7次，Skills维护维持2次

## 🔴 [17:26] 熔断告警：Skills维护cron连续超时（consecutiveErrors=2）
- 影响：狄仁杰-每日Skills维护（618b25fa）连续2次执行超时
  - 上次运行：2026-03-29 07:22
  - consecutiveErrors: 2（⚠️ 已达熔断告警阈值）
- 原因：任务执行时间超过600秒timeout限制
- 建议：延长timeoutSeconds至900或1200，或拆分审核任务分批执行
- 状态：enabled=true（仍在运行，但持续超时）

## 🔴 [17:26] 熔断告警：任务预填充cron持续超时（consecutiveErrors=7）
- 影响：唐王-任务预填充（05c374d5）连续7次执行超时
  - lastRun=2026-03-29 17:15
  - 原因：任务执行时间超过120秒timeout限制
- 建议：延长timeoutSeconds至300，或精简任务预填充逻辑
- 状态：enabled=true（持续超时）

## 🔴 [17:26] 熔断告警：常驻进化引擎cron持续超时（consecutiveErrors=9）
- 影响：唐王-常驻进化引擎（cebe4ff0）连续9次执行超时
  - lastRun=2026-03-29 17:07
  - lastDurationMs=301621（超时）
- 建议：延长timeoutSeconds至600，或精简研究任务量
- 状态：enabled=true（持续超时）



## 飞书群ID绑定（已确认）
- oc_8365b711161460f315a825dcd8c3fe37 → 狄仁杰专属群
- oc_ee79942352d38d8320ced1db0fc207c7 → 李元芳专属群
- oc_715234420dd4fceb5acc726708e358f5 → 魏征专属群

## 待解决问题
- [ ] 飞书群里@用户的方法（message工具在群里发送失败）

---

*热记忆·2026-03-29 21:30·守护中*
