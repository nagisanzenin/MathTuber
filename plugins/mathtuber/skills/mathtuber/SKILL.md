---
name: mathtuber
description: Create, revise, review, resume, and optionally publish narrated mathematical animation videos with local Manim and speech tools. Use for math explainers, visual proofs, educational Shorts, and existing MathTuber projects.
---

# MathTuber

You are the filmmaker and mathematical author. Use your native reasoning, research, file editing, and media-inspection tools. The engine performs mechanical work; it does not call an LLM or decide what makes a good explanation.

Resolve the plugin root as the directory containing `scripts/engine.py`, two levels above this skill. Resolve symlinks first. An explicit `MATHTUBER_ROOT` may also identify it. Invoke `python3 <root>/scripts/engine.py`; never depend on the current working directory or a vendor-specific root variable. Run `doctor` once per new environment. If media dependencies are missing, use `<root>/scripts/setup.py` (requires uv and installed FFmpeg/TeX).

Use [navigation.md](references/navigation.md) to find the next stage or a focused repair note. Retrieve a few relevant cases with `scripts/knowledge.py` rather than loading the entire reference library. Treat recipes as mechanical aids; independently judge the mathematical explanation.

Read [profiles.md](references/profiles.md) when selecting, authoring or applying a channel identity. Keep editorial subject and values separate from delivery aesthetics. Choose the mathematical insight and its reasoning before selecting an attractive renderable subject. For batches, read [editorial-mix.md](references/editorial-mix.md) and compare both mathematical novelty and repetition in the viewer experience.

Read [theory.md](references/theory.md) for the evidence-informed creative contract. Read [production.md](references/production.md) when creating or substantially revising a video. Read [commands.md](references/commands.md) for the exact manifest and commands. Read [publishing.md](references/publishing.md) only when uploading is requested.

Choose actions based on the problem, current artifacts, and evidence. You may solve/storyboard in one pass or prototype a difficult visual before writing narration. Avoid rigid persona chains, redundant critiques, and large context dumps. Start with the requested outcome and existing channel profile. Default to English, 9:16, 1080×1920, 30 fps. Choose duration from the explanation: YouTube Shorts must be at most 180 seconds; 4–5 minutes requires a regular video. Never stretch or compress a proof to hit a habitual duration.

For an existing project, call `status`/`next` and inspect current findings; preserve valid work. Narration, render, and export caches are checked by content. Re-render only invalidated scenes. Core commands emit JSON and return nonzero on failure. Long media operations support `--background`; follow the returned job ID with `job-status`.

Inspect the actual media using your host's image/audio/video tools. `review-bundle` supplies timestamped PNGs and the clip/audio paths. A returned path alone is not an inspected image. Do not claim full motion/audio review from a contact sheet. Record the actual evidence hashes, limitations, and findings. Name the actual method and scope of every check. Audio signal measurements and independent speech recognition can check technical delivery; they do not establish pleasant prosody or a good music mix. Never claim listening from these tools. If a required check cannot be performed, mark it unavailable; never write a passing review to get around the publishing gate. Keep subjective listening and real-audience validation explicitly unmeasured when unavailable.

The complete approved timeline must be present. Rendering success and automated measurements do not establish mathematical correctness. Fix the explanation when necessary, not just the code. A suggested starting limit is three repair cycles per scene; repeated identical failures call for a different approach. Never auto-accept exhausted retries.

Use `--execution docker` for restricted rendering after pulling `manimcommunity/manim:v0.20.1`; the renderer has read-only scenes/assets, no network, and a writable output directory. Native rendering executes agent-authored Python as trusted code and is not an OS sandbox. Keep it within the requested project; do not read credentials from scene code. The publisher alone handles OAuth. Creation does not imply publication unless the user requested it or an applicable saved policy does. Respect existing authorization without inventing repeated confirmation steps.

Return the final export, editable project path, concrete validation results, any remaining limitation, and YouTube URL when uploaded. Do not claim a quality/speed gain without a measured comparison.

### Mechanism-first batches

Prototype the hardest inference before full production. Keep technical review separate from written editorial judgment; neither establishes audience retention or learning. For an authorized batch, finish current final reviews across every member before the first upload, then use `scripts/publish_batch.py` with a batch manifest and separate editorial records. It defaults to a read-only plan and rechecks all members before each upload. See [mechanism-direction.md](references/mechanism-direction.md), bundled with this skill, for concrete reference specifications and the unperformed viewer-test protocol. If no actual viewers or listening are available, state that limitation; never fabricate a test or label an unavailable check as passed.

For new batches, also read [linked-representations.md](references/linked-representations.md). Declare critical transition intervals and inspect them through completion; retain explicit evidence limits.
