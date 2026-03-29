$file = "C:\Users\TL\.openclaw\workspace-main\knowledge\李元芳\全天学习方案-2026-03-29.md"
$content = Get-Content $file -Encoding UTF8 -Raw
$content = $content -replace "圣子-深度研究", "李元芳-深度研究"
[System.IO.File]::WriteAllText($file, $content, [System.Text.Encoding]::UTF8)
Write-Host "Done"
