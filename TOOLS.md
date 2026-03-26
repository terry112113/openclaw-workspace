# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

### TTS集成流程（MiniMax HD）

**核心流程：**
1. Agent生成文本（含动作描写如"（抚须）"）
2. 清洗过滤括号内容 → 省字符额度
3. API调用MiniMax HD → 消耗1/50次数
4. 语音下发（WAV/MP3）

**本地缓存（关键！）：**
- 短句如"准奏"、"朕心甚慰"、"朕卿所言"生成一次存本地
- 下次直接播放，不消耗额度

**HD模型优势：**
- 胸腔共鸣，适合帝王语气
- 逗号处有呼吸感，更自然

### TTS语音合成限制（MiniMax/海螺AI）

**额度规则：**
- 0/50 = 今日调用次数（满血状态）
- 每次点"生成"算1次，50次用完需等重置
- 4000字符额度是另一个限制（字数）

**省着用技巧：**
1. **合并长句** → 一次请求一句话，不要循环调用
2. **本地缓存** → 口头禅（"微臣遵旨"等）生成一次存本地，下次直接用
3. **避免Bug** → 不要循环调用，每句话单独调一次 = 浪费次数
4. **500字/次** → 单次请求内容充实最大化价值
5. **先校对再发** → 点之前检查文字，避免白扣次数

### 账号密码体系

主人通用密码：**427521427521tan**

| 平台 | 账号 |
|------|------|
| GitHub | terry112113114@gmail.com |
| 其他待补充 | - |

### GitHub仓库备份
- 仓库：https://github.com/terry112113/openclaw-workspace
- 远程：origin
- 认证方式：已配置git credentials store

---

Add whatever helps you do your job. This is your cheat sheet.
