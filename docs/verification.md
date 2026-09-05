# Implementation and verification — 2026-09-05

This is the implementation record. `architecture.md` includes a broader target roadmap; not every researched adapter or feature is implemented.

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

## Executed checks

- 30 unit tests: state, path escapes, lock contention, cache invalidation, missing scenes, review evidence/acceptance gates and mocked YouTube publication/retry/visibility behavior.
- Native Manim → FFmpeg fixture: render, cached rerender, complete assembly, decoding verification and evidence extraction all passed.
- Docker Manim → FFmpeg fixture: the same checks passed with network disabled, read-only root/inputs and bounded resources.
- Pi loader/protocol integration: all five checks passed using installed Pi, actual bash execution and a local simulated model endpoint. See `pi-verification.json`.
- Codex plugin validator and skill validator passed.
- A real six-scene English Kokoro/Manim proof exported successfully at 1080×1920, 30 fps, **131.488 seconds**. All scenes and speech tracks are present; full decode and duration checks passed.

On Apple M2 / 16 GiB, the six-section speech batch took **94.31s** and final scene rendering took **90.11s** summed across scene workers. This excludes setup/downloads, authoring, previews, assembly and review. These are first-run measurements of this project, not a comparative performance claim. Dependencies and model weights are shared across plugin hosts. Cache fixtures demonstrate skipped identical rendering; unit tests demonstrate local scene edits preserve unrelated render fingerprints and preserve speech.

The root agent inspected 18 actual sampled frames via a contact sheet. The square-growth construction and algebra are consistent and readable in the samples. This is sampled visual review, not full motion or acoustic review. Final acceptance was deliberately not fabricated; publication remains gated. No claim of vastly superior quality has yet been validated against the old channel with matched prompts and human ratings.

## YouTube readiness

Legacy credentials were migrated using a restricted pickle allowlist into a protected JSON file outside Git. A read-only channel-readiness check failed with Google `RefreshError`: that existing OAuth connection requires reconnection before a live upload. No upload was attempted. Mocked publisher tests cover channel mismatch, uncertain initialization, receipt reuse, metadata updates and public-to-private changes. Live resumable upload and Google processing remain unverified.

## Implemented versus planned

Implemented: portable skill and manifests; shared local runtime; content-addressed artifacts; per-scene renders; batched Kokoro; measured narration timing; predicted word-timestamp SRT; native/Docker rendering; background jobs; atomic state; complete timeline assembly; mechanical checks; evidence bundle/review gate; resumable YouTube worker; legacy credential migration; editable example.

Planned/experimental: generic MLX model-specific support, Gemini TTS fallback, local ASR/forced alignment, automated layout geometry diagnostics, advanced shot transitions, learned channel style profiles, parallel rendering across one project, scheduling/analytics and a calibrated quality benchmark. The engine currently serializes project writes to avoid races. SRT is provided as a separate artifact; `captions.burn_in=true` additionally creates ASS captions, burns them into the MP4 and normalizes loudness. This opt-in path was exercised on the 143-second necklace project.

## Primary references

- [Omniplugin](https://github.com/nagisanzenin/omniplugin), inspected commit `3b72803214fd3fc3becbc68ea2d31b9d9d4999bf`.
- [SmartUber](https://github.com/nagisanzenin/smartuber), inspected commit `7bc16868319b8422efdc24e207975777d8896bd0`.
- [Codex plugin format](https://developers.openai.com/plugins/build/plugins).
- [Claude Code plugins](https://code.claude.com/docs/en/plugins).
- [Pi packages](https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/packages.md); runtime checks additionally used the actual installed `@earendil-works/pi-coding-agent` docs.
- [OpenCode skills](https://opencode.ai/docs/skills/).
- [Gemini CLI extensions](https://geminicli.com/docs/extensions/writing-extensions/).
- ZCode's installed `zcode-guide-plugin/skills/diagnosing-plugins/SKILL.md` and actual `plugins list`/`skills list` commands establish the supported inline directory format.
- [Kokoro model](https://huggingface.co/hexgrad/Kokoro-82M), [Manim documentation](https://docs.manim.community/en/stable/).

## Follow-up production validation

The OAuth connection was renewed and real resumable uploads subsequently completed with public visibility confirmed by the YouTube API. The follow-up production used independent local faster-whisper transcription plus source/final audio signal measurements, sampled rendered frame inspection, measured speech cues, exact math enumeration/derivations and full-file decoding. This is an automated technical/content review, not a claim of subjective human listening or continuous human viewing. Account identifiers, upload credentials and channel inventories are kept outside this repository.

## Evidence-informed discovery batch

The subsequent [five-video batch](discovery-batch.md) completed public YouTube processing, 37 unit tests and scoped production review. The linked report records actual checks and their limits. The earlier historical checkpoints above remain as the development record.
