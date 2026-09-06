# Channel identity portability

The Gemini Gauss clip prompted a local code audit. It showed that legacy NarratedScene defaults could produce a dark palette while WorkshopScene used the channel's warm paper identity. The clip alone cannot establish which instructions Gemini read or which source it used.

New channel projects should use `init --profile ivisualizethings-workshop` (or another channel's profile). This pins the asset and records required_profile. Plan and render checks reject a missing or mismatched required identity. Both scene bases inherit palette/background, including legacy aliases imported by authored code. Bound renders reject plain Manim Scene. Existing unbound projects remain supported; channel projects should migrate explicitly.

The portable plugin now includes an executable starter, an annotated identity reference, safe-region checks and a fresh-context evaluation brief. These travel with the plugin rather than requiring repository history. Channel-specific guidance is in skills/mathtuber/references/channel-handoff.md.

Validation: Python suite passes; real Manim checks cover legacy palette inheritance, font selection and out-of-bounds rejection. The starter rendered at 360×640 and its first frame was inspected. The annotated reference was inspected too. This is a mechanical/visual smoke check, not a full educational video or audience test.

Limits: authored code can override colors/fonts or setup. Safe bounds do not detect overlaps, tiny lettering, caption reflow or motion between inspected states. Models must inspect captioned prototypes and critical transitions. No independent Gemini/Claude/Pi generation comparison was performed for this change. The supplied three-topic protocol is the next empirical validation, not a claimed result.
