# Consulting Analysis

**version**: 1.0.0

**description**: 商业咨询分析，支持市场分析、竞品研究和战略建议

---

## 一句话描述

商业咨询分析，支持市场分析、竞品研究和战略建议

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| company | string | 是 | 公司/产品名称 | "某在线教育平台" |
| analysis_type | string | 否 | 分析类型：market/competitor/strategy | "market" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 咨询分析报告 | "{'market_size':'100亿','growth':'15%'}" |

---

## 适用场景

### 适用场景
+商业分析
+战略咨询

### 不适用场景
-技术细节
-实时数据

---

## 依赖

网络搜索API

---

## 测试用例

```json
{
  "input": {"company":"某教育平台","analysis_type":"market"},
  "expected_output": "咨询分析报告"
}
```
