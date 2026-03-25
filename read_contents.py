# -*- coding: utf-8 -*-
import os
import json

texts_dir = r'C:\Users\TL\.openclaw\workspace-main\texts'
files = os.listdir(texts_dir)

# Sort by size descending
files_sorted = sorted(files, key=lambda x: os.path.getsize(os.path.join(texts_dir, x)), reverse=True)

# Read first 500 chars of each top file
for fname in files_sorted[:5]:
    fp = os.path.join(texts_dir, fname)
    with open(fp, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    print(f'=== {fname} ({len(content)} chars) ===')
    print(content[:500])
    print()
