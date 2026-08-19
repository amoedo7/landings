#!/usr/bin/env python3
"""MiDispositivo — diagnóstico local, portable y explícito.

Por defecto no realiza solicitudes de red. Usa --online para añadir IP pública,
ubicación aproximada por IP, ASN y proveedor de red.
"""

from __future__ import annotations

import argparse
import ctypes
import datetime as dt
import json
import os
import platform
import shutil
import socket
import subprocess
import sys
import urllib.request
from pathlib import Path

SCHEMA = "desarrollamo.midispositivo.v1"


def run(cmd: list[str], timeout: float = 2.5) -> str:
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, check=False)
        return (p.stdout or "").strip()
    except Exception:
        return ""


def first_nonempty(*values):
    for value in values:
        if value:
            return value
    return None


def cpu_model() -> str | None:
    system = platform.system()
    if system == "Linux":
        try:
            for line in Path("/proc/cpuinfo").read_text(errors="ignore").splitlines():
                if line.lower().startswith(("model name", "hardware")) and ":" in line:
                    return line.split(":", 1)[1].strip()
        except Exception:
            pass
    elif system == "Darwin":
        return first_nonempty(run(["sysctl", "-n", "machdep.cpu.brand_string"]), platform.processor())
    elif system == "Windows":
        return first_nonempty(
            run(["powershell", "-NoProfile", "-Command", "(Get-CimInstance Win32_Processor | Select-Object -First 1 -ExpandProperty Name)"]),
            platform.processor(),
        )
    return platform.processor() or None


def memory_bytes() -> tuple[int | None, int | None]:
    system = platform.system()
    if system == "Linux":
        data = {}
        try:
            for line in Path("/proc/meminfo").read_text().splitlines():
                key, value = line.split(":", 1)
                data[key] = int(value.strip().split()[0]) * 1024
            return data.get("MemTotal"), data.get("MemAvailable")
        except Exception:
            return None, None
    if system == "Darwin":
        total = run(["sysctl", "-n", "hw.memsize"])
        return (int(total) if total.isdigit() else None), None
    if system == "Windows":
        class MEMORYSTATUSEX(ctypes.Structure):
            _fields_ = [
                ("dwLength", ctypes.c_ulong), ("dwMemoryLoad", ctypes.c_ulong),
                ("ullTotalPhys", ctypes.c_ulonglong), ("ullAvailPhys", ctypes.c_ulonglong),
                ("ullTotalPageFile", ctypes.c_ulonglong), ("ullAvailPageFile", ctypes.c_ulonglong),
                ("ullTotalVirtual", ctypes.c_ulonglong), ("ullAvailVirtual", ctypes.c_ulonglong),
                ("ullAvailExtendedVirtual", ctypes.c_ulonglong),
            ]
        try:
            status = MEMORYSTATUSEX()
            status.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
            ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(status))
            return int(status.ullTotalPhys), int(status.ullAvailPhys)
        except Exception:
            return None, None
    return None, None


def disk_info() -> dict:
    try:
        root = Path.home().anchor or "/"
        usage = shutil.disk_usage(root)
        return {"root": root, "total_bytes": usage.total, "free_bytes": usage.free}
    except Exception:
        return {"root": None, "total_bytes": None, "free_bytes": None}


def local_ip() -> str | None:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except Exception:
        try:
            return socket.gethostbyname(socket.gethostname())
        except Exception:
            return None
    finally:
        s.close()


def gateway() -> str | None:
    system = platform.system()
    if system == "Linux":
        out = run(["ip", "route", "show", "default"])
        parts = out.split()
        if "via" in parts:
            i = parts.index("via")
            if i + 1 < len(parts):
                return parts[i + 1]
    elif system == "Darwin":
        out = run(["route", "-n", "get", "default"])
        for line in out.splitlines():
            if "gateway:" in line:
                return line.split("gateway:", 1)[1].strip()
    elif system == "Windows":
        out = run(["powershell", "-NoProfile", "-Command", "(Get-NetRoute -DestinationPrefix '0.0.0.0/0' | Sort-Object RouteMetric | Select-Object -First 1 -ExpandProperty NextHop)"])
        return out or None
    return None


def dns_servers() -> list[str]:
    system = platform.system()
    found: list[str] = []
    if system == "Windows":
        out = run(["powershell", "-NoProfile", "-Command", "(Get-DnsClientServerAddress -AddressFamily IPv4).ServerAddresses -join '\n'"])
        found = [x.strip() for x in out.splitlines() if x.strip()]
    elif system == "Darwin":
        out = run(["scutil", "--dns"])
        for line in out.splitlines():
            if "nameserver[" in line and ":" in line:
                found.append(line.split(":", 1)[1].strip())
    else:
        try:
            for line in Path("/etc/resolv.conf").read_text(errors="ignore").splitlines():
                if line.startswith("nameserver "):
                    found.append(line.split()[1])
        except Exception:
            pass
    return list(dict.fromkeys(found))[:6]


def online_info(timeout: float = 5.0) -> dict:
    req = urllib.request.Request(
        "https://ipapi.co/json/",
        headers={"User-Agent": "MiDispositivo/1.0 (+https://github.com/amoedo7)"},
    )
    started = dt.datetime.now(dt.timezone.utc)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = json.loads(r.read().decode("utf-8", errors="replace"))
        elapsed = int((dt.datetime.now(dt.timezone.utc) - started).total_seconds() * 1000)
        lat = raw.get("latitude")
        lon = raw.get("longitude")
        return {
            "enabled": True,
            "ok": True,
            "public_ip": raw.get("ip"),
            "provider": raw.get("org"),
            "asn": raw.get("asn"),
            "location": {
                "city": raw.get("city"),
                "region": raw.get("region"),
                "country": raw.get("country_name"),
                "timezone": raw.get("timezone"),
                "latitude_approx": round(float(lat), 2) if lat is not None else None,
                "longitude_approx": round(float(lon), 2) if lon is not None else None,
                "method": "public-IP geolocation (approximate)",
            },
            "lookup_ms": elapsed,
        }
    except Exception as exc:
        return {"enabled": True, "ok": False, "error": exc.__class__.__name__}


def build_report(include_online: bool) -> dict:
    total_mem, free_mem = memory_bytes()
    uname = platform.uname()
    report = {
        "schema": SCHEMA,
        "generated_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
        "privacy": {
            "online_lookup_requested": include_online,
            "mac_addresses_collected": False,
            "wifi_ssid_collected": False,
            "exact_gps_collected": False,
        },
        "device": {
            "hostname": socket.gethostname(),
            "os": uname.system,
            "os_release": uname.release,
            "os_version": uname.version,
            "architecture": uname.machine,
            "cpu": cpu_model(),
            "logical_cores": os.cpu_count(),
            "memory_total_bytes": total_mem,
            "memory_available_bytes": free_mem,
            "disk": disk_info(),
            "python": platform.python_version(),
        },
        "network": {
            "local_ip": local_ip(),
            "default_gateway": gateway(),
            "dns_servers": dns_servers(),
        },
        "online": online_info() if include_online else {"enabled": False},
    }
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description="MiDispositivo: diagnóstico local y portable")
    parser.add_argument("--online", action="store_true", help="añade IP pública y ubicación aproximada por IP")
    parser.add_argument("--output", help="guarda también el JSON en un archivo")
    parser.add_argument("--compact", action="store_true", help="JSON en una sola línea")
    args = parser.parse_args()

    report = build_report(args.online)
    text = json.dumps(report, ensure_ascii=False, indent=None if args.compact else 2)
    print(text)
    if args.output:
        Path(args.output).write_text(text + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
