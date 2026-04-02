# Skill Creator

**version**: 1.0.0

**description**: 创建和改进Skills，包含测试用例编写和性能基准测试

---

## 一句话描述

创建和改进Skills，包含测试用例编写和性能基准测试

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| task | string | 是 | 任务类型：create/improve/test/benchmark | "create" |
| skill_name | string | 否 | 技能名称（improve/test时必填） | "my-new-skill" |
| description | string | 否 | 技能描述（create时必填） | "处理X任务的技能" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 创建的SKILL.md内容或测试结果 | "SKILL.md已创建，包含完整IO定义" |

---

## 适用场景

### 适用场景
+创建新技能
+改进现有技能
+技能测试

### 不适用场景
-日常任务
-非技能开发

---

## 依赖

Claude Code（用于测试）

---

## 测试用例

```json
{
  "input": {"task":"create","description":"测试技能"},
  "expected_output": "创建的SKILL.md内容或测试结果"
}
```
