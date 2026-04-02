# Tavily Research

**version**: 1.0.0

**description**: AI优化的网页搜索和内容聚合，支持深度研究和实时情报

---

## 一句话描述

AI优化的网页搜索和内容聚合，支持深度研究和实时情报

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| query | string | 是 | 搜索查询词 | "最新AI发展趋势2026" |
| depth | string | 否 | 搜索深度：basic/deep | "deep" |
| topic | string | 否 | 主题分类：general/news/science | "general" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 搜索结果摘要和链接列表 | "{'results':[{'title':'...','url':'...','summary':'...'}],'count':10}" |

---

## 适用场景

### 适用场景
+深度研究
+竞品分析
+市场调研

### 不适用场景
-需要精确事实
-学术引用

---

## 依赖

Tavily API

---

## 测试用例

```json
{
  "input": {"query":"AI趋势2026","depth":"deep"},
  "expected_output": "搜索结果摘要和链接列表"
}
```
