# Claude To Deerflow

**version**: 1.0.0

**description**: Claude到DeerFlow的迁移工具，支持项目和任务转换

---

## 一句话描述

Claude到DeerFlow的迁移工具，支持项目和任务转换

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| project_path | string | 是 | 项目路径 | "./my-project" |
| target_format | string | 否 | 目标格式 | "deerflow" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 转换结果 | "{'status':'converted','files':5}" |

---

## 适用场景

### 适用场景
+项目迁移
+格式转换

### 不适用场景
-非兼容项目
-实时协作

---

## 依赖

DeerFlow CLI

---

## 测试用例

```json
{
  "input": {"project_path":"./myproject","target_format":"deerflow"},
  "expected_output": "转换结果"
}
```
