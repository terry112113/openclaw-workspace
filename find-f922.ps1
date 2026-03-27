$files = Get-ChildItem 'C:\Users\TL\.openclaw' -Recurse -File -EA SilentlyContinue | Where-Object { $_.DirectoryName -notmatch 'sessions|logs' }
$results = @()
foreach ($f in $files) {
    try {
        $content = [System.IO.File]::ReadAllText($f.FullName)
        if ($content -match 'f922') {
            $results += @{ File=$f.FullName; Line=($content -split "`n" | Where-Object { $_ -match 'f922' } | Select-Object -First 1) }
        }
    } catch {}
}
$results | Format-Table -AutoSize
