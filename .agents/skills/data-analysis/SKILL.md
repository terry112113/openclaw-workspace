# Data Analysis

**version**: 1.0.0

**description**: 数据分析与统计，支持CSV/Excel数据处理和可视化

---

## 一句话描述

数据分析与统计，支持CSV/Excel数据处理和可视化

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| data_path | string | 是 | 数据文件路径 | "sales.csv" |
| analysis_type | string | 否 | 分析类型：summary/group/trend | "summary" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 数据分析结果和统计报告 | "{'total':100,'avg':25.5}" |

---

## 适用场景

### 适用场景
+CSV/Excel数据分析
+数据统计和汇总

### 不适用场景
-图片数据提取
-非结构化文本分析

---

## 依赖

pandas

---

## 测试用例

```json
{
  "input": {"data_path":"sales.csv","analysis_type":"summary"},
  "expected_output": "数据分析结果和统计报告"
}
```
