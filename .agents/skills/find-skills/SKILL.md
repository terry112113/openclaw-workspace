# Find Skills

**version**: 1.0.0

**description**: 在ClawHub上搜索和安装Skills，支持关键词匹配和评分排序

---

## 一句话描述

在ClawHub上搜索和安装Skills，支持关键词匹配和评分排序

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| query | string | 是 | 搜索关键词 | "web scraper" |
| category | string | 否 | 技能分类筛选 | "data" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 匹配的Skills列表 | "{'skills':[{'name':'web-scraper','rating':4.8}],'count':5}" |

---

## 适用场景

### 适用场景
+查找新技能
+技能推荐

### 不适用场景
-已知的技能
-需要深度评测

---

## 依赖

ClawHub

---

## 测试用例

```json
{
  "input": {"query":"web scraper","category":"data"},
  "expected_output": "匹配的Skills列表"
}
```
