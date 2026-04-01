# 项目研究：superpowers 技能框架

**魏征 · 刑部尚书 · 2026-03-29**

---

## 一、项目概述

| 项目 | 地址 |
|------|------|
| 仓库 | https://github.com/obra/superpowers |
| Stars | 121k |
| 作者 | Jesse Vincent (Prime Radiant) |
| 协议 | MIT |
| 定位 | Agentic Skills Framework & 软件开发方法论 |

**一句话总结：** Superpowers 是一套让 AI  coding agent 具备系统性开发流程的技能框架，核心是"先设计再动手，任务原子化，测试驱动"。

---

## 二、框架设计解析

### 2.1 核心技能（Skills）体系

技能目录结构：
```
skills/
  brainstorming/               # 先脑暴，再动手（设计阶段）
  using-git-worktrees/          # Git Worktree 隔离分支
  writing-plans/                # 拆解任务为原子步骤
  subagent-driven-development/  # 子 Agent 并行执行 + 两阶段 review
  executing-plans/              # 计划执行（单 session 内）
  test-driven-development/      # 红绿重构循环
  requesting-code-review/       # 任务间 code review
  receiving-code-review/        # 接受 review 反馈
  finishing-a-development-branch/ # 分支收尾（合并/PR/保留）
  systematic-debugging/         # 4 步根源分析
  verification-before-completion/ # 验证确实修好了
  dispatching-parallel-agents/ # 并行子 agent 调度
  writing-skills/               # 如何写新技能（meta 技能）
  using-superpowers/            # 框架介绍
```

共 **14 个技能**，覆盖：设计 → 计划 → 执行 → Review → 调试 → 分支管理 → 技能创作全流程。

### 2.2 技能文件格式（SKILL.md）

每个技能是一个 `SKILL.md` 文件，YAML frontmatter 格式：

```yaml
---
name: skill-name-with-hyphens
description: Use when [触发条件 - 何时调用此技能]
---

# 技能标题

## Overview
核心原则，1-2 句话

## When to Use
触发条件、适用症状

## Core Pattern
核心模式（技术细节）

## Quick Reference
快速参考

## Common Mistakes
常见错误
```

**关键设计点：**
- Flat namespace，所有技能在同一命名空间
- 技能按需触发，非预设流程
- description 只写"何时用"，不写"怎么用"（防止 LLM 跳读）

### 2.3 核心流程图

```
用户需求
  ↓
brainstorming（设计脑暴）
  → 探索上下文、提问、2-3 方案比选、用户确认设计
  → 输出：docs/superpowers/specs/YYYY-MM-DD-<feature>-design.md
  ↓
writing-plans（写实施计划）
  → 原子化任务（2-5 分钟/步）
  → 输出：docs/superpowers/plans/YYYY-MM-DD-<feature>.md
  ↓
subagent-driven-development（子 Agent 驱动执行）
  OR executing-plans（单 session 内执行）
  ↓
requesting-code-review（任务间 review）
  ↓
finishing-a-development-branch（分支收尾）
```

### 2.4 关键创新：Subagent-Driven Development

这是 superpowers 最独特的能力：

1. **每个任务分配一个 fresh subagent**
2. **两阶段 review**：
   - Stage 1：Spec compliance（是否符合计划）
   - Stage 2：Code quality（代码质量）
3. 人类可以在任意节点 checkpoint
4. 声称 Claude 可以 autonomous 工作数小时不偏离计划

### 2.5 TDD 融入工作流

每个实现任务都强制走 RED-GREEN-REFACTOR：
- 写失败测试 → 确认失败 → 写最小代码 → 确认通过 → 提交

---

## 三、评估：能否移植到三司会审

### 3.1 对应关系分析

| Superpowers 概念 | 三司会审对应 |
|-----------------|------------|
| brainstorming | 狄仁杰主持讨论阶段 |
| writing-plans | 李元芳起草奏章/宋慈准备方案 |
| subagent-driven-development | 李元芳/宋慈各自执行 |
| requesting-code-review | 狄仁杰审核双方结论 |
| verification-before-completion | 验证结论有效性 |
| writing-skills | 持续沉淀方法论 |

