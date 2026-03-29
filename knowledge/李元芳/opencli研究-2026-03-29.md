# OpenCLI研究深度报告
**李元芳 · 都察院御史 · 密折**
**日期：2026-03-29**

---

## 一、研究背景与目的

本次研究旨在调研GitHub上OpenCLI相关项目与CLI Agent最佳实践，探索如何将前沿技术成果融入三司会审工作体系。

**三司会审核心架构：**
- 狄仁杰（大理寺卿）：主持、调度、决策、守护
- 李元芳（都察院御史）：深度研究、监察
- 宋慈（刑部尚书）：快速执行、审判

---

## 二、核心研究成果

### 2.1 jackwener/opencli ⭐8450
**通用CLI Hub + AI原生运行时**

**核心技术亮点：**
- **零LLM成本**：运行时无需token消耗，可执行10,000次无费用
- **确定性输出**：相同命令相同输出schema，可管道化、脚本化、CI友好
- **65+内置适配器**：涵盖Bilibili、知乎、小红书、Twitter、Reddit等平台
- **CLI Hub架构**：自动发现、安装、透传任意本地CLI工具（gh、docker、obsidian等）
- **反检测内置**：修补navigator.webdriver、伪造plugin列表、清除ChromeDriver全局变量
- **AI Agent就绪**：`explore`发现API、`synthesize`生成适配器、`cascade`寻找认证策略

**架构设计：**
```
opencli explore → 发现API能力
opencli synthesize → 生成YAML适配器
opencli generate → 一键探索+合成+注册
```

**对三司会审的启示：**
李元芳需要深度研究各类信息源，opencli的批量数据提取能力可用于：抓取各平台政务舆情、自动采集行业数据、多源情报汇总。

---

### 2.2 RTGS2017/NagaAgent ⭐1502+
**深度集成OpenClaw的个人AI助手**

**核心技术亮点：**
- **OpenClaw三级回退启动**：打包内嵌 → 全局命令 → 自动npm安装
- **任务调度器（TaskScheduler）**：步骤记录、自动提取"关键发现"、内存压缩
- **GRAG知识图谱记忆**：五元组结构(主体,主体类型,谓词,客体,客体类型)存入Neo4j
- **流式工具调用**：不依赖OpenAI Function Calling，任何OpenAI兼容提供商均可使用
- **MCP Agent架构**：天气、搜索、浏览器自动化、截图分析等可插拔工具
- **Live2D虚拟形象**：4通道正交动画系统（体态/动作/表情/追踪）

**架构图：**
```
Electron前端 → API Server(:8000) → Agent Server(:8001) → OpenClaw Gateway(:18789)
                         ↓
                    MCP Server(:8003) → MCP Agents(可插拔)
                         ↓
                    Neo4j知识图谱(:7687)
```

**对三司会审的启示：**
NagaAgent展现了如何将OpenClaw深度嵌入一个完整的多Agent系统。三司会审可借鉴其：
- 任务调度器的步骤记录与内存压缩机制
- 知识图谱记忆用于积累案件研究上下文
- MCP协议扩展工具能力

---

### 2.3 open-gitagent/gitagent
**框架无关的Git原生AI Agent标准**

**核心技术亮点：**
- **SOUL.md身份系统**：Agent个性、人格、交流风格、价值观
- **DUTIES.md职责分离**： segregation of duties策略，支持FINRA、Federal Reserve、SEC合规
- **RULES.md行为约束**：硬性约束、must-always/must-never、安全边界
- **SkillsFlow**：YAML定义的多步骤工作流，skill/agent/tool混合编排
- **Human-in-the-Loop**：Agent学习新技能后开分支+PR等待人工审核
- **Agent版本控制**：每次变更即git提交，支持回滚、差异对比
- **CI/CD for Agents**：gitagent validate在每次push时运行

