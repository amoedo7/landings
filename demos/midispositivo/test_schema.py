#!/usr/bin/env python3
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
p = subprocess.run([sys.executable, str(HERE / 'midispositivo.py'), '--compact'], capture_output=True, text=True, check=True)
report = json.loads(p.stdout)

assert report['schema'] == 'desarrollamo.midispositivo.v1'
assert isinstance(report['device'], dict)
assert isinstance(report['network'], dict)
assert report['privacy']['online_lookup_requested'] is False
assert report['privacy']['mac_addresses_collected'] is False
assert report['privacy']['wifi_ssid_collected'] is False
assert report['privacy']['exact_gps_collected'] is False
assert report['online']['enabled'] is False
assert 'os' in report['device']
assert 'local_ip' in report['network']

print('MiDispositivo schema OK')
