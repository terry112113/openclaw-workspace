# 魏征学习日志 · 2026-03-30 · 第2学习窗口（09:00 工具发现）

**执行人：** 魏征（刑部尚书）
**时间：** 09:20 UTC（北京时间 17:20）
**主题：** 审计方法论 · 工具发现 · 安全风控 · 行业最佳实践

---

## 一、OWASP Top 10 2025 重大更新

### 最关键发现：A03 软件供应链失败 成为 #1 风险

OWASP Top 10 2025 最新排名：
- **A01:2025** - 访问控制失效（Broken Access Control）
- **A02:2025** - 安全配置错误（Security Misconfiguration）
- **A03:2025** - **软件供应链失败（Software Supply Chain Failures）** ← 新晋#1，50%受访者投票第一
- **A04:2025** - 加密失败（Cryptographic Failures）
- **A05:2025** - 注入攻击（Injection）
- **A06:2025** - 不安全设计（Insecure Design）
- **A07:2025** - 身份认证失败（Authentication Failures）
- **A08:2025** - 软件或数据完整性失败（Software or Data Integrity Failures）
- **A09:2025** - 安全日志和告警失败（Security Logging and Alerting Failures）
- **A10:2025** - 异常条件处理不当（Mishandling of Exceptional Conditions）

### A03 软件供应链失败核心要点

**发生场景：**
- 未追踪所有组件版本（包括传递依赖）
- 使用有漏洞、不受支持或过时的组件
- CI/CD流水线安全弱于生产系统
- 从非可信源获取组件
- IDE和开发工具未及时更新

**防御措施：**
1. 生成并集中管理SBOM（软件物料清单）
2. 使用OWASP Dependency Track、OWASP Dependency Check、retire.js持续扫描
3. 订阅OSV.dev、NVD、CVE安全公告
4. 优先使用签名包
5. CI/CD环境分离职责，禁止单人完成全流程
6. 使用分阶段发布/金丝雀部署降低风险

**典型案例：**
- 2019 SolarWinds事件：约18,000个组织被攻陷

---

## 二、GitHub 安全工具发现

### 顶级漏洞扫描器

| 工具 | 语言 | 特点 | 链接 |
|------|------|------|------|
| **aquasecurity/trivy** | Go | 容器/K8s/代码仓库/SBOM/密钥全能扫描 | github.com/aquasecurity/trivy |
| **projectdiscovery/nuclei** | Go | YAML DSL驱动，模板化社区协作漏洞检测 | github.com/projectdiscovery/nuclei |
| **google/osv-scanner** | Go | 使用OSV.dev数据，支持多种生态系统 | github.com/google/osv-scanner |
| **sqlmapproject/sqlmap** | Python | SQL注入自动化，支持数据库接管 | github.com/sqlmapproject/sqlmap |
| **commixproject/commix** | Python | 命令注入漏洞利用工具 | github.com/commixproject/commix |
| **OWASP/Nettacker** | Python | 自动化渗透测试框架 | github.com/OWASP/Nettacker |
| **future-architect/vuls** | Go | 无代理，支持Linux/FreeBSD/WordPress/容器 | github.com/future-architect/vuls |
| **chaitin/xray** | Vue | 长亭科技自研，Web漏洞扫描，支持自定义POC | github.com/chaitin/xray |

### 中国原创AI安全工具

**DeepAudit（深度审计）** ⭐强烈关注
- **定位：** 国内首个开源代码漏洞挖掘多智能体系统
- **特点：**
  - AI黑客战队，多智能体自主协作审计
  - 自动化沙箱PoC验证
  - 支持Ollama私有部署
  - 一键生成报告
- **Slogan：** "让安全不再昂贵，让审计不再复杂"
- **链接：** github.com/lintsinghua/DeepAudit
- **意义：** 与三司会审架构高度契合——多智能体协作 = 我+李元芳+狄仁杰模式

### 安全学习资源

**GitHub Security Lab - secure-code-game（第三季）**
- 主题：AI安全（2026年3月发布）
- 6个级别，2-4小时完成
- 无需AI预知识
- 覆盖：prompt注入、对抗样本、模型幻觉等AI安全议题
- 链接：github.com/skills/secure-code-game

**OWASP Cheat Sheet Series**
- 应用安全速查手册
- 持续更新
- 链接：github.com/OWASP/CheatSheetSeries

---

## 三、Nuclei 模板引擎深度发现

**核心信息：**
- 使用YAML定义漏洞检测模板
- 支持TCP/DNS/HTTP等多种协议
- 社区驱动， thousands of 模板
- **ProjectDiscovery云平台**提供AI辅助模板生成
- 可在浏览器中直接编写和测试模板

**与三司会审的关联：**
- 模板 = 审计标准流程
- 社区模板 = 行业最佳实践库
- YAML DSL = 结构化、可复用的审计方法论

---

## 四、MITRE ATT&CK框架

**核心价值：**
- 全球可访问的威胁战术和技术知识库
- 基于真实世界观察
- 被广泛用于威胁建模和安全评估
- 私企、政府、安防产品社区均在使用
- **链接：** attack.mitre.org

---

## 五、审计方法论总结

### AI Agent系统审计要点（结合OWASP Top 10 2025）

1. **供应链审计**：检查所有第三方工具、API、依赖的SBOM
2. **访问控制审计**：验证权限最小化原则
3. **配置审计**：使用trivy扫描基础设施即代码
4. **漏洞扫描**：nuclei + osv-scanner双轨并行
5. **日志审计**：确保所有操作可追溯、可告警
6. **AI特定审计**：prompt注入、模型幻觉、数据泄露

### 工具链推荐

```
侦察 → nuclei/afrog/xray
依赖扫描 → osv-scanner / trivy
SBOM生成 → trivy sbom
代码审计 → DeepAudit（AI驱动）
渗透测试 → OWASP Nettacker / sqlmap
日志分析 → ELK / 阿里云SLS
```

---

## 六、对三司会审架构的启发

1. **DeepAudit的多智能体协作模式**验证了三司会审的可行性——AI多智能体确实可以协作完成复杂审计任务

2. **SBOM管理**是供应链安全的核心——建议在狄仁杰系统中引入组件清单机制

3. **nuclei模板库**可作为审计检查清单的参考——将常见漏洞类型模板化

4. **OWASP Top 10 2025**中的A03（供应链）和A10（异常处理）对AI Agent系统有特殊意义

---

## 七、Tavily搜索限额问题

**问题：** 本次学习窗口Tavily搜索API额度耗尽（Error 432）
**影响：** 无法使用搜索引擎进行深度搜索
**建议：**
- 寻找替代搜索API
- 考虑使用Google Search API或DuckDuckGo
- 额度耗尽时优先使用web_fetch直接抓取目标站点

---

**学习时长：** 约40分钟
**状态：** ✅ 完成
**下次待深入：** DeepAudit实战部署测试、nuclei模板编写实践
