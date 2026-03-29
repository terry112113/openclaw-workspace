import os
import json

skill_dirs = [
    r'C:\Users\TL\.openclaw\skills',
    r'C:\Users\TL\.openclaw\workspace-main\skills',
    r'C:\Users\TL\.openclaw\workspace-main\.agents\skills'
]

unique = {}
for base in skill_dirs:
    if os.path.exists(base):
        for d in os.listdir(base):
            full = os.path.join(base, d)
            if os.path.isdir(full):
                skill_md = os.path.join(full, 'SKILL.md')
                if os.path.exists(skill_md):
                    if d not in unique:
                        unique[d] = skill_md

def score_skill(name, content):
    """Score a skill on 6 dimensions: 高效/智能/深度/广度/博学/自觉进化, each 1-5"""
    c = content.lower()
    wc = len(content.split())
    
    # 1. 高效 (Efficiency) - brevity, clear steps, actionable
    eff = 1
    if wc < 50: eff = 2
    if wc >= 50 and wc < 150: eff = 3
    if wc >= 150 and wc < 400: eff = 4
    if wc >= 400: eff = 5
    if 'step' in c or '流程' in content or '步骤' in content: eff = min(5, eff+1)
    if 'error' in c or 'exception' in c or 'bug' in c: eff = min(5, eff+1)
    if 'retry' in c or 'timeout' in c: eff = min(5, eff+1)
    
    # 2. 智能 (Intelligence) - uses AI APIs, LLM, ML concepts
    intel = 1
    ai_keywords = ['llm', 'gpt', 'openai', 'claude', 'gemini', 'ai model', 'embedding', 
                   'rag', 'retrieval', 'chain', 'agent', 'langchain', 'vector',
                   'nlp', 'nlu', 'chatgpt', 'deepseek', 'qwen', 'mistral', 'ragas']
    for kw in ai_keywords:
        if kw in c:
            intel += 1
    intel = min(5, intel)
    
    # 3. 深度 (Depth) - detail, edge cases, advanced topics
    depth = 1
    if wc >= 200: depth = 2
    if wc >= 400: depth = 3
    if wc >= 800: depth = 4
    if wc >= 1500: depth = 5
    deep_keywords = ['advanced', '深入', '底层', '原理', 'architecture', 'design pattern',
                     'optimization', 'benchmark', 'performance', 'scalability', 'production']
    for kw in deep_keywords:
        if kw in c:
            depth = min(5, depth+1)
    if 'example' in c and ('```' in c or 'code' in c): depth = min(5, depth+1)
    
    # 4. 广度 (Breadth) - multiple tools, integrations, cross-domain
    breadth = 1
    integration_keywords = ['api', 'integration', 'webhook', 'cli', 'sdk', 'http', 
                            'database', 'postgresql', 'mysql', 'mongodb', 'redis',
                            'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'k8s',
                            'github', 'slack', 'discord', 'telegram', 'feishu']
    count = sum(1 for kw in integration_keywords if kw in c)
    if count >= 1: breadth = 2
    if count >= 3: breadth = 3
    if count >= 5: breadth = 4
    if count >= 8: breadth = 5
    if 'multi' in c or 'cross' in c or 'heterogeneous' in c: breadth = min(5, breadth+1)
    
    # 5. 博学 (Knowledge) - broad domain coverage
    know = 1
    if wc >= 100: know = 2
    if wc >= 300: know = 3
    if wc >= 600: know = 4
    if wc >= 1200: know = 5
    domain_keywords = ['finance', '医疗', '法律', '教育', '医疗', 'biomedical', 
                       '学术', 'research', 'science', 'data science', 'mlops',
                       'blockchain', 'crypto', 'security', 'audit', 'compliance']
    for kw in domain_keywords:
        if kw in c:
            know = min(5, know+1)
    
    # 6. 自觉进化 (Self-evolution) - self-improvement, meta-cognition
    evo = 1
    evo_keywords = ['self-improv', 'reflect', 'learn from', 'feedback loop', 'iterate',
                     'evolution', 'improve', 'benchmark', 'metrics', 'monitor',
                     'root cause', 'debug', 'self-corr', 'auto-adjust', '自适应']
    for kw in evo_keywords:
        if kw in c:
            evo += 1
    evo = min(5, evo)
    if 'monitor' in c or 'observability' in c: evo = min(5, evo+1)
    
    # Bonus/penalty
    # Penalize very generic names with thin content
    if wc < 30: eff = max(1, eff-2); intel = max(1, intel-2)
    # Penalize duplicate-like names
    if name.count('-') >= 3: pass  # No penalty for complex names
    
    total = eff + intel + depth + breadth + know + evo
    
    # Determine elimination reason
    reasons = []
    if total <= 12:
        reasons.append('内容单薄/过短')
    if intel <= 1:
        reasons.append('无AI智能特性')
    if depth <= 1 and wc < 200:
        reasons.append('缺乏深度')
    if breadth <= 1 and know <= 1:
        reasons.append('覆盖过窄')
    if evo <= 1:
        reasons.append('无自我进化机制')
    if wc < 50:
        reasons.append('内容严重不足')
    
    reason = '; '.join(reasons) if reasons else '综合评分低'
    
    # Core advantage for kept skills
    advantages = []
    if eff >= 4: advantages.append('高效')
    if intel >= 4: advantages.append('智能')
    if depth >= 4: advantages.append('深度')
    if breadth >= 4: advantages.append('广度')
    if know >= 4: advantages.append('博学')
    if evo >= 4: advantages.append('自觉进化')
    advantage = '/'.join(advantages) if advantages else '均衡'
    
    return {
        'name': name,
        'path': unique[name],
        'word_count': wc,
        '高效': eff,
        '智能': intel,
        '深度': depth,
        '广度': breadth,
        '博学': know,
        '自觉进化': evo,
        'total': total,
        'reason': reason,
        'advantage': advantage
    }

