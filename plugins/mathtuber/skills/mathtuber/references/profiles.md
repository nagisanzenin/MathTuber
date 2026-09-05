# Channel profiles

Profiles are portable creative guidance and optional drawing primitives. They do not choose a topic, write a script or score taste. Keep channel promise and identity stable, select an appropriate format, and invent the episode composition. Platform delivery constraints remain separate.

`profile-list` lists bundled profiles. After init, use `profile-bind --project PATH --profile ivisualizethings-workshop` (or an absolute JSON path). The engine copies a validated, content-addressed snapshot into project assets. It does not follow a mutable external profile. Use `--replace` for an intentional update; re-render and review the resulting changes. Custom profiles follow the bundled JSON structure and may define their own formats.

Add `creative.profile_application` with `format` (a key in profile.formats), `signature` (how this episode enacts the channel identity), `episode_variation` (what is original about its visual explanation), and `exceptions` (list of justified preference deviations, possibly empty). Run `profile-check` or `plan-check`. These check completeness, not recognition, beauty or learning.

The candidate workshop profile uses warm paper and tactile objects, but is not an audience-validated best style. It is a concrete starting direction. `components.WorkshopScene` reads the pinned profile through the render worker and offers `lettering` and `tile`; use custom exact geometry when these are inappropriate. Use color with labels, shape or position. Do not distort mathematical quantities to satisfy a material or motion preference.

Iterate the key visual, explanation and script together. Prototype a consequential transformation at preview resolution before scaling a new direction across a batch. Compare actual images and motion; retain annotated examples and exceptions. A channel profile should work across different topics, not force every topic into the same scene layout.

A profile project review additionally records `profile_review` strings for identity, variation, exceptions and limitations. Describe evidence and departures; no numeric brand-fit score. Agent inspection does not measure audience recognition. Keep full-motion review and subjective listening coverage honest.

The research and proposed viewer experiments are in repository docs/research/CHANNEL-PROFILES.md. Compare recognition, appeal and comprehension separately; real viewer testing is still needed.
