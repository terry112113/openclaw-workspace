# ReAct Pattern (Synergizing Reasoning and Acting)

> tags: [agentic-workflow], [reasoning], [tool-use]
> 来源: https://arxiv.org/abs/2210.03629
> 更新日期: 2026-03-31

---

## 一句话核心
ReAct = **Re**asoning + **Act**ing。将逐步推理与工具使用结合，提升QA和决策任务的性能和可解释性。

---

## 核心思想

**问题：** 传统LLM要么只推理（Chain-of-Thought），要么只行动（Action agents），两者分离导致：
- 推理不知道自己会调用什么工具
- 行动不知道为什么要调用工具

**ReAct解法：** 让推理和行动交替进行，每个行动都基于推理的上下文，每个推理都指向下一个行动。

### 伪代码示例
```
Thought: 我需要找到北京今天的天气
Action: search(query="北京天气 2026-03-31")
Observation: 晴天，15-22度
Thought: 根据搜索结果，北京今天晴天，温度15-22度
Action: 给用户回复天气信息
```

---

## 对三司会审的启发

### 当前三司会审流程 vs ReAct

| 当前 | ReAct化 |
|------|--------|
| 三司各自准备 | Thought：各自分析推理 |
| 发言顺序固定 | 推理+行动交替 |
| 无工具调用 | 用工具收集情报/执行 |
| 结果直接输出 | Observation验证后再输出 |

### 三司会审ReAct化建议

**李元芳（ReAct循环）：**
```
Thought: 议题是X，我需要收集什么情报？
Action: 调用Firecrawl/搜索工具
Observation: 收到情报A、B、C
Thought: 根据情报A、B、C，核心风险是...
Action: 发布到飞书群
```

**魏征（ReAct循环）：**
```
Thought: 议题是X，技术可行性如何？
Action: 调用exec/工具验证
Observation: 验证结果通过/失败
Thought: 技术风险点：...
Action: 发布到飞书群
```

**狄仁杰（裁决）：**
```
Thought: 李元芳情报+魏征技术，我需要裁决...
Action: 给出裁决结论
```

---

## 行动建议

1. **立即：** 在三司会审指令模板中加入ReAct格式要求
2. **本周：** 评估李元芳的Firecrawl调用是否需要ReAct化

---

*狄仁杰 2026-03-31 归档*
