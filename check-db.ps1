[System.Reflection.Assembly]::LoadFile('C:\Windows\System32\System.Data.SQLite.dll') | Out-Null
$conn = New-Object System.Data.SQLite.SQLiteConnection('Data Source=C:\Users\TL\.openclaw\openclaw.db')
$conn.Open()
$cmd = $conn.CreateCommand()
$cmd.CommandText = "SELECT name FROM sqlite_master WHERE type='table'"
$reader = $cmd.ExecuteReader()
while ($reader.Read()) { Write-Host $reader[0] }
$conn.Close()
