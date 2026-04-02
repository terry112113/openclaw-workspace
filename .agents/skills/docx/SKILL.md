# Docx

**version**: 1.0.0

**description**: Word文档创建和编辑，支持格式化文本、表格、图片

---

## 一句话描述

Word文档创建和编辑，支持格式化文本、表格、图片

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| content | string | 是 | 文档内容（Markdown格式） | "# 标题\n内容" |
| output_path | string | 是 | 输出文件路径 | "report.docx" |
| style | string | 否 | 文档样式：normal/report/scientific | "normal" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 操作结果 | "文档已创建: report.docx" |

---

## 适用场景

### 适用场景
+创建Word文档
+报告生成

### 不适用场景
-需要复杂排版
-需要保留原有格式

---

## 依赖

python-docx

---

## 测试用例

```json
{
  "input": {"content":"# 标题\n内容","output_path":"out.docx"},
  "expected_output": "操作结果"
}
```
