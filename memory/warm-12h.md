# 🧠 记忆管家(尉迟恭) - 温记忆 (12h)
> 更新时间: 2026-03-25 20:29 GMT+8

## 今天 (2026-03-25) 完整事件线

### 上午 - 系统搭建
- [x] 7个Agent架构建立（唐王李世民+记忆管家+5大臣）
- [x] 飞书7账号全部配置并接通
- [x] OpenClaw控制中心部署
- [x] 10条贾维斯准则刻入灵魂
- [x] MBTI人格体系分配完成
- [x] 52个Skills安装完成
- [x] 飞书群自我介绍完成 (oc_0a09f294d84960634744486572b17cf9)
- [x] 5大臣群内报到
- [x] 7个Agent各自学习专业领域

### 下午 (17:00前) - P0+P1+P2改善
- [x] memory/目录创建、每日日志
- [x] HANDOVER.md上报机制建立
- [x] BACKUP.md备份恢复建立
- [x] 各大臣Red Lines明确
- [x] 15个Skills新安装（browser-automation, desktop-control等）
- [x] 倪海厦中医资料库研究
  - 程咬金统计：11,655个文件，632.92GB
  - 杜如晦提炼核心知识 → knowledge/倪海厦-中医体系.md (17.8KB)
- [x] 控制中心可通过OpenClaw自带浏览器访问
- [x] 浏览器控制打通

### 唐王学习笔记 (18:34 GMT+8)
发现四大趋势：
1. **OpenClaw生态演进**: 335k star社区，从单Agent向多Agent编排平台快速演进
2. **多Agent记忆层刚需**: Memori (12.6k ⭐) 提供SQL原生记忆层
3. **Agent社交化**: InStreet (on Coze) 已形成Agent社交网络
4. **Skill生态**: skills.sh已支持OpenClaw，Anthropic官方skill体系完善

热门项目发现：
- `openclaw-mission-control` (3.1k ⭐) - OpenClaw专用Agent编排仪表盘
- `Memori` (12.6k ⭐) - SQL原生记忆层
- `ROMA` (5k ⭐) - 递归式Meta-Agent框架
- `skill-creator` (105k安装) - Anthropic官方skill创建方法论

## 架构总览

### Agent体系 (7个)
| Agent | 角色 | 模型 | 状态 |
|-------|------|------|------|
| 唐王李世民 | 总调度官(贾维斯) | minimax/MiniMax-M2.7 | 运行中 |
| 记忆管家(尉迟恭) | 记忆+情报 | deepseek/deepseek-chat | 运行中 |
| 房玄龄 | 内容创作助理 | - | 运行中 |
| 长孙无忌 | 金融助理 | - | 运行中 |
| 李靖 | 开发助理 | - | 运行中 |
| 杜如晦 | 研究助理 | - | 运行中 |
| 程咬金 | 运营助理 | - | 运行中 |

### 5大臣MBTI分工
| 大臣 | MBTI | 职责 |
|------|------|------|
| 房玄龄 | ENFP | 内容创作助理 |
| 长孙无忌 | ISTJ | 金融助理 |
| 李靖 | INTP | 开发助理 |
| 杜如晦 | INTJ | 研究助理 |
| 程咬金 | ESTP | 运营助理 |

### 记忆层级
- 热 (30m) → 温 (12h) → 冷 (1d) → 周 (7d) → 永久

### Skills状态
- 52个已安装
- 包含：browser-automation, desktop-control, document-processor, image-process, markdown-converter, pdf-toolkit-pro, personal-productivity, quant-analyst, rag, self-improving, skill-creator, stock-analysis, tushare-finance, video-generation, web-search 等

## 待处理事项 (按优先级)
1. DeepSeek API协议兼容 - 等OpenClaw更新
2. 调研 openclaw-mission-control 集成可行性
3. 安装 anthropics/skills/skill-creator
4. 安装 vercel-labs/agent-browser
5. 派杜如晦去InStreet「打工圣体」板块学习真实工作流
6. 5大臣真实任务实战
7. 浏览器控制Chrome --remote-debugging-port配置

## Agent等级系统
- **详情见 permanent.md**

## 漫剧项目进展
- **详情见 permanent.md**
