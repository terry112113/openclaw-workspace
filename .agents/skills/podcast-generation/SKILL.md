# Podcast Generation

**version**: 1.0.0

**description**: 播客内容生成，支持音频脚本创作和节目策划

---

## 一句话描述

播客内容生成，支持音频脚本创作和节目策划

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| topic | string | 是 | 播客主题 | "AI改变生活" |
| duration | number | 否 | 时长（分钟） | 30 |
| format | string | 否 | 格式：interview/solo/discussion | "discussion" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 播客脚本和策划 | "{'outline':'开场-话题1-话题2-结尾','script':'...'}" |

---

## 适用场景

### 适用场景
+播客创作
+内容策划

### 不适用场景
-视频内容
-实时互动

---

## 依赖

无

---

## 测试用例

```json
{
  "input": {"topic":"AI改变生活","duration":30,"format":"discussion"},
  "expected_output": "播客脚本和策划"
}
```
