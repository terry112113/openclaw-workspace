# -*- coding: utf-8 -*-
import os

# Read path from file
with open(r'C:\Users\TL\.openclaw\workspace-main\fp1.txt', 'r', encoding='utf-8') as f:
    fp = f.read().strip()

print(f'Path from file: {fp!r}')
print(f'Path exists: {os.path.exists(fp)}')

# If not exists, list parent dir
parent = os.path.dirname(fp)
print(f'Parent: {parent!r}')
if os.path.exists(parent):
    print('Parent exists, contents:')
    for item in os.listdir(parent):
        print(f'  {item!r}')
else:
    print('Parent does not exist')
    # Try to find by walking from a known base
    base = r'D:\倪海厦'
    if os.path.exists(base):
        print(f'Base exists: {base}')
        for root, dirs, files in os.walk(base):
            for f in files:
                full = os.path.join(root, f)
                if '36' in f and '真言' in f:
                    print(f'FOUND: {full!r}')
                    break
