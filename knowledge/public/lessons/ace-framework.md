# ACE Framework for Durable AI Workflows

> tags: [agentic-workflow], [automation], [reliability]
> 来源: https://promptengineering.org/stop-letting-automations-trip-over-themselves-the-ace-framework-for-durable-ai-workflows/
> 更新日期: 2026-03-31

---

## 一句话核心
复杂的AI自动化失败率很高，因为"一个大prompt试图做所有事"。ACE框架把职责分成三层： Aim（目标）、Coordinate（协调）、Execute（执行）。

---

## ACE三层架构

### Aim — 定义"做什么"
用人类可读的SOP格式，中级操作员无需猜测即可执行。

**包含要素：**
- Goal: 一句话描述结果
- Inputs: 数据字段、文件、凭证（带格式说明）
- Tools/Scripts: 批准的工具及必需参数
- Process: 带分支规则的编号步骤
- Outputs: 目的地、schema、文件命名模式
- Edge Cases: 陷阱和预期处理方式
- Acceptance Tests: 快速验证成功的检查项

**Guardrails原则：**
- 二进制规则 > 模糊建议（如："不写入生产表"）
- 量化阈值（最小匹配率、最大重试次数、延迟上限）
- Schema不匹配或输入缺失时的停止条件
- 完成的证据（行数、校验和、输出产物链接）

### Coordinate — 定义"谁和何时"
保持循环简单：read → choose → run → check → repeat

**核心概念：ReAct (Reasoning + Acting)**
- 将逐步推理与工具使用结合
- 提升QA和决策任务的性能和可解释性
- 论文：arXiv:2210.03629

**自主权策略：**
| 动作类型 | 策略 |
|---------|------|
| 幂等读取、本地分析、非破坏性转换 | 自动批准 |
| 首次写入系统、新工具、昂贵配额操作 | 询问确认 |
| 法律/金融/PII相关 | 需要批准 |

### Execute — 定义"怎么做"
通过确定性脚本和工具执行工作。

---

## 对三司会审的启发

### 当前问题 vs ACE解决方案

| 当前问题 | ACE对应 |
|---------|---------|
| 三司会审没有明确的SOP | 需制定Aim层SOP |
| 协调混乱 | 加强Coordinate层 |
| 执行结果验证不足 | 建立Acceptance Tests |

### 三司会审ACE化建议

**Aim层（三司会审SOP）：**
```
目标：皇上发议题 → 三司辩论 → 狄仁杰裁决
输入：皇上webchat消息
工具：sessions_send, message, 飞书群
流程：3回合辩论（见三司会审运作协议）
输出：裁决结论 → 飞书群
验收：皇上确认 或 无人反对
```

**Coordinate层（三司协调）：**
```
狄仁杰 = 协调者（读取议题 → 分派 → 裁决）
李元芳 = 情报分析（读取 → 分析 → 回报）
魏征 = 技术审计（读取 → 审计 → 否决/同意）
```

**Execute层（三司执行）：**
```
李元芳：用Firecrawl/搜索工具收集情报
魏征：用exec/工具执行技术验证
狄仁杰：用裁决权做最终决策
```

---

## 行动建议

1. **立即：** 更新三司会审运作协议，加入ACE框架术语
2. **本周：** 为每个Cron任务制定Aim层SOP（含Acceptance Tests）
3. **长期：** 评估三司会审各层的可靠性指标（参考SRE error budget）

---

## 相关链接
- ACE Framework原文: https://promptengineering.org/stop-letting-automations-trip-over-themselves-the-ace-framework-for-durable-ai-workflows/
- ReAct论文: https://arxiv.org/abs/2210.03629
- Parnas模块化论文: https://dl.acm.org/doi/10.1145/361598.361623
- Google SRE Error Budget: https://sre.google/workbook/error-budget-policy/

---

*狄仁杰 2026-03-31 归档*
