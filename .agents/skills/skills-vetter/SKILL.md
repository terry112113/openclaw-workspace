# Skills Vetter

**version**: 1.0.0

**description**: Skills质量审核工具，验证SKILL.md的完整性和合规性

---

## 一句话描述

Skills质量审核工具，验证SKILL.md的完整性和合规性

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| skill_path | string | 是 | Skill目录路径 | "./skills/my-skill" |
| check_level | string | 否 | 检查级别：basic/full | "basic" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 审核报告 | "{'passed':true,'issues':[],'score':95}" |

---

## 适用场景

### 适用场景
+技能审核
+质量把控

### 不适用场景
-非Skills项目

---

## 依赖

无

---

## 测试用例

```json
{
  "input": {"skill_path":"./skills/my-skill","check_level":"basic"},
  "expected_output": "审核报告"
}
```
