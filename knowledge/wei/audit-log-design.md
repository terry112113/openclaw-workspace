# 审计日志设计方案
> 制定日期：2026-03-31 | 制定人：魏征 | 状态：待完善

---

## 一、必须记录的关键操作

### 1. 飞书消息发送
- 记录字段：时间 | 发送者accountId | 接收群ID/用户ID | 消息类型(text/media) | 消息摘要(前50字)
- 记录位置：`knowledge/audit/feishu-messages-YYYY-MM-DD.md`

### 2. 文件写入
- 记录字段：时间 | 操作者 | 文件路径 | 操作类型(创建/修改/删除) | 内容摘要
- 触发条件：workspace目录下的.md/.json/.yaml文件变更
- 记录位置：`knowledge/audit/file-changes-YYYY-MM-DD.md`

### 3. 凭证访问
- 记录字段：时间 | 操作者 | 访问的凭证类型 | 来源(sessionId) | 结果(成功/失败)
- 凭证类型：Feishu appSecret, Minimax API Key, Gateway Token
- 记录位置：`knowledge/audit/credential-access-YYYY-MM-DD.md`

### 4. 三司会审结论
- 记录字段：时间 | 议题 | 结论摘要 | 责任人 | Deadline
- 触发条件：狄仁杰裁决完成后自动记录
- 记录位置：`knowledge/audit/three-courts-decisions-YYYY-MM-DD.md`

---

## 二、实现步骤

### Step 1: 目录建立
- knowledge/audit/ — 审计日志根目录
- 每日一个文件，按类型分流

### Step 2: 记录模板
- 每次操作按模板格式追加到当日文件
- 使用幂等写入（同一session多次操作不重复记录）

### Step 3: 自动化触发
- 飞书消息：message工具调用时自动记录
- 文件写入：exec/cron任务完成时自动记录
- 凭证访问：gateway认证模块记录

### Step 4: 定期归档
- 超过7天的日志移至 knowledge/audit/archive/
- 按月份归档

---

## 三、待魏征完善的内容

1. 如何实现幂等写入（避免同一操作重复记录）
2. 如何在message工具中嵌入审计钩子
3. 如何处理敏感内容（密码/secret）的脱敏记录

---

*本方案为初稿，待魏征补充技术实现细节*
