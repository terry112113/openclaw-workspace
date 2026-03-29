# Multi-Agent Orchestration 研究 - 2026-03-30

## 项目：oh-my-claudecode
- GitHub: Yeachan-Heo/oh-my-claudecode (15k+ stars)
- 定位：Teams-first Multi-agent orchestration for Claude Code

## 核心架构

### 1. Team-first编排
- Multi-agent team是标准方式
- 阶段性管道：team-plan → team-prd → team-exec → team-verify → team-fix
- 每个阶段由专门的agent负责

### 2. 32个专业agent
不是3个，是32个！
- 架构agent、Research agent、设计agent、测试agent、数据科学agent...
- 每个agent专注于自己的领域
- 自动委托给正确的agent

### 3. 智能路由
- 简单任务 → Haiku（快，省钱）
- 复杂任务 → Opus（强，准）
- 自动判断任务复杂度

### 4. 真实并行
- tmux workers
- 任务完成就销毁，不浪费资源
- 按需生成，不idle

### 5. 执行模式
| 模式 | 用途 |
|------|------|
| Team（推荐） | 协调多agent共享任务 |
| omc team | tmux CLI真实并行 |
| ccg | 三模型混合（Codex+Gemini+Claude） |
| Autopilot | 单agent自主执行 |
| Ultrawork | 最大并行度 |

## 对臣的启发

### 三位一体可以扩展
现在只有狄仁杰+李元芳+魏征，可以考虑：
- 狄仁杰（主持/决策）
- 李元芳（深度研究/监察）
- 魏征（快速执行/审计）
- 可以再加：程咬金（行业运营）、房玄龄（知识管理）...

### 阶段性管道的思路
臣的cron任务可以参考这个管道：
- 计划阶段（早间扫描）
- 执行阶段（午间研究）
- 验证阶段（晚间输出）
- 修复循环（如果有错）

### 智能路由
臣可以用不同复杂度的任务分配给不同的agent：
- 简单任务 → 快速模型
- 复杂任务 → 深度模型
- 目前臣统一用MiniMax M2.7，可能不是最优

## 待思考
臣是否需要扩展到更多专业agent？还是保持3个但让每个更强？
