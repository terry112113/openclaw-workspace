# Self Improving Agent

**version**: 1.0.0

**description**: 自进化Agent框架，根据执行结果自动反思和改进决策策略

---

## 一句话描述

自进化Agent框架，根据执行结果自动反思和改进决策策略

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| task | string | 是 | 需要完成的任务描述 | "完成代码审查" |
| feedback | string | 是 | 执行结果的反馈信息 | "审查结果不够深入" |
| iteration | number | 否 | 当前迭代次数 | 1 |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 改进后的任务执行方案 | "{'improved_approach':'重点关注安全性','confidence':0.8}" |

---

## 适用场景

### 适用场景
+持续改进
+复杂推理
+自适应决策

### 不适用场景
-一次性任务
-简单操作

---

## 依赖

无

---

## 测试用例

```json
{
  "input": {"task":"代码审查","feedback":"不够深入","iteration":1},
  "expected_output": "改进后的任务执行方案"
}
```
