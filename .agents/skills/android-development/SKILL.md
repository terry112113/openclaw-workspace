# Android Development

**version**: 1.0.0

**description**: Android原生应用开发，支持Kotlin/Java和Jetpack Compose

---

## 一句话描述

Android原生应用开发，支持Kotlin/Java和Jetpack Compose

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| action | string | 是 | 操作：create/build/analyze | "create" |
| app_name | string | 是 | 应用名称 | "my_android_app" |
| language | string | 否 | 开发语言：kotlin/java | "kotlin" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 操作结果 | "Android项目已创建: my_android_app" |

---

## 适用场景

### 适用场景
+原生Android
+性能关键

### 不适用场景
-跨平台需求
-iOS独占

---

## 依赖

Android SDK

---

## 测试用例

```json
{
  "input": {"action":"create","app_name":"my_app","language":"kotlin"},
  "expected_output": "操作结果"
}
```
