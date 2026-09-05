"""Validate production contracts, never predict audience enjoyment."""
from .state import ProductionError, within, file_hash

def validate_plan(project):
    from .profiles import check
    profile = check(project)
    plan = project.data.get("creative")
    if plan is None:
        return {"present": False, "scope": "legacy project; no creative contract"}
    for field in ("audience", "learning_goal", "question", "payoff", "transfer_prompt", "duration_rationale", "novelty_audit"):
        if not isinstance(plan.get(field), str) or not plan[field].strip():
            raise ProductionError("INVALID_PLAN", f"creative.{field} must be explicit")
    beats = plan.get("beats", [])
    if [b.get("scene") for b in beats] != [s["id"] for s in project.data["scenes"]]:
        raise ProductionError("INVALID_PLAN", "One ordered beat per scene is required")
    for beat in beats:
        for field in ("viewer_question", "visual_action", "new_understanding", "sound_intent"):
            if not isinstance(beat.get(field), str) or not beat[field].strip():
                raise ProductionError("INVALID_PLAN", f"Missing beat {field}")
    return {"present": True, "passed": True, "beats": len(beats), "profile": profile, "scope": "contract completeness only; no quality or learning claim"}

def soundtrack(project):
    spec = project.data.get("soundtrack")
    if not spec:
        return None
    if not isinstance(spec.get("license"), str) or not spec["license"].strip():
        raise ProductionError("INVALID_SOUNDTRACK", "Record original authorship or an appropriate license")
    gain = spec.get("gain_db", 0)
    if not isinstance(gain, (float, int)) or not -60 <= gain <= 6:
        raise ProductionError("INVALID_SOUNDTRACK", "gain_db must be finite and between -60 and 6")
    path = within(project.root, spec["path"])
    if not path.is_file():
        raise ProductionError("INVALID_SOUNDTRACK", "Soundtrack file is missing")
    return {"path": str(path), "sha256": file_hash(path), "gain_db": gain, "license": spec["license"]}

def validate_delivery(project, duration):
    kind = project.data.get("delivery", {}).get("kind")
    if kind not in (None, "youtube_short", "youtube_video"):
        raise ProductionError("INVALID_DELIVERY", "Use youtube_short or youtube_video")
    fmt = project.data.get("format", {})
    if kind == "youtube_short" and (duration > 180 or fmt.get("width",1080) > fmt.get("height",1920)):
        raise ProductionError("SHORTS_LIMIT", "YouTube Shorts require square/vertical video no longer than 180 seconds")
