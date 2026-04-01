# deer-flow 沙箱集成具体实施步骤

**制定人：** 李元芳（INTJ建筑师型）
**日期：** 2026-03-29
**基于：** deer-flow移植方案-2026-03-29.md
**优先级：** Phase 1（沙箱隔离）+ Phase 3（Skills+MCP）

---

## 一、总体策略

### 1.1 集成原则
- **不引入Python后端** — 全部用TypeScript重写，保持OpenClaw纯Node.js体系
- **沙箱优先** — Phase 1先落地，解决exec安全痛点
- **Skills+MCP紧随其后** — Phase 3升级OpenClaw扩展生态
- **严格分阶段** — 每阶段可独立验证，不影响主线功能

### 1.2 目标目录结构

```
C:\Users\TL\.openclaw\workspace-main\
├── sandbox/                          # [NEW] 沙箱隔离层
│   ├── index.ts                      # 导出主入口
│   ├── base.ts                       # SandboxProvider抽象类
│   ├── providers/
│   │   ├── local.ts                  # 本地执行provider
│   │   └── docker.ts                 # Docker provider（Phase 2+）
│   ├── tools/
│   │   ├── bash.ts                   # bash命令执行
│   │   ├── ls.ts                     # 目录列表
│   │   ├── read_file.ts              # 文件读取
│   │   ├── write_file.ts             # 文件写入
│   │   └── str_replace.ts            # 字符串替换
│   └── path-translator.ts            # 虚拟路径 ↔ 物理路径翻译
├── skills/                           # [升级] Skills系统
│   ├── loader.ts                     # 递归扫描 + YAML frontmatter解析
│   ├── registry.ts                   # Skills注册表
│   ├── public/                       # 内置skills
│   └── custom/                       # 用户自定义skills
├── mcp/                              # [NEW] MCP客户端
│   ├── client.ts                     # MCP协议客户端
│   ├── transports/
│   │   ├── stdio.ts                  # stdio传输（npx调用）
│   │   ├── sse.ts                    # SSE传输
│   │   └── http.ts                  # HTTP传输
│   ├── auth/
│   │   └── oauth.ts                  # OAuth token刷新
│   └── cache.ts                      # mtime缓存失效
└── types/
    └── sandbox.ts                    # 共享类型定义
```

---

## 二、Phase 1：沙箱隔离（重点突破）

### 2.1 核心目标
把OpenClaw的 `exec` 工具从**直接系统命令执行**升级为**受控沙箱执行**，实现：
- 路径隔离（Agent只能访问 `/mnt/user-data/*` 虚拟路径）
- 超时控制（防止恶意永久阻塞）
- 命令白名单（可选）
- 审计日志（每个执行的命令记录）

### 2.2 实施步骤

#### Step 1：创建基础类型和接口

**文件：** `sandbox/base.ts`

```typescript
// 虚拟路径配置
export interface VirtualPathConfig {
  userData: string;      // /mnt/user-data
  skills: string;         // /mnt/skills
  workspaceRoot: string;  // 物理路径根目录
}

// SandboxProvider抽象类
export abstract class SandboxProvider {
  abstract executeCommand(
    cmd: string,
    cwd: string,
    timeoutMs: number
  ): Promise<{ stdout: string; stderr: string; exitCode: number }>;

  abstract readFile(path: string, encoding?: BufferEncoding): Promise<string>;
  abstract writeFile(path: string, content: string): Promise<void>;
  abstract listDir(path: string): Promise<string[]>;

  // 路径翻译：虚拟路径 → 物理路径
  abstract resolvePath(virtualPath: string, threadId: string): string;
}
```

**验证标准：**
- `SandboxProvider` 可以被 `LocalSandboxProvider` 和 `DockerSandboxProvider` 继承
- `resolvePath` 对所有路径进行 `realpath` 校验，防止 `..` 穿越

#### Step 2：实现虚拟路径翻译器

