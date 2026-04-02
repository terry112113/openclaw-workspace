# Devops Cicd

**version**: 1.0.0

**description**: CI/CD流水线配置和优化，支持GitHub Actions等平台

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| platform | string | 是 | CI/CD平台：github/gitlab/jenkins |
| action | string | 否 | 操作类型：setup(创建)/optimize(优化)/debug |

### 输出（Returns）

| 类型 | 说明 |
|------|------|
| string | 流水线配置文件或调试建议 |

---

## 适用场景

- 需要CI/CD流水线配置和优化的场景
- 自动化任务执行
- 信息检索和分析

---

## 依赖

- 依赖其他Skill：无
- 环境要求：无

---

## 版本历史

- 1.0.0 (2026-04-01): 补充真实IO文档

## 测试用例

```json
{
  "input": {
    "platform": "test value"
  },
  "expected_output": "流水线配置文件或调试建议"
}
```
