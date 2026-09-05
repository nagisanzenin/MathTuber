# MathTuber

Agentic math filmmaking across Codex, Claude Code, Pi, ZCode, OpenCode and Gemini CLI. The host agent solves the problem, designs and writes the animation, inspects the result, and repairs it. A local engine handles speech, rendering, caching, assembly, evidence and authorized YouTube publication. **No LLM API key or second orchestrator is required.** Host subscriptions and limits still apply.

Built using the [omniplugin portability rules](https://github.com/nagisanzenin/omniplugin), inspired by [SmartUber](https://github.com/nagisanzenin/smartuber). One complete plugin tree, lightweight host manifests, and no vendor-specific agent API.

## Install

Clone this complete repository and keep it in a stable location. Python 3.12+, uv, FFmpeg, LaTeX, dvisvgm and espeak-ng are required for the media runtime. On macOS, Homebrew provides `ffmpeg`, `espeak-ng`, `pkg-config`, `cairo`, `pango` and the `mactex-no-gui` cask. Other operating systems need equivalent Manim system dependencies.

```sh
git clone https://github.com/nagisanzenin/MathTuber.git
cd MathTuber
python3 plugins/mathtuber/scripts/setup.py
python3 scripts/install.py codex  # or claude, pi, zcode, opencode, gemini
python3 plugins/mathtuber/scripts/engine.py doctor
```

The shared runtime lives under `~/.local/share/mathtuber/media`; installing on another agent does not reinstall models. First TTS use downloads Kokoro weights. Local synthesis then uses no paid inference API. Start a fresh host session after installation. Hosts may require their normal login before installing extensions or calling models.

Tell your agent: **“Use MathTuber to create a 2–3 minute YouTube Short explaining why consecutive odd numbers sum to a square. Show a visual proof, inspect the animation and narration, repair problems, and return the finished video.”**

For Pi the explicit invocation is `/skill:mathtuber`. Claude/ZCode can expose the namespaced `mathtuber:mathtuber` skill. Portable hosts can discover the skill from its description. Do not copy only SKILL.md: it needs the adjacent engine and references.

## What runs locally

- Manim 0.20.1 and FFmpeg: deterministic mathematical geometry, equations, motion and final encoding.
- Kokoro 82M: tested English narration, batched model loading and predicted word timestamps for SRT captions; optional burned subtitles and final loudness normalization.
- SQLite and content hashes: resume, provenance, stale review detection, scene cache reuse and duplicate upload prevention.
- Optional Docker rendering: no network, read-only inputs, limited writable output and no OAuth mount. Use `--execution docker` after `docker pull manimcommunity/manim:v0.20.1`.
- Native rendering is faster to start but executes trusted agent-authored Python with the user's filesystem access.

The engine imports existing WAV narration too. The generic MLX adapter is experimental and not a claim that every Qwen/MLX model works. Gemini TTS, local ASR, voice cloning and music are future/optional integrations, not hidden requirements.

## Architecture and quality

[Full research and architecture](docs/architecture.md) separates the target design from this first implementation. [Implementation and platform evidence](docs/verification.md) records what was actually tested. The [skill](plugins/mathtuber/skills/mathtuber/SKILL.md) defines the agent's workflow; [tool contract](plugins/mathtuber/skills/mathtuber/references/commands.md) defines project manifests and JSON commands.

The engine never silently omits a scene, accepts exhausted retries, or treats successful encoding as proof of correctness. Final publishing requires an explicit current review of math, visuals, timing and audio, plus mechanical verification. The agent must use the media capabilities actually available on its host and report unavailable modalities honestly.

Audio changes invalidate the affected scene; scene code changes retain audio. Declare imported helper files in each scene's `dependencies` array, or put common Python helpers under `scenes/_shared/`. Assets conservatively invalidate all scenes. Preview renders are small; full-resolution rendering follows inspection. Measured duration drives scene timing, rather than guessing seconds from word count.

## YouTube

[Publishing contract](plugins/mathtuber/skills/mathtuber/references/publishing.md). Credentials stay outside the repository and renderer. Existing Google authorized-user JSON credentials are supported; `scripts/migrate_youtube_token.py` can migrate the legacy SmartUber credential pickle with a restricted class allowlist. Creation alone does not authorize publication. When the user explicitly requests an upload and the final review passes, the agent can upload, reconcile interrupted resumable transfers and set the requested visibility without a redundant confirmation.

## TikTok

[TikTok publishing research](docs/tiktok-publishing.md) compares Studio, inbox upload and Direct Post, including app review and required user controls. TikTok upload is not yet implemented.

## Development

```sh
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 tests/integration_media.py --project /tmp/mathtuber-fixture --execution native
python3 tests/integration_media.py --project /tmp/mathtuber-docker --execution docker
python3 tests/integration_pi.py
```

The media fixture uses a tone to test mechanics, not voice quality. Pi integration uses the real installed Pi loader and tools against a local model-protocol fixture, not a real model account. See the verification document before interpreting these as end-to-end platform claims.

The editable `examples/odd-squares` project demonstrates a complete six-scene narrated proof. Initialize a separate project from its manifest, copy its scenes, then let your host agent produce and inspect the media. Generated media and credentials are excluded from Git.

## Evidence-informed production

The [research library](docs/research/README.md) informs the [creative workflow](plugins/mathtuber/skills/mathtuber/references/theory.md). New projects record audience-state beats, topic novelty, format rationale and review provenance. The engine supports an original sound layer with speech ducking and an explicit Shorts duration check. These are implemented production tools, not evidence that the resulting videos improve learning or retention.

Watch the [five discovery examples and validation report](docs/discovery-batch.md). Their editable scene sources and narration are included under `examples/discovery`.


## Channel profiles

Bind a portable channel identity with `profile-bind --project PATH --profile ivisualizethings-workshop`; inspect available definitions with `profile-list`. The candidate workshop profile includes editorial promise, visual/motion/audio guidance, annotated examples and optional Manim primitives. Each project pins its own snapshot, so profile changes invalidate rendering and review instead of silently changing old work. No platform-specific model API is required.

See [profile commands and authoring](plugins/mathtuber/skills/mathtuber/references/profiles.md) and [research and evaluation plan](docs/research/CHANNEL-PROFILES.md). Profiles guide creative choices; they do not establish viewer enjoyment or learning.

The [workshop batch](docs/workshop-batch.md) includes five published examples, a visual gallery, mathematical verification and explicit review limitations.

The [mechanism batch and reflection](docs/mechanism-batch.md) adds five new public Shorts, continuous-scene source projects, local reference remakes, and workshop profile 0.2. The [concrete direction guide](docs/research/MECHANISM-DIRECTION.md) supplies reference frames and anti-examples. `publish_batch.py` checks all current technical and editorial reviews before the first upload.

Latest release: [five linked-representation Shorts and reflection](docs/linked-batch.md), with [research update](docs/research/LINKED-REPRESENTATIONS.md) and [editable examples](examples/linked).

Latest release: [five events Shorts and reflection](docs/events-batch.md), with [editable sources](examples/events).

Latest release: [five nature Shorts and reflection](docs/nature-batch.md), with [editable sources](examples/nature).

Latest release: [five motion Shorts and reflection](docs/motion-batch.md), with [editable sources](examples/motion).

Latest release: [five quiet Shorts and reflection](docs/quiet-batch.md), with [editable sources](examples/quiet).

Latest release: [five flow Shorts and reflection](docs/flow-batch.md), with [editable sources](examples/flow).

Latest release: [five everyday-object Shorts and reflection](docs/objects-batch.md), with [editable sources](examples/objects).

Latest release: [five meaningful-ending Shorts and reflection](docs/endings-batch.md), with [editable sources](examples/endings).

Latest release: [five focal-staging Shorts and reflection](docs/focal-batch.md), with [editable sources](examples/focal).

Latest release: [five material-presence Shorts and reflection](docs/material-batch.md), with [editable sources](examples/material).
