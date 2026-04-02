# Linkedin Content

**version**: 1.0.0

**description**: LinkedIn内容创作，支持专业文章和动态发布

---

## 一句话描述

LinkedIn内容创作，支持专业文章和动态发布

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| content | string | 是 | 内容 | "分享一个职业洞察..." |
| type | string | 否 | 内容类型：post/article/update | "post" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 创作建议 | "{'hashtags':['#职业','#成长'],'engagement':'预计中等'}" |

---

## 适用场景

### 适用场景
+职业内容
+个人品牌

### 不适用场景
-非专业内容
-产品推销

---

## 依赖

无

---

## 测试用例

```json
{
  "input": {"content":"职业洞察...","type":"post"},
  "expected_output": "创作建议"
}
```
