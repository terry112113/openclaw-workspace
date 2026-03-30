# 热记忆 - 最近1小时
> 最后更新：2026-03-30 19:18 GMT+8
> 版本：三司会审v3.0深度清理进行中

---

## 📍 当前状态
- **时间**：2026-03-30 19:18（周一晚）
- **地点**：三司会审架构v3.0深度清理
- **事件**：皇上指示清理旧大臣数据和安全隐患

---

## 🔴 发现的安全隐患

### 1. memory-keeper/.env 暴露API密钥
- 尉迟恭的ANTHROPIC_API_KEY和MINIMAX_API_KEY明文存储
- 路径：C:\Users\TL\.openclaw\memory-keeper\.env
- 状态：待删除

### 2. feishu/dedup/残留旧大臣数据
- 待删除：chengqiaojin, duruhui, fang, li, lijing, song, yuchigong, zhangsun
- 保留：di, main, memory-keeper, shensi, wei

---

## ✅ 已完成的清理
1. 删除shensi/wei/minsters/yuchigong/claude-code-skill目录
2. 删除agents/下8个旧大臣目录
3. 删除credentials/下13个旧API凭证
4. Git存档完成

---

## 📝 待执行
- 删除memory-keeper/.env（暴露API key）
- 清理feishu/dedup/旧大臣数据

---

*最后更新：2026-03-30 19:18 GMT+8*