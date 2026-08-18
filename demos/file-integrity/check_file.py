#!/usr/bin/env python3
import hashlib,json,sys
from datetime import datetime,timezone
from pathlib import Path
SCHEMA="desarrollamo.file-integrity.v1"
def inspect_file(raw_path):
    path=Path(raw_path).expanduser()
    if not path.is_file(): raise FileNotFoundError(f"File not found: {path}")
    h=hashlib.sha256(); size=0
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""):
            size+=len(chunk); h.update(chunk)
    return {"schema":SCHEMA,"file":path.name,"bytes":size,"sha256":h.hexdigest(),"checked_at":datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00","Z")}
def main():
    if len(sys.argv)!=2:
        print(f"Usage: {Path(sys.argv[0]).name} <file>",file=sys.stderr); return 2
    try:
        print(json.dumps(inspect_file(sys.argv[1]),ensure_ascii=False,separators=(",",":"))); return 0
    except Exception as exc:
        print(json.dumps({"schema":SCHEMA,"ok":False,"error":str(exc)},ensure_ascii=False,separators=(",",":")),file=sys.stderr); return 1
if __name__=="__main__": raise SystemExit(main())
