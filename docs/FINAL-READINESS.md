# MathTuber handoff

MathTuber is an agent-first local production plugin. The installed host agent researches, reasons, writes Manim and judges the result. Local tools provide speech, rendering, assembly, evidence, resumable state and authorized YouTube publishing. The production workflow does not require a separate LLM API orchestrator or this conversation's private helper scripts.

The current release is a usable open-source implementation with explicitly bounded verification. It is not a guarantee that every host model can independently make excellent films.

## Start on another host

Follow the [installation instructions](../README.md#install), retain the complete repository in a stable location, and install the adapter for the chosen host. Run doctor and resolve the capabilities needed for that project. Native Codex and Claude installations must be refreshed after changing a versioned plugin; start a fresh host session to load the new skill. Generic skill links and inline adapters resolve the complete plugin, not a detached SKILL.md.

Then ask the host, for example:

> Use MathTuber to create a math-first Short explaining why averaging predictions can reduce squared error. Aim for a curious beginner, use a calm elegant style, make the mechanism visible and keep the claim's limits clear. Inspect the rendered media and report the review scope. Save the final video locally.

Publication requires the user's explicit instruction or applicable saved authorization, credentials outside Git, current final review and successful mechanical checks. Use the [publishing workflow](../plugins/mathtuber/skills/mathtuber/references/publishing.md). All members of a batch must pass review before its first upload. Read publication status after an interrupted upload; preserve receipts and reconcile uncertainty instead of duplicating videos.

## Knowledge available without this conversation

| Need | Bundled resource |
| --- | --- |
| Determine what to do next | [State-based navigation](../plugins/mathtuber/skills/mathtuber/references/navigation.md) and engine status |
| Understand command inputs and outputs | [Command contract](../plugins/mathtuber/skills/mathtuber/references/commands.md) |
| Plan and produce a film | [Production guide](../plugins/mathtuber/skills/mathtuber/references/production.md) |
| Preserve mathematics-first topic breadth | [Channel direction](CHANNEL-DIRECTION.md), pinned profile and editorial mix |
| Make a valid animation understandable | [Annotated decisions](../plugins/mathtuber/skills/mathtuber/references/annotated-decisions.md), transition consistency and ending-case guides |
| Repair a concrete failure | Offline `scripts/knowledge.py --query "symptom"`; filter by stage or retrieve an exact note ID |
| Reuse tested mechanics | [Runnable recipes](../plugins/mathtuber/recipes/README.md) and profile scene primitives |
| Understand the educational rationale | [Research library](research/README.md) and bundled creative theory |
| Evaluate a different or smaller model | [Controlled handoff protocol](HANDOFF-EVALUATION.md) |

The repository's editable examples provide additional source material; core plugin operation does not depend on their presence in a native cache. Adapt the mechanism to the explanation rather than making every film share a template.

## Verification and remaining limits

[Current verification](verification.md) records the actual platform matrix. Codex and Claude native caches match all 71 current non-bytecode plugin files and execute doctor from an unrelated directory. Pi's real loader and tool transport pass against a simulated model. ZCode and OpenCode discovery were checked; Gemini's authenticated extension loading remains untested. Renewed Claude/Pi model login was explicitly waived by the project owner.

The final implementation passes 128 unit tests. The [committed archive fixture](handoff-verification.json) tests installation, paths with spaces, native rendering, caching, assembly, decoding and review gates. It reuses the existing macOS runtime; it is not a clean OS setup test. [Pi evidence](pi-verification.json) does not establish model reasoning competence. Live publication evidence is in the release ledger and individual batch reports.

The strongest production checks in the final batch combine exact mathematics, current full-source transcription, full-file decoding, signal measurements and actual inspection of all sampled evidence pages. They do not replace continuous viewing and listening. A host must describe the modalities it actually used; unavailable perception cannot be replaced with fabricated approval.

Several local faster-whisper processes terminated with a native mutex error during final production. Subsequent calls produced or retrieved complete current reports; no underlying library fix is claimed. Keep this dependency issue visible if it recurs on another machine.

TikTok upload is researched but not implemented. Gemini TTS and generic MLX support are not production-verified alternatives to the tested Kokoro path. Analytics-driven improvement, human comprehension/retention evaluation and independent weaker-model filmmaking evaluation are unfinished future work. Local media avoids paid inference calls for speech/rendering, but host subscriptions, compute, setup downloads and external platform quotas still apply; no controlled cost or speed superiority benchmark was run.

## Stop condition and editorial judgment

The authorized run ends at twenty production cycles. The final [batch reflection](synthesis-batch.md) records meaningful mathematical mechanisms and remaining weaknesses: abstract openings, static explanatory stretches and limited artistic variation. A coherent restrained palette is useful, but it does not establish exceptional beauty, engagement or reduced fear of mathematics. Quality has not reached a demonstrated ceiling.

Any future iteration should target evidence of viewer understanding and interest, and evaluate another model from the installed package alone. This handoff preserves the knowledge and safeguards needed for that work without claiming those evaluations have already happened.
