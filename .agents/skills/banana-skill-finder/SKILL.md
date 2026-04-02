# Banana Skill Finder

**version**: 1.0.0

**description**: 从Banana.ski发现和搜索AI Skills

---

## 一句话描述

从Banana.ski发现和搜索AI Skills

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| query | string | 是 | 搜索词 | "code review" |
| category | string | 否 | 分类筛选 | "productivity" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 匹配的Skills列表 | "{'skills':[{'name':'code-review','rating':4.8}]}" |

---

## 适用场景

### 适用场景
+发现新Skills
+工具推荐

### 不适用场景
-本地Skills
-深度评测

---

## 依赖

Banana.ski API

---

## 测试用例

```json
{
  "input": {"query":"code review","category":"productivity"},
  "expected_output": "匹配的Skills列表"
}
```
