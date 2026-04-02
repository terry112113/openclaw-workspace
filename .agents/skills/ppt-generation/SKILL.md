# Ppt Generation

**version**: 1.0.0

**description**: PPT演示文稿生成，支持多模板和自动化排版

---

## 一句话描述

PPT演示文稿生成，支持多模板和自动化排版

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| content | string | 是 | PPT内容或主题 | "Q1季度汇报" |
| template | string | 否 | 模板：business/creative/minimal | "business" |
| slides | number | 否 | 幻灯片数量 | 10 |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 生成的PPT文件路径 | "{'file':'Q1汇报.pptx','slides':10}" |

---

## 适用场景

### 适用场景
+商务演示
+报告展示

### 不适用场景
-复杂设计
-实时演示

---

## 依赖

python-pptx

---

## 测试用例

```json
{
  "input": {"content":"Q1汇报","template":"business","slides":10},
  "expected_output": "生成的PPT文件路径"
}
```
