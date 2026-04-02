# Ios Development

**version**: 1.0.0

**description**: iOS原生应用开发，支持Swift和SwiftUI

---

## 一句话描述

iOS原生应用开发，支持Swift和SwiftUI

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| action | string | 是 | 操作：create/build/analyze | "create" |
| app_name | string | 是 | 应用名称 | "my_ios_app" |
| ui_framework | string | 否 | UI框架：swiftui/uikit | "swiftui" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 操作结果 | "iOS项目已创建: my_ios_app" |

---

## 适用场景

### 适用场景
+原生iOS
+Apple生态

### 不适用场景
-跨平台需求
-Android独占

---

## 依赖

Xcode, iOS SDK

---

## 测试用例

```json
{
  "input": {"action":"create","app_name":"my_app","ui_framework":"swiftui"},
  "expected_output": "操作结果"
}
```
