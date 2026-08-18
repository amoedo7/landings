#!/usr/bin/env bash
set -u

URL="${1:-https://desarrollamo.com.ar}"
RESULT="$(curl -L -sS -o /dev/null -w '%{http_code} %{time_total}' --max-time 15 "$URL" 2>/dev/null || true)"
STATUS="${RESULT%% *}"
SECONDS="${RESULT#* }"

if [ -z "$STATUS" ] || [ "$STATUS" = "$RESULT" ]; then
  STATUS="000"
  SECONDS="0"
fi

ELAPSED_MS="$(awk -v s="$SECONDS" 'BEGIN { printf "%d", s * 1000 }')"
if [ "$STATUS" -ge 200 ] 2>/dev/null && [ "$STATUS" -lt 400 ] 2>/dev/null; then
  OK=true
else
  OK=false
fi

printf '{"schema":"desarrollamo.url-check.v1","url":"%s","status":%s,"ok":%s,"elapsed_ms":%s,"checked_at":"%s"}\n' \
  "$URL" "${STATUS#0}" "$OK" "$ELAPSED_MS" "$(date -u +'%Y-%m-%dT%H:%M:%SZ')"
