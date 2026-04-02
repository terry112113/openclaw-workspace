# Summarize

**version**: 1.0.0

**description**: 文章和长文本摘要，将长内容压缩为关键要点

---

## 一句话描述

文章和长文本摘要，将长内容压缩为关键要点

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| content | string | 是 | 要摘要的内容 | "长篇文章内容..." |
| length | string | 否 | 摘要长度：brief/medium/detailed | "brief" |
| format | string | 否 | 输出格式：bullet/paragraph/json | "bullet" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 摘要内容 | "- 关键点1\n- 关键点2" |

---

## 适用场景

### 适用场景
+长文摘要
+会议记录
+报告总结

### 不适用场景
-短内容
-需要完整细节

---

## 依赖

无

---

## 测试用例

```json
{
  "input": {"content":"长篇文章...","length":"brief","format":"bullet"},
  "expected_output": "摘要内容"
}
```
