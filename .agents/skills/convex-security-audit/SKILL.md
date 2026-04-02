# Convex Security Audit

**version**: 1.0.0

**description**: 智能合约安全审计，支持漏洞检测和风险评估

---

## 一句话描述

智能合约安全审计，支持漏洞检测和风险评估

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| contract_code | string | 是 | 合约代码 | "contract Token { ... }" |
| audit_level | string | 否 | 审计级别：basic/full | "basic" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 审计报告 | "{'vulnerabilities':[],'risk':'low'}" |

---

## 适用场景

### 适用场景
+智能合约审计
+安全检测

### 不适用场景
-普通代码
-非区块链

---

## 依赖

安全分析工具

---

## 测试用例

```json
{
  "input": {"contract_code":"contract Demo { ... }","audit_level":"basic"},
  "expected_output": "审计报告"
}
```
