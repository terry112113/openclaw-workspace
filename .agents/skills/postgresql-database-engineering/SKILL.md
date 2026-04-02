# Postgresql Database Engineering

**version**: 1.0.0

**description**: PostgreSQL数据库工程，支持Schema设计、查询优化和备份

---

## 一句话描述

PostgreSQL数据库工程，支持Schema设计、查询优化和备份

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| action | string | 是 | 操作：design/query/optimize/backup | "design" |
| spec | string | 否 | 数据库规格描述 | "用户和订单系统" |
| sql | string | 否 | SQL语句（query/optimize时必填） | "SELECT * FROM users" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 操作结果 | "{'schema':'CREATE TABLE...','tables':5}" |

---

## 适用场景

### 适用场景
+数据库设计
+查询优化
+数据迁移

### 不适用场景
-NoSQL需求
-实时大数据

---

## 依赖

PostgreSQL

---

## 测试用例

```json
{
  "input": {"action":"design","spec":"用户系统"},
  "expected_output": "操作结果"
}
```