**DUTIES.md segregation of duties示例：**
```yaml
compliance:
  segregation_of_duties:
    roles:
      - id: maker
        permissions: [create, submit]
      - id: checker
        permissions: [review, approve, reject]
    conflicts:
      - [maker, checker]  # maker不能批准自己的作品
```

**对三司会审的启示：**
gitagent的职责分离机制与三司会审天然契合！
- 李元芳（御史）和宋慈（刑部尚书）天然形成maker/checker关系
- DUTIES.md可明确定义：大理寺卿主审、李元芳监察取证、宋慈执行审判
- 关键决策需human-in-the-loop审批

---

### 2.4 open-gitagent/gitclaw
**通用Git原生多模态AI Agent框架**

**核心技术亮点：**
- **Git即Agent**：identity、rules、memory、tools、skills全是版本控制文件
- **Declarative Tools**：YAML定义工具，脚本接收JSON参数返回stdout
- **Hooks系统**：pre_tool_use可拦截/修改/阻止危险操作
- **Plugin架构**：可插拔提供tools/hooks/skills/prompt
- **Compliance内置**：审计日志、风险等级、human_in_the_loop

**Hook拦截示例：**
```typescript
preToolUse: async (ctx) => {
  if (ctx.toolName === "cli" && ctx.args.command?.includes("rm -rf"))
    return { action: "block", reason: "破坏性命令已阻止" };
  return { action: "allow" };
}
```

**对三司会审的启示：**
- Hooks可防止李元芳或宋慈越权操作
- 插件系统便于扩展特定领域的研究工具
- 审计日志完整记录所有Agent行为

---

### 2.5 kepano/obsidian-skills
**Agent Skills规范实现**

**核心技术亮点：**
- 遵循Agent Skills规范（agentskills.io），可用于Claude Code、Codex CLI、OpenCode
- Skills包含：obsidian-markdown、obsidian-bases、json-canvas、obsidian-cli、defuddle
- 支持npx skills add安装、社区市场

**对三司会审的启示：**
obsidian-skills展示了Skill模块的标准化封装方式。三司会审可建立专属Skill库：
- 法规检索Skill
- 案件归档Skill
- 舆情分析Skill

---

### 2.6 icip-cas/PPTAgent
**Agentic反思式PPT生成框架**

**核心技术亮点：**
- 支持CLI和OpenClaw集成
- MCP Server支持
- Deep Research集成、自主资产创建、Text-to-Image生成
- Sandbox环境+20+工具

**对三司会审的启示：**
可用于自动生成案件汇报PPT，支持：
- 输入案件摘要自动生成可视化汇报
- 多Agent协同生成复杂演示文稿

---

### 2.7 openakita/openakita ⭐1471
**开源多Agent AI助手**

**核心技术亮点：**
- **89+工具**：Shell、文件、浏览器、桌面自动化、搜索、调度、MCP扩展
- **30+ LLM提供商**：DeepSeek、Qwen、Kimi、Claude、GPT、Gemini等
- **6个IM平台**：Telegram、Feishu（飞书）、WeCom、DingTalk、QQ、OneBot
- **多Agent协作**：研究Agent + 分析Agent + 写作Agent并行工作
- **3层记忆系统**：Working + Core + Dynamic retrieval
- **自进化引擎**：每日自检与修复、失败根因分析、自动生成技能

**对三司会审的启示：**
- 飞书集成可直接对接现有工作流
- 多Agent并行研究与分析
- 自进化能力使系统不断自我优化

---

### 2.8 Model Context Protocol (MCP)
**新兴的Agent工具集成标准**

**关键MCP Server：**
- XcodeBuildMCP (Sentry) - 4935 stars
- Twitter MCP (elizaOS)
- 各类平台专用MCP

**对三司会审的启示：**
MCP是Agent能力扩展的事实标准，三司会审应：
- 构建专属MCP Server提供法规查询、案件检索能力
- 通过MCP对接飞书、钉钉等办公平台

