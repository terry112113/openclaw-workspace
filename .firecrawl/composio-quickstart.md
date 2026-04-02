# Quickstart

Copy page [View Markdown](https://docs.composio.dev/docs/quickstart.md) Ask AIFeedback

Build your first AI agent with Composio Tools. You'll create a [session](https://docs.composio.dev/docs/users-and-sessions) for a user, give your agent access to [tools](https://docs.composio.dev/docs/tools-and-toolkits), and let it take action across 1000+ apps.

Choose your framework

![OpenAI Agents logo](https://docs.composio.dev/images/providers/openai-logo.svg?dpl=dpl_7moVdYtMAaFtYXFY9d5hYAjsdTnc)![OpenAI Agents logo](https://docs.composio.dev/images/providers/openai-logo-dark.svg?dpl=dpl_7moVdYtMAaFtYXFY9d5hYAjsdTnc)
OpenAI Agents
![Claude Agent SDK logo](https://docs.composio.dev/images/providers/anthropic-logo.svg?dpl=dpl_7moVdYtMAaFtYXFY9d5hYAjsdTnc)![Claude Agent SDK logo](https://docs.composio.dev/images/providers/anthropic-logo-dark.svg?dpl=dpl_7moVdYtMAaFtYXFY9d5hYAjsdTnc)
Claude Agent SDK
![Vercel AI SDK logo](https://docs.composio.dev/images/providers/vercel-logo.svg?dpl=dpl_7moVdYtMAaFtYXFY9d5hYAjsdTnc)![Vercel AI SDK logo](https://docs.composio.dev/images/providers/vercel-logo-dark.svg?dpl=dpl_7moVdYtMAaFtYXFY9d5hYAjsdTnc)
Vercel AI SDK [→Other providers](https://docs.composio.dev/docs/providers)

Choose your integration type · [Use this guide to decide](https://docs.composio.dev/docs/native-tools-vs-mcp)

![Native Tools](https://docs.composio.dev/images/providers/native-tools-logo.svg?dpl=dpl_7moVdYtMAaFtYXFY9d5hYAjsdTnc)![Native Tools](https://docs.composio.dev/images/providers/native-tools-logo-dark.svg?dpl=dpl_7moVdYtMAaFtYXFY9d5hYAjsdTnc)
Native Tools
![MCP](https://docs.composio.dev/images/mcp-logo.svg?dpl=dpl_7moVdYtMAaFtYXFY9d5hYAjsdTnc)![MCP](https://docs.composio.dev/images/mcp-logo-dark.svg?dpl=dpl_7moVdYtMAaFtYXFY9d5hYAjsdTnc)
MCP

Use skills or copy prompt to get started faster!

[Skills↗](https://skills.sh/composiohq/skills/composio) Copy prompt

**Add Composio tools to an OpenAI Agents app (Native Tools)**

Give your OpenAI Agent access to 1000+ tools (Gmail, GitHub, Slack, Notion, etc.) via Composio. Composio handles authentication, tool discovery, and execution. You create a **session** for a user, get tools from that session, and pass them to your Agent.

**Key concepts**

- **Session**: Scoped environment for a user. Created with `composio.create(userId)`. Sessions have access to all toolkits by default — the agent discovers which tools to use via `COMPOSIO_SEARCH_TOOLS`.
- **Provider**: Translates Composio tools into the framework's tool format. For OpenAI Agents, use `OpenAIAgentsProvider`.
- **Authentication**: When a tool requires auth (e.g., GitHub OAuth), Composio returns an auth URL. The user authenticates once; Composio manages tokens.

**Rules**

ALWAYS:

- Initialize with `OpenAIAgentsProvider` as the provider
- Create a session with a user ID before getting tools
- Use `session.tools()` to get tools — this returns framework-ready tools
- Store API keys in .env, load with dotenv

NEVER:

- Hardcode API keys in source code
- Call tools directly without a session
- Import from `composio-core` (the package is `composio` for Python, `@composio/core` for TS)
- Use `composio.tools.get()` or `composio.tools.execute()` — these are deprecated direct execution patterns

**Deprecated (DO NOT use)**

Python:

```
# WRONG — old direct execution pattern
tools = composio.tools.get(user_id, { toolkits: ['github'] })
result = composio.tools.execute('GITHUB_STAR_REPO', {...})

# WRONG — old package name
from composio_core import Composio
```

TypeScript:

```
// WRONG — old direct execution pattern
const tools = composio.tools.get(userId, { toolkits: ['github'] });
const result = composio.tools.execute('GITHUB_STAR_REPO', {...});
```

**Verify before responding**

1. Is `OpenAIAgentsProvider` passed to `Composio()`?
2. Is a session created with `composio.create(user_id)`?
3. Are tools retrieved from `session.tools()`, not `composio.tools.get()`?
4. Are API keys in .env, not hardcoded?
5. Are imports from `composio` (Python) or `@composio/core` (TS)?

Install

PythonTypeScript

```
pip install python-dotenv composio composio-openai-agents openai-agents
```

```
npm install @composio/core @composio/openai-agents @openai/agents
```

Configure API Keys

Get your `COMPOSIO_API_KEY` from [Settings](https://platform.composio.dev/settings) and `OPENAI_API_KEY` from [OpenAI](https://platform.openai.com/api-keys).

.env

```
COMPOSIO_API_KEY=your_composio_api_key
OPENAI_API_KEY=your_openai_api_key
```

Create session and run agent

PythonTypeScript

```
from dotenv import load_dotenv
from composio import Composio
from agents import Agent, Runner, SQLiteSession
from composio_openai_agents import OpenAIAgentsProvider

load_dotenv()

# Initialize Composio with OpenAI Agents provider
composio = Composio(provider=OpenAIAgentsProvider())

# Create a session for your user
user_id = "user_123"
session = composio.create(user_id=user_id)
tools = session.tools()

agent = Agent(
    name="Personal Assistant",
    instructions="You are a helpful personal assistant. Use Composio tools to take action.",
    model="gpt-5.2",
    tools=tools,
)

# Memory for multi-turn conversation
memory = SQLiteSession("conversation")

print("""
What task would you like me to help you with?
I can use tools like Gmail, GitHub, Linear, Notion, and more.
(Type 'exit' to exit)
Example tasks:
  - 'Summarize my emails from today'
  - 'List all open issues on the composio github repository'
""")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "exit":
        break

    print("Assistant: ", end="", flush=True)
    result = Runner.run_sync(starting_agent=agent, input=user_input, session=memory)
    print(f"{result.final_output}\n")
```

```
import "dotenv/config";
import { Composio } from "@composio/core";
import { Agent, run, MemorySession } from "@openai/agents";
import { OpenAIAgentsProvider } from "@composio/openai-agents";
import { createInterface } from "readline/promises";

// Initialize Composio with OpenAI Agents provider
const composio = new Composio({ provider: new OpenAIAgentsProvider() });

// Create a session for your user
const userId = "user_123";
const session = await composio.create(userId);
const tools = await session.tools();

const agent = new Agent({
  name: "Personal Assistant",
  instructions: "You are a helpful personal assistant. Use Composio tools to take action.",
  model: "gpt-5.2",
  tools,
});

const memory = new MemorySession();
const readline = createInterface({ input: process.stdin, output: process.stdout });

console.log(`
What task would you like me to help you with?
I can use tools like Gmail, GitHub, Linear, Notion, and more.
(Type 'exit' to exit)
Example tasks:
  - 'Summarize my emails from today'
  - 'List all open issues on the composio github repository'
`);

while (true) {
  const input = (await readline.question("You: ")).trim();
  if (input.toLowerCase() === "exit") break;

  process.stdout.write("Assistant: ");
  const result = await run(agent, input, { session: memory });
  process.stdout.write(`${result.finalOutput}\n`);
}
readline.close();
```

By default, sessions have access to **all available toolkits** in the Composio catalog. Your agent can discover and use any of them through `COMPOSIO_SEARCH_TOOLS`. To restrict which toolkits are available, see [Enable and disable toolkits](https://docs.composio.dev/docs/toolkits/enable-and-disable-toolkits).

## [Next steps](https://docs.composio.dev/docs/quickstart\#next-steps)

[**Configuring Sessions** \\
Restrict toolkits, set custom auth configs, and select connected accounts](https://docs.composio.dev/docs/configuring-sessions) [**Authenticating Users** \\
Learn how users connect their accounts via Connect Links, OAuth, and API keys](https://docs.composio.dev/docs/authentication) [**How Composio works** \\
Understand what happens under the hood: sessions, meta tools, and the tool execution lifecycle](https://docs.composio.dev/docs/how-composio-works) [**Build a chat app** \\
Full Next.js tutorial: tool discovery, auth, and multi-turn conversations](https://docs.composio.dev/cookbooks/chat-app)

### On this page

[Next steps](https://docs.composio.dev/docs/quickstart#next-steps)

 Ask AI

Chat Widget

Loading...