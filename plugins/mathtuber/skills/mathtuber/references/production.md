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
