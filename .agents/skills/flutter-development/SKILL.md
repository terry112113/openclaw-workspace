# Flutter Development

**version**: 1.0.0

**description**: Flutter移动应用开发，支持跨平台iOS/Android应用构建

---

## 一句话描述

Flutter移动应用开发，支持跨平台iOS/Android应用构建

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| action | string | 是 | 操作类型：create/build/analyze | "create" |
| app_name | string | 是 | 应用名称 | "my_flutter_app" |
| template | string | 否 | 项目模板：flutter/react/screen | "flutter" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 操作结果 | "Flutter项目已创建: my_flutter_app" |

---

## 适用场景

### 适用场景
+跨平台App
+原型开发

### 不适用场景
-Web应用
-游戏开发

---

## 依赖

Flutter SDK

---

## 测试用例

```json
{
  "input": {"action":"create","app_name":"my_app","template":"flutter"},
  "expected_output": "操作结果"
}
```
