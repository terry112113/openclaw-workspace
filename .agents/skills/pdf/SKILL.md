# Pdf

**version**: 1.0.0

**description**: PDF文档处理，包括读取文本、提取表格、合并拆分

---

## 一句话描述

PDF文档处理，包括读取文本、提取表格、合并拆分

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| action | string | 是 | 操作类型：read/extract/merge/split | "read" |
| file_path | string | 是 | PDF文件路径 | "doc.pdf" |
| pages | string | 否 | 页码范围（如'1-5'） | "1-3" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | PDF内容或操作结果 | "提取的PDF文本内容..." |

---

## 适用场景

### 适用场景
+PDF文本提取
+合并/拆分PDF

### 不适用场景
-扫描版PDF（需要OCR）
-大批量处理

---

## 依赖

pypdf2或pdfplumber

---

## 测试用例

```json
{
  "input": {"action":"read","file_path":"doc.pdf","pages":"1-3"},
  "expected_output": "PDF内容或操作结果"
}
```
