# Ov Search Context

**version**: 1.0.0

**description**: 在OpenViking知识库中语义搜索相关上下文

---

## 一句话描述

在OpenViking知识库中语义搜索相关上下文

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| query | string | 是 | 搜索查询 | "微服务架构设计" |
| top_k | number | 否 | 返回结果数 | 5 |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 相关文档片段 | "{'contexts':[{'content':'...','score':0.9}],'count':3}" |

---

## 适用场景

### 适用场景
+上下文检索
+知识复用

### 不适用场景
-实时信息
-简单查询

---

## 依赖

OpenViking, 向量数据库

---

## 测试用例

```json
{
  "input": {"query":"微服务架构","top_k":5},
  "expected_output": "相关文档片段"
}
```
