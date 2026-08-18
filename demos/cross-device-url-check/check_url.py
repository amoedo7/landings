#!/usr/bin/env python3
import json
import sys
import time
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

url = sys.argv[1] if len(sys.argv) > 1 else "https://desarrollamo.com.ar"
started = time.perf_counter()
status = 0
ok = False

try:
    request = Request(url, method="HEAD", headers={"User-Agent": "DesarrollAMO-URL-Check/1.0"})
    with urlopen(request, timeout=15) as response:
        status = int(response.status)
        ok = 200 <= status < 400
except HTTPError as exc:
    status = int(exc.code)
except URLError:
    pass

elapsed_ms = int((time.perf_counter() - started) * 1000)

print(json.dumps({
    "schema": "desarrollamo.url-check.v1",
    "url": url,
    "status": status,
    "ok": ok,
    "elapsed_ms": elapsed_ms,
    "checked_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
}, separators=(",", ":")))
