# -*- coding: utf-8 -*-
from docx import Document

# The actual path bytes (GBK)
fp_bytes = b'D:\\xe6\\x97\\xa5\\xe6\\xb5\\xb7\\xe5\\x8d\\x8e\\x5c\\xe4\\xb8\\xad\\xe5\\x8c\\xbb\\xe5\\x8c\\xbb\\xe7\\x83\\xad\\xe8\\xaf\\x8a\\xe6\\x97\\xa5\\xe5\\x8d\\x8f\\xef\\xbc\\x88\\xe7\\x8f\\x8e\\xe8\\xb4\\xa5\\xe8\\xb5\\x84\\xe6\\x96\\x99\\xef\\xbc\\x89.doc\\xe6\\x97\\xa5\\xe6\\xb5\\xb7\\xe5\\x8d\\x8e\\xe6\\xb1\\x89\\xe5\\x94\\x90\\xe4\\xb8\\xad\\xe5\\x8d\\x8e\\xe7\\x99\\x96\\xe6\\xa1\\x88-\\xe5\\x88\\x86\\xe6\\x9d\\x82\\xe5\\x8c\\xbb\\xe7\\x96\\x91\\xe5\\xba\\x93\\xe7\\xae\\x97\\xef\\xbc\\x89\\xe5\\x80\\xaa\\xe6\\xb5\\xb7\\xe5\\x8d\\x8e36\\xe6\\x9d\\xa1\\xe7\\x9c\\x9f\\xe8\\x8a\\x82.doc'

# Decode as utf-8 to get the actual string
fp = fp_bytes.decode('utf-8')

# Check if file exists
import os
exists = os.path.exists(fp)
print(f'Path exists: {exists}')
print(f'Path: {fp}')

if exists:
    doc = Document(fp)
    paras = [p.text for p in doc.paragraphs if p.text.strip()]
    content = '\n'.join(paras)
    with open(r'C:\Users\TL\.openclaw\workspace-main\36zhenyan.txt', 'w', encoding='utf-8') as out:
        out.write(content)
    print(f'SUCCESS: Read {len(content)} chars')
else:
    # Try with GBK encoding
    fp_gbk = fp_bytes.decode('gbk', errors='replace')
    print(f'Trying GBK path: {fp_gbk}')
    exists2 = os.path.exists(fp_gbk)
    print(f'GBK path exists: {exists2}')
