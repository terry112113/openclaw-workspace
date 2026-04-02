# Agent Tools

**version**: 1.0.0

**description**: Agent工具集成框架，支持多工具编排和复杂任务自动化

---

## 一句话描述

Agent工具集成框架，支持多工具编排和复杂任务自动化

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| task | string | 是 | 需要完成的复合任务 | "完成市场调研并生成报告" |
| tools | array | 是 | 可用的工具列表 | ["web-scraper","tavily-research","docx"] |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 任务执行结果和工具调用记录 | "{'result':'报告已完成','tools_used':['web-scraper']}" |

---

## 适用场景

### 适用场景
+多工具协作
+自动化流程
+复杂任务

### 不适用场景
-单一工具任务
-实时交互

---

## 依赖

多个工具Skills

---

## 测试用例

```json
{
  "input": {"task":"市场调研报告","tools":["web-scraper","docx"]},
  "expected_output": "任务执行结果和工具调用记录"
}
```
