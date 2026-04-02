# Frontend Dev Guidelines

**version**: 1.0.0

**description**: 前端开发规范指南，提供React/Vue等框架的最佳实践

---

## 一句话描述

前端开发规范指南，提供React/Vue等框架的最佳实践

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| framework | string | 是 | 前端框架：react/vue/svelte | "react" |
| topic | string | 否 | 规范主题：state/css/performance/testing | "state" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 开发规范说明 | "{'title':'React状态管理','rules':['使用useState','优先本地状态']}" |

---

## 适用场景

### 适用场景
+开发规范参考
+代码评审

### 不适用场景
-后端开发
-移动端

---

## 依赖

无

---

## 测试用例

```json
{
  "input": {"framework":"react","topic":"state"},
  "expected_output": "开发规范说明"
}
```
