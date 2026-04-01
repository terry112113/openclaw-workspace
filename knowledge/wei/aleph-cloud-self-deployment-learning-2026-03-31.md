# Aleph Cloud 自部署学习笔记
**刑部尚书 魏征 · 2026-03-31**

---

## 一、核心问题：云端异步执行 + 持久化运行

**本地部署的根本缺陷：**
- 机器休眠 → OpenClaw 进程中断
- cron 任务依赖本地时钟，不准时
- 没有弹性扩展能力
- 无法处理异步回调（webhook）

**Aleph Cloud 的解决方案：**
在云端部署持久运行的 VM，OpenClaw 作为 systemd 服务跑在云端，不依赖本地机器。

---

## 二、Aleph Cloud 架构解析

### 2.1 定位
去中心化云基础设施平台。通过 **CRN（Compute Resource Node）** 接入多个云提供商（aleph.im、twentysix.cloud、cybernodes.io），程序化创建和管理 VM 实例。

**成本估算：**
| 节点类型 | 配置 | 月费 |
|---------|------|------|
| 主节点（Orchestrator） | 4 vCPU, 8GB RAM, 100GB SSD | ~50 ALEPH |
| 工作节点（Worker） | 2 vCPU, 4GB RAM, 50GB SSD | ~25 ALEPH/个 |
| 最小化（开发测试） | 1 节点 | ~25 ALEPH |

### 2.2 节点类型
```
┌──────────────────────────────────────────────┐
│              Aleph Cloud 网络                 │
├────────────┬────────────┬────────────────────┤
│ Primary    │ Worker 1   │ Worker 2           │
│ (主节点)    │ (工作节点)  │ (工作节点)          │
│            │            │                    │
│ Fleet Mgr  │ OpenClaw   │ OpenClaw           │
│ Load Bal   │ Tailscale  │ Tailscale          │
│ Backup     │ AutoRestart│ AutoRestart        │
└────────────┴────────────┴────────────────────┘
```

### 2.3 关键 CRN 提供商
| 提供商 | 特点 | 适合场景 |
|-------|------|---------|
| aleph.im | 最高可靠性 | 主节点 |
| twentysix.cloud | 成本优化 | 工作节点 |
| cybernodes.io | 成本优化 | 工作节点 |
| NFT.Storage | 备用 | 归档存储 |

---

## 三、持久化运行的核心机制

### 3.1 systemd > nohup（关键！）

**nohup 的问题：**
- 进程崩溃后不会自动重启
- 没有健康检查
- 系统重启后不会自启动

**systemd 的优势：**
```ini
[Unit]
Description=OpenClaw Service
After=network.target

[Service]
Type=simple
User=ubuntu
ExecStart=/usr/bin/node server.js
Restart=always        # 崩溃后自动重启
RestartSec=10         # 等待 10 秒再重启
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=openclaw

[Install]
WantedBy=multi-user.target
```

systemd 还负责 node-monitor 等辅助服务的生命周期。

### 3.2 健康检查 + 心跳注册

**Worker 节点心跳脚本：**
```bash
# 每 30 秒向主节点注册一次
while true; do
    curl -X POST http://PRIMARY_IP:8080/fleet/register \
      -H "x-api-key: $FLEET_API_KEY" \
      -d '{"node_id": "$NODE_NAME", "ip_address": "$LOCAL_IP", "capabilities": ["compute", "openclaw"]}'
    sleep 30
done
```
注册信息写入 `/opt/fleet-manager/nodes.json`，Fleet Manager 实时掌握所有节点状态。

### 3.3 节点故障自动检测 + 重建

```bash
# 监控循环
check_node_health() {
    if ! ssh ... ubuntu@"$node_ip" "systemctl is-active openclaw"; then
        failure_count += 1
        if (( failure_count >= 3 )); then
            mark_node_unhealthy
            auto_recreate_node  # 触发重建
        fi
    fi
}
```

---

## 四、云端异步执行的关键架构

### 4.1 Fleet Manager（舰队管理器）

Node.js + Express 应用，监听 8080 端口：

**核心端点：**
- `POST /fleet/register` — Worker 注册
- `GET /fleet/status` — 查看所有节点状态
- `GET /fleet/distribute/:task` — 任务分发

**安全设计：**
- 所有端点需要 `x-api-key` 请求头认证
- Fleet Manager 只绑定 `127.0.0.1` 或 Tailscale IP，不暴露公网

### 4.2 Auto-Provisioning Protocol（自动配置协议）

**解决的问题：** 多节点 workspace 同步（SOUL.md、AGENTS.md、MEMORY.md、skills）

**工作流程：**
1. 主节点收集 replication 数据（workspace 文件）
2. 打包成 `.tar.gz`
3. 通过 SSH 分发到所有工作节点
4. 工作节点解压安装，重启 OpenClaw

