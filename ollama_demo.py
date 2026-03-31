#!/usr/bin/env python3
"""
Ollama API 调用示例
模型: gpt-oss:20b / qwen3-coder:30b
"""

import requests
import json
import time

OLLAMA_URL = "http://localhost:11434"


def chat(model: str, prompt: str, thinking: bool = False) -> dict:
    """发送聊天请求"""
    start = time.time()
    response = requests.post(
        f"{OLLAMA_URL}/api/chat",
        json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
            "thinking": thinking,  # qwen3支持，gpt-oss不支持
        },
        timeout=300,
    )
    elapsed = time.time() - start
    result = response.json()
    result["_elapsed"] = elapsed
    return result


def generate(model: str, prompt: str) -> dict:
    """发送生成请求（非对话）"""
    start = time.time()
    response = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={"model": model, "prompt": prompt, "stream": False},
        timeout=300,
    )
    elapsed = time.time() - start
    result = response.json()
    result["_elapsed"] = elapsed
    return result


def list_models():
    """列出所有可用模型"""
    resp = requests.get(f"{OLLAMA_URL}/api/tags")
    return resp.json()


if __name__ == "__main__":
    # 1. 列出模型
    print("=== 可用模型 ===")
    models = list_models()
    for m in models["models"]:
        print(f"  - {m['name']} ({m['details']['parameter_size']})")

    # 2. 测试 gpt-oss:20b
    print("\n=== 测试 gpt-oss:20b ===")
    r = chat("gpt-oss:20b", "What is 2+2? Answer in one word.")
    print(f"耗时: {r['_elapsed']:.1f}s")
    print(f"回复: {r['message']['content']}")

    # 3. 测试 qwen3-coder:30b（带thinking）
    print("\n=== 测试 qwen3-coder:30b (with thinking) ===")
    r = chat("qwen3-coder:30b", "What is 2+2? Answer in one word.", thinking=False)
    print(f"耗时: {r['_elapsed']:.1f}s")
    print(f"回复: {r['message']['content']}")
