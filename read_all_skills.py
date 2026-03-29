import os

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

output = []
for name, path in sorted(unique.items()):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    output.append(f'=== {name} ===\n{content}\n')

with open(r'C:\Users\TL\.openclaw\workspace-main\all_skills_content.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output))

print(f'Written {len(output)} skills to all_skills_content.txt')
