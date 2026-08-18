param(
  [string]$Url = "https://desarrollamo.com.ar"
)

$watch = [System.Diagnostics.Stopwatch]::StartNew()
$status = 0
$ok = $false

try {
  $response = Invoke-WebRequest -Uri $Url -Method Head -MaximumRedirection 5 -TimeoutSec 15 -UseBasicParsing
  $status = [int]$response.StatusCode
  $ok = ($status -ge 200 -and $status -lt 400)
}
catch {
  if ($_.Exception.Response -and $_.Exception.Response.StatusCode) {
    $status = [int]$_.Exception.Response.StatusCode
  }
}
finally {
  $watch.Stop()
}

[ordered]@{
  schema = "desarrollamo.url-check.v1"
  url = $Url
  status = $status
  ok = $ok
  elapsed_ms = [int]$watch.ElapsedMilliseconds
  checked_at = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
} | ConvertTo-Json -Compress
