param([string]$filepath, [string]$searchPattern = $null)
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
try {
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    $doc = $word.Documents.Open($filepath)
    $text = $doc.Content.Text
    $doc.Close($false)
    $word.Quit()
    if ($searchPattern) {
        $lines = $text -split "`n"
        $matches = $lines | Select-String -Pattern $searchPattern | Select-Object -First 80
        foreach ($m in $matches) {
            Write-Output "$($m.LineNumber): $($m.Line)"
        }
    } else {
        Write-Output $text
    }
} catch {
    Write-Output "ERROR: $_"
}
