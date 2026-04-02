# Vercel Deploy

**version**: 1.0.0

**description**: Vercel平台部署，支持前端项目和Serverless函数一键部署

---

## 一句话描述

Vercel平台部署，支持前端项目和Serverless函数一键部署

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| action | string | 是 | 操作：deploy/status/rollback | "deploy" |
| project_path | string | 是 | 项目路径 | "./my-project" |
| env | string | 否 | 部署环境：production/preview | "production" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 部署结果和URL | "{'url':'https://my-project.vercel.app','status':'deployed'}" |

---

## 适用场景

### 适用场景
+前端部署
+SSR应用
+Serverless

### 不适用场景
-需要长期运行的服务
-复杂后端

---

## 依赖

Vercel CLI

---

## 测试用例

```json
{
  "input": {"action":"deploy","project_path":"./my-project","env":"production"},
  "expected_output": "部署结果和URL"
}
```
