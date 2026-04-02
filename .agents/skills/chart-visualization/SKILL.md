# Chart Visualization

**version**: 1.0.0

**description**: 图表可视化，支持多种图表类型和数据绑定

---

## 一句话描述

图表可视化，支持多种图表类型和数据绑定

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| chart_type | string | 是 | 图表类型：bar/line/pie/scatter/radar | "bar" |
| data | array | 是 | 数据数组 | [["苹果",30],["香蕉",50]] |
| title | string | 否 | 图表标题 | "水果销量" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 图表配置或图片路径 | "{'type':'bar','data':[...],'config':{}}" |

---

## 适用场景

### 适用场景
+数据可视化
+报表图表

### 不适用场景
-非结构化数据
-复杂关系图

---

## 依赖

matplotlib/echarts

---

## 测试用例

```json
{
  "input": {"chart_type":"bar","data":[["苹果",30]],"title":"水果销量"},
  "expected_output": "图表配置或图片路径"
}
```
