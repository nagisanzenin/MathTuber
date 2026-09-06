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

## Portable review and quota recovery — 2026-09-06

The shared publisher now records a definite daily quota rejection as `quota_wait`, preserves any resumable session, and stops batch publication with exit code 2. It returns the pending wait without API calls until the Pacific reset plus ten minutes. Unknown initialization outcomes still stop for reconciliation. The quota change passed 109 unit tests and CI; the daily rejection itself was encountered in live production, while after-reset recovery is covered by simulated transport and awaits a live reset. Published receipts remain authoritative; a partial batch is not a completed release.

Independent audio inspection is now a bundled command, rather than a private batch helper. `scripts/audio_review.py` uses current artifact fingerprints, local optional faster-whisper, complete source text comparisons and source/final signal measurements. It never writes a review verdict. A real 98.1-second production export was checked through the portable command: the entire source transcript was read, reported differences were number formatting, and both source and final measured clipping fractions were zero. This remains technical/transcription evidence, not subjective listening. The report binds the exact source and final hashes; the accepted export was unchanged.

The current suite has 116 unit tests. Three additional real-worker audio-inspection tests cover stale input rejection, opposing stereo peaks and changed mathematical wording without requiring an ASR download. ASR inference was exercised on the existing macOS runtime and cached model weights; this does not establish fresh installation or real-model filmmaking on every host.

`scripts/visual_review.py` now bundles final distributed frames, opening samples, all compiled cues, every declared critical interval and the final video frame. It handles scene-local cue offsets in multi-scene timelines, rejects incomplete interval mappings, preserves aspect ratio and paginates sheets. A real FFmpeg fixture checks landscape geometry, page splitting, hashes and final-frame extraction. The real 98.1-second film produced 77 sampled frames in 14 pages; four selected pages were actually inspected for opening, cue, interval and final-frame output. This tool validation is separate from the film's earlier final acceptance and is not a claim that all newly extracted samples were viewed.

The subsequent publication-status addition brings the unit suite to 120 tests. `scripts/publication_status.py` independently reads visibility, processing and duration for the exact current-export receipt. A live five-entry readback correctly reported one public/processed video, one quota wait and three unattempted videos, without inserting or updating a video. Transport tests enforce the read-only path; report tests require both correct visibility and successful processing. Clean-install/handoff checks and the final readiness report remain pending after the authorized production cycles.

## Committed archive handoff smoke

[Machine-readable check results](handoff-verification.json).

A tracked-file archive of commit `0cf0d4f55f748bc7d19f28937d71a52adc1b517e` was extracted into a separate directory with spaces. The generic skill installer ran twice without duplicating or overwriting the skill; resolving that symlink found the complete plugin. From another working directory, engine doctor, portable command entry points and the real native four-second media fixture passed: imported tone, render, cached rerender, assembly, full decode and frame extraction. The resulting film remained unaccepted. Audio inspection correctly reported ASR unavailable when explicitly disabled. This reused the existing macOS runtime; it was not a clean OS installation, host-model test or speech-quality evaluation. The reproducible check is now `tests/integration_handoff.py` and intentionally tests committed files only.

The handoff review exposed overly broad doctor readiness: render-package detection alone could hide missing narration dependencies. Doctor now lists capability-specific dependency gaps and explicitly excludes authentication, model downloads and runtime import success from its claim. Regression tests cover render-only installations, optional ASR and Pacific timezone availability. The suite now has 123 unit tests; the real current runtime reports all listed dependencies present. Final native-host installation/update checks and the cycle-twenty readiness report remain outstanding.

## Current native cache update check

The versioned Codex and Claude caches were refreshed on 2026-09-06. Seven representative engine/skill files match current source byte-for-byte, and each installed engine executed doctor successfully from an unrelated directory. Claude initially reported the old version as current; advancing its manifest version and refreshing its local marketplace resolved that stale installation. See [native cache evidence](native-cache-verification.json). Existing media dependencies were reused; no model or OAuth call was made. Start a fresh host session to load updated skills. ZCode's native loader still reports the inline plugin enabled with one skill; Pi's installed package resolves to the local repository.

Cue preflight now checks missing/repeated literal phrases against narration before synthesis without reading audio or replacing measured timings. Two regression tests cover complete diagnostics and preservation of real timing artifacts. The unit suite has 125 tests; CI passed for commit `ca5b70d`. This script check is not pronunciation or synchronization review.
