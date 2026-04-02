# Github Deep Research

**version**: 1.0.0

**description**: GitHub深度代码搜索和分析，支持正则、文件类型过滤

---

## 一句话描述

GitHub深度代码搜索和分析，支持正则、文件类型过滤

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| query | string | 是 | 搜索查询 | "react useState language:TypeScript" |
| max_results | number | 否 | 最大结果数 | 10 |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 匹配的代码片段和文件路径 | "{'file':'src/App.tsx','repo':'user/project'}" |

---

## 适用场景

### 适用场景
+代码搜索
+技术方案调研

### 不适用场景
-非GitHub仓库
-私有仓库

---

## 依赖

GitHub API

---

## 测试用例

```json
{
  "input": {"query":"react useState language:TypeScript","max_results":5},
  "expected_output": "匹配的代码片段和文件路径"
}
```