### 3.2 优势（可移植）

1. **工作流结构化**：brainstorming → planning → execution → review 完美对应三司：
   - brainstorm = 三司会审讨论
   - writing-plans = 李元芳/宋慈各自准备方案
   - subagent-driven = 两人并行执行
   - review = 狄仁杰主持辩论、审核

2. **Skills 的 flat namespace 设计**：适合 OpenClaw 的 skill 体系
   - 技能可复用、可组合
   - 每个技能有清晰触发条件

3. **原子化任务（2-5 分钟步骤）**：
   - 对应三司会审中的"分解审理要点"
   - 每个步骤有具体文件/动作/验证方式
   - 可迁移为"审理要点清单"

4. **两阶段 review**：
   - Spec compliance = 论点是否符合事实/法律
   - Code quality = 论据充分性、逻辑严密性
   - 非常适合三司的"辩论—裁定"机制

5. **121k stars 的成熟度**：
   - 经过大量用户验证
   - 文档完善，TDD 方法论严谨
   - 值得直接借鉴

### 3.3 挑战（需改造）

1. **目标不同**：Superpowers 服务软件开发（code），三司会审服务推理/决策（reasoning）
   - 需要将 TDD → 证据驱动论证
   - 需要将 code review → 法律/逻辑 review

2. **Human-in-the-loop 频率**：
   - Superpowers 设计为 autonomous 运行数小时
   - 三司会审需要太上皇（用户）实时参与决策
   - 需要更高频的 checkpoint

3. **子 Agent 数量**：
   - Superpowers 主张每个任务一个 fresh subagent
   - 三司会审固定两个子 agent（李元芳/宋慈）
   - 需要调整适配两个固定角色

4. **Trigger 机制**：
   - Superpowers 用 description 自动触发（"Use when..."）
   - 三司会审需要明确启动条件（如：用户提出议题）

### 3.4 移植优先级

| 优先级 | 内容 | 理由 |
|-------|------|------|
| P0 | brainstorming → 三司讨论流程 | 最核心的设计决策流程 |
| P0 | writing-plans → 审理要点分解 | 原子化步骤是方法论核心 |
| P1 | 两阶段 review → 狄仁杰审核 | 直接对应审核机制 |
| P2 | systematic-debugging → 根源分析 | 案件调查可用 |
| P3 | writing-skills → 沉淀新技能 | 持续迭代 |

---

## 四、集成方案建议

### 方案 A：直接迁移（推荐 P0-P1）

将 superpowers 的 skill 格式引入 OpenClaw，在 `~/.openclaw/skills/` 下建立技能目录：

```
~/.openclaw/skills/
  三司-brainstorming/    SKILL.md
  三司-writing-plans/     SKILL.md
  三司-review/            SKILL.md
  三司-根源分析/          SKILL.md
  ...
```

**优势：** 快速复用成熟设计，skill 格式兼容
**挑战：** 需要调整触发条件和内容适配推理场景

### 方案 B：概念映射（中期）

保留 superpowers 的流程骨架，但为每个阶段创建三司专用的 skill：
- brainstorming → "会审筹备"（收集信息、梳理争议）
- writing-plans → "审理要点"（分解为可审理的任务）
- review → "裁定审议"（双方案比较）

### 方案 C：深度融合（长期）

将 superpowers 视为"技术领域的方法论"，三司会审视为"推理决策领域的方法论"，提取共同模式：
- 都是"先设计后执行"
- 都是"任务原子化"
- 都是"多层 review"

---

## 五、结论

**Superpowers 值得高度重视。** 121k stars 说明它是目前最成熟的 coding agent 技能框架。它的核心价值不在于某个具体技能，而在于**"技能可触发、工作流结构化、任务原子化、review 两阶段"** 的方法论。

这套方法论**完全可以移植到三司会审**，但需要针对推理/决策场景做内容调整。最高优先级的移植是 brainstorming 和 writing-plans，因为这两个技能直接对应三司的核心价值：深思熟虑再行动。

---

*本报告由魏征研究，2026-03-29*
