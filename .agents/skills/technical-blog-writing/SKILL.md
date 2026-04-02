# Technical Blog Writing

**version**: 1.0.0

**description**: 技术博客写作，支持代码片段、架构图说明和技术深度分析

---

## 一句话描述

技术博客写作，支持代码片段、架构图说明和技术深度分析

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| topic | string | 是 | 技术主题 | "微服务架构设计" |
| depth | string | 否 | 深度：intro/deep/expert | "deep" |
| code_lang | string | 否 | 主要代码语言 | "python" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 技术博客文章 | "# 微服务架构设计\n## 什么是微服务..." |

---

## 适用场景

### 适用场景
+技术分享
+开发经验总结

### 不适用场景
-非技术内容
-新闻资讯

---

## 依赖

无

---

## 测试用例

```json
{
  "input": {"topic":"微服务架构","depth":"deep","code_lang":"python"},
  "expected_output": "技术博客文章"
}
```
