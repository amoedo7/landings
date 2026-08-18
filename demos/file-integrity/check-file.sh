#!/usr/bin/env bash
set -euo pipefail
SCHEMA="desarrollamo.file-integrity.v1"
if [ "$#" -ne 1 ]; then echo "Usage: $(basename "$0") <file>" >&2; exit 2; fi
FILE="$1"
if [ ! -f "$FILE" ]; then printf '{"schema":"%s","ok":false,"error":"file not found"}\n' "$SCHEMA" >&2; exit 1; fi
if command -v sha256sum >/dev/null 2>&1; then HASH="$(sha256sum "$FILE" | awk '{print $1}')"; elif command -v shasum >/dev/null 2>&1; then HASH="$(shasum -a 256 "$FILE" | awk '{print $1}')"; else printf '{"schema":"%s","ok":false,"error":"sha256 tool not available"}\n' "$SCHEMA" >&2; exit 1; fi
BYTES="$(wc -c < "$FILE" | tr -d '[:space:]')"
NAME="$(basename "$FILE" | sed 's/\\/\\\\/g; s/"/\\"/g')"
CHECKED_AT="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
printf '{"schema":"%s","file":"%s","bytes":%s,"sha256":"%s","checked_at":"%s"}\n' "$SCHEMA" "$NAME" "$BYTES" "$HASH" "$CHECKED_AT"
