# DPAPI加密存储方案 - P2执行设计
> 制定日期：2026-03-31 | 制定人：狄仁杰（待魏征完善）

---

## 一、方案概述

Windows DPAPI（Data Protection API）可以将数据加密，只有同一Windows用户账户才能解密。

**优势：**
- 无需密钥管理，Windows自动绑定到用户账户
- 不需要Machine级权限
- 即使文件被拷贝走，其他Windows账户也无法解密

---

## 二、执行方案

### Step 1：创建DPAPI加密工具
位置：`C:\Users\TL\.openclaw\dpapi-protect.ps1`

用法：
```powershell
# 加密
.\dpapi-protect.ps1 -action encrypt -text "原始secret"

# 解密
.\dpapi-protect.ps1 -action decrypt -text "加密后的base64"
```

### Step 2：加密openclaw.json中的敏感字段

需要加密的字段：
- `channels.feishu.accounts.di.appSecret`
- `channels.feishu.accounts.shensi.appSecret`
- `channels.feishu.accounts.wei.appSecret`
- `gateway.auth.token`

### Step 3：修改openclaw.json存储格式

原始：
```json
"appSecret": "dvENt7ppgAzPDpVaHmjiQujtAn8x6Ivi"
```

加密后：
```json
"appSecret": "DPAPI:AQAAANCMnd8BFdERjHoAwE/Cl+sBAAAA..."
```

### Step 4：修改gateway启动流程

gateway启动时：
1. 读取openclaw.json
2. 检测以"DPAPI:"开头的字段
3. 调用PowerShell DPAPI解密
4. 将解密后的值写入内存配置
5. 正常启动

---

## 三、待解决问题

1. **gateway集成**：需要修改gateway代码以支持DPAPI解密（需OpenClaw官方支持）
2. **或使用PowerShell wrapper**：在openclaw配置中引用外部解密脚本
3. **初始加密**：第一次需要手动运行加密工具

---

## 四、当前状态

- DPAPI加密验证：✅ 通过
- DPAPI解密验证：⚠️ 需在同一用户session中测试
- 工具脚本：✅ 已创建 C:\Users\TL\.openclaw\dpapi-protect.ps1
- gateway集成：❌ 待OpenClaw官方支持或自写wrapper

---

## 五、替代方案（臣可立即执行）

臣可以编写一个PowerShell脚本，在openclaw启动时自动解密配置文件：
- 在openclaw服务启动前运行解密脚本
- 将解密后的配置写入临时文件
- 启动openclaw读取临时文件
- 临时文件在openclaw启动后自动删除

**风险：临时文件可能留下痕迹。**

---

*本方案待魏征完善技术细节*
