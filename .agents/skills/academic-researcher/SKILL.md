# Academic Researcher

**version**: 1.0.0

**description**: 学术论文搜索和研究，支持关键词检索、引用分析和论文摘要

---

## 一句话描述

学术论文搜索和研究，支持关键词检索、引用分析和论文摘要

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| query | string | 是 | 搜索关键词 | "machine learning optimization" |
| max_results | number | 否 | 最大结果数 | 10 |
| field | string | 否 | 学科领域 | "computer science" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 论文列表和摘要 | "{'papers':[{'title':'...','abstract':'...','citations':100}]}" |

---

## 适用场景

### 适用场景
+学术研究
+论文检索
+引用分析

### 不适用场景
-实时新闻
-商业报告

---

## 依赖

学术数据库API

---

## 测试用例

```json
{
  "input": {"query":"deep learning","max_results":5},
  "expected_output": "论文列表和摘要"
}
```
