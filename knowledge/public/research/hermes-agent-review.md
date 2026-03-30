# hermes-agent 评估报告

**评估人：** 李元芳（都察院御史）
**日期：** 2026-03-30
**研究对象：** NousResearch/hermes-agent

---

## 核心能力

### 1. 内置学习循环（最大亮点）
hermes-agent 是**唯一**自称有内置学习循环的 AI agent：

- **自主记忆入库**：agent 会自动判断"这条知识该记住"，主动调用 memory 工具写入 MEMORY.md
- **自动创建 skill**：复杂任务（≥5次工具调用）完成后，agent 自动将工作流封装为 SKILL.md，供后续复用
- **skill 自我改进**：使用过程中 agent 发现更好的方法，会主动 patch/update 已有的 skill
- **FTS5 会话搜索**：跨会话全文本搜索 + LLM 摘要总结（session_search 工具）
- **周期性 nudge**：agent 会主动提醒自己"该记住这个了"，防止知识流失

### 2. Skill 系统
- **SKILL.md 格式**：与 agentskills.io 开放标准兼容，可跨平台移植
- **渐进式披露（3级加载）**：skills_list → skill_view → skill_view(path)，节省 token
- **Skills Hub**：社区 skill 市场，支持从 GitHub/skills.sh/mintlify 等直接安装
- **条件激活**：skill 可声明 fallback_for_toolsets（免费替代方案自动兜底）
- **外部目录扫描**：可共享其他工具的 skill 目录（如 OpenClaw 的 skills/）

### 3. 记忆系统
- **双文件机制**：MEMORY.md（agent笔记，2200字符）+ USER.md（用户画像，1375字符）
- **容量硬限制**：防止系统 prompt 膨胀，超限需先合并/删除旧条目
- **会话搜索**：SQLite FTS5 全文索引所有历史会话
- **Honcho 集成**：可选的云端跨平台用户建模层（dual-peer 架构，user+AI 双视角）

### 4. 用户建模（Honcho）
- **跨会话学习**：不只记住用户说了什么，而是从对话中推断用户偏好、目标、沟通风格
- **双视角架构**：同时观察用户消息和 AI 回复，建模双方
- **动态推理深度**：根据消息复杂度自动调节 dialectic reasoning 层级
- **多平台共享**：通过 linkedHosts 跨 Telegram/Discord/Slack 等平台整合用户画像

### 5. 多端部署
| 方式 | 说明 | 成本 |
|------|------|------|
| 本地 CLI | Linux/macOS/WSL2 | 纯本地，零额外成本 |
| Docker | 隔离容器 | 同上 |
| SSH | 远程安全执行 | 服务器成本 |
| **Daytona** | Serverless 沙箱，按秒计费，可 hibernation | vCPU $0.0504/h，内存 $0.0162/GiB/h；注册送 $200 免费额度 |
| **Modal** | Serverless，弹性扩缩，零时休眠 | $0.00003942/core/sec，$0.00000672/GiB/sec；创业公司送 $25k 额度 |
| Singularity | HPC 容器 | 集群成本 |

### 6. 多消息平台
Telegram、Discord、Slack、WhatsApp、Signal、Email，统一 gateway 管理，一次配置全端可达。

### 7. OpenClaw 迁移支持
内置 `hermes claw migrate` 命令，可自动导入：SOUL.md、记忆文件、skills、API keys、TTS 资源等。

---

## 对三司会审的价值

### 高度匹配的能力

1. **Skill 创建机制 → 可成为宋慈（刑部尚书）的"案例库"**
   - 宋慈每审完一个案子，自动生成 skill 供下次复用
   - 团队共享的审判经验 skill 库，直接从 agentskills.io 安装

2. **学习循环 → 持续进化的御史台**
   - agent 自我改进能力极强，随着使用越来越懂太上皇的偏好
   - 不需要每次从头训练，持久化学习

3. **Honcho 跨平台用户建模 → 更懂太上皇的数字管家**
   - 三司会审架构中，狄仁杰（主agent）可以借助 Honcho 更深理解太上皇
   - 跨 Telegram/Discord 多平台感知用户状态

4. **Serverless 部署 → 极低成本7×24候命**
   - Daytona/Modal 在闲置时 hibernation，几乎零成本
   - 适合作为"永不打扰但随时待命"的御史助手

5. **渐进式 skill 加载 → token 高效**
   - 不需要把所有 skill 说明塞进 context，按需加载
   - 与 OpenClaw 的 skill 系统理念相似，可互补

### 可借鉴的设计

| hermes 设计 | 三司会审对应 |
|------------|-------------|
| memory nudge（周期性提醒自己记忆）| 御史台"记事"传统 |
| skill self-improvement | 判例累积迭代 |
| FTS5 session search | 翻阅档案查找旧案 |
| Honcho dual-peer modeling | 君臣双向了解 |

