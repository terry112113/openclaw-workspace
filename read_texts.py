# -*- coding: utf-8 -*-
import json
import os

with open(r'C:\Users\TL\.openclaw\workspace-main\file_index.json', 'r', encoding='utf-8') as f:
    files = json.load(f)

# Read each text file
for fp in files:
    if fp.endswith('.txt') and os.path.exists(fp):
        try:
            # Try utf-8 first
            with open(fp, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            try:
                with open(fp, 'r', encoding='gbk') as f:
                    content = f.read()
            except:
                continue
        
        fname = os.path.basename(fp)
        # Save to output
        safe_name = fname.replace('\\', '_').replace('/', '_').replace(':', '_')
        outpath = rf'C:\Users\TL\.openclaw\workspace-main\texts\{safe_name}'
        os.makedirs(r'C:\Users\TL\.openclaw\workspace-main\texts', exist_ok=True)
        with open(outpath, 'w', encoding='utf-8') as out:
            out.write(content)
        print(f'Saved: {fname} ({len(content)} chars)')
