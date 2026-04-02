# Agent Governance

**version**: 1.0.0

**description**: Agent治理框架，支持多Agent协作、任务分配和冲突仲裁

---

## 一句话描述

Agent治理框架，支持多Agent协作、任务分配和冲突仲裁

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| task | string | 是 | 任务描述 | "完成产品需求分析" |
| agents | array | 是 | 参与Agent列表 | ["狄仁杰","李元芳","魏征"] |
| mode | string | 否 | 协作模式：sequential/parallel/hierarchical | "hierarchical" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 任务分配结果和执行状态 | "{'分配':{'狄仁杰':'决策','李元芳':'调研'},'状态':'进行中'}" |

---

## 适用场景

### 适用场景
+多Agent协作
+任务分配
+冲突解决

### 不适用场景
-单一Agent任务
-实时操作

---

## 依赖

三司会审流程

---

## 测试用例

```json
{
  "input": {"task":"产品需求分析","agents":["狄仁杰","李元芳"],"mode":"hierarchical"},
  "expected_output": "任务分配结果和执行状态"
}
```
