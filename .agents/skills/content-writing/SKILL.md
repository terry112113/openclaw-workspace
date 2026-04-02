# Content Writing

**version**: 1.0.0

**description**: 专业内容写作辅助，支持文章、博客、文档等多种格式

---

## 一句话描述

专业内容写作辅助，支持文章、博客、文档等多种格式

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| topic | string | 是 | 内容主题 | "AI发展趋势" |
| format | string | 否 | 格式：article/blog/doc/report | "article" |
| length | string | 否 | 长度：short/medium/long | "medium" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 结构化的内容文本 | "一篇关于AI发展的专业文章..." |

---

## 适用场景

### 适用场景
+需要快速生成文章/报告
+多格式内容创作

### 不适用场景
-需要实时新闻
-需要专业知识深度研究

---

## 依赖

无

---

## 测试用例

```json
{
  "input": {"topic":"AI发展趋势","format":"article","length":"medium"},
  "expected_output": "结构化的内容文本"
}
```
