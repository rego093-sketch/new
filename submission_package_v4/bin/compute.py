#!/usr/bin/env python3
# Reads SEAL.json and computes E1_eV, a_H_Angstrom -> out/results.json
import json
from pathlib import Path
ROOT = Path("/mnt/data")
SEAL_PATH = ROOT/"SEAL.json"
OUT_DIR = ROOT/"out"
OUT_DIR.mkdir(parents=True, exist_ok=True)
def compute_scales_from_seal(seal: dict):
    g=seal["gates"]; s=seal["scales"]
    Se=float(s["S_energy_to_eV"]); Sl=float(s["S_length_to_Angstrom"])
    if not g.get("Gamma3",True): return float("nan"), float("nan")
    if (not g.get("EM_c",True)) or (not g.get("MASS",True)): return 0.0, float("inf")
    if not g.get("JIN",True): return float("inf"), 0.0
    return Se, Sl
def main():
    seal=json.loads(SEAL_PATH.read_text())
    Se,Sl=compute_scales_from_seal(seal)
    E1_eV=0.5*Se; aH=1.0*Sl
    out={"E1_eV":E1_eV,"a_H_Angstrom":aH}
    (OUT_DIR/"results.json").write_text(json.dumps(out, indent=2))
    print(json.dumps({"results_path":str(OUT_DIR/"results.json"),**out}, indent=2))
if __name__=="__main__": main()
