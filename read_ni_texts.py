# -*- coding: utf-8 -*-
import os
import json

# Read the file index
with open(r'C:\Users\TL\.openclaw\workspace-main\file_index.json', 'r', encoding='utf-8') as f:
    all_files = json.load(f)

# Find the key 倪海厦 files
ni_files = [fp for fp in all_files if any(k in fp for k in ['倪海厦', '伤寒', '气化', '度量衡', '辨证', '秘方']) and fp.endswith('.txt')]

print(f'Found {len(ni_files)} key files')
for fp in ni_files:
    fname = os.path.basename(fp)
    try:
        with open(fp, 'r', encoding='gbk', errors='replace') as f:
            content = f.read()
        # Save to texts dir
        safe_name = 'key_' + str(ni_files.index(fp)).zfill(3) + '_' + fname[:30]
        outpath = rf'C:\Users\TL\.openclaw\workspace-main\key_texts\{safe_name}'
        os.makedirs(r'C:\Users\TL\.openclaw\workspace-main\key_texts', exist_ok=True)
        with open(outpath, 'w', encoding='utf-8') as out:
            out.write(content)
        print(f'Saved: {fname} ({len(content)} chars)')
    except Exception as e:
        print(f'Error: {fname}: {e}')
