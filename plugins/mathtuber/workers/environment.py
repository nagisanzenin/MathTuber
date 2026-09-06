"""Inspect the selected runtime without model downloads, synthesis or credentials."""
import importlib.metadata
import json
from pathlib import Path
import sys
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from mathtuber.environment import PACKAGES

packages={}
for name in PACKAGES:
    try:packages[name]=importlib.metadata.version(name)
    except importlib.metadata.PackageNotFoundError:packages[name]=None
try:
    ZoneInfo('America/Los_Angeles');pacific=True
except ZoneInfoNotFoundError:pacific=False
print(json.dumps({'packages':packages,'pacific_timezone':pacific}))
