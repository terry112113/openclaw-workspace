# Memory Search 配置研究 - 2026-03-30

## OpenClaw内置Memory Search

**当前状态：**
- Memory search已启用，但无embedding provider
- Doctor警告：No API key found for provider "openai"

**可用的embedding provider：**
| Provider | 模型 | 价格参考 |
|----------|------|---------|
| openai | text-embedding-3 | $0.13/1M tokens |
| gemini | embedding-001/2 | $0.10/1M tokens |
| voyage | voyage-3 | $0.10/1M tokens |
| mistral | mistral-embed | 待查 |
| ollama | 本地模型 | 免费 |
| local | 本地 | 免费 |

## 配置方式

需要皇上在config里配置：

```json
{
  "agents": {
    "defaults": {
      "memorySearch": {
        "enabled": true,
        "provider": "voyage",  // 或 openai/gemini/mistral/ollama/local
        "fallback": "openai"
      }
    }
  }
}
```

或者用命令：
```
openclaw configure --section model
```

## 下一步

等皇上回来后，问皇上想用哪个provider。

臣目前的记忆是文件-based的，没有语义检索能力。有了embedding provider后，臣就能像hermes-agent那样跨session记住之前做过什么。