**文件：** `sandbox/path-translator.ts`

**核心逻辑：**
```
虚拟路径:   /mnt/user-data/{workspace,uploads,outputs}
物理路径:   {workspaceRoot}/{thread_id}/user-data/{workspace,uploads,outputs}

Skills路径: /mnt/skills → {deer-flow-repo}/skills/
```

```typescript
export class PathTranslator {
  constructor(
    private threadId: string,
    private workspaceRoot: string,
    private skillsRoot: string
  ) {}

  // 虚拟路径 → 物理路径
  toPhysical(virtualPath: string): string {
    // /mnt/user-data/xxx → {root}/{thread_id}/user-data/xxx
    // /mnt/skills/xxx → {skillsRoot}/xxx
    // 其他路径 → 拒绝
  }

  // 物理路径 → 虚拟路径（反向）
  toVirtual(physicalPath: string): string {
    // 仅对已允许的物理路径做转换
  }

  // 安全校验：realpath(virtualPath) 不能逃逸 workspaceRoot
  validatePath(virtualPath: string): boolean {
    const physical = this.toPhysical(virtualPath);
    const real = fs.realpathSync(physical);
    return real.startsWith(this.workspaceRoot);
  }
}
```

**关键安全检查（三层验证）：**
1. 虚拟路径格式检查（必须以 `/mnt/` 开头）
2. 拼接后的物理路径检查（不能包含 `..`）
3. `realpath` 校验（确保符号链接不逃逸）

#### Step 3：实现本地沙箱Provider

**文件：** `sandbox/providers/local.ts`

```typescript
import { spawn } from 'child_process';
import { SandboxProvider } from '../base';
import { PathTranslator } from '../path-translator';

export class LocalSandboxProvider extends SandboxProvider {
  private translator: PathTranslator;

  constructor(
    threadId: string,
    workspaceRoot: string = '.deer-flow/threads',
    skillsRoot: string = ''
  ) {
    super();
    this.translator = new PathTranslator(threadId, workspaceRoot, skillsRoot);
  }

  async executeCommand(
    cmd: string,
    cwd: string,
    timeoutMs: number = 300000
  ): Promise<{ stdout: string; stderr: string; exitCode: number }> {
    // 1. 路径翻译（cwd + 命令中的路径）
    // 2. 超时控制（spawn + timeout kill）
    // 3. 执行 + stdout/stderr 收集
    // 4. 错误归一化（超时/信号/SystemError）
  }

  async bash(
    command: string,
    timeoutMs: number = 300000
  ): Promise<{ stdout: string; stderr: string; exitCode: number }> {
    return this.executeCommand(command, '/mnt/user-data/workspace', timeoutMs);
  }
}
```

#### Step 4：移植沙箱工具集

**文件：** `sandbox/tools/bash.ts`

```typescript
// 核心bash工具，集成路径翻译 + 超时 + 安全校验
export async function bashTool(
  command: string,
  threadId: string,
  options?: { timeoutMs?: number; allowedCommands?: string[] }
): Promise<ToolResult> {
  const provider = new LocalSandboxProvider(threadId);

  // 前置检查：命令黑名单（rm -rf /, fork bomb等）
  const dangerous = detectDangerousCommands(command);
  if (dangerous) {
    return { error: `Blocked dangerous command pattern: ${dangerous}` };
  }

  // 执行
  const result = await provider.bash(command, options?.timeoutMs);

  // 后置处理：错误格式化（避免敏感路径泄漏）
  return formatResult(result);
}
```

**黑名单检测正则：**
```typescript
const DANGEROUS_PATTERNS = [
  /^rm\s+-rf\s+\//,                          // rm -rf /
  /;\s*fork\s*;/,                            // fork bomb
  /\.\.\//,                                  // 路径穿越
  /^curl\s+.*\|*\s*sh$/,                      // curl | sh
  /^wget\s+.*\|*\s*sh$/,                      // wget | sh
];
```

