# -*- coding: utf-8 -*-
import os
import json

texts_dir = r'C:\Users\TL\.openclaw\workspace-main\texts'

# Read the file index
with open(r'C:\Users\TL\.openclaw\workspace-main\file_index.json', 'r', encoding='utf-8') as f:
    all_files = json.load(f)

# Only .txt files
txt_files = [fp for fp in all_files if fp.endswith('.txt')]

print(f'Total .txt files: {len(txt_files)}')

# For each file, read with GBK and display content preview
for fp in txt_files:
    try:
        with open(fp, 'r', encoding='gbk', errors='replace') as f:
            content = f.read()
        fname = os.path.basename(fp)
        print(f'\n=== {fname} ({len(content)} chars) ===')
        print(content[:2000])
        print('...')
    except Exception as e:
        print(f'Error reading {fp}: {e}')
