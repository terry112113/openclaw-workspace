# Shader Programming

**version**: 1.0.0

**description**: Shader着色器编程，支持GLSL/HLSL代码生成和实时渲染

---

## 一句话描述

Shader着色器编程，支持GLSL/HLSL代码生成和实时渲染

---

## 输入输出

### 输入（Parameters）

| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|--------|
| shader_type | string | 是 | 着色器类型：vertex/fragment/compute | "fragment" |
| effect | string | 是 | 效果描述 | "水波纹动画" |

### 输出（Returns）

| 类型 | 说明 | 示例 |
|------|------|------|
| string | Shader代码 | "{'code':'void main() {...}','type':'fragment'}" |

---

## 适用场景

### 适用场景
+视觉效果
+游戏开发
+实时渲染

### 不适用场景
-非图形任务
-通用计算

---

## 依赖

GPU编程环境

---

## 测试用例

```json
{
  "input": {"shader_type":"fragment","effect":"火焰效果"},
  "expected_output": "Shader代码"
}
```
