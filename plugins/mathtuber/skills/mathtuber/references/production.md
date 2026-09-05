# Production judgment

Solve the mathematics before polishing. Record assumptions and distinguish a proof from a simulation. Verify identities/examples with symbolic or numerical tools when useful; a set of examples is not a proof.

Choose a visual that performs the explanation: preserve object identity, use consistent colors for concepts, and reveal the relevant transformation when it is spoken. Keep one clear learning objective. The opening poses a question; the ending resolves it. Avoid filler to reach a requested duration.

Plan narration and visual beats together. Normalize equations into spoken language (x squared, n plus one); keep display math distinct. Synthesize by coherent sections. Actual WAV duration controls scene duration. If total length misses the brief, revise before final rendering.

The optional `components.NarratedScene` gives `target_duration`, `cue(fraction)`, `finish()`, and a restrained dark theme. Fractions are coarse timing aids. For precise speech synchronization use the measured word timestamps in the audio sidecar and explicit waits. Design any Manim scene you need; components are helpers, not the allowable visual vocabulary.

Use quick previews for layout/motion, then final resolution for typography. Avoid placing crucial content near the bottom or right edge where Shorts UI overlays it. Check at phone scale. A long hold may be pedagogically intentional but must not hide a failed animation.

Review math, visual clarity, timing, and speech separately. Locate defects by timestamp and propose a specific change. Preview fast transitions with multiple adjacent frames or actual video. Final review includes assembly transitions and captions. Do not use scores alone as evidence.

Keep source files under scenes/ and assets/ so dependency tracking includes helpers. Keep external imports pinned in the runtime. Each project is independent, so resuming on another platform only requires the same project path and plugin/runtime installation.
