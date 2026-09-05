#!/usr/bin/env python3
"""Provision one shared media runtime; plugin installs stay lightweight."""
import argparse
import os
from pathlib import Path
import shutil
import subprocess
p=argparse.ArgumentParser()
p.add_argument("--home",default=os.environ.get("MATHTUBER_RUNTIME_HOME",str(Path.home()/".local/share/mathtuber")))
a=p.parse_args()
if not shutil.which("uv"): raise SystemExit("Install uv from https://docs.astral.sh/uv/getting-started/installation/")
missing=[x for x in ("ffmpeg","ffprobe","latex","dvisvgm","espeak-ng") if not shutil.which(x)]
if missing: raise SystemExit("Install system dependencies first: "+", ".join(missing))
env=Path(a.home).expanduser()/"media"
if not env.exists(): subprocess.run(["uv","venv","--python","3.12",str(env)],check=True)
python=env/("Scripts/python.exe" if os.name=="nt" else "bin/python")
requirements=Path(__file__).resolve().parents[1]/"requirements-media.txt"
subprocess.run(["uv","pip","install","--python",str(python),"-r",str(requirements)],check=True)
print(f"Media runtime ready: {python}")
