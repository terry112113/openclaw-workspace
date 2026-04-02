# Ai Video Generation

**version**: 1.0.0

**description**: AI视频生成，支持文字转视频和图片转视频

---

## 一句话描述

AI视频生成，支持文字转视频和图片转视频

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| prompt | string | 是 | 视频描述 | "日出云海航拍" |
| duration | number | 否 | 时长（秒） | 5 |
| fps | number | 否 | 帧率 | 30 |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 视频文件路径 | "{'video':'/path/to/video.mp4'}" |

---

## 适用场景

### 适用场景
+短视频生成
+概念演示
+营销视频

### 不适用场景
-长视频
-复杂剧情

---

## 依赖

视频生成API

---

## 测试用例

```json
{
  "input": {"prompt":"海浪日出","duration":5},
  "expected_output": "视频文件路径"
}
```
