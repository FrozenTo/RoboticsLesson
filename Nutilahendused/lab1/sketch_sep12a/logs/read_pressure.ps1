param([string]$Port, [string]$OutFile)
$serial = [System.IO.Ports.SerialPort]::new($Port, 115200, [System.IO.Ports.Parity]::None, 8, [System.IO.Ports.StopBits]::One)
$serial.DtrEnable = $false
$serial.RtsEnable = $false
$serial.ReadTimeout = 2000
[System.IO.File]::WriteAllText($OutFile, "# timestamp`tserial_output`n")
$serial.Open()
try {
  while ($true) {
    try {
      $line = $serial.ReadLine().TrimEnd("`r")
      $entry = (Get-Date -Format 'yyyy-MM-ddTHH:mm:ss.fff') + "`t" + $line
      [System.IO.File]::AppendAllText($OutFile, $entry + "`n")
    } catch [System.TimeoutException] {}
  }
} finally { $serial.Close() }
