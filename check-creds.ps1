Get-ChildItem 'C:\Users\TL\.openclaw\credentials' -File | Format-Table Name, LastWriteTime -AutoSize
Get-Content 'C:\Users\TL\.openclaw\credentials\deepseek-api.json' -ErrorAction SilentlyContinue
Get-Content 'C:\Users\TL\.openclaw\credentials\kimi-api.json' -ErrorAction SilentlyContinue
