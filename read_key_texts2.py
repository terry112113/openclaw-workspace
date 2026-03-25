# -*- coding: utf-8 -*-
import os
import json

texts_dir = r'C:\Users\TL\.openclaw\workspace-main\texts'
os.makedirs(texts_dir, exist_ok=True)

# Read the file index
with open(r'C:\Users\TL\.openclaw\workspace-main\file_index.json', 'r', encoding='utf-8') as f:
    all_files = json.load(f)

# Only .txt files
txt_files = [fp for fp in all_files if fp.endswith('.txt')]

# Read each file with GBK and save to texts dir
for fp in txt_files:
    fname = os.path.basename(fp)
    safe_fname = ''.join(c if c.isalnum() or c in '._-（）()' else '_' for c in fname)
    
    try:
        with open(fp, 'r', encoding='gbk', errors='replace') as f:
            content = f.read()
        
        outpath = os.path.join(texts_dir, safe_fname)
        with open(outpath, 'w', encoding='utf-8') as out:
            out.write(content)
        print(f'OK: {fname} -> {safe_fname} ({len(content)} chars)')
    except Exception as e:
        print(f'ERR: {fname}: {e}')
