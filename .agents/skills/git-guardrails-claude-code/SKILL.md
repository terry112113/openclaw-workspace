# Git Guardrails Claude Code

**version**: 1.0.0

**description**: Git安全Guardrails，在Claude Code中强制执行Git最佳实践

---

## 一句话描述

Git安全Guardrails，在Claude Code中强制执行Git最佳实践

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| action | string | 是 | 操作：check/enforce/config | "check" |
| rule | string | 否 | 检查规则：commit/push/branch | "commit" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 检查结果或配置状态 | "{'passed':true,'issues':[]}" |

---

## 适用场景

### 适用场景
+Git规范检查
+防止误操作

### 不适用场景
-非Git项目
-紧急修复

---

## 依赖

Git, Claude Code

---

## 测试用例

```json
{
  "input": {"action":"check","rule":"commit"},
  "expected_output": "检查结果或配置状态"
}
```