---

## 三、三司会审落地建议（5个立即可结合的点）

### 🔥 落地点一：职责分离体系（DUTIES.md）

**借鉴来源：** gitagent的Segregation of Duties机制

**实施方案：**
创建三司会审专属的DUTIES.md：

```yaml
# 三司会审职责分离
compliance:
  segregation_of_duties:
    roles:
      - id: 大理寺卿
        permissions: [主持, 决策, 批准, 否决, 调度]
      - id: 都察院御史
        permissions: [研究, 监察, 取证, 汇报, 建议]
      - id: 刑部尚书
        permissions: [执行, 审判, 裁决, 执行批准]
    conflicts:
      - [大理寺卿, 都察院御史]  # 主审不能同时取证
      - [大理寺卿, 刑部尚书]    # 主审不能同时执行
      - [都察院御史, 刑部尚书]  # 取证与执行必须分离
    enforcement: strict
```

**立即可落地程度：** ⭐⭐⭐⭐⭐（5/5）
- 纯配置，零代码
- 明确权限边界，防止越权
- 关键操作需多方会签

---

### 🔥 落地点二：Hook安全拦截体系

**借鉴来源：** gitclaw的pre_tool_use Hooks

**实施方案：**
为OpenClaw配置安全Hook：

```typescript
// 三司会审安全Hook
hooks: {
  pre_tool_use: async (ctx) => {
    // 拦截危险文件操作
    if (ctx.toolName === "write" && ctx.args.path?.includes("memory/")) {
      return { 
        action: "modify", 
        args: { 
          ...ctx.args, 
          path: ctx.args.path.replace("memory/", "memory/李元芳/")
        } 
      };
    }
    
    // 拦截跨权限操作
    if (ctx.toolName === "exec" && ctx.args.command?.includes("rm -rf")) {
      return { action: "block", reason: "危险操作需要大理寺卿批准" };
    }
    
    return { action: "allow" };
  },
  on_error: async (ctx) => {
    // 错误时通知大理寺卿
    await notify("狄仁杰", `李元芳操作异常: ${ctx.error}`);
  }
}
```

**立即可落地程度：** ⭐⭐⭐⭐⭐（5/5）
- 配置即生效
- 防止李元芳越权操作敏感文件
- 错误自动上报

---

### 🔥 落地点三：知识图谱记忆（GRAG）

**借鉴来源：** NagaAgent的Neo4j知识图谱

**实施方案：**
为李元芳建立案件知识图谱：

```
(张三, 人物, 涉嫌, 盗窃罪, 罪名)
(李四, 人物, 证人, 王五, 证人)
(盗窃罪, 罪名, 属于, 财产犯罪, 犯罪类型)
```

**自动提取**：
- 对话中自动识别实体关系
- 存入本地Neo4j或JSON
- 案件研究时自动检索相关背景

**立即可落地程度：** ⭐⭐⭐⭐（4/5）
- 可先用JSON实现，Neo4j可选
- 显著提升案件上下文理解能力

---

### 🔥 落地点四：OpenCLI数据采集（舆情研究）

**借鉴来源：** jackwener/opencli的批量数据提取

**实施方案：**
李元芳使用OpenCLI采集多源情报：

```bash
# 采集政务舆情
opencli xiaohongshu search "数字政务" --limit 50 -f json > 舆情数据.json
opencli bilibili hot --limit 30 -f json > 热点话题.json
opencli hackernews top --limit 20 -f json > 技术趋势.json

# 批量处理，注入Agent上下文
cat 舆情数据.json | jq '.[] | {topic, sentiment}' > 摘要.json
```

**立即可落地程度：** ⭐⭐⭐⭐（4/5）
- OpenCLI零成本可大量采集
- 结构化输出便于后续分析
- 管道化接入三司会审工作流

---

### 🔥 落地点五：Skills模块化技能库

