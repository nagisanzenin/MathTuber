# Tool contract

Set `ENGINE` to the absolute plugin `scripts/engine.py`. All results are JSON. `MATHTUBER_PYTHON` can point to an existing media virtual environment. Otherwise setup creates the shared runtime under `~/.local/share/mathtuber/media` (override `MATHTUBER_RUNTIME_HOME`).

Create a manifest file, then `python3 "$ENGINE" init --project /absolute/project --manifest /absolute/brief.json`.

```json
{
  "schema_version": 1,
  "brief": {"topic": "Why odd numbers build squares", "min_seconds": 120, "max_seconds": 175},
  "format": {"width": 1080, "height": 1920, "fps": 30},
  "speech": {"provider": "kokoro", "voice": "af_heart", "language": "a", "speed": 0.95},
  "scenes": [
    {"id": "s01", "source": "scenes/opening.py", "class_name": "Opening", "narration": "Your complete narration section."}
  ]
}
```

Write scene sources inside the project. The worker enforces the format. Each scene must last the measured narration duration rounded to video frames. An imported `NarratedScene` can use `self.cue(.3)` to wait until 30% and `self.finish()` to end exactly. Do not add uncontrolled long holds.

```sh
python3 "$ENGINE" audio --project "$PROJECT" --scene all --background
python3 "$ENGINE" job-status --project "$PROJECT" --job JOB_ID
python3 "$ENGINE" render --project "$PROJECT" --scene s01 --quality preview --execution native
python3 "$ENGINE" review-bundle --project "$PROJECT" --scene s01 --quality preview
python3 "$ENGINE" render --project "$PROJECT" --scene s01 --quality final --execution native --background
python3 "$ENGINE" assemble --project "$PROJECT"
python3 "$ENGINE" verify --project "$PROJECT"
python3 "$ENGINE" review-bundle --project "$PROJECT"
python3 "$ENGINE" status --project "$PROJECT"
```

`--execution native` is deliberate acknowledgement of trusted-code rendering, not a sandbox setting. All scene renders must be current before assembly. The brief's minimum/maximum duration is enforced. For a short integration fixture explicitly use a smaller brief.

After inspecting evidence write a review file and call `review-record --project ... --file ...`:

```json
{
  "snapshot": "exact snapshot from the bundle",
  "scope": "final",
  "reviewer": "host/model identity when known",
  "verdict": "revise",
  "evidence": [{"path": "/absolute/project/reviews/.../frame-000.png", "sha256": "hash from bundle"}],
  "checks": {"math": "pass", "visual": "pass", "timing": "pass", "audio": "unavailable"},
  "findings": ["Audio could not be inspected in this host."]
}
```

Acceptance requires all four checks to pass, no findings, current evidence, and successful mechanical verification. This record is the reviewer's attestation, not an automatic proof of quality. Editing project inputs invalidates stale acceptance.

Use `--execution docker` for the restricted container renderer. Scene helpers outside `scenes/_shared/` must be declared in `dependencies`, a list of project-relative file paths. Changes to one scene then preserve unrelated scene renders. Shared assets conservatively invalidate every scene.

Set `"captions": {"burn_in": true}` in the manifest to burn readable portrait subtitles into the final export and normalize narration loudness. SRT and ASS remain editable beside the MP4. Final assembly includes this setting in its cache key.

## Creative contract and sound

`plan-check --project PATH` validates the optional `creative` contract described in theory.md. New authored projects should include it. `delivery: {"kind": "youtube_short"}` enforces a square/vertical export of at most 180 seconds; use `youtube_video` for longer work. `soundtrack: {"path": "assets/score.wav", "gain_db": 0, "license": "Original synthesis; CC0"}` mixes a full-timeline audio layer under speech. Silence can be encoded in this stem; it need not be continuous music. Changes invalidate assembly. Creative-project reviews also require `methods` for math/visual/timing/audio (each with method, coverage, limitations) and an honest `audience_validation` string.
