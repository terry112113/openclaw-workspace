# Data Visualization

**version**: 1.0.0

**description**: 数据可视化工程，支持复杂图表和仪表盘设计

---

## 一句话描述

数据可视化工程，支持复杂图表和仪表盘设计

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| data_source | string | 是 | 数据源 | "sales.csv" |
| viz_type | string | 否 | 可视化类型：dashboard/report/explore | "dashboard" |
| metrics | array | 否 | 关键指标 | ["销售额","增长率"] |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 可视化配置或HTML | "{'dashboard_url':'...','widgets':5}" |

---

## 适用场景

### 适用场景
+数据仪表盘
+BI报表

### 不适用场景
-简单图表
-实时监控

---

## 依赖

可视化库

---

## 测试用例

```json
{
  "input": {"data_source":"sales.csv","viz_type":"dashboard","metrics":["销售额"]},
  "expected_output": "可视化配置或HTML"
}
```