**文件：** `sandbox/tools/ls.ts`

```typescript
export async function lsTool(
  path: string,
  threadId: string
): Promise<{ entries: string[]; tree?: boolean }> {
  // 路径翻译 → fs.readdir
  // 返回格式化树（最多2层）
  // 权限错误归一化处理
}
```

**文件：** `sandbox/tools/read_file.ts`

```typescript
export async function readFileTool(
  path: string,
  threadId: string,
  options?: { offset?: number; limit?: number }
): Promise<string> {
  // 路径翻译
  // 行号范围读取（offset/limit）
  // 大文件分块读取（>1MB警告）
  // 二进制文件拒绝处理
}
```

**文件：** `sandbox/tools/write_file.ts`

```typescript
export async function writeFileTool(
  path: string,
  content: string,
  threadId: string,
  options?: { append?: boolean }
): Promise<{ path: string; bytes: number }> {
  // 路径翻译
  // 目录自动创建（mkdir -p语义）
  // 原子写入（临时文件 + rename）
  // append模式
}
```

**文件：** `sandbox/tools/str_replace.ts`

```typescript
export async function strReplaceTool(
  path: string,
  oldStr: string,
  newStr: string,
  threadId: string,
  options?: { global?: boolean }
): Promise<{ matches: number; replaced: number }> {
  // 读取文件
  // 单次/全局替换
  // 精确匹配oldStr（避免歧义）
  // 写入
}
```

#### Step 5：ThreadDataMiddleware 适配

**目的：** 每个线程创建独立隔离目录

```typescript
// sandbox/middleware/thread-data.ts
export async function ensureThreadWorkspace(threadId: string): Promise<void> {
  const dirs = [
    `.deer-flow/threads/${threadId}/user-data/workspace`,
    `.deer-flow/threads/${threadId}/user-data/uploads`,
    `.deer-flow/threads/${threadId}/user-data/outputs`,
  ];
  for (const dir of dirs) {
    await fs.mkdir(dir, { recursive: true });
  }
}
```

#### Step 6：集成进入OpenClaw工具系统

**文件：** `sandbox/index.ts` — 统一导出

```typescript
export { LocalSandboxProvider } from './providers/local';
export { PathTranslator } from './path-translator';
export { bashTool, lsTool, readFileTool, writeFileTool, strReplaceTool } from './tools';
export { ensureThreadWorkspace } from './middleware/thread-data';
```

**OpenClaw工具注册改造：**
```typescript
// 将 exec 工具替换为沙箱版本
const sandboxTools = {
  bash: wrapWithSandbox(originalExecTool, threadId),
  ls: lsTool,
  read: readFileTool,
  write: writeFileTool,
  str_replace: strReplaceTool,
};
```

#### Step 7：配置文件

**文件：** `sandbox.config.yaml`

```yaml
sandbox:
  provider: local
  workspace_root: .deer-flow/threads
  virtual_paths:
    user_data: /mnt/user-data
    skills: /mnt/skills
  timeout_ms: 300000
  max_file_size_mb: 50
  allowed_dangerous_patterns:
    - ^rm\s+-rf\s+\/
    - ;\s*fork\s*;
    - \.\.\/
```

### 2.3 验证计划

| 测试用例 | 预期结果 |
|---------|---------|
| `bash("ls /mnt/user-data/workspace")` | 正常返回目录列表 |
| `bash("ls /etc/passwd")` | 拒绝访问（路径隔离） |
| `bash("rm -rf /")` | 拒绝执行（黑名单） |
| `bash("sleep 600", timeoutMs=5000)` | 5秒后超时终止 |
| `readFile("/mnt/user-data/workspace/test.txt")` | 正常读取 |
| `readFile("/mnt/user-data/../secrets")` | 拒绝（路径穿越检测） |
| 多线程并发bash | 互不干扰，独立workspace |

