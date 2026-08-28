#!/usr/bin/env bash
set -euo pipefail

python3 - <<'PY'
import json
from pathlib import Path

contract = json.loads(Path('.amo').read_text(encoding='utf-8'))
assert contract['schema'] == 'desarrollamo.amo.v1'
assert contract['id'] == 'landings'
checks = contract.get('health', {}).get('checks', [])
assert checks and checks[0].get('command') == 'bash scripts/autocheck.sh'
PY

python3 demos/file-integrity/test_contract.py
python3 demos/midispositivo/test_schema.py

echo 'LANDINGS_AUTOCHECK_OK'
