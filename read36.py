# -*- coding: utf-8 -*-
from docx import Document
import os

# Read path from file
with open(r'C:\Users\TL\.openclaw\workspace-main\fp1.txt', 'r', encoding='utf-8') as f:
    fp = f.read().strip()

print(f'Path: {fp}')
print(f'Exists: {os.path.exists(fp)}')

if os.path.exists(fp):
    try:
        doc = Document(fp)
        paras = [p.text for p in doc.paragraphs if p.text.strip()]
        content = '\n'.join(paras)
        with open(r'C:\Users\TL\.openclaw\workspace-main\36zhenyan.txt', 'w', encoding='utf-8') as out:
            out.write(content)
        print(f'SUCCESS: Read {len(content)} chars')
        print(content[:1000])
    except Exception as e:
        print(f'Error: {e}')