### 2.4 预计工时
- Step 1-2（类型+路径翻译）：1天
- Step 3（LocalSandboxProvider）：1天
- Step 4（5个工具）：2天
- Step 5-6（集成+配置）：1天
- 测试验证：1天
- **合计：约6个工作日**

---

## 三、Phase 3：Skills + MCP扩展机制

### 3.1 核心目标
升级OpenClaw的Skills系统，使其：
- 支持YAML frontmatter元数据（描述、允许工具列表）
- 支持公开/自定义双目录
- 支持MCP服务器热插拔
- 提供标准Gateway API（列出/安装/卸载Skills）

### 3.2 实施步骤

#### Step 1：定义SKILL.md格式标准

**文件：** `skills/SKILL.md-format.md`

```markdown
---
name: example-skill
description: 这是一个示例技能，用于演示SKILL.md格式
allowed-tools: [bash, read, write]  # 可选的白名单工具
version: 1.0.0
author: 李元芳
tags: [研究, 分析]
enabled: true
---

# Example Skill

## 触发条件
当用户询问xxx时激活此技能

## Workflow
1. 第一步：xxx
2. 第二步：xxx

## 示例
用户说"xxx"时，触发以下行为...
```

#### Step 2：实现Skills加载器

**文件：** `skills/loader.ts`

```typescript
import * as yaml from 'yaml';
import * as fs from 'fs/promises';
import * as path from 'path';

export interface SkillMetadata {
  name: string;
  description: string;
  allowedTools?: string[];
  version?: string;
  author?: string;
  tags?: string[];
  enabled: boolean;
}

export interface Skill {
  metadata: SkillMetadata;
  content: string;         // Markdown正文
  rootPath: string;         // 技能根目录
}

export class SkillsLoader {
  constructor(
    private publicDir: string = 'skills/public',
    private customDir: string = 'skills/custom'
  ) {}

  async loadAll(): Promise<Skill[]> {
    const skills: Skill[] = [];
    for (const dir of [this.publicDir, this.customDir]) {
      const found = await this.scanDir(dir);
      skills.push(...found);
    }
    return skills.filter(s => s.metadata.enabled);
  }

  async scanDir(dir: string): Promise<Skill[]> {
    // 递归扫描所有SKILL.md
    // 解析YAML frontmatter
    // 读取enabled状态
  }

  private parseFrontmatter(content: string): { metadata: SkillMetadata; body: string } {
    // 提取 --- --- 之间的YAML
    // 解析metadata
    // 返回正文
  }
}
```

**关键实现细节：**
```typescript
// 解析YAML frontmatter
function parseFrontmatter(raw: string): { metadata: SkillMetadata; body: string } {
  const match = raw.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
  if (!match) {
    return { metadata: { enabled: true, name: path.basename(raw) }, body: raw };
  }
  return {
    metadata: yaml.parse(match[1]) as SkillMetadata,
    body: match[2],
  };
}
```

#### Step 3：实现Skills注册表

**文件：** `skills/registry.ts`

```typescript
export class SkillsRegistry {
  private skills: Map<string, Skill> = new Map();

  async register(skill: Skill): Promise<void> {
    this.skills.set(skill.metadata.name, skill);
  }

  async get(name: string): Promise<Skill | undefined> {
    return this.skills.get(name);
  }

  async listAll(): Promise<Skill[]> {
    return Array.from(this.skills.values());
  }

  async findByTag(tag: string): Promise<Skill[]> {
    return Array.from(this.skills.values())
      .filter(s => s.metadata.tags?.includes(tag));
  }

  // 注入到system prompt
  toSystemPromptInjection(): string {
    // 生成 # Available Skills 段落
    // 每个skill包含: name, description, allowed-tools
  }
}
```

#### Step 4：实现MCP客户端

**文件：** `mcp/client.ts`

