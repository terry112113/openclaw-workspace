# Security Auditor

**version**: 1.0.0

**description**: 安全审计工具，检测代码和配置中的安全漏洞

---

## 一句话描述

安全审计工具，检测代码和配置中的安全漏洞

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| target | string | 是 | 审计目标：code/config/deploy | "code" |
| path | string | 是 | 文件或目录路径 | "./" |
| severity | string | 否 | 漏洞等级过滤：critical/high/medium/low | "high" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 安全漏洞报告 | "{'vulnerabilities':[{'type':'SQL注入','line':10}],'total':1}" |

---

## 适用场景

### 适用场景
+代码安全审计
+配置检查
+部署前检查

### 不适用场景
-性能问题
-代码风格

---

## 依赖

安全扫描工具

---

## 测试用例

```json
{
  "input": {"target":"code","path":"./src","severity":"high"},
  "expected_output": "安全漏洞报告"
}
```
