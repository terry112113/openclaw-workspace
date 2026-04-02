# Apify Ultimate Scraper

**version**: 1.0.0

**description**: 网页抓取工具，支持动态渲染和反爬处理

---

## 一句话描述

网页抓取工具，支持动态渲染和反爬处理

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| url | string | 是 | 目标URL | "https://example.com" |
| extract | string | 否 | 提取类型：text/links/images/structured | "structured" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 提取内容 | "{'title':'...','data':[...]}" |

---

## 适用场景

### 适用场景
+网页抓取
+竞品分析
+数据采集

### 不适用场景
-需要登录
-大型全站抓取

---

## 依赖

Apify API

---

## 测试用例

```json
{
  "input": {"url":"https://example.com","extract":"text"},
  "expected_output": "提取内容"
}
```