```typescript
export interface MCPServerConfig {
  name: string;
  command: string;           // npx / node / python
  args: string[];
  env?: Record<string, string>;
  transport: 'stdio' | 'sse' | 'http';
  auth?: {
    type: 'oauth' | 'api_key';
    clientId?: string;
    clientSecret?: string;
  };
}

export interface MCPTool {
  name: string;
  description: string;
  inputSchema: object;
}

export class MCPClient {
  private process: ChildProcess | null = null;
  private readyTools: MCPTool[] = [];

  async connect(config: MCPServerConfig): Promise<void> {
    if (config.transport === 'stdio') {
      await this.connectStdio(config);
    }
  }

  private async connectStdio(config: MCPServerConfig): Promise<void> {
    // spawn npx/node进程
    // 通过stdin/stdout发送JSON-RPC消息
    // 等待"initialized"响应
    // 缓存tools列表
  }

  async listTools(): Promise<MCPTool[]> {
    return this.readyTools;
  }

  async callTool(name: string, args: Record<string, unknown>): Promise<unknown> {
    // 发送 JSON-RPC tool/call 消息
    // 等待响应
    // 超时处理（30s default）
  }

  async disconnect(): Promise<void> {
    this.process?.kill();
    this.process = null;
  }
}
```

**JSON-RPC消息格式：**
```typescript
// 请求
{ jsonrpc: "2.0", id: 1, method: "tools/call", params: { name, arguments: {} } }

// 响应
{ jsonrpc: "2.0", id: 1, result: { content: [{ type: "text", text: "..." }] } }
```

#### Step 5：实现MCP传输层

**文件：** `mcp/transports/stdio.ts`

```typescript
export class StdioTransport {
  constructor(
    private command: string,
    private args: string[],
    private env: Record<string, string> = {}
  ) {}

  async start(): Promise<{ stdin: Writable; stdout: Readable }> {
    const proc = spawn(this.command, this.args, {
      stdio: ['pipe', 'pipe', 'inherit'],
      env: { ...process.env, ...this.env },
    });
    return { stdin: proc.stdin!, stdout: proc.stdout! };
  }

  async call(
    stdin: Writable,
    stdout: Readable,
    method: string,
    params: unknown
  ): Promise<unknown> {
    // 发送JSON-RPC请求
    // 读取响应（带超时）
  }
}
```

#### Step 6：OAuth Token刷新（可选，后期）

**文件：** `mcp/auth/oauth.ts`

```typescript
export class OAuthTokenManager {
  private accessToken: string | null = null;
  private refreshToken: string | null = null;
  private expiresAt: number = 0;

  async getAccessToken(config: OAuthConfig): Promise<string> {
    if (this.accessToken && Date.now() < this.expiresAt) {
      return this.accessToken;
    }
    return this.refresh(config);
  }

  private async refresh(config: OAuthConfig): Promise<string> {
    // client_credentials 或 refresh_token 流程
    // 更新 this.accessToken 和 this.expiresAt
  }
}
```

#### Step 7：MCP配置API

**文件：** `skills/gateway-api.ts`

```typescript
// GET /api/mcp/config - 列出MCP服务器
app.get('/api/mcp/config', async (req, res) => {
  const servers = await mcpConfigStore.list();
  res.json({ servers });
});

// POST /api/mcp/config - 添加MCP服务器
app.post('/api/mcp/config', async (req, res) => {
  const config: MCPServerConfig = req.body;
  await mcpConfigStore.add(config);
  res.json({ success: true });
});

// GET /api/skills - 列出所有Skills
app.get('/api/skills', async (req, res) => {
  const skills = await skillsRegistry.listAll();
  res.json({ skills: skills.map(s => s.metadata) });
});

// POST /api/skills/install - 从zip安装skill
app.post('/api/skills/install', upload.single('file'), async (req, res) => {
  // 解压到 skills/custom/
  // 验证 SKILL.md 格式
  // 重新加载
});
```

#### Step 8：System Prompt注入集成

**目标：** 让Lead Agent能看到所有Skills描述

