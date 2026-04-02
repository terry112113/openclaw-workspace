# Health

**version**: 1.0.0

**description**: 健康检查和系统诊断，支持服务状态和性能监控

---

## 一句话描述

健康检查和系统诊断，支持服务状态和性能监控

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| target | string | 是 | 检查目标：system/service/deployment | "system" |
| detail | string | 否 | 详细程度：basic/detailed | "basic" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 健康检查结果 | "{'status':'healthy','cpu':30,'memory':60}" |

---

## 适用场景

### 适用场景
+系统监控
+服务健康检查

### 不适用场景
-代码调试
-功能测试

---

## 依赖

系统工具

---

## 测试用例

```json
{
  "input": {"target":"system","detail":"basic"},
  "expected_output": "健康检查结果"
}
```
