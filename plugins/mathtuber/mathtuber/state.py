"""Atomic project state, provenance, dependency fingerprints and locking."""
from contextlib import contextmanager
import hashlib
import json
import os
from pathlib import Path
import sqlite3
import time

class ProductionError(Exception):
    def __init__(self, code, message):
        self.code = code
        super().__init__(message)

def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def file_hash(path):
    h = hashlib.sha256()
    with open(path, "rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def read_json(path):
    return json.loads(Path(path).read_text())

def atomic_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + f".{os.getpid()}.tmp")
    with tmp.open("w") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(tmp, path)

def within(root, relative):
    path = (Path(root) / relative).resolve()
    if not path.is_relative_to(Path(root).resolve()):
        raise ProductionError("INVALID_PATH", "Artifact paths must stay inside the project")
    return path

def validate_manifest(data):
    if data.get("schema_version") != 1:
        raise ProductionError("INVALID_MANIFEST", "schema_version must be 1")
    brief = data.get("brief", {})
    if not isinstance(brief.get("topic"), str) or not brief["topic"].strip():
        raise ProductionError("INVALID_MANIFEST", "brief.topic is required")
    fmt = data.get("format", {})
    for key, default in (("width", 1080), ("height", 1920), ("fps", 30)):
        value = fmt.get(key, default)
        if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
            raise ProductionError("INVALID_MANIFEST", f"format.{key} must be a positive integer")
    if fmt.get("fps", 30) > 120 or max(fmt.get("width", 1080), fmt.get("height", 1920)) > 7680:
        raise ProductionError("INVALID_MANIFEST", "Format exceeds supported limits")
    scenes = data.get("scenes", [])
    if not scenes:
        raise ProductionError("INVALID_MANIFEST", "At least one scene is required")
    ids = set()
    import re
    for scene in scenes:
        sid = scene.get("id", "")
        if not re.fullmatch(r"[a-zA-Z0-9_-]{1,64}", sid) or sid in ids:
            raise ProductionError("INVALID_MANIFEST", "Scene IDs must be unique safe identifiers")
        ids.add(sid)
        for key in ("narration", "source", "class_name"):
            if not isinstance(scene.get(key), str) or not scene[key].strip():
                raise ProductionError("INVALID_MANIFEST", f"{sid}.{key} is required")
        if not re.fullmatch(r"[A-Za-z_]\w*", scene["class_name"]):
            raise ProductionError("INVALID_MANIFEST", "Invalid scene class")
        source = Path(scene["source"])
        if source.is_absolute() or ".." in source.parts or source.suffix != ".py":
            raise ProductionError("INVALID_MANIFEST", "Scene source must be a project-relative Python file")
    return data

class Project:
    def __init__(self, root):
        self.root = Path(root).expanduser().resolve()
        self.manifest_path = self.root / "project.json"
        if not self.manifest_path.exists():
            raise ProductionError("PROJECT_NOT_FOUND", str(self.manifest_path))
        self.data = validate_manifest(read_json(self.manifest_path))
        self.db_path = self.root / ".mathtuber" / "state.sqlite"
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        with self.connect() as db:
            db.executescript('''
                CREATE TABLE IF NOT EXISTS artifacts(key TEXT PRIMARY KEY, fingerprint TEXT,
                    path TEXT, sha256 TEXT, metadata TEXT, created REAL);
                CREATE TABLE IF NOT EXISTS reviews(id INTEGER PRIMARY KEY, snapshot TEXT,
                    payload TEXT, created REAL);
                CREATE TABLE IF NOT EXISTS events(id INTEGER PRIMARY KEY, kind TEXT,
                    payload TEXT, created REAL);
                CREATE TABLE IF NOT EXISTS locks(name TEXT PRIMARY KEY, pid INTEGER, created REAL);
                CREATE TABLE IF NOT EXISTS publications(intent TEXT PRIMARY KEY, payload TEXT);
            ''')
    def connect(self):
        conn = sqlite3.connect(self.db_path, timeout=15)
        conn.row_factory = sqlite3.Row
        return conn
    def scene(self, sid):
        for scene in self.data["scenes"]:
            if scene["id"] == sid:
                return scene
        raise ProductionError("SCENE_NOT_FOUND", sid)
    def artifact(self, key, fingerprint=None):
        with self.connect() as db:
            row = db.execute("SELECT * FROM artifacts WHERE key=?", (key,)).fetchone()
        if row is None:
            return None
        result = dict(row)
        path = within(self.root, result["path"])
        if not path.is_file() or file_hash(path) != result["sha256"]:
            return None
        if fingerprint is not None and result["fingerprint"] != fingerprint:
            return None
        result["metadata"] = json.loads(result["metadata"])
        result["absolute_path"] = str(path)
        return result
    def record(self, key, fingerprint, path, metadata):
        path = Path(path).resolve()
        relative = str(path.relative_to(self.root))
        with self.connect() as db:
            db.execute("INSERT OR REPLACE INTO artifacts VALUES(?,?,?,?,?,?)",
                       (key, fingerprint, relative, file_hash(path), json.dumps(metadata), time.time()))
        return self.artifact(key, fingerprint)
    def event(self, kind, payload):
        with self.connect() as db:
            db.execute("INSERT INTO events(kind,payload,created) VALUES(?,?,?)",
                       (kind, json.dumps(payload), time.time()))
    @contextmanager
    def lock(self, name="production"):
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            row = db.execute("SELECT pid FROM locks WHERE name=?", (name,)).fetchone()
            if row:
                try:
                    os.kill(row["pid"], 0)
                except ProcessLookupError:
                    db.execute("DELETE FROM locks WHERE name=?", (name,))
                else:
                    raise ProductionError("PROJECT_BUSY", f"{name} held by PID {row['pid']}")
            db.execute("INSERT INTO locks VALUES(?,?,?)", (name, os.getpid(), time.time()))
        try:
            yield
        finally:
            with self.connect() as db:
                db.execute("DELETE FROM locks WHERE name=? AND pid=?", (name, os.getpid()))
    def snapshot(self):
        sources = {}
        for s in self.data["scenes"]:
            path = within(self.root, s["source"])
            sources[s["source"]] = file_hash(path) if path.exists() else None
        # Include helper modules and data: changes must invalidate review approval.
        for pattern in ("scenes/**/*", "assets/**/*"):
            for path in self.root.glob(pattern):
                if path.is_file() and "__pycache__" not in path.parts:
                    sources[str(path.relative_to(self.root))] = file_hash(path)
        with self.connect() as db:
            artifacts = [dict(r) for r in db.execute("SELECT key,sha256,fingerprint FROM artifacts ORDER BY key")]
        return digest({"manifest": self.data, "sources": sources, "artifacts": artifacts})

def create(root, manifest):
    root = Path(root).expanduser().resolve()
    if (root / "project.json").exists():
        raise ProductionError("PROJECT_EXISTS", str(root))
    validate_manifest(manifest)
    atomic_json(root / "project.json", manifest)
    for name in ("scenes", "assets", "audio", "renders", "exports", "reviews"):
        (root / name).mkdir(exist_ok=True)
    return {"project": str(root), "next": "Write scene code; synthesize narration and inspect previews"}
