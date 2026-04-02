# Github Workflow Automation

**version**: 1.0.0

**description**: GitHub Actions工作流自动化，支持CI/CD配置和触发

---

## 一句话描述

GitHub Actions工作流自动化，支持CI/CD配置和触发

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| action | string | 是 | 操作：create/trigger/status | "create" |
| workflow_file | string | 否 | 工作流文件内容 | "name: CI\non: push" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 操作结果 | "工作流已创建: .github/workflows/ci.yml" |

---

## 适用场景

### 适用场景
+CI/CD自动化
+GitHub Actions配置

### 不适用场景
-GitLab CI
-Jenkins

---

## 依赖

GitHub CLI或API

---

## 测试用例

```json
{
  "input": {"action":"create","workflow_file":"name: CI\non: push"},
  "expected_output": "操作结果"
}
```
