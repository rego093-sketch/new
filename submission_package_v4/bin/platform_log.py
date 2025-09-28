#!/usr/bin/env python3
import sys, json, platform, hashlib, importlib.util, csv
from pathlib import Path
ROOT=Path("/mnt/data"); SEAL=ROOT/"SEAL.json"; OUT=ROOT/"out"; OUT.mkdir(parents=True, exist_ok=True)
CSVF=OUT/"platform_log.csv"; RES=OUT/"results.json"
sh=hashlib.sha256(SEAL.read_bytes()).hexdigest()
row={"os":platform.platform(),"python":sys.version.split()[0],"numpy":"not-installed","seal_sha256":sh,"E1_eV":"","a_H_Angstrom":""}
if importlib.util.find_spec("numpy"):
    import numpy as np; row["numpy"]=np.__version__
if RES.exists():
    r=json.loads(RES.read_text()); row["E1_eV"]=r.get("E1_eV",""); row["a_H_Angstrom"]=r.get("a_H_Angstrom","")
write_header = not CSVF.exists()
with CSVF.open("a", newline="") as f:
    w=csv.DictWriter(f, fieldnames=list(row.keys()));
    if write_header: w.writeheader();
    w.writerow(row)
print(f"Wrote: {CSVF}")
