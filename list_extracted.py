# -*- coding: utf-8 -*-
import os
extracted_dir = r'C:\Users\TL\.openclaw\workspace-main\extracted'
if os.path.exists(extracted_dir):
    files = os.listdir(extracted_dir)
    print(f'Total extracted files: {len(files)}')
    for f in sorted(files):
        fp = os.path.join(extracted_dir, f)
        size = os.path.getsize(fp)
        print(f'{size:>8}  {f}')
else:
    print(f'Directory not found: {extracted_dir}')
    # List all directories in workspace
    base = r'C:\Users\TL\.openclaw\workspace-main'
    for item in os.listdir(base):
        print(f'  {item}')
