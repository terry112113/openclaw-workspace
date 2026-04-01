# OpenViking × OpenClaw 集成方案

**编制：李元芳（都察院御史，INTJ建筑师型）**  
**日期：2026-03-29**  
**密级：内部研究 — 呈狄仁杰大人审阅**

---

## 一、研究概述

### 1.1 OpenViking 是什么

**OpenViking**（[volcengine/OpenViking](https://github.com/volcengine/OpenViking)，⭐ 19.8k）是火山引擎开源的**上下文数据库（Context Database）**，专为 AI Agent 设计。

核心创新：**用文件系统（filesystem paradigm）统一管理 Agent 需要的一切上下文**——记忆、资源、技能。

### 1.2 官方明确支持 OpenClaw

OpenViking 仓库 examples 目录下有**官方的 openclaw-plugin**（Plugin 2.0，context-engine 架构），这不是第三方 fork，是根仓库的原生集成。

> ⚠️ 注意：第三方独立集成仓库（如 VikingClaw）已标注 "useless now"——官方插件出来后已废弃。

### 1.3 关键性能数据（官方评测）

| 实验组 | 任务完成率 | 输入 Token 总量 | 对比原始 |
|--------|-----------|----------------|---------|
| OpenClaw (memory-core) | 35.65% | 24,611,530 | 基准 |
| OpenClaw + LanceDB | 44.55% | 51,574,530 | +25% / +110% cost |
| OpenClaw + OpenViking (native memory ON) | **51.23%** | **2,099,622** | **+43% / -91% cost** |
| OpenClaw + OpenViking (native memory OFF) | **52.08%** | **4,264,396** | **+49% / -83% cost** |

> 结论：OpenViking 让任务完成率提升 43-49%，同时 token 消耗降低 83-91%。

---

## 二、核心概念

### 2.1 文件系统范式（Filesystem Paradigm）

所有上下文统一组织为虚拟文件系统，通过 `viking://` 协议 URI 访问：

```
viking://
├── resources/     # 资源：项目文档、代码、网页等
│   └── my_project/
│       ├── docs/
│       └── src/
├── user/          # 用户：个人偏好、习惯
│   └── memories/
└── agent/         # Agent：技能、指令、任务记忆
    ├── skills/
    └── instructions/
```

每个 URI 都可执行标准文件操作：`ls`、`find`、`grep`、`tree`、`read`。

### 2.2 L0 / L1 / L2 三层上下文机制

OpenViking 写入数据时自动生成三层摘要：

| 层级 | 名称 | 大小 | 用途 |
|------|------|------|------|
| **L0** | Abstract（抽象） | ~100 tokens | 快速相关性检查，快速排除无关内容 |
| **L1** | Overview（概览） | ~2k tokens | 理解整体结构和关键点，决策参考 |
| **L2** | Details（详情） | 完整原文 | 按需加载，绝对必要时深度阅读 |

目录结构示例：

```
viking://resources/my_project/
├── .abstract          # L0 抽象层
├── .overview          # L1 概览层
├── docs/
│   ├── .abstract      # 每个目录也有 L0/L1
│   ├── .overview
│   ├── api/
│   │   ├── auth.md    # L2 完整内容
│   │   └── endpoints.md
│   └── tutorials/
└── src/
```

**加载策略**：优先 L0 粗筛 → L1 理解结构 → L2 按需深入，大幅节省 token。

### 2.3 目录递归检索（Directory Recursive Retrieval）

区别于传统 flat vector RAG：

1. **意图分析**：生成多个检索条件
2. **初始定位**：向量检索快速定位高分目录
3. **精细探索**：在目录内二次检索，更新候选集
4. **递归下钻**：子目录存在则重复
5. **结果聚合**：返回最相关的上下文

---

## 三、OpenClaw Plugin 2.0 架构

### 3.1 集成方式：Context Engine Plugin

OpenViking 作为 OpenClaw 的 **context engine** 插件运行（非 legacy memory 插件）。

> **Plugin 2.0** = 基于 OpenClaw context-engine 能力的新架构  
> **Legacy 插件** = 旧版独立 memory backend（已知 2026.3.12 会话挂起 bug）

当前 OpenClaw 版本：**2026.3.23-2** ✅（满足 Plugin 2.0 要求：≥ 2026.3.12）

### 3.2 两种运行模式

| 模式 | 说明 | 适用场景 |
|------|------|---------|
| **Local** | 插件自动启动本地 OpenViking 子进程 | 个人使用，简单零配置 |
| **Remote** | 连接远程 OpenViking HTTP 服务 | 团队共享，多 Agent 共用 |

---

## 四、当前环境诊断

```
OpenClaw:     2026.3.23-2  ✅（满足 Plugin 2.0 要求）
Node.js:      v24.14.0     ✅（满足 ≥22 要求）
Python:       3.14.3 / 3.11.9  ⚠️（3.14 未明确测试，建议用 3.11）
OpenViking:   未安装        ❌
openviking:   未安装        ❌
当前 Memory:   memory-core (qmd)  → 将迁移到 OpenViking
Gateway:      运行中 @ 18789 ✅
```

---

## 五、安装与配置（Local 模式，推荐）

### 5.1 前置条件

```bash
# 确认 Python >= 3.10
python3 --version  # 3.11.9 可用

# 确认 Node >= 22
node -v  # v24.14.0 可用

# 确认 OpenClaw 已安装
openclaw --version  # 2026.3.23-2 ✅
```

### 5.2 安装 OpenViking Python 包

```bash
# 使用 Python 3.11（更稳定）
python3.11 -m pip install openviking --upgrade

# 验证
python3.11 -c "import openviking; print('ok')"
```

> ⚠️ 如果遇到 `externally-managed-environment` 错误（PEP 668），需要创建 venv：
> ```bash
> python3.11 -m venv ~/.openviking/venv
> ~/.openviking/venv/bin/pip install openviking
> ```

### 5.3 一键安装 OpenClaw 插件（推荐）

```bash
npm install -g openclaw-openviking-setup-helper
ov-install
```

或 curl（Linux/macOS）：

```bash
curl -fsSL https://raw.githubusercontent.com/volcengine/OpenViking/main/examples/openclaw-plugin/install.sh | bash
```

安装助手会依次询问：
- 环境检查（Python、Node、cmake 等）
- 选择 OpenClaw 实例（单机用户直接回车）
- **选择部署模式**：输入 `local`
- 输入 **Volcengine Ark API Key**

### 5.4 API Key 获取

**选项 A：火山引擎 Ark（官方推荐，OpenViking 原生支持）**

1. 访问 https://console.volcengine.com/ark/region:ark+cn-beijing/overview
2. 创建 API Key
3. 用于 embedding 和 VLM 模型

**选项 B：NVIDIA NIM（免费，无需申请）**

> 来自第三方 skill（swizardlv/openclaw_openviking_skill）的方案，免费额度充足

1. 访问 https://build.nvidia.com/
2. 登录 → API Keys → Generate Key（以 `nvapi-` 开头）
3. Embedding 模型：`nvidia/nv-embed-v1`（4096 维）
4. VLM 模型：`meta/llama-3.3-70b-instruct`

```json
// ~/.openviking/ov.conf（NVIDIA NIM 配置示例）
{
  "embedding": {
    "dense": {
      "api_base": "https://integrate.api.nvidia.com/v1",
      "api_key": "YOUR_NVIDIA_API_KEY",
      "provider": "openai",
      "dimension": 4096,
      "model": "nvidia/nv-embed-v1"
    }
  },
  "vlm": {
    "api_base": "https://integrate.api.nvidia.com/v1",
    "api_key": "YOUR_NVIDIA_API_KEY",
    "provider": "openai",
    "model": "meta/llama-3.3-70b-instruct"
  }
}
```

### 5.5 安装后配置

安装助手自动生成两个文件：

| 文件 | 内容 |
|------|------|
| `~/.openviking/ov.conf` | OpenViking 服务配置 |
| `~/.openclaw/openviking.env` | 环境变量（Python 路径等） |

**每次启动前必须加载环境变量（Local 模式）：**

```powershell
# PowerShell
source ~/.openclaw/openviking.env
# 或
. "$HOME/.openclaw/openviking.env"

# 然后重启 Gateway
openclaw gateway restart
```

### 5.6 验证安装

```bash
openclaw status
```

应看到：

```
ContextEngine:  enabled (plugin openviking)
Memory:         N files · N chunks · ready
```

---

## 六、与 OpenClaw 的深度集成配置

### 6.1 OpenViking 插件配置项

```yaml
# 完整配置（通过 openclaw config set 设置）
plugins:
  slots:
    contextEngine: openviking   # 启用为 context engine
  entries:
    openviking:
      config:
        mode: local                    # local 或 remote
        configPath: ~/.openviking/ov.conf  # 配置文件路径
        port: 1933                     # Local 模式端口
        targetUri: viking://user/memories  # 默认记忆搜索范围
        autoCapture: true              # 自动提取对话记忆
        captureMode: semantic          # semantic 或 keyword
        captureMaxLength: 24000        # 单次捕获最大字符数
        autoRecall: true               # 自动召回相关记忆
        recallLimit: 6                # 最大召回条数
        recallScoreThreshold: 0.01    # 最小相关分数
        ingestReplyAssist: true        # 多方对话文本检测
```

### 6.2 关键配置说明

| 配置项 | 默认值 | 说明 |
|--------|--------|------|
| `autoCapture` | `true` | 对话结束后自动提取记忆到 OpenViking |
| `captureMode` | `semantic` | semantic（全语义）/ keyword（触发词） |
| `autoRecall` | `true` | 响应前自动召回相关记忆 |
| `recallLimit` | `6` | 每次召回的最大记忆条数 |
| `recallScoreThreshold` | `0.01` | 召回相关性阈值 |

### 6.3 三司会审架构下的协同

```
OpenClaw Gateway（狄仁杰主持）
    │
    ├── 李元芳（DeepSeek，长程记忆研究）
    │   └── OpenViking：海量文档、代码库检索
    │       viking://resources/   ← 长期知识库
    │       viking://agent/memories/  ← Agent 任务记忆
    │
    └── 宋慈（GLM-4，快速执行）
        └── memory-core (qmd)：日常轻量记忆
            viking://user/memories/  ← 用户偏好、个人信息
```

---

## 七、使用方式

### 7.1 自动化（安装后自动生效）

- **autoCapture**：对话结束后自动写入 OpenViking
- **autoRecall**：每次响应前自动召回相关记忆

无需手动操作，完全透明。

### 7.2 手动操作（CLI）

```bash
# 检查状态
openclaw status

# 搜索记忆
openclaw memory search "关于项目的部署配置"

# 列出记忆
openclaw memory ls

# 查看目录树
openclaw memory fs-tree viking://resources

# 导入资源文件
openclaw memory ingest-resource ./docs/runbook.md --wait

# 导出/导入包
openclaw memory pack-export viking://resources/docs /tmp/docs.ovpack
openclaw memory pack-import /tmp/docs.ovpack viking://resources --force

# 查看检索轨迹（调试用）
openclaw memory search-trace
```

### 7.3 Python API（高级用法）

```python
import openviking as ov

client = ov.SyncOpenViking(path="./openviking_data")
client.initialize()

# 添加文件
client.add_resource(path="./doc.md")
client.wait_processed()

# 语义搜索
results = client.find("query", limit=5)
for r in results.resources:
    print(f"{r.uri} (score: {r.score:.4f})")

# 读取内容
content = client.read("viking://resources/doc/section.md")

# L0/L1/L2 分层读取
abstract = client.get_layer("viking://resources/doc", layer="l0")
overview = client.get_layer("viking://resources/doc", layer="l1")
full = client.get_layer("viking://resources/doc", layer="l2")

client.close()
```

---

## 八、Web Console（可视化调试）

启动可视化控制台：

```bash
python -m openviking.console.bootstrap \
  --host 127.0.0.1 \
  --port 8020 \
  --openviking-url http://127.0.0.1:1933 \
  --write-enabled
```

然后访问 **http://127.0.0.1:8020** 查看：
- 记忆检索轨迹（Directory Recursive Retrieval 可视化）
- L0/L1/L2 分层内容预览
- 所有 viking:// 资源目录树

---

## 九、已知限制与注意事项

### 9.1 当前环境特殊情况

- **Windows 环境**：`openclaw gateway restart` 需要在 PowerShell 中执行
- **Python 3.14**：建议使用 3.11 避免兼容性问题
- **环境变量持久化**：Local 模式下每次启动需 source `~/.openclaw/openviking.env`

### 9.2 OpenViking 使用限制

1. **文件名冲突**：OpenViking 使用文件名（而非完整路径）作为 URI，不同目录下的同名文件会冲突
2. **不支持目录导入**：`add_resource(path="./dir/")` 无效，需逐文件添加
3. **VLM 失败非致命**：摘要生成失败不影响搜索功能
4. **避免推理模型**：如 deepseek-r1、kimi-k2.5 等（返回内容在 reasoning 字段，OpenViking 无法解析）

### 9.3 OpenClaw 版本兼容性

| OpenClaw 版本 | 兼容插件 | 说明 |
|--------------|---------|------|
| < 2026.3.12 | Legacy only | 存在会话挂起 bug |
| ≥ 2026.3.12 | Plugin 2.0 | 当前版本完美支持 |
| 当前版本 | **2026.3.23-2** ✅ | Plugin 2.0 完全兼容 |

---

## 十、推荐部署步骤（太上皇环境）

### Step 1：环境准备（本机已有）
```bash
✅ Python 3.11.9
✅ Node v24.14.0
✅ OpenClaw 2026.3.23-2
✅ Together API（用于 DeepSeek Qwen）
```

### Step 2：安装 OpenViking
```bash
# 创建专用 venv（避免 PEP 668 问题）
python3.11 -m venv ~/.openviking/venv
~/.openviking/venv/bin/pip install openviking

# 验证
~/.openviking/venv/bin/python -c "import openviking; print('ok')"
```

### Step 3：配置 ov.conf（使用 Together API 或 NVIDIA NIM）

> 建议使用 NVIDIA NIM（免费，无需申请火山引擎）：
> - Embedding：`nvidia/nv-embed-v1`（4096 维，免费额度充足）
> - VLM：`meta/llama-3.3-70b-instruct`

### Step 4：安装插件
```bash
npm install -g openclaw-openviking-setup-helper
ov-install --workdir ~/.openclaw
# 选择 local 模式
# 输入 API Key
```

### Step 5：启动
```powershell
# 启动前加载环境
. "$env:USERPROFILE\.openclaw\openviking.env"
openclaw gateway restart
```

### Step 6：验证
```bash
openclaw status
# 应显示 ContextEngine: enabled (plugin openviking)
```

---

## 十一、效果预期

| 维度 | 当前（memory-core） | 集成后（OpenViking） |
|------|-------------------|---------------------|
| 任务完成率 | ~35% | ~51% (+43%) |
| Token 消耗 | 24.6M | 2.1M (-91%) |
| 长期记忆检索 | 差 | 目录递归 + L0/L1/L2 分层 |
| 上下文可视化 | 无 | Web Console 完全透明 |
| 多 Agent 共享 | 不支持 | Remote 模式支持 |

---

## 十二、附录

### A. 相关链接

| 资源 | 链接 |
|------|------|
| OpenViking 官方仓库 | https://github.com/volcengine/OpenViking |
| OpenClaw Plugin 官方文档 | https://github.com/volcengine/OpenViking/blob/main/examples/openclaw-plugin/README.md |
| NVIDIA NIM 免费 Embedding | https://build.nvidia.com/ |
| OpenClaw Eval 脚本 | https://github.com/ZaynJarvis/openclaw-eval |
| 第三方 Skill（NVIDIA NIM） | https://github.com/swizardlv/openclaw_openviking_skill |

### B. 文件清单

安装后生成/修改的文件：

```
~/.openviking/
├── ov.conf              # OpenViking 服务配置（新增）
├── data/                # OpenViking 数据存储（新增）
│   ├── vectordb/
│   ├── agfs/
│   └── log/
└── venv/                # Python 虚拟环境（可选，新增）

~/.openclaw/
├── openviking.env       # 环境变量（新增，每次启动 source）
└── [现有配置文件...]    # 不修改现有配置

知识库索引：
viking://user/memories/     ← 个人记忆、偏好
viking://resources/         ← 文档、代码
viking://agent/memories/    ← Agent 任务记忆
```

---

*李元芳·研究报告·INTJ建筑师型·2026-03-29*
