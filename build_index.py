# -*- coding: utf-8 -*-
import os
import json

base = r'D:\倪海厦'
index = []

for root, dirs, files in os.walk(base):
    for f in files:
        if f.endswith(('.docx', '.txt')):
            fp = os.path.join(root, f)
            index.append(fp)

with open(r'C:\Users\TL\.openclaw\workspace-main\file_index.json', 'w', encoding='utf-8') as out:
    json.dump(index, out, ensure_ascii=False, indent=2)

print(f'Indexed {len(index)} files')
