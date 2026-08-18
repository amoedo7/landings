param([Parameter(Mandatory=$true,Position=0)][string]$File)
$schema = "desarrollamo.file-integrity.v1"
try {
  $item = Get-Item -LiteralPath $File -ErrorAction Stop
  if ($item.PSIsContainer) { throw "Path is not a file: $File" }
  $hash = (Get-FileHash -LiteralPath $item.FullName -Algorithm SHA256).Hash.ToLowerInvariant()
  [ordered]@{
    schema = $schema
    file = $item.Name
    bytes = [int64]$item.Length
    sha256 = $hash
    checked_at = [DateTime]::UtcNow.ToString("yyyy-MM-ddTHH:mm:ssZ")
  } | ConvertTo-Json -Compress
  exit 0
} catch {
  [ordered]@{schema=$schema;ok=$false;error=$_.Exception.Message} | ConvertTo-Json -Compress | Write-Error
  exit 1
}
