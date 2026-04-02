# Frontend Mobile Development Component Scaffold

**version**: 1.0.0

**description**: 前端移动端组件脚手架，支持React Native和Flutter组件生成

---

## 一句话描述

前端移动端组件脚手架，支持React Native和Flutter组件生成

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| component_name | string | 是 | 组件名称 | "LoginForm" |
| framework | string | 否 | 框架：react-native/flutter | "react-native" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 组件代码 | "{'code':'export const LoginForm...','files':1}" |

---

## 适用场景

### 适用场景
+快速原型
+组件生成

### 不适用场景
-复杂业务逻辑
-全栈应用

---

## 依赖

React Native/Flutter

---

## 测试用例

```json
{
  "input": {"component_name":"UserCard","framework":"react-native"},
  "expected_output": "组件代码"
}
```
