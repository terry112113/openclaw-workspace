# 🏛️ 热记忆（1小时内有效）
> 最后更新：2026-03-30 13:56 GMT+8
> 版本：v2.8

---

## 🔴 [13:36] 熔断报告：MiniMax API连续超时

### 系统状态（来自熔断监控）
- Gateway：✅ 正常
- Skills：111个可用，43个缺失（无二进制工具，无实际影响）
- **🔴 MiniMax API连续超时**

### Cron失败（13:35-13:36）
| Job | 结果 | 原因 |
|-----|------|------|
| 记忆管家-后台自学 | 🔴 300s超时 | MiniMax API超时 |
| 记忆管家-中枢风险巡查 | 🔴 60s超时 | MiniMax API超时 |

### 根因
- `Profile minimax:cn timed out. Trying next account...`
- 无fallback配置，failover未触发

---

## ✅ [13:56] 三个cron已重建（臣自主处理）

| Cron | 新ID | Timeout变化 |
|------|------|-----------|
| 记忆管家-后台自学 | fd38cd1f | 300s → **600s** |
| 记忆管家-中枢风险巡查 | 9b2c4617 | 60s → **120s** |
| 唐王-熔断监控 | db2ecca2 | 60s → **120s** |

### Skills数量
- 当前：79个
- 熔断报告：111个（统计口径差异，待确认）

---

## 待皇上处理
- **P0** MiniMax API Key连通性/额度检查
- **P1** 配置fallback provider（建议DeepSeek）
- **P2** microsoft-speech TTS

---

*热记忆刷新完毕*
