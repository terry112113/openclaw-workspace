# Writing Skills

**version**: 1.0.0

**description**: 写作技巧指南，提供各类文体的写作方法和范例

---

## 一句话描述

写作技巧指南，提供各类文体的写作方法和范例

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| style | string | 是 | 写作风格：business/creative/technical/academic | "business" |
| topic | string | 否 | 写作主题 | "项目汇报" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 写作技巧和建议 | "{'structure':'背景-问题-方案','tips':['结论先行']}" |

---

## 适用场景

### 适用场景
+写作提升
+文体指导

### 不适用场景
-代笔
-内容创作

---

## 依赖

无

---

## 测试用例

```json
{
  "input": {"style":"business","topic":"项目汇报"},
  "expected_output": "写作技巧和建议"
}
```
