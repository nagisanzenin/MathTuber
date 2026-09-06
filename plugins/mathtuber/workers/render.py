"""Render trusted scene code with centrally enforced dimensions and timing."""
import importlib.util
import json
from pathlib import Path
import sys
from manim import tempconfig

request = json.loads(Path(sys.argv[1]).read_text())
sys.path.insert(0, request["components"])
sys.path.insert(0, request["project"])
import components
components.TARGET_DURATION = request["duration"]
components.configure_profile(request.get("profile"))
with tempconfig({"pixel_width": request["width"], "pixel_height": request["height"],
                 "frame_rate": request["fps"], "frame_width": 8,
                 "frame_height": 8*request["height"]/request["width"],
                 "media_dir": request["media_dir"], "output_file": "scene",
                 "preview": False, "write_to_movie": True, "disable_caching": False,
                 "verbosity": "WARNING"}):
    spec = importlib.util.spec_from_file_location("mathtuber_user_scene", request["source"])
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    cls = getattr(module, request["class_name"])
    if request.get("profile") and not issubclass(cls, components.NarratedScene):
        raise ValueError("Profile-bound scenes must inherit WorkshopScene or NarratedScene")
    scene = cls()
    scene.render()
