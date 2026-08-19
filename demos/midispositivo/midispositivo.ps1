param(
  [switch]$Online,
  [string]$Output
)

$ErrorActionPreference = 'SilentlyContinue'

function First-IPv4 {
  $ip = Get-NetIPAddress -AddressFamily IPv4 |
    Where-Object { $_.IPAddress -notlike '127.*' -and $_.PrefixOrigin -ne 'WellKnown' } |
    Sort-Object InterfaceMetric |
    Select-Object -First 1 -ExpandProperty IPAddress
  return $ip
}

$os = Get-CimInstance Win32_OperatingSystem
$cpu = Get-CimInstance Win32_Processor | Select-Object -First 1
$disk = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='C:'"
$gateway = Get-NetRoute -DestinationPrefix '0.0.0.0/0' |
  Sort-Object RouteMetric |
  Select-Object -First 1 -ExpandProperty NextHop
$dns = @((Get-DnsClientServerAddress -AddressFamily IPv4).ServerAddresses | Where-Object { $_ }) | Select-Object -Unique

$onlineBlock = [ordered]@{ enabled = $false }
if ($Online) {
  try {
    $sw = [System.Diagnostics.Stopwatch]::StartNew()
    $geo = Invoke-RestMethod -Uri 'https://ipapi.co/json/' -TimeoutSec 5 -Headers @{ 'User-Agent' = 'MiDispositivo/1.0 (+https://github.com/amoedo7)' }
    $sw.Stop()
    $onlineBlock = [ordered]@{
      enabled = $true
      ok = $true
      public_ip = $geo.ip
      provider = $geo.org
      asn = $geo.asn
      location = [ordered]@{
        city = $geo.city
        region = $geo.region
        country = $geo.country_name
        timezone = $geo.timezone
        latitude_approx = if ($null -ne $geo.latitude) { [math]::Round([double]$geo.latitude, 2) } else { $null }
        longitude_approx = if ($null -ne $geo.longitude) { [math]::Round([double]$geo.longitude, 2) } else { $null }
        method = 'public-IP geolocation (approximate)'
      }
      lookup_ms = $sw.ElapsedMilliseconds
    }
  } catch {
    $onlineBlock = [ordered]@{ enabled = $true; ok = $false; error = $_.Exception.GetType().Name }
  }
}

$report = [ordered]@{
  schema = 'desarrollamo.midispositivo.v1'
  generated_at = (Get-Date).ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ')
  privacy = [ordered]@{
    online_lookup_requested = [bool]$Online
    mac_addresses_collected = $false
    wifi_ssid_collected = $false
    exact_gps_collected = $false
  }
  device = [ordered]@{
    hostname = $env:COMPUTERNAME
    os = 'Windows'
    os_release = $os.Caption
    os_version = $os.Version
    architecture = $env:PROCESSOR_ARCHITECTURE
    cpu = $cpu.Name
    logical_cores = $cpu.NumberOfLogicalProcessors
    memory_total_bytes = [int64]$os.TotalVisibleMemorySize * 1024
    memory_available_bytes = [int64]$os.FreePhysicalMemory * 1024
    disk = [ordered]@{
      root = 'C:\'
      total_bytes = [int64]$disk.Size
      free_bytes = [int64]$disk.FreeSpace
    }
    powershell = $PSVersionTable.PSVersion.ToString()
  }
  network = [ordered]@{
    local_ip = First-IPv4
    default_gateway = $gateway
    dns_servers = @($dns | Select-Object -First 6)
  }
  online = $onlineBlock
}

$json = $report | ConvertTo-Json -Depth 8
$json
if ($Output) {
  $json | Set-Content -Encoding UTF8 $Output
}