results = []
for name, path in sorted(unique.items()):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    score = score_skill(name, content)
    results.append(score)

# Sort by total score ascending
results.sort(key=lambda x: x['total'])

# Output full ranking
output_lines = []
output_lines.append(f'{"排名":<4} {"名称":<50} {"高效":<4} {"智能":<4} {"深度":<4} {"广度":<4} {"博学":<4} {"进化":<4} {"总分":<4} {"字数":<6} {"路径"}')
output_lines.append('-' * 140)
for i, r in enumerate(results):
    output_lines.append(f'{i+1:<4} {r["name"]:<50} {r["高效"]:<4} {r["智能"]:<4} {r["深度"]:<4} {r["广度"]:<4} {r["博学"]:<4} {r["自觉进化"]:<4} {r["total"]:<4} {r["word_count"]:<6} {r["path"]}')

output_lines.append('')
output_lines.append('=== 淘汰名单（总分最低20个）===')
for i, r in enumerate(results[:20]):
    output_lines.append(f'{i+1}. {r["name"]} (总分={r["total"]}, 高效={r["高效"]} 智能={r["智能"]} 深度={r["深度"]} 广度={r["广度"]} 博学={r["博学"]} 进化={r["自觉进化"]}) - {r["reason"]}')

output_lines.append('')
output_lines.append('=== 保留名单亮点（前20高分）===')
for i, r in enumerate(results[-20:][::-1]):
    output_lines.append(f'{i+1}. {r["name"]} (总分={r["total"]}) - {r["advantage"]}')

# Save to JSON for programmatic use
with open(r'C:\Users\TL\.openclaw\workspace-main\skills_ranking.json', 'w', encoding='utf-8') as f:
    # Don't save paths to avoid bloat
    safe_results = [{k: v for k, v in r.items() if k != 'path'} for r in results]
    json.dump(safe_results, f, ensure_ascii=False, indent=2)

# Save to text
with open(r'C:\Users\TL\.openclaw\workspace-main\skills_ranking.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output_lines))

print(f'Processed {len(results)} skills')
print(f'Bottom 20: {[r["name"] for r in results[:20]]}')
print(f'Top 20: {[r["name"] for r in results[-20:][::-1]]}')
print('Done. Files written.')
