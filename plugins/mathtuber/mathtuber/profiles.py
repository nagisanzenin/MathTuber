"""Portable, project-pinned creative profiles. Validation is not a taste score."""
import re
from pathlib import Path
from .state import ProductionError, read_json, atomic_json, within, file_hash

CATALOG = Path(__file__).resolve().parents[1] / "profiles"

def validate(data):
    def fail(message):
        raise ProductionError("INVALID_PROFILE", message)
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        fail("Profile schema_version must be 1")
    for key in ("id", "version", "promise", "audience", "personality", "license"):
        if not isinstance(data.get(key), str) or not data[key].strip():
            fail(f"Profile {key} is required")
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,63}", data["id"]):
        fail("Profile id must be a safe lowercase identifier")
    if data.get("status") not in ("candidate", "emerging", "audience-tested"):
        fail("Use candidate, emerging or audience-tested status")
    identity = data.get("identity")
    if not isinstance(identity, dict):
        fail("Profile identity must be an object")
    colors = identity.get("colors", {})
    for role in ("background", "ink", "surface", "primary", "secondary", "accent", "muted"):
        if not isinstance(colors, dict) or not re.fullmatch(r"#[0-9a-fA-F]{6}", str(colors.get(role, ""))):
            fail(f"identity.colors.{role} must be #RRGGBB")
    for field in ("materials", "motion", "voice", "sound"):
        if not isinstance(identity.get(field), str) or not identity[field].strip():
            fail(f"identity.{field} must be explicit")
    typography = identity.get("type", {})
    if not isinstance(typography, dict) or any(not isinstance(typography.get(k), str) or not typography[k].strip() for k in ("font", "fallback")):
        fail("Specify font and fallback")
    roles = typography.get("roles", {})
    for role in ("claim", "label", "detail"):
        value = roles.get(role) if isinstance(roles, dict) else None
        if isinstance(value, bool) or not isinstance(value, (float, int)) or not 8 <= value <= 120:
            fail(f"Invalid type size for {role}")
    for key in ("hard_constraints", "preferences"):
        if not isinstance(data.get(key), list) or not data[key] or any(not isinstance(x, str) or not x.strip() for x in data[key]):
            fail(f"{key} must contain explicit rules")
    if not isinstance(data.get("formats"), dict) or not data["formats"] or any(not isinstance(x, str) or not x.strip() for x in data["formats"].values()):
        fail("Specify at least one format")
    if not isinstance(data.get("examples"), list) or not data["examples"]:
        fail("Provide annotated examples")
    for example in data["examples"]:
        if not isinstance(example, dict) or any(not isinstance(example.get(k), str) or not example[k].strip() for k in ("situation", "prefer", "avoid", "reason")):
            fail("Examples require situation, prefer, avoid and reason")
    evidence = data.get("evidence", {})
    if not isinstance(evidence, dict) or not evidence.get("status") or not evidence.get("validation"):
        fail("State evidence status and validation plan/results")
    return data

def catalog():
    return [validate(read_json(path)) for path in sorted(CATALOG.glob("*.json"))]

def load(project):
    binding = project.data.get("channel_profile")
    if binding is None:
        return None
    if not isinstance(binding, dict) or not isinstance(binding.get("path"), str):
        raise ProductionError("INVALID_PROFILE", "channel_profile.path is required")
    path = within(project.root, binding["path"])
    data = validate(read_json(path))
    if data["id"] != binding.get("id") or data["version"] != binding.get("version") or file_hash(path) != binding.get("sha256"):
        raise ProductionError("PROFILE_CHANGED", "Pinned profile differs; deliberately rebind the updated profile")
    return data

def bind(project, source, replace=False):
    candidate = CATALOG / (source + ".json") if re.fullmatch(r"[a-z0-9][a-z0-9-]{0,63}", source) else Path(source).expanduser()
    data = validate(read_json(candidate))
    old = project.data.get("channel_profile")
    if old and not replace:
        if load(project) == data:
            return {"cached": True, "profile": old}
        raise ProductionError("PROFILE_BOUND", "Use --replace to deliberately change a project profile")
    # Content-addressed assets keep projects portable and edits invalidate render/review caches.
    from .state import digest
    relative = f"assets/profile-{digest(data)[:16]}.json"
    path = within(project.root, relative)
    atomic_json(path, data)
    project.data["channel_profile"] = {"id": data["id"], "version": data["version"], "path": relative, "sha256": file_hash(path)}
    atomic_json(project.manifest_path, project.data)
    return {"cached": False, "profile": project.data["channel_profile"], "status": data["status"]}

def check(project):
    data = load(project)
    if data is None:
        return {"present": False, "scope": "No profile; legacy project supported"}
    application = project.data.get("creative", {}).get("profile_application", {})
    if not isinstance(application, dict):
        raise ProductionError("INVALID_PROFILE_APPLICATION", "profile_application must be an object")
    for key in ("format", "signature", "episode_variation"):
        if not isinstance(application.get(key), str) or not application[key].strip():
            raise ProductionError("INVALID_PROFILE_APPLICATION", f"Specify profile_application.{key}")
    if application["format"] not in data["formats"]:
        raise ProductionError("INVALID_PROFILE_APPLICATION", "Format is not defined by the profile")
    if not isinstance(application.get("exceptions"), list) or any(not isinstance(x, str) or not x.strip() for x in application["exceptions"]):
        raise ProductionError("INVALID_PROFILE_APPLICATION", "exceptions must be a list of explanations, possibly empty")
    return {"present": True, "id": data["id"], "version": data["version"], "status": data["status"], "scope": "Contract completeness; recognition, appeal and learning remain separate unmeasured outcomes"}
