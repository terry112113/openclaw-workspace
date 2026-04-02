# Github

**version**: 1.0.0

**description**: GitHub仓库搜索、项目分析和开发者信息查询

---

## 一句话描述

GitHub仓库搜索、项目分析和开发者信息查询

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| query | string | 是 | 搜索关键词或GitHub URL | "openai GPT language:python" |
| action | string | 否 | 操作：search/repo/user | "search" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 搜索结果、仓库信息或用户资料 | "{'repos':[{'name':'gpt','stars':1000}],'total':50}" |

---

## 适用场景

### 适用场景
+代码搜索
+项目调研
+开发者信息

### 不适用场景
-私有仓库
-复杂代码分析

---

## 依赖

GitHub API

---

## 测试用例

```json
{
  "input": {"query":"openai GPT language:python","action":"search"},
  "expected_output": "搜索结果、仓库信息或用户资料"
}
```
