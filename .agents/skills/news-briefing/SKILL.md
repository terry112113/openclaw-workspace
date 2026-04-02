# News Briefing

**version**: 1.0.0

**description**: 每日新闻摘要，支持行业分类和时间范围筛选

---

## 一句话描述

每日新闻摘要，支持行业分类和时间范围筛选

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| category | string | 否 | 新闻分类：tech/business/science | "tech" |
| date | string | 否 | 日期（YYYY-MM-DD） | "2026-04-01" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 新闻摘要列表 | "[{'title':'...','summary':'...','source':'...'}]" |

---

## 适用场景

### 适用场景
+每日新闻
+行业动态

### 不适用场景
-深度报道
-历史新闻

---

## 依赖

新闻API

---

## 测试用例

```json
{
  "input": {"category":"tech","date":"2026-04-01"},
  "expected_output": "新闻摘要列表"
}
```