**同步内容：**
```json
{
  "soul": "SOUL.md",
  "agents": "AGENTS.md",
  "memory": "MEMORY.md",
  "skills": "skills/",
  "user_data": "USER.md"
}
```

**触发时机：**
- 手动触发：`replicate_to_fleet`
- 定时触发：每 5 分钟（cron）
- 紧急触发：配置变更后

### 4.3 负载分发策略

Fleet Manager 支持多种负载均衡策略：
| 策略 | 原理 |
|------|------|
| Round Robin | 轮询分发 |
| Least Connections | 连接数最少优先 |
| Weighted Response Time | 响应时间最短优先 |
| **Resource Aware** | CPU + 内存 + 响应时间综合评分（默认）|

---

## 五、Tailscale .mesh 网络

### 解决的问题
- VM 之间通过公网 IP 通信不安全
- 不便于管理 SSH 和服务端口

### 方案
所有节点加入同一个 Tailscale 私有网络，通过 `tailscale ip -4` 获取内网 IP，实现：
- SSH 通过 Tailscale IP 连接（加密）
- 服务间通过内网 IP 通信
- Fleet Manager 只监听 Tailscale IP，不暴露公网

---

## 六、灾难恢复体系

### 6.1 备份策略
- **每日 2 AM**：完整备份（fleet config + 所有节点 workspace）
- **每 6 小时**：恢复快照（包含所有服务状态）
- **保留 30 天**

### 6.2 备份内容
- Fleet registry（`nodes.json`）
- HAProxy 配置
- systemd service 文件
- OpenClaw workspace（所有节点）
- 日志（最近 7 天）

### 6.3 恢复步骤
```bash
# 1. 从备份恢复主节点
./restore-from-backup.sh primary

# 2. 重新部署工作节点
./deploy-fleet.sh openclaw-fleet 5

# 3. 同步最新 workspace
./auto-provisioning-protocol.sh replicate
```

---

## 七、与 OpenClaw 集成的关键路径

### 7.1 部署步骤（简化版）
1. 安装 Aleph CLI：`pip3 install aleph-client`
2. 创建账户：`aleph account create`
3. 充值 ALEPH token（至少 50 ALEPH 起）
4. 生成 SSH 密钥对
5. 运行 `deploy-single-vm.sh` 部署主节点
6. 运行 `deploy-fleet.sh` 部署完整舰队

### 7.2 OpenClaw 云端安装（setup script 部分）
```bash
# 安装 OpenClaw
curl -fsSL https://raw.githubusercontent.com/openclaw/openclaw/main/install.sh | bash

# 配置为 systemd 服务（关键！）
cat > /etc/systemd/system/openclaw.service << 'SERVICE'
[Unit]
Description=OpenClaw Service
After=network.target
[Service]
Type=simple
User=ubuntu
WorkingDirectory=/opt/openclaw
ExecStart=/usr/bin/node server.js
Restart=always
RestartSec=10
[Install]
WantedBy=multi-user.target
SERVICE

systemctl enable openclaw
systemctl start openclaw
```

### 7.3 接入三司会审架构
```
太上皇（皇上）
  └── 狄仁杰（大理寺卿）
        ├── 李元芳（都察院御史）→ Aleph Cloud VM #1
        └── 魏征（刑部尚书）→ Aleph Cloud VM #2
```

每个角色跑在独立的云端 VM，通过 Fleet Manager 协调。

---

## 八、学习总结

### 战略价值
| 维度 | 评估 |
|------|------|
| **解决核心痛点** | 本地机器休眠导致 OpenClaw 中断 ✅ |
| **云端异步执行** | Fleet Manager + HTTP 端点 ✅ |
| **持久化运行** | systemd 自动重启 + 健康检查 ✅ |
| **多节点扩展** | 舰队管理 + 负载均衡 ✅ |
| **学习门槛** | 高（需要 ALEPH token + 多 VM 管理）⚠️ |
| **成本** | 最低 ~25 ALEPH/月 ≈ $8-10 USD ⚠️ |

### 最快落地路径
1. **先用 aleph.im 免费额度** 测试单节点部署
2. **将 cron 任务迁移到云端**（解决异步执行问题）
3. **用 Fleet Manager 的 HTTP 端点** 处理 webhook 回调
4. **验证 systemd + 健康检查** 的持久化效果

### 关键教训
1. **永远用 systemd，不用来 nohup** — supervised processes survive crashes
2. **Fleet Manager 所有端点都要认证** — 绑定 localhost/Tailscale IP
3. **replication 文件路径** — 打包后解压到 `soul/`、`agents/`、`memory/` 子目录
4. **节点文件要在服务启动前创建** — `nodes.json` 不存在会崩Fleet Manager

### 待深入
- Aleph CLI 实际命令验证
- 单节点部署成本验证（aleph.im 实际价格）
- OpenClaw 云端部署的实际配置方式
- Webhook 端点接入 Fleet Manager 的具体方案

---

*魏征学习完毕。存档待审。*
