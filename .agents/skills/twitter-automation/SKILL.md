# Twitter Automation

**version**: 1.0.0

**description**: Twitter内容自动化，支持发帖、回复和趋势分析

---

## 一句话描述

Twitter内容自动化，支持发帖、回复和趋势分析

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| action | string | 是 | 操作：post/reply/analysis | "post" |
| content | string | 否 | 内容（post时必填） | "最新观点..." |
| 话题 | string | 否 | 分析话题（analysis时必填） | "AI" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 操作结果或分析报告 | "{'tweet_id':'123','status':'posted'}" |

---

## 适用场景

### 适用场景
+社交媒体运营
+趋势追踪

### 不适用场景
-深度讨论
-正式内容

---

## 依赖

Twitter API

---

## 测试用例

```json
{
  "input": {"action":"post","content":"最新观点..."},
  "expected_output": "操作结果或分析报告"
}
```
