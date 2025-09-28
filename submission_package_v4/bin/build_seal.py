#!/usr/bin/env python3
# Creates SEAL.json (scales + gates), prints SHA256, and writes SEAL_PIN.txt / seal_hash.tex.
import json, math, hashlib
from pathlib import Path
ROOT = Path("/mnt/data")
SEAL_PATH = ROOT / "SEAL.json"
e_C = 1.602176634e-19
h = 6.62607015e-34
hbar = h/(2.0*3.141592653589793)
m_e = 9.1093837015e-31
epsilon0 = 8.8541878128e-12
Eh_J = (m_e * (e_C**4)) / (((4*3.141592653589793*epsilon0)**2) * (hbar**2))
a0_m = (4*3.141592653589793*epsilon0 * (hbar**2)) / (m_e * (e_C**2))
S_energy_to_eV = Eh_J / e_C
S_length_to_Angstrom = a0_m / 1.0e-10
SEAL = {"scales":{"S_energy_to_eV":S_energy_to_eV,"S_length_to_Angstrom":S_length_to_Angstrom},
        "gates":{"TIME":True,"JIN":True,"EM_c":True,"MASS":True,"Gamma3":True}}
SEAL_PATH.write_text(json.dumps(SEAL, indent=2))
sha256 = hashlib.sha256(SEAL_PATH.read_bytes()).hexdigest()
(ROOT/"SEAL_PIN.txt").write_text(sha256+"\n")
(ROOT/"seal_hash.tex").write_text("\\paragraph{Seal hash.} \\texttt{"+sha256+"}\\\\\n")
print(json.dumps({"SEAL":str(SEAL_PATH),"SHA256":sha256,
 "S_energy_to_eV":S_energy_to_eV,"S_length_to_Angstrom":S_length_to_Angstrom}, indent=2))