---

## 风险/问题

### 1. 身份定位冲突
- **问题**：hermes-agent 是一个通用 agent，与三司会审的角色分工（狄仁杰主持/李元芳研究/魏征执行）存在重叠
- **风险**：如果直接使用 hermes 作为某一角色，会与 OpenClaw 体系产生竞争关系
- **建议**：仅作为**工具型 skill 库**引入，不作为独立 agent 角色

### 2. SOUL.md 与 OpenClaw SOUL.md 可能冲突
- hermes 的 SOUL.md 位于 `~/.hermes/SOUL.md`（固定位置）
- OpenClaw 的 SOUL.md 位于 workspace 根目录（多 workspace 时各不同）
- 如果同时运行两者，需要精心管理两份 SOUL.md

### 3. Honcho 是第三方依赖
- Honcho 有自己的 API key、账户体系、云端存储
- 用户画像数据存储在 honcho.dev，而非本地
- **隐私风险**：太上皇的用户画像会上传到第三方（即便 honcho 支持自托管）

### 4. Windows 不支持
- hermes-agent 明确不支持 Windows Native，需要 WSL2
- 太上皇的系统是 Windows（DESKTOP-CT9HFKB），必须通过 WSL2 运行
- 这会增加一定的运维复杂度

### 5. 学习循环的可靠性
- agent 自动创建 skill 是基于规则触发的（≥5次工具调用），不是真正的 RL
- "自我改进"能力依赖模型自身的判断质量，可能产生质量参差不齐的 skill
- 御史台的专业性要求 skill 质量稳定，自动创建可能产生"噪声 skill"

### 6. Serverless 冷启动延迟
- Daytona 和 Modal 在 hibernation 后需要重新唤醒
- 对于需要即时响应的御史台场景，冷启动延迟可能影响体验

### 7. 与 OpenClaw 的迁移完整性存疑
- 虽然有迁移工具，但迁移后 hermes 的 skill 与 OpenClaw 的 skill 是两套独立系统
- 无法在两者之间双向同步

---

## 技术细节摘要

### 学习循环工作流
```
任务执行（≥5次工具调用）
    ↓
agent 判断"该创建 skill" 或 "该改进 skill"
    ↓
skill_manage tool → 写入 ~/.hermes/skills/[category]/[skill-name]/SKILL.md
    ↓
下次遇到类似任务 → skill_view 加载 → 执行
    ↓
执行中发现更好方法 → skill_manage(patch) → 更新 skill
```

### 记忆系统 vs OpenClaw

| 维度 | hermes-agent | OpenClaw |
|------|-------------|----------|
| 容量管理 | 硬限制（2200/1375字符）| 无硬限制，按需增长 |
| 写入方式 | agent 主动自动 | agent 主动 + 用户提醒 |
| 会话搜索 | FTS5 SQLite 全文索引 | 依赖 daily notes 手动记录 |
| 用户建模 | Honcho（云端 dual-peer）| USER.md（本地单视角）|
| skill 创建 | 自动触发 + 自动改进 | 手动 skill-create（当前能力范围内）|
| 安全扫描 | memory entry 有注入扫描 | 依赖系统 prompt 隔离 |

---

## 结论：条件推荐

**评分：★★★☆☆（三星半）**

### 推荐引入的场景
- 太上皇希望三司会审系统拥有**更强的学习能力**和**skill 自我进化**
- 需要从 hermes 的 Skills Hub 引入**第三方专业 skill**（如复杂开发、MLOps 等）
- 计划在 **serverless 架构**上部署一个 7×24 待命的轻量御史助手

### 不推荐引入的场景
- 太上皇更看重**本地化、隐私优先**（Honcho 上云是障碍）
- OpenClaw 本身已能很好满足当前需求（避免架构冗余）
- Windows 环境为主（WSL2 依赖增加复杂度）

### 最佳整合方式
**以 skill 库 + 工具集成的方式引入，而非作为独立 agent 角色：**

1. 迁移 hermes 的优质 bundled skills 到 OpenClaw skills/
2. 借鉴 hermes 的 `memory nudge` 机制改进 OpenClaw 的主动记忆触发
3. 评估 Honcho 自托管方案（如本地部署 honcho）解决隐私问题
4. Daytona serverless 作为 OpenClaw agent 的远程执行后端（替代危险的本地 terminal）

### 一句话评价
> hermes-agent 是目前开源 agent 中学习机制最完整的项目之一，其 skill 自进化和周期性 nudge 设计值得 OpenClaw 深度借鉴；但其云端依赖（Honcho）和 Windows 不友好的限制，使其更适合作为 OpenClaw 的**外部 skill 技能库和架构参考**，而非直接替换三司会审中的任何角色。
