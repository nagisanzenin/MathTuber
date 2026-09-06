# Channel identity across agents

A new model must be able to work from this package without prior chat history.
For IVisualizeThings use `init --project PATH --manifest FILE --profile ivisualizethings-workshop`.
For another channel select its profile ID or JSON path. Do not silently use this channel's identity for everyone.
`init --profile` pins the profile and records `required_profile`. Removing or replacing that binding with another ID blocks plan-check and render. Legacy projects without a required identity remain supported; migrate channel work by declaring `required_profile` and binding it.

Before coding, read the pinned JSON and profiles.md, and VIEW identity-reference.png and mechanism-references.jpg in this directory. These are drawing/reference aids, not evidence of viewer preference. The contact sheet compares acceptable palette/type/spacing with specific layout failures; do not copy a single composition into every episode.

Use `<plugin-root>/examples/channel_scene.py` as a runnable starting point, not a storytelling template. `WorkshopScene` supplies profile lettering and geometry. Both scene bases now inherit the profile background and legacy color aliases; plain Manim Scene is rejected for profile-bound renders. Hardcoded colors/fonts can still bypass helpers: inspect them and remove unintended overrides. Explicit caption style overrides also require visual review. Renderer enforcement is not a security boundary or a beauty guarantee.

Keep fixed: channel palette, lettering family (documented fallback), caption treatment, readable object identity. Vary: mathematical domain, camera composition, mechanism, narrative and timing. Math first; tranquil delivery does not mean static frames or only geometry.

Use `assert_safe` for essential groups at opening, payoff and transition endpoints. It checks a conservative portrait region only; it cannot detect label collisions, tiny text, caption reflow, intermediate motion or platform UI changes. Keep annotation and subtitle regions separate. Compare a captioned prototype at phone size before full production. Inspect critical transitions through completion. Never mark visual review passed from a filename or successful render.

## Independent handoff evaluation

Give each available model a fresh context containing only this plugin and the same brief:
“Create a 60–90 second IVisualizeThings explanation of pairing 1 through 100. Use the pinned channel profile, show why the pairing works, and include a transfer example. Produce the hardest captioned prototype first. Do not upload.”

Repeat on averaging predictions (ML) and compound growth (daily life). Record host/model/version, prompt, loaded plugin/profile hashes, scene source, preview, actual visual evidence and repairs. Evaluate separately: math correctness, identity consistency, cropped/overlapping labels, correspondence through motion, explanatory clarity, and listening if available. Record unavailable checks honestly. Do not equate passing Python fixtures with a successful Gemini/Claude/Pi model trial. No real-model comparative result is claimed by this release.

A failed prototype must be revised before full production. Aesthetic exceptions need a reason in profile_application.exceptions and must be inspected; they are not blanket permission to ignore the channel.
