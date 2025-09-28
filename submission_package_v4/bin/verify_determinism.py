#!/usr/bin/env python3
import sys,re
from pathlib import Path
B=Path("/mnt/data/bin"); bad=[]
pats=[r"\bimport\s+random\b",r"\bfrom\s+random\s+import\b",r"\bnumpy\.random\b",r"\bnp\.random\b",r"\brandint\(",r"\brandom\(",r"\bseed\(",r"\btorch\b",r"\bjax\b"]
for p in B.glob("*.py"):
 s=p.read_text()
 for pat in pats:
  import re
  if re.search(pat,s): bad.append((p.name,pat))
print("Determinism check: PASS" if not bad else f"RNG patterns: {bad}")
