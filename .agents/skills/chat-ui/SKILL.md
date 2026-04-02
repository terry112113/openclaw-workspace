# Chat Ui

**version**: 1.0.0

**description**: 对话界面设计，支持聊天机器人UI和对话流设计

---

## 一句话描述

对话界面设计，支持聊天机器人UI和对话流设计

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| action | string | 是 | 操作：design/preview/generate | "design" |
| platform | string | 否 | 平台：web/mobile/embed | "web" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | UI设计或代码 | "{'html':'<div>...','css':'...'}" |

---

## 适用场景

### 适用场景
+聊天UI设计
+对话流设计

### 不适用场景
-后端逻辑
-后端API

---

## 依赖

前端框架

---

## 测试用例

```json
{
  "input": {"action":"design","platform":"web"},
  "expected_output": "UI设计或代码"
}
```
