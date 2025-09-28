# Scientific Reports Submission — NO-CAL Hydrogen Reproducibility Kit

Author: **LEE YOUNG JAE** (Independent Researcher, Daegu, Republic of Korea)  
Email: **rego093@naver.com**

Seal SHA256 (pinned in manuscript): **cf3c1684f369a1f5aa6b7e40384002fa9e807d98e27807c4d556c14cb06f4453**

## Reproduction (command-line)
```bash
python bin/build_seal.py
python bin/compute.py
python bin/verify.py --echo              # exit 0 expected
python bin/verify.py --gate-off EM_c --echo   # exit 1 expected
python bin/verify.py --gate-off JIN  --echo   # exit 1 expected
python bin/verify.py --gate-off Gamma3 --echo # exit 1 expected
python bin/platform_log.py
```
