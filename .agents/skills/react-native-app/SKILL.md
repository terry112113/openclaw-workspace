# React Native App

**version**: 1.0.0

**description**: React Native跨平台移动开发，一套代码同时支持iOS和Android

---

## 一句话描述

React Native跨平台移动开发，一套代码同时支持iOS和Android

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| action | string | 是 | 操作：create/build/analyze | "create" |
| app_name | string | 是 | 应用名称 | "my_rn_app" |
| template | string | 否 | 项目模板：default/tabs/expo | "default" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 操作结果 | "React Native项目已创建: my_rn_app" |

---

## 适用场景

### 适用场景
+跨平台App
+快速开发

### 不适用场景
-需要原生性能
-复杂游戏

---

## 依赖

React Native CLI

---

## 测试用例

```json
{
  "input": {"action":"create","app_name":"my_app","template":"default"},
  "expected_output": "操作结果"
}
```
