# Docker

**version**: 1.0.0

**description**: Docker容器管理，支持镜像构建、容器运行和编排

---

## 一句话描述

Docker容器管理，支持镜像构建、容器运行和编排

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| action | string | 是 | 操作：build/run/ps/pull | "build" |
| image | string | 否 | 镜像名称 | "myapp:latest" |
| container_name | string | 否 | 容器名称 | "myapp-prod" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 操作结果 | "镜像构建成功: myapp:latest" |

---

## 适用场景

### 适用场景
+容器化部署
+开发环境搭建

### 不适用场景
-Windows原生应用
-需要GPU的应用

---

## 依赖

Docker

---

## 测试用例

```json
{
  "input": {"action":"build","image":"myapp:latest"},
  "expected_output": "操作结果"
}
```
