# -*- coding: utf-8 -*-
from docx import Document
import os

paths = [
    r'D:\倪海厦\2，人纪之《黄帝内经笔记【文字】》\倪海厦人纪教程简体整理稿之黄帝内经.docx',
    r'D:\倪海厦\6、倪海厦老师电子书全集（绝版珍藏）.doc\【05】倪海厦《医案》及推荐文档\【04】倪海厦临床医案\倪海厦08年医案959篇\4.倪海厦08年医案103篇\818.倪海厦08年医案.docx',
]

for i, fp in enumerate(paths):
    print(f'[{i}] Checking: {fp}')
    print(f'    Exists: {os.path.exists(fp)}')
    if os.path.exists(fp):
        try:
            doc = Document(fp)
            paras = [p.text for p in doc.paragraphs if p.text.strip()]
            content = '\n'.join(paras)
            print(f'    SUCCESS: {len(content)} chars')
            # Save first 5000 chars
            with open(rf'C:\Users\TL\.openclaw\workspace-main\content_{i}.txt', 'w', encoding='utf-8') as out:
                out.write(content[:5000])
        except Exception as e:
            print(f'    Error: {e}')
