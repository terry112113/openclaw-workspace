Get-ChildItem -Path "D:\倪海厦" -Recurse | Measure-Object -Property Length -Sum | ForEach-Object {
    Write-Host "Total Files: $($_.Count)"
    Write-Host "Total Size (GB): $([math]::Round($_.Sum/1GB, 2))"
    Write-Host "Total Size (MB): $([math]::Round($_.Sum/1MB, 2))"
}
