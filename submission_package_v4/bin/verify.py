#!/usr/bin/env python3
# Verifier: R7/R8 exit(0|1), seal hash pinning, gate-off negative controls, optional Lyman-α, no-random audit.
import argparse, json, hashlib, math, sys
from pathlib import Path
ROOT=Path("/mnt/data")
SEAL_PATH=ROOT/"SEAL.json"
PIN_PATH=ROOT/"SEAL_PIN.txt"
OUT_DIR=ROOT/"out"
RESULTS=OUT_DIR/"results.json"
TARGET_E1=13.6057
TARGET_aH=0.529177
TARGET_LYA=10.204
def load_json(p:Path): return json.loads(p.read_text())
def sha256_path(p:Path)->str: return hashlib.sha256(p.read_bytes()).hexdigest()
def compute_scales_from_seal(seal:dict):
    g=seal["gates"]; s=seal["scales"]
    Se=float(s["S_energy_to_eV"]); Sl=float(s["S_length_to_Angstrom"])
    if not g.get("Gamma3",True): return float("nan"), float("nan")
    if (not g.get("EM_c",True)) or (not g.get("MASS",True)): return 0.0, float("inf")
    if not g.get("JIN",True): return float("inf"), 0.0
    return Se, Sl
def compute_results_from_seal(seal:dict):
    Se,Sl=compute_scales_from_seal(seal)
    return 0.5*Se, 1.0*Sl
def metrics(E1_eV,aH):
    def safe(err,base):
        return abs(err)/(0.01*base) if (math.isfinite(err) and base>0) else float("inf")
    r7=safe(E1_eV-TARGET_E1, TARGET_E1)
    r8=safe(aH-TARGET_aH, TARGET_aH)
    return r7,r8,(r7<=1.0) and (r8<=1.0)
def randomness_audit():
    patterns=["import random","np.random","from random import"]
    for p in (ROOT/"bin").rglob("*.py"):
        if p.name == "verify.py":
            continue
        try: txt=p.read_text()
        except Exception: continue
        for pat in patterns:
            if pat in txt: return False, str(p), pat
    return True, "", ""
def lya_check_from_seal(seal:dict):
    Eh=float(seal["scales"]["S_energy_to_eV"]) # eV per Hartree
    Elya=0.75*0.5*Eh
    r9=abs(Elya-TARGET_LYA)/(0.01*TARGET_LYA)
    return Elya, r9, (r9<=1.0)
def main(argv=None):
    ap=argparse.ArgumentParser()
    ap.add_argument("--gate-off", choices=["EM_c","JIN","Gamma3"], default=None)
    ap.add_argument("--echo", action="store_true")
    ap.add_argument("--with-lya", action="store_true")
    ap.add_argument("--no-random", action="store_true")
    args=ap.parse_args(argv)
    seal_hash_pre=sha256_path(SEAL_PATH)
    pin=PIN_PATH.read_text().strip() if PIN_PATH.exists() else None
    seal=load_json(SEAL_PATH)
    if args.gate_off:
        seal=json.loads(json.dumps(seal)); seal["gates"][args.gate_off]=False
    E1_eV,aH=compute_results_from_seal(seal)
    if (args.gate_off is None) and RESULTS.exists():
        prev=load_json(RESULTS)
        consistent=(abs(prev.get("E1_eV",float("nan"))-E1_eV)<1e-12 and abs(prev.get("a_H_Angstrom",float("nan"))-aH)<1e-12)
    else:
        consistent=True
    seal_hash_post=sha256_path(SEAL_PATH)
    seal_locked=(seal_hash_pre==seal_hash_post)
    r7,r8,passed=metrics(E1_eV,aH)
    ok_pin=(pin is None) or (pin==seal_hash_pre)
    opt_ok=True; E_LYA=None; R9=None; PASS_LYA=None
    if args.with_lya:
        E_LYA,R9,PASS_LYA=lya_check_from_seal(seal)
    if args.no_random:
        ok_rand,where,pat=randomness_audit()
        if not ok_rand: opt_ok=False
    if args.echo:
        print(json.dumps({"gate_off":args.gate_off or "NONE","E1_eV":E1_eV,"a_H_Angstrom":aH,
            "R7":r7,"R8":r8,"PASS":passed,"SEAL_hash_pre":seal_hash_pre,"SEAL_hash_post":seal_hash_post,
            "SEAL_locked":seal_locked,"PIN_match":ok_pin,"consistent_with_results_json":consistent,
            "E_LYA":E_LYA,"R9":R9,"PASS_LYA":PASS_LYA,"no_random_ok":(None if not args.no_random else opt_ok)}, indent=2))
    sys.exit(0 if (passed and seal_locked and ok_pin and consistent and (not args.no_random or opt_ok)) else 1)
if __name__=="__main__": main()
