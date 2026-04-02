# Agent Ui

**version**: 1.0.0

**description**: 用户界面Agent，支持UI设计评审和前端代码审查

---

## 一句话描述

用户界面Agent，支持UI设计评审和前端代码审查

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| action | string | 是 | 操作类型：review/design/implement | "review" |
| context | string | 是 | UI上下文或需求描述 | "移动端注册页面" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | UI评审意见、设计方案或实现代码 | "{'issues':['按钮过小'],'suggestions':[]}" |

---

## 适用场景

### 适用场景
+UI评审
+设计建议
+前端实现

### 不适用场景
-后端逻辑
-数据库设计

---

## 依赖

ui-ux-pro-max

---

## 测试用例

```json
{
  "input": {"action":"review","context":"移动端注册页面"},
  "expected_output": "UI评审意见、设计方案或实现代码"
}
```
