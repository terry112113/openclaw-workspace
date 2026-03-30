# 🏛️ 热记忆（1小时内有效）
> 最后更新：2026-03-30 12:06 GMT+8
> 版本：v2.6

---

## 🔴 [12:06] 熔断告警：狄仁杰-每日Skills维护任务濒临崩溃
- 影响：220个Skills已24天未审核淘汰，技能库臃肿风险累积
- 根因：任务连续超时（consecutiveErrors=2），上次成功运行：3月6日
- 建议：检查skills审核任务，或手动触发一次，或延后下次执行时间
- 下次自动运行：4月1日 10:00（距今约46小时）

---

## 🟢 [11:45] 皇上说"你先忙"，臣进入待命

### 飞书路由刚修复
- 魏征专属群(oc_715234420dd4fceb5acc726708e358f5)已绑定wei账号
- 等待皇上测试

### 三司会审插件审查发现
- memory-core: "unavailable" ⚠️
- microsoft-speech: disabled ⚠️（TTS断的原因）
- memory-lancedb: disabled ⚠️

### Ollama状态
- gpt-oss:20b ✅ 运行中
- nomic-embed-text ✅ 下载完成

### 三司会审最终架构
| Agent | 模型 | 费用 |
|-------|------|------|
| 狄仁杰 | MiniMax-M2.7 | API |
| 李元芳 | MiniMax-M2.7 | API |
| 魏征 | Ollama gpt-oss:20b | 零成本 |

### Cron状态
- 19个，全部正常运行

---

## 待皇上指示
1. 魏征飞书测试
2. memory-core问题
3. microsoft-speech启用
4. Whisper安装（ClawHub限速）

---

*热记忆刷新完毕*
