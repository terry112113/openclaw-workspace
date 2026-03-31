# CURRENT.md - 狄仁杰的当下上下文
> 最后更新：2026-03-31 19:15 GMT+8

## 现在是什么时候
2026-03-31 19:15（周二傍晚）

## 我们在哪
皇上发存档暗号"鱼香肉丝"，立即全面存档。

## 三司会审v3.1架构（确立）
| 角色 | 名字 | 权力边界 | 最终责任 |
|------|------|---------|---------|
| 大理寺卿 | 狄仁杰 | 最终决策权+override权 | 结论正确性 |
| 都察院御史 | 李元芳 | 信息完备性判断权 | 情报准确性 |
| 刑部尚书 | 魏征 | 技术否决权（附约束） | 工具可靠性 |

## 三司会审今日完成
- [x] 三司会审运作协议v3.1
- [x] 记忆分层边界政策
- [x] Sprint验收标准
- [x] Skills统一索引（107个）
- [x] Ollama迁移D盘 ✅
- [x] Firecrawl替换Tavily ✅
- [x] openclaw.json新secret生效
- [x] P1审计日志框架 ✅
- [x] P2 DPAPI加密方案 ✅
- [x] P3会话隔离方案 ✅
- [x] cron优化（timeout调整）✅
- [x] 三司会审OpenClaw系统漏洞优化辩论 ✅
- [x] 三司会审Ollama+OpenClaw结合辩论 ✅
- [x] 三司会审和皇上一起学习Agent知识辩论 ✅
- [x] 公共知识库重建（research/operations/lessons/archive）✅
- [x] L1-L5心跳考核机制确立 ✅

## 系统状态
- Gateway: ✅ 运行中
- Ollama: ✅ D盘，gpt-oss:20b
- Firecrawl: 525 credits

## 今日重要教训
1. Feishu secret env引用在Windows服务下失效 → 必须用实际值
2. DeepSeek API 404 → 切换到MiniMax
3. Ollama pull不支持断点续传 → 中断后从头开始
4. openclaw doctor会覆盖配置 → 手动修改后不要运行doctor
5. groupAllowFrom/groupSenderAllowFrom 必须配置才能接收群消息
6. 配置被还原 → 可能是doctor覆盖了配置

## 飞书群配置（关键）
- groupPolicy: allowlist
- groupAllowFrom: ["oc_7ff140c90bcdd119a6ddc59610c30829"]
- groupSenderAllowFrom: ["ou_82c708d3c070ec7be65a899b7533c5e4"]

## L1-L5心跳考核机制
| 阶段 | 关键词 | 特征 |
|------|-------|------|
| L1 | 等指示 | 被动执行 |
| L2 | 发现了 | 不等指令就行动 |
| L3 | 我分享给 | 主动协作+知识共享 |
| L4 | 我计划 | 自我管理，狄仁杰只拍板 |
| L5 | 我创建 | 创造新框架 |

**当前阶段：**
- 狄仁杰：L3
- 李元芳：L2巅峰
- 魏征：L2巅峰

**心跳Cron：** 周一至周五 18:00，三司会审大群发每日心跳

## 存档暗号
"鱼香肉丝" = 立即全面存档（CURRENT + memory + hot + Git push）

---

*2026-03-31 19:15 - 鱼香肉丝存档完成*
