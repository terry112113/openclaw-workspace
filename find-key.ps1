$content = [System.IO.File]::ReadAllText('C:\Users\TL\.openclaw\openclaw.json')
if ($content -match '(deepseek[^}]+?apiKey[^,]+)') { Write-Host $Matches[1] }
$content.Substring([Math]::Max(0, $content.IndexOf('deepseek') - 1), 500) | Out-String | Write-Host
