# Frontend Design

**version**: 1.0.0

**description**: 前端设计系统，支持组件库选择、设计模式和应用架构

---

## 一句话描述

前端设计系统，支持组件库选择、设计模式和应用架构

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| action | string | 是 | 操作：recommend/design/implement | "recommend" |
| app_type | string | 否 | 应用类型：dashboard/ecommerce/social/admin | "dashboard" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 推荐方案或设计方案 | "{'component_lib':'Ant Design','pattern':'原子设计'}}" |

---

## 适用场景

### 适用场景
+技术选型
+架构设计

### 不适用场景
-内容为主
-简单静态页

---

## 依赖

ui-ux-pro-max

---

## 测试用例

```json
{
  "input": {"action":"recommend","app_type":"dashboard"},
  "expected_output": "推荐方案或设计方案"
}
```
