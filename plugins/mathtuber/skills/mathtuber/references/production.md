# Production judgment

Solve the mathematics before polishing. Record assumptions and distinguish a proof from a simulation. Verify identities/examples with symbolic or numerical tools when useful; a set of examples is not a proof.

Choose a visual that performs the explanation: preserve object identity, use consistent colors for concepts, and reveal the relevant transformation when it is spoken. Keep one clear learning objective. The opening poses a question; the ending resolves it. Avoid filler to reach a requested duration.

Plan narration and visual beats together. Normalize equations into spoken language (x squared, n plus one); keep display math distinct. Synthesize by coherent sections. Actual WAV duration controls scene duration. If total length misses the brief, revise before final rendering.

The optional `components.NarratedScene` gives `target_duration`, `cue(fraction)`, `finish()`, and a restrained dark theme. Fractions are coarse timing aids. For precise speech synchronization use the measured word timestamps in the audio sidecar and explicit waits. Design any Manim scene you need; components are helpers, not the allowable visual vocabulary.

Use quick previews for layout/motion, then final resolution for typography. Avoid placing crucial content near the bottom or right edge where Shorts UI overlays it. Check at phone scale. A long hold may be pedagogically intentional but must not hide a failed animation.

Before freezing a difficult scene, run `python3 <root>/scripts/caption_preview.py --project <path> --scene <id>` after its current preview render. This uses the same caption phrasing/style logic as final assembly, with local narration at preview resolution. Inspect the returned file; it is a scene prototype, excludes the soundtrack, and never records an accepted final export.

Match spoken quantifiers to intermediate states: in recursive interpolation, the final point can reach an endpoint while an intermediate point remains elsewhere. Check the referent of “all,” “equal” and “shortest” as well as the final conclusion. During linked motion, inspect the midpoint and completion. With Manim `UpdateFromAlphaFunc`, animate a group containing every object the callback changes; mutating markers outside that group can leave their static cached images behind.

For exact diagrams or numerals, `WorkshopScene.focus_outline(target)` offers emphasis without changing the target's geometry or fill. Default scaling/recoloring effects can change a displayed relationship or erase glyph contrast. These are optional helpers, not a required visual vocabulary. Let the subject determine the composition; persistent top headings are optional. Place brief identifying labels near the relevant objects, while keeping narration captions in a stable readable area.

Review math, visual clarity, timing, and speech separately. Locate defects by timestamp and propose a specific change. Preview fast transitions with multiple adjacent frames or actual video. Final review includes assembly transitions and captions. Do not use scores alone as evidence.

Keep source files under scenes/ and assets/ so dependency tracking includes helpers. Keep external imports pinned in the runtime. Each project is independent, so resuming on another platform only requires the same project path and plugin/runtime installation.

For a deliberate pause after a key idea, opt into `speech.paragraph_pause_seconds` and separate spoken paragraphs with a blank line. Silence is inserted between paragraphs and later word timestamps shift with it; single newlines do not add pauses. Keep the relevant relationship visible during the pause. Recompile cues and inspect the actual captioned sequence. Imported WAV audio owns its timing and rejects this synthesis-only option. See `docs/research/QUIET-BEATS.md` in the repository for evidence and limits; the agent chooses where a pause helps.

For a process whose rate matters, use `self.process_clock(rate=1, initial=0)` and read its `.value` in object updaters. The clock follows renderer time across `play` and `wait`; `.pause()` / `.resume()` retain phase during deliberate inspection. Add it before dependent objects; clearing the scene removes its invisible driver. Use static states when the viewer must compare spatial structure. This is an optional presentation clock, not a physics integrator or a requirement for constant movement. See `docs/research/PROCESS-AND-INSPECTION.md` for the evidence and limits. Measure the full quiet gap around paragraph pauses: inserted silence adds to silence already present in synthesized speech.

For a selected inspection or listening window, put `paragraph_pauses: [0.4, 4.0, 0.4]` on the scene containing four blank-line-separated paragraphs. Every boundary has an explicit duration in seconds (0–10); list length must equal paragraphs minus one. This overrides the global pause for that scene. It adds no leading/trailing silence. Re-synthesize after editing it: audio cache keys include the list. Use the resulting `paragraph_pauses` timestamps to place a demonstration inside the speech-free interval; captions and later cues follow the shifted word timeline. Imported audio rejects this option. A listening window is an authored experiment, not evidence that adding sound improves learning.

