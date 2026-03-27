Get-ChildItem 'C:\Users\TL\.openclaw' -Recurse -File -EA SilentlyContinue | Where-Object { $_.DirectoryName -notmatch 'sessions|logs' } | Select-Object -First 50 | ForEach-Object { 
    try { 
        $c = [System.IO.File]::ReadAllText($_.FullName)
        if ($c -match 'f922') { Write-Host ('FOUND: ' + $_.FullName); Write-Host ($c -split "`n" | Where-Object { $_ -match 'f922' } | Select-Object -First 1) }
    } catch {}
}
Write-Host 'Search done'
