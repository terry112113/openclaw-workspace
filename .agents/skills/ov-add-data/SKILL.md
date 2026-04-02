# Ov Add Data

**version**: 1.0.0

**description**: 向OpenViking知识库添加数据，支持文档和项目信息录入

---

## 一句话描述

向OpenViking知识库添加数据，支持文档和项目信息录入

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| data_type | string | 是 | 数据类型：doc/project/note | "doc" |
| content | string | 是 | 数据内容 | "项目文档内容..." |
| tags | array | 否 | 标签 | ["AI","项目"] |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 添加结果 | "{'id':'doc-123','status':'added'}" |

---

## 适用场景

### 适用场景
+知识积累
+文档入库

### 不适用场景
-敏感信息
-临时数据

---

## 依赖

OpenViking

---

## 测试用例

```json
{
  "input": {"data_type":"doc","content":"内容...","tags":["AI"]},
  "expected_output": "添加结果"
}
```
