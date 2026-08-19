#!/usr/bin/env sh
set -eu

# Launcher simple para Android/Termux, Linux y macOS.
# El núcleo Python conserva el mismo contrato entre plataformas.

HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)

if command -v python3 >/dev/null 2>&1; then
  exec python3 "$HERE/midispositivo.py" "$@"
elif command -v python >/dev/null 2>&1; then
  exec python "$HERE/midispositivo.py" "$@"
else
  printf '%s\n' 'MiDispositivo necesita Python 3 en Android/Termux, Linux o macOS.' >&2
  printf '%s\n' 'Termux: pkg install python' >&2
  exit 127
fi
