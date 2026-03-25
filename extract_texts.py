# -*- coding: utf-8 -*-
import os
import json

# Read the file index
with open(r'C:\Users\TL\.openclaw\workspace-main\file_index.json', 'r', encoding='utf-8') as f:
    all_files = json.load(f)

# Only .txt files
txt_files = [fp for fp in all_files if fp.endswith('.txt')]

# Read each file and save with index number
os.makedirs(r'C:\Users\TL\.openclaw\workspace-main\extracted', exist_ok=True)

for i, fp in enumerate(txt_files):
    try:
        with open(fp, 'r', encoding='gbk', errors='replace') as f:
            content = f.read()
        
        # Save with index number
        outpath = rf'C:\Users\TL\.openclaw\workspace-main\extracted\{i:03d}.txt'
        with open(outpath, 'w', encoding='utf-8') as out:
            out.write(content)
        
        # Print first 200 chars
        fname = os.path.basename(fp)
        print(f'[{i:03d}] {fname[:40]} -> {len(content)} chars')
        print(content[:300])
        print('---')
    except Exception as e:
        print(f'[{i:03d}] ERROR: {e}')
