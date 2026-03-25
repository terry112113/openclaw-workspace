# -*- coding: utf-8 -*-
import os
import json

with open(r'C:\Users\TL\.openclaw\workspace-main\file_index.json', 'r', encoding='utf-8') as f:
    all_files = json.load(f)

# Find files containing '气化' or '度量衡'
key_files = [fp for fp in all_files if any(k in os.path.basename(fp) for k in ['气化', '度量衡', '真言', '医案']) and fp.endswith('.txt')]

print(f'Key files found: {len(key_files)}')
for fp in key_files[:5]:
    print(f'\nFile: {fp}')
    try:
        with open(fp, 'r', encoding='gbk', errors='replace') as f:
            content = f.read()
        print(f'Content ({len(content)} chars):')
        print(content[:3000])
    except Exception as e:
        print(f'Error: {e}')
