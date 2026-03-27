$items = Get-ChildItem 'C:\Users\TL\.openclaw' | Where-Object { $_.Name -notin 'sessions','logs' }
$dest = 'D:\openclaw-backup-2026-03-27-20-07.zip'
Compress-Archive -Path $items.FullName -DestinationPath $dest -Force
Get-Item $dest | Select-Object Name, Length
