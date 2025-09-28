FROM python:3.11-slim
WORKDIR /app
COPY bin bin
COPY out out
COPY SEAL.json SEAL.json
COPY SEAL_PIN.txt SEAL_PIN.txt
CMD python bin/build_seal.py && python bin/compute.py && python bin/verify.py --echo && python bin/platform_log.py
