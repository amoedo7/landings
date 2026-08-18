#!/usr/bin/env python3
import json,os,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def run_json(command):
    return json.loads(subprocess.check_output(command,text=True).strip())
with tempfile.TemporaryDirectory() as tmp:
    fixture=Path(tmp)/"fixture.txt"
    fixture.write_bytes(b"DesarrollAMO demo\n")
    expected=run_json([sys.executable,str(ROOT/"check_file.py"),str(fixture)])
    if os.name=="nt":
        candidate=run_json(["powershell","-NoProfile","-ExecutionPolicy","Bypass","-File",str(ROOT/"check-file.ps1"),str(fixture)])
        platform_name="windows"
    else:
        candidate=run_json(["bash",str(ROOT/"check-file.sh"),str(fixture)])
        platform_name="unix"
    assert expected["schema"]==candidate["schema"]=="desarrollamo.file-integrity.v1"
    assert expected["sha256"]==candidate["sha256"]
    assert expected["bytes"]==candidate["bytes"]
    assert expected["file"]==candidate["file"]=="fixture.txt"
    print(json.dumps({"ok":True,"platform":platform_name,"sha256":expected["sha256"],"bytes":expected["bytes"]},separators=(",",":")))
