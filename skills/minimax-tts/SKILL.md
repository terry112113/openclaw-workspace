---
name: minimax-tts
description: MiniMax Text-to-Speech HD - 将文本转换为语音并自动播放。使用时说"播报"或"朗读"加上内容。
---

# MiniMax TTS 技能

## 功能
- 将中文文本转换为高清语音
- 自动播放音频
- 支持缓存短语直接播放

## 核心脚本
- `speak.js` - 主脚本，调用 MiniMax TTS 并播放

## 使用方式
```
node C:\Users\TL\.openclaw\workspace-main\skills\minimax-tts\scripts\speak.js "要播报的文本"
```

## 已缓存短句（直接播放，不消耗 API）：
- 准奏、朕心甚慰、微臣遵旨、善、朕卿所言极是、退下吧、来人、宣、早朝、有事启奏、无事退朝

## API 配置
- Endpoint: https://api.minimaxi.com/v1/t2a_v2
- Model: speech-2.8-hd
- Voice: audiobook_male_2（威严成熟男声）
- Speed: 0.8（较慢）
- Pitch: -2（低沉威严）
- API Key: sk-cp-e_kZnDB6jUSF6tmnzHCzpQajNFsUN9nGyZdywv13Z8oCgS059F6u0k72-n_EFFLPMdwiUDeAqqciSjsmv5gEvTiR69RrcahlVBLc8Vyr5QW-2IL35zCGUiY

## 帝王之声配置（太上皇认证9分！）
- Voice: audiobook_male_2
- Speed: 0.8
- Pitch: -2
- 代表音频：`C:\Users\TL\.openclaw\tts-han.mp3`（寇可往，我亦可往！）
- 用途：帝王宣言、重大决策、威严时刻
