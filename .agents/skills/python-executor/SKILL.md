# Python Executor

**version**: 1.0.0

**description**: 安全执行Python代码，支持数据分析、脚本运行和原型验证

---

## 一句话描述

安全执行Python代码，支持数据分析、脚本运行和原型验证

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| code | string | 是 | Python代码 | "print('Hello')" |
| timeout | number | 否 | 超时时间（秒） | 30 |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 执行结果或错误 | "{'output':'Hello','error':null,'exec_time':'0.01s'}" |

---

## 适用场景

### 适用场景
+代码执行
+数据分析
+原型验证

### 不适用场景
-复杂应用
-需要持久化

---

## 依赖

Python解释器

---

## 测试用例

```json
{
  "input": {"code":"print(1+1)","timeout":10},
  "expected_output": "执行结果或错误"
}
```
