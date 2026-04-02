# Image Generation

**version**: 1.0.0

**description**: AI图像生成，支持文生图、图生图和图像编辑

---

## 一句话描述

AI图像生成，支持文生图、图生图和图像编辑

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| prompt | string | 是 | 图像描述词 | "一只可爱的猫咪" |
| size | string | 否 | 图像尺寸：1024x1024/1536x1024 | "1024x1024" |
| model | string | 否 | 生成模型 | "dall-e-3" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 生成的图像URL或路径 | "https://.../image.png" |

---

## 适用场景

### 适用场景
+插图/配图生成
+概念可视化

### 不适用场景
-需要精确人脸/文字
-商业logo设计

---

## 依赖

OpenAI API或DALL-E

---

## 测试用例

```json
{
  "input": {"prompt":"一只可爱的猫咪","size":"1024x1024"},
  "expected_output": "生成的图像URL或路径"
}
```
