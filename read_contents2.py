# -*- coding: utf-8 -*-
import os
import json

texts_dir = r'C:\Users\TL\.openclaw\workspace-main\texts'

# Read the file index
with open(r'C:\Users\TL\.openclaw\workspace-main\file_index.json', 'r', encoding='utf-8') as f:
    all_files = json.load(f)

# Filter only .txt files that exist
txt_files = [fp for fp in all_files if fp.endswith('.txt')]

print(f'Total .txt files: {len(txt_files)}')

# Read and display first 1000 chars of each (properly decoded)
for fp in txt_files[:15]:
    fname = os.path.basename(fp)
    try:
        # Try GBK first (most Chinese text files)
        with open(fp, 'r', encoding='gbk', errors='replace') as f:
            content = f.read()
        encoding_used = 'gbk'
    except:
        try:
            with open(fp, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
            encoding_used = 'utf-8'
        except:
            content = '[UNREADABLE]'
            encoding_used = 'none'
    
    print(f'\n=== {fname} ({encoding_used}, {len(content)} chars) ===')
    print(content[:1000])