Before final review, run `python3 <root>/scripts/ending_preview.py --project <path>` on the current assembled export. Inspect its last fifteen seconds as a sequence, including the final decodable frame. Use `--seconds` to cover a longer authored conclusion. The hash-bound sheet supplements critical-interval review; it does not prove continuous pacing or audiovisual quality. Ask what the ending lets the viewer see or infer that was unavailable at the opening. When useful, change one meaningful condition, allow an unhurried observation, visibly resolve it, then return to the original object. Do not append a quiz, generic inspiration, or a new unanswered problem by default. A narrator summary is not evidence of learner-generated explanation. See `docs/research/ENDINGS-AND-CURIOSITY.md` for the research and limits.

### Focal staging

Use `WorkshopScene.stage_focus(subject, center, width, height)` when moving the same drawn object into a closer explanatory view helps. It uniformly fits an existing group into an authored rectangle, leaving camera and captions fixed. Include the reference level, partner or endpoint needed to understand the detail. Subjects with active updaters are rejected: pause their process, remove/rebuild geometry updaters with the new coordinate mapping, and resume deliberately. A bounding box is not an attention or aesthetic score. Inspect the entire transition and attached labels on the final export. See `docs/research/FOCAL-STAGING.md` in the repository for the evidence and its limits.


### Material presence without losing the explanation

A tangible bob or bead may use `WorkshopScene.bead(radius, color, layers=18)` for a restrained painted volume. The silhouette remains circular. It is a stylized depth cue, not a physical shading simulation. Probability dots, area comparisons, symbolic points and magnitude-encoded fills should remain unambiguous mathematical marks. Keep lighting orientation stable when moving an object; rotate an attached physical marker separately if needed.

Before extending this treatment across an episode, render a small comparison and inspect both object recognition and the causal relation. Material richness and explanatory clarity are separate judgments. Preserve recognizable context while bringing relevant parts closer. Do not count perceived depth as evidence of learning, enjoyment or retention. Avoid fading in an object already visible in the opening: establish it once and let its actual motion begin.

### Make the reasoning inspectable

When a middle passage merely adds labels to an unchanged diagram, consult [visible reasoning](visible-reasoning.md). State the before, change, preserved reference and after-inference in the storyboard. Animate the relationship only when it contributes evidence: a rearrangement, equal displacement, paired area comparison or visible superposition. Synchronize the operation with its phrase, inspect intermediate states and retain a legible endpoint. A highlighted object alone is not an explanation. Use native geometry and existing cue tools; no new service or mandatory effect is required. See `docs/research/VISIBLE-REASONING.md` for the primary studies and their limits.

### Compare mechanisms before rendering a batch

When the user requests new topics, compare the proposed learning goal, governing relationship and visible operation against earlier project manifests and release reflections. A different title or setting does not make the same proof new. Record the closest earlier episode, the substantive difference, and a decision before synthesis or rendering. Use archived titles only as an initial search aid; explicitly record when earlier transcripts or project sources are unavailable. A failed comparison requires a replacement topic before publication.

For example, two garden films both reassembling a fixed-perimeter rectangle to expose its squared area deficit are duplicates even with different narration. Changing that proposal to a semicircle construction of the geometric mean changes both the theorem and the proof operation. Keep a mechanism index alongside published examples so future agents can retrieve these relationships without repeatedly reading every frame.

### When the films still feel like detached diagrams

Apply [physical context](physical-context.md): prototype a recognizable subject and useful setting, preserve correspondence into the mathematical explanation, and inspect the result before expanding the batch. Treat the sequence as an editorial hypothesis; concrete-first is not a universal rule.

### When sound can perform the explanation

Use [explanatory listening](explanatory-listening.md) for explicit tones inside measured speech-free pauses. The shared score compiler preserves both action events and listening plans. Make the relationship visible for muted viewing and distinguish signal validation from subjective listening.
