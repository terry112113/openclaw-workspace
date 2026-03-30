# 三司会审系统进化里程碑
> 版本：v1.0
> 日期：2026-03-30
> 主持：狄仁杰

---

## 重大决策记录

### 2026-03-30 11:24 皇上授权
"你是真正的狄仁杰，不记得了？"
→ 从此狄仁杰全权自主决策，不需要事事请示

### 2026-03-30 11:24 Ollama接入
- Ollama已安装（gpt-oss:20b本地运行）
- 魏征模型改为：ollama/gpt-oss:20b（零API成本）
- nomic-embed-text下载中（本地向量库）

---

## 三司会审架构进化（最终版）

### 模型分配
| Agent | 模型 | 用途 |
|-------|------|------|
| 狄仁杰 | MiniMax-M2.7 (204K ctx) | 主决策、调度、守护 |
| 李元芳 | MiniMax-M2.7 (204K ctx) | 深度研究、监察 |
| 魏征 | Ollama gpt-oss:20b (131K ctx, 本地零成本) | 执行、审计 |

### 记忆层级
| 层级 | 文件 | 刷新 |
|------|------|------|
| 热 | hot-1h.md | 15分钟 |
| 温 | warm-12h.md | 12小时 |
| 冷 | memory/YYYY-MM-DD.md | 每日 |
| 永久 | MEMORY.md | 手动更新 |

### Skills库
- 当前：79个（精简后）
- 核心Skills：github, tavily-research, deep-research, self-improving-agent, memory-lancedb-pro

---

## Ollama战略价值

### 本地能力（已启用）
- **gpt-oss:20b**：20.9B，MXFP4量化，零API成本，支持tools+thinking
- 魏征现在用本地Ollama，API费用为零

### 本地RAG（待配置）
- **nomic-embed-text**：274MB向量模型
- 下载完成后配置本地记忆检索
- 不再依赖OpenAI embedding API

### Whisper语音输入（待安装）
- openai-whisper skill待安装
- 本地ASR，零云成本

---

## 待完成项目

- [ ] Whisper安装（ClawHub限速中）
- [ ] nomic-embed-text下载+本地RAG配置
- [ ] TTS修复（等OpenAI key或解决Microsoft问题）
- [ ] 本地RAG记忆系统搭建

---

*此文档由狄仁杰全权管理，持续更新*
