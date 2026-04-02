# Case Study Writing

**version**: 1.0.0

**description**: 案例研究文档写作，支持商业/技术案例的结构化呈现

---

## 一句话描述

案例研究文档写作，支持商业/技术案例的结构化呈现

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| case_type | string | 是 | 案例类型：business/technical/success/failure | "business" |
| subject | string | 是 | 案例主题 | "某电商平台转型" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 结构化案例文档 | "背景:... 问题:... 解决方案:..." |

---

## 适用场景

### 适用场景
+商业案例
+项目复盘

### 不适用场景
-新闻报道
-营销文案

---

## 依赖

无

---

## 测试用例

```json
{
  "input": {"case_type":"business","subject":"电商转型"},
  "expected_output": "结构化案例文档"
}
```
