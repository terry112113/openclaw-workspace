# Opencode

**version**: 1.0.0

**description**: 本地AI编程工具，支持代码生成、调试和项目分析

---

## 一句话描述

本地AI编程工具，支持代码生成、调试和项目分析

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| task | string | 是 | 任务描述 | "修复登录Bug" |
| codebase | string | 否 | 代码库路径 | "./src" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 任务结果 | "{'fixed':true,'files_modified':2}" |

---

## 适用场景

### 适用场景
+代码生成
+Bug修复
+代码审查

### 不适用场景
-非代码任务
-文档编写

---

## 依赖

opencode CLI

---

## 测试用例

```json
{
  "input": {"task":"添加单元测试","codebase":"./src"},
  "expected_output": "任务结果"
}
```
