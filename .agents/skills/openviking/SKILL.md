# Openviking

**version**: 1.0.0

**description**: OpenViking开源项目研究，支持项目分析和技术调研

---

## 一句话描述

OpenViking开源项目研究，支持项目分析和技术调研

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| action | string | 是 | 操作：analyze/summarize/compare | "analyze" |
| project_url | string | 是 | 项目URL或名称 | "https://github.com/.../repo" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 项目分析报告 | "{'tech_stack':['React','Node'],'stars':1000,'analysis':'...'}" |

---

## 适用场景

### 适用场景
+开源项目研究
+技术选型参考

### 不适用场景
-非开源项目
-商业软件

---

## 依赖

网络访问

---

## 测试用例

```json
{
  "input": {"action":"analyze","project_url":"https://github.com/.../repo"},
  "expected_output": "项目分析报告"
}
```
