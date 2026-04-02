# Cron

**version**: 1.0.0

**description**: 定时提醒和周期性任务调度，支持一次性提醒和循环任务

---

## 一句话描述

定时提醒和周期性任务调度，支持一次性提醒和循环任务

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| action | string | 是 | 操作类型：add/list/remove | "add" |
| message | string | 是 | 提醒内容 | "会议5分钟后开始" |
| every_seconds | number | 否 | 循环间隔秒数 | 3600 |
| at | string | 否 | 一次性执行时间(ISO格式) | "2026-04-01T15:00:00" |
| job_id | string | 否 | 任务ID（remove时必填） | "job-123" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 操作结果或执行反馈 | "{'job_id':'job-123','next_run':'15:00'}" |

---

## 适用场景

### 适用场景
+定时提醒
+周期任务
+自动化调度

### 不适用场景
-实时任务
-长时间运行任务

---

## 依赖

Cron系统

---

## 测试用例

```json
{
  "input": {"action":"add","message":"会议5分钟后","every_seconds":3600},
  "expected_output": "操作结果或执行反馈"
}
```