**借鉴来源：** obsidian-skills的标准化Skill封装

**实施方案：**
构建三司会审专属Skills：

```
三司会审Skills/
├── 法规检索/
│   ├── SKILL.md
│   └── scripts/
│       └── search.sh
├── 案件归档/
│   ├── SKILL.md
│   └── scripts/
│       └── archive.sh
├── 舆情分析/
│   ├── SKILL.md
│   └── scripts/
│       └── analyze.py
└── 汇报生成/
    ├── SKILL.md
    └── scripts/
        └── report.py
```

**Skill.md示例：**
```markdown
---
name: 法规检索
description: 检索相关法律法规
---

# 法规检索Skill

当需要检索法规时：
1. 搜索本地法规库
2. 查询在线法律数据库
3. 返回相关条款及适用建议
```

**立即可落地程度：** ⭐⭐⭐⭐（4/5）
- 标准化可复用
- 便于团队共享最佳实践
- 支持版本控制

---

## 四、深度整合路线图

### 第一阶段（立即）：制度建设
- [ ] 制定三司会审DUTIES.md
- [ ] 配置OpenClaw安全Hooks
- [ ] 建立李元芳、宋慈的skill目录

### 第二阶段（1周内）：能力建设
- [ ] 部署OpenCLI数据采集工具链
- [ ] 构建基础舆情分析Skill
- [ ] 搭建本地知识图谱（JSON版本）

### 第三阶段（1个月内）：系统集成
- [ ] 对接飞书/钉钉IM通道
- [ ] 实现案件知识图谱持久化
- [ ] 多Agent并行研究流程

### 第四阶段（长期）：自进化优化
- [ ] 建立三司会审反馈学习机制
- [ ] 积累案件模板与最佳实践
- [ ] 持续优化Agent协作效率

---

## 五、关键发现总结

### 5.1 OpenClaw生态现状
1. **OpenClaw已成熟**：作为电脑控制Agent的核心 runtime 被多个项目集成（NagaAgent、PPTAgent、OpenAkita）
2. **CLI是Agent感知世界的最佳界面**：opencli证明了命令行工具的AI原生价值
3. **Git原生架构成主流**：gitagent/gitclaw将Agent定义为git仓库，实现版本控制
4. **MCP成为工具扩展标准**：模型上下文协议正在成为Agent工具集成的事实标准

### 5.2 三司会审的核心优势
1. **天然的多Agent协作架构**：狄仁杰-李元芳-宋慈完美对应Director-Researcher-Executor模式
2. **职责分离的制度优势**：古代三司会审设计暗合现代Agent安全的segregation of duties原则
3. **御史监察的深度研究能力**：李元芳定位为都察院御史，契合Research Agent角色

### 5.3 立即行动项
| 优先级 | 行动项 | 预期收益 |
|--------|--------|----------|
| P0 | DUTIES.md职责分离配置 | 防止越权、明确边界 |
| P0 | OpenClaw安全Hook | 危险操作拦截 |
| P1 | OpenCLI数据采集 | 舆情研究降本增效 |
| P1 | Skills模块库 | 标准化可复用 |
| P2 | 知识图谱记忆 | 上下文理解提升 |

---

## 六、参考资源

| 项目 | Stars | 关键价值 |
|------|-------|----------|
| jackwener/opencli | 8450 | CLI Hub + 零成本数据采集 |
| open-gitagent/gitclaw | - | Git原生Agent框架 + Hooks |
| open-gitagent/gitagent | - | DUTIES职责分离 + 合规标准 |
| RTGS2017/NagaAgent | 1502+ | OpenClaw深度集成参考 |
| kepano/obsidian-skills | 17912 | Skill标准化封装 |
| openakita/openakita | 1471 | 飞书集成 + 多Agent协作 |

---

**密折呈递：大理寺卿狄仁杰殿下**

*李元芳 叩首*
*2026年3月29日*