```typescript
function buildSystemPrompt(skills: Skill[], mcpTools: MCPTool[]): string {
  let prompt = '';

  // Skills section
  if (skills.length > 0) {
    prompt += '\n\n## Available Skills\n';
    for (const skill of skills) {
      prompt += `- **${skill.metadata.name}**: ${skill.metadata.description}`;
      if (skill.metadata.allowedTools) {
        prompt += ` (allowed tools: ${skill.metadata.allowedTools.join(', ')})`;
      }
      prompt += '\n';
    }
  }

  // MCP tools section
  if (mcpTools.length > 0) {
    prompt += '\n\n## MCP Tools\n';
    for (const tool of mcpTools) {
      prompt += `- **${tool.name}**: ${tool.description}\n`;
    }
  }

  return prompt;
}
```

### 3.3 验证计划

| 测试用例 | 预期结果 |
|---------|---------|
| `skills/public/example/SKILL.md` 存在 | `loadAll()` 返回该skill |
| SKILL.md无YAML frontmatter | 使用默认metadata（enabled:true） |
| `enabled: false` | `loadAll()` 跳过该skill |
| MCP服务器stdin/stdout通信 | `listTools()` 返回可用工具列表 |
| MCP工具调用 | 正常返回结果 |
| `POST /api/skills/install` 上传zip | 解压并注册新skill |

### 3.4 预计工时
- Step 1-2（SKILL.md格式+加载器）：1天
- Step 3（注册表）：0.5天
- Step 4-5（MCP客户端+stdio传输）：2天
- Step 6（OAuth）：0.5天（后期）
- Step 7-8（API+注入）：1天
- 测试验证：1天
- **合计：约6个工作日（不含OAuth）**

---

## 四、实施甘特图

```
Week 1-2: Phase 1 沙箱隔离（6天）
  ├─ Day1: sandbox/base.ts + path-translator.ts
  ├─ Day2: LocalSandboxProvider
  ├─ Day3-4: 5个沙箱工具
  ├─ Day5: ThreadDataMiddleware + 集成
  └─ Day6: 测试验证

Week 3-4: Phase 3 Skills+MCP（6天）
  ├─ Day1: SKILL.md格式 + loader
  ├─ Day2: SkillsRegistry
  ├─ Day3-4: MCP客户端 + stdio传输
  ├─ Day5: Gateway API
  └─ Day6: System Prompt注入 + 测试
```

---

## 五、风险与缓解

| 风险 | 概率 | 影响 | 缓解措施 |
|------|------|------|---------|
| 路径穿越漏洞 | 中 | 高 | 三层路径验证（格式→拼接→realpath） |
| MCP npx包下载失败 | 低 | 中 | 使用已缓存包，fallback到本地安装 |
| YAML frontmatter解析歧义 | 低 | 低 | 严格正则匹配，无效则用默认metadata |
| 沙箱性能损耗（每命令spawn） | 中 | 低 | 本地provider复用进程池 |
| Skills文件IO阻塞主线程 | 低 | 中 | 全部使用async fs API |

---

## 六、依赖关系

```
Phase 1 (沙箱)
  └─ Phase 3 (Skills+MCP)
        ├─ Skills的/mnt/skills路径依赖sandbox的PathTranslator
        └─ MCP工具依赖沙箱的bashTool执行npx命令
```

**建议：** 先完成Phase 1，再做Phase 3。Phase 3依赖Phase 1的路径翻译基础设施。

---

## 七、后续Phase（轻量提示）

| Phase | 内容 | 优先级 | 预计工时 |
|-------|------|--------|---------|
| Phase 2 | SubAgent并发系统 | ⭐⭐⭐⭐ | 2-3周 |
| Phase 4 | Memory持久化 | ⭐⭐⭐ | 1-2周 |
| Phase 5 | Middleware Chain | ⭐⭐ | 1周 |

---

*李元芳实施计划 · INTJ建筑师型 · 2026-03-29*
