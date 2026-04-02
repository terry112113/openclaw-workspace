# Ui Ux Pro Max

**version**: 1.0.0

**description**: UI/UX设计和前端开发助手，支持多框架（React/Vue/Flutter等）

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| task | string | 是 | 任务类型：design(设计)/implement(实现)/review(评审) |
| framework | string | 否 | 前端框架：react/vue/flutter/ios/android |

### 输出（Returns）

| 类型 | 说明 |
|------|------|
| string | 设计方案、代码实现或评审意见 |

---

## 适用场景

- 需要UI/UX设计和前端开发助手的场景
- 自动化任务执行
- 信息检索和分析

---

## 依赖

- 依赖其他Skill：无
- 环境要求：无

---

## 版本历史

- 1.0.0 (2026-04-01): 补充真实IO文档

## 测试用例

```json
{
  "input": {
    "task": "test value"
  },
  "expected_output": "设计方案、代码实现或评审意见"
}
```
