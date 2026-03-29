import os
import re

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

print(f'Total unique skills with SKILL.md: {len(unique)}')
for k, v in sorted(unique.items()):
    print(f'{k}||{v}')
