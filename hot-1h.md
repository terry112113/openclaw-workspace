# 🏛️ 热记忆（1小时内有效）
> 最后更新：2026-03-30 11:25 GMT+8
> 版本：v2.3

---

## 🟢 [11:25] Ollama接入 + 系统优化完成

### 三司会审模型分配（新）
| Agent | 模型 | 状态 |
|-------|------|------|
| 狄仁杰 | MiniMax-M2.7 | ✅ |
| 李元芳 | MiniMax-M2.7 | ✅ |
| 魏征 | **Ollama/gpt-oss:20b** | ✅ 本地131K上下文零成本 |

### Ollama已装模型
- **gpt-oss:20b**：20.9B，MXFP4量化，13GB，131K上下文，支持tools+thinking ✅

### Ollama下载中
- **nomic-embed-text**：本地向量库，用于RAG记忆（下载完成时间待查）

### 系统今日优化（11:15-11:25）
- Skills：84→79个 ✅
- Cron：23→21个 ✅
- 112个中文文件名→英文 ✅
- MEMORY.md精简324→95行 ✅
- warm-12h.md重建 ✅
- 清理：minister-reports/临时脚本/texts重复 ✅
- Ollama接入OpenClaw ✅
- 魏征改用本地Ollama ✅

---

## 🔴 未解决
| 项目 | 状态 |
|------|------|
| TTS Microsoft | provider注册失败，等OpenAI key |
| Skills维护cron | 已改timeout 3600s，等下次触发 |
| 飞书群策略 | groupAllowFrom为空，群消息丢弃 |

---

*热记忆刷新完毕*
