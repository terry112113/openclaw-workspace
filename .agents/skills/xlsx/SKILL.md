# Xlsx

**version**: 1.0.0

**description**: Excel表格创建和编辑，支持公式、数据透视表、多sheet

---

## 一句话描述

Excel表格创建和编辑，支持公式、数据透视表、多sheet

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| action | string | 是 | 操作类型：create/edit/read | "create" |
| data | array | 是 | 表格数据（二维数组） | [["Name","Age"],["Tom",25]] |
| output_path | string | 否 | 输出文件路径 | "data.xlsx" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 操作结果或数据 | "{'sheet1':[['Name','Age'],['Tom',25]]}" |

---

## 适用场景

### 适用场景
+Excel数据处理
+报表生成

### 不适用场景
-需要复杂图表
-跨文件引用

---

## 依赖

openpyxl

---

## 测试用例

```json
{
  "input": {"action":"create","data":[["Name","Age"],["Tom",25]]},
  "expected_output": "操作结果或数据"
}
```
