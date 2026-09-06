# Current implementation and verification

Checked 2026-09-06. MathTuber provides one complete local plugin, host adapters and evidence-scoped production/publication tools. The host model supplies reasoning and creative work. Platform installation is not proof of autonomous filmmaking quality.

## Platform compatibility

| Host | Installed version | Actual evidence | Limit |
|---|---|---|---|
| Codex | 0.153.4 | Local marketplace/plugin installation; a real model read the installed skill and executed engine doctor + project status successfully | Bounded tool smoke, not a complete autonomous film evaluation |
| Claude Code | 2.1.261 | Native marketplace install and versioned plugin update succeeded | Real model call failed OAuth refresh; user waived login testing |
| Pi | 0.85.0 | Native package install; real Pi discovered/expanded the skill and executed bash through a local model-protocol fixture | Model was simulated; no provider account configured |
| ZCode | bundled CLI 0.16.5 | Native inline plugin loader reports enabled=true and skillCount=1; qualified skill discovered | Real model invocation requires model configuration |
| OpenCode | 1.18.23 | Official global skill directory symlink; `opencode debug skill` returns full MathTuber skill | No model generation test |
| Gemini CLI | 0.27.0 | Extension manifest and skill tree follow official extension docs; installer provided | CLI requires authentication even for extension link on this installation; not installed or runtime-tested |

The user explicitly accepted documentation/omniplugin conformance instead of renewed Claude/Pi logins. No claim that all six hosts have completed a real-model video production. Skills do not give a text-only host audio/video perception: media review uses capabilities of the selected host.

## Final verification

- 128 unit tests passed on the current implementation: state, caching, review gates, scene helpers, speech/caption timing, media sampling and publication/retry behavior.
- Codex and Claude native caches were refreshed. All 71 non-bytecode plugin source files matched each installed cache; each cached engine ran doctor from an unrelated working directory. [Cache evidence](native-cache-verification.json).
- Real Pi loader, skill expansion and bash transport passed all five checks against a local simulated model endpoint. [Pi evidence](pi-verification.json).
- Plugin and skill validators passed. Generic installation and native media can be reproduced with `tests/integration_handoff.py`; its committed archive revision and scope are recorded in [handoff evidence](handoff-verification.json).
- Live YouTube uploads, successful processing and public visibility are independently verified in the batch release reports. The initial OAuth failure is resolved and belongs only to the historical record.

Existing macOS dependencies were reused. These checks do not establish clean operating-system bootstrap, current Docker behavior on every machine, authenticated generation on every host, or competence of a weaker model. The earlier Docker fixture and bounded real Codex model smoke remain historical evidence, not fresh cross-platform full-film evaluations.

## Available production capabilities

Shared local Kokoro speech, imported WAV narration, Manim rendering, native and Docker execution paths, content-addressed artifacts, per-project serialization, measured speech cues, optional burned captions/loudness normalization, original synthesized sound layers, pinned channel profiles, background jobs, full-file mechanical verification, local optional ASR, sampled visual evidence, explicit current review gates, resumable YouTube upload, quota waiting and independent publication readback are implemented.

The plugin includes navigation, searchable repair notes, tested scene primitives and runnable recipes. [Knowledge handoff evaluation](HANDOFF-EVALUATION.md) defines a controlled evaluation for another model; that evaluation has not been completed. No transcript or successful render automatically approves a film.

TikTok publishing, Gemini TTS, general model-specific MLX compatibility, automatic perceptual layout checking, analytics-driven optimization and a calibrated audience-quality benchmark remain unimplemented or experimental. Media perception comes from the host; a text-only host does not gain vision or hearing by installing the plugin.

## Reproduce

Run from the repository root using the configured media Python for native media checks:

```sh
python3 -m unittest discover -s tests -p 'test_*.py'
python3 tests/integration_handoff.py --output /tmp/mathtuber-handoff.json
python3 tests/integration_pi.py --output /tmp/mathtuber-pi.json
```

The handoff fixture extracts committed files only, installs the generic skill twice, resolves the full plugin, runs from another directory with spaces, renders and assembles a four-second tone fixture, checks caching and decoding, and confirms that an unreviewed film remains unaccepted. A tone fixture tests mechanics, not speech or editorial quality. Optional ASR explicitly disabled during that fixture is reported as unavailable.

[Historical checkpoints and primary references](verification-history.md) preserve earlier observations without treating them as current status. [Architecture](architecture.md) includes a broader roadmap; it is not an implementation checklist marked complete.
