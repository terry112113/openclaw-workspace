# Agent Fullstack Developer

**version**: 1.0.0

**description**: 全栈开发助手，支持前端、后端和数据库的代码生成和架构设计

---

## 一句话描述

全栈开发助手，支持前端、后端和数据库的代码生成和架构设计

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| component | string | 是 | 组件类型：frontend/backend/database/api | "backend" |
| spec | string | 是 | 功能描述或规格说明 | "RESTful API用于用户管理" |
| framework | string | 否 | 技术框架偏好 | "fastapi" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 完整的代码实现和说明文档 | "代码片段和架构图" |

---

## 适用场景

### 适用场景
+快速原型开发
+全栈项目
+代码生成

### 不适用场景
-复杂系统架构
-性能优化

---

## 依赖

无

---

## 测试用例

```json
{
  "input": {"component":"backend","spec":"RESTful API","framework":"fastapi"},
  "expected_output": "完整的代码实现和说明文档"
}
```
