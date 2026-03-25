# -*- coding: utf-8 -*-
import os
texts_dir = r'C:\Users\TL\.openclaw\workspace-main\texts'
if os.path.exists(texts_dir):
    files = os.listdir(texts_dir)
    print(f'Total files in texts: {len(files)}')
    for f in sorted(files, key=lambda x: os.path.getsize(os.path.join(texts_dir, x)), reverse=True)[:10]:
        fp = os.path.join(texts_dir, f)
        size = os.path.getsize(fp)
        with open(fp, 'r', encoding='utf-8', errors='replace') as fi:
            content = fi.read()
        print(f'\n{size:>8}  {f[:50]}')
        print(content[:500])
else:
    print(f'Dir not found: {texts_dir}')
