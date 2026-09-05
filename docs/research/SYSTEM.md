# MathTuber: proposed creative system specification

Status: architecture proposal, not implemented runtime behavior. Research date: 2026-09-05. Read THEORY.md for the rationale and EVIDENCE.md for the evidence boundaries.

**Purpose and governing decisions**

The native agent plans, critiques and revises. Portable deterministic tools handle reproducible calculations, media generation, inspection assets, assembly and publishing. The architecture is platform-independent: explicit files and state transitions should work with the host agent rather than require a proprietary agent framework or extra paid model API calls.

Use research as conditional guidance. Separate product requirements, evidence-backed defaults, local hypotheses, aesthetic choices and platform rules. Never label all five as 'scientifically proven.'

The user permits 4–5 minutes when needed. YouTube Shorts currently have a three-minute maximum for square/vertical uploads; longer work needs a regular-video profile. [Official guidance](https://support.google.com/youtube/answer/15424877?hl=en)

**Required planning artifacts**

| Artifact | Required information | Purpose |
|---|---|---|
| audience.json | Prior knowledge, language, likely motivation, device, accessibility needs, familiarity with topic; assumptions explicitly marked | Prevent a mathematically expert author from silently assuming an expert audience |
| brief.json | One primary experiential/learning purpose, intended takeaway, format constraints, acceptable length range, publication authorization scope | Define what completeness means |
| claims.json | Claim, assumptions, exact verification, scope of illustration, sources, dependencies | Preserve mathematical truth through script and visuals |
| concepts.json | At least two genuinely different hook/representation proposals when the creative choice is uncertain; costs and risks | Explore before polishing |
| beats.json | Viewer knowledge before/after, live question, intended inference, focal object, visible action, narration, sound, duration, prerequisite and claim IDs | Make every beat reviewable |
| representations.json | Object identity, mathematical meaning, allowed transformations, invariants, scale/area conventions, simulation or exact status | Prevent misleading animations |
| style.json | Stable channel vocabulary plus episode-specific staging and assets | Recognition without identical layouts |
| sound.json | Voice direction, pronunciation dictionary, music intent by beat, silence, SFX semantics, stems, licenses | Give audio the same planning status as images |
| reviews.json | Dimension, observation, timestamp/frame, consequence, revision, provenance, actual modalities inspected | Avoid unsupported quality approvals |
| experiment.json | Hypothesis, intervention, audience, comparison, outcomes, design, stopping rule, limitations | Turn taste changes into testable decisions |
| production-metrics.json | Stage times, cache hits, model usage if available, rerenders, asset reuse | Improve cost and speed without silently reducing quality |

These files are contracts between stages, not evidence that the contracts have been satisfied. The schema can begin lightweight and grow only when fields influence a real decision.

**Format selection**

1. Define the complete intended takeaway and prerequisites.
2. Build a rough sequence with real narration timing and time for looking, comparing and thinking.
3. If it fits comfortably within 180 seconds and mobile vertical composition, consider a Short.
4. If it requires 4–5 minutes, use a regular video. Consider 16:9 for simultaneous comparisons or broad constructions; retain vertical only when the intended composition benefits. This is an editorial choice, not a platform requirement.
5. If both formats are worthwhile, share claims and underlying mathematical assets, but write separate narratives and layouts. Do not simply crop or speed up the long version.
6. A Short may teach a narrower, complete insight while the regular video develops the proof. It must resolve its own advertised question.
7. Verify encoded duration and dimensions before publishing. Leave a small configurable encoding margin below a hard platform boundary; the margin is engineering practice, not a content-quality principle.
8. Recheck platform rules when deploying or changing a platform profile. Store verification date and source.

Proposed profiles: youtube_short (duration at most 180 seconds, square/vertical); youtube_regular (user-approved 240–300 seconds when useful, aspect ratio chosen for explanation). The second range is a preference, not a scientific optimum or mandatory minimum.

Regular-video packaging needs its own honest title and thumbnail; Shorts additionally need an effective first visible moment. Measure these entry points using the appropriate platform denominators.

**Beat contract example: dice**

```json
{
  "id": "dice_counter_explanation",
  "claim_ids": ["A_beats_B_two_thirds"],
  "viewer_before": ["knows a die has six equally likely faces", "knows higher roll wins"],
  "open_question": "Why does A have an advantage over B?",
  "focal_objects": ["A_faces", "B_faces"],
  "visible_operation": "Reveal B's six threes; group A's four winning faces and two losing faces",
  "inference": "A wins on four of six equally likely A outcomes because B is constant",
  "viewer_after": ["can explain this matchup without a formula"],
  "misreading_to_prevent": "a two-thirds advantage guarantees the next roll",
  "audio_direction": "clear conversational explanation; emphasize four and six",
  "music_policy": "quiet or absent during counting",
  "sfx_policy": "one restrained selection sound; no sound on every numeral",
  "hold_policy": "enough time to inspect both groups, determined in animatic review",
  "assessment": "Which two faces lose, and could A still lose the next roll?"
}
```

**Review stages**

| Stage | Decision | Evidence required | Repair route |
|---|---|---|---|
| Mathematical brief | Is the promise correct and feasible? | Claim derivation, assumptions, prerequisite graph | Narrow or change the promise |
| Concept selection | Is the situation legible and worth exploring? | Competing storyboards, specific critique | Try a different representation/hook |
| Animatic | Can a newcomer follow the sequence at actual pace? | Timed rough playback, visible objects, scratch audio, critique of gaps | Revise beats before final rendering |
| Visual production | Are actions and relationships perceptible? | Final-size frames plus motion review at transitions | Change scale, continuity or timing |
| Audio production | Is narration accurate, intelligible and appropriate? | ASR/signal checks plus actual listening when available | Regenerate phrase or remix stems |
| Complete experience | Does the promise resolve with a usable insight? | Whole-video review, scope and modality recorded | Repair the smallest responsible unit |
| Audience validation | Do actual people enjoy and understand it? | Human observations and/or declared experiment | Update a conditional design hypothesis |
| Publication | Is the reviewed artifact authorized for this destination? | Final hash, applicable review policy, credentials isolated, intent | Resolve actual failed requirements |

Review statuses: observed_pass, observed_fail, unassessed, not_applicable. Human-audience validation is separately labeled pending/exploratory/validated_within_scope. It is not silently inferred from a model's critique.

The standing authorization policy determines whether an automatically reviewed video may publish before human testing. Requiring new confirmation for every routine upload is unnecessary when authorization already exists. Conversely, no model may state that a person listened or that a test audience approved unless that happened.

**Quality evaluation**

Use hard requirements for correct claims, no misleading depiction, legible essential content, valid media and authorized destination. Use anchored qualitative reviews for editorial dimensions:

- Hook: unclear promise / understandable promise / compelling and honestly fulfilled promise.
- Inference: answer asserted / partially demonstrated / viewer can derive the intended relationship from the sequence.
- Orientation: repeated searching / minor friction / continuity and focus are clear.
- Motion: decoration / helpful cue / mathematical change is visibly explained.
- Audio: obstructive or inaccurate / clear / expressive, coherent with the beat and comfortable to hear.
- Payoff: incomplete / resolved / resolved with a usable new capability.
- Identity: generic or repetitive / coherent / recognizable while adapted to this topic.

These are rubric anchors, not calibrated psychological scales. Scores cannot be meaningfully averaged into predicted retention until calibrated. A serious failure remains visible rather than being washed out by strong scores elsewhere.

The critic's first pass should receive the rendered artifact and declared audience, not an essay persuading it that the work is excellent. Ask it to locate errors or friction and propose falsifiable revisions. Compare alternatives without author labels; reverse order to expose preference instability. Use human evidence to audit where the critic was wrong.

**Audio and visual engineering implications**

Keep narration, music and event sounds as separate stems with beat-aligned time anchors. Use editable gain envelopes and ducking. Inspect spoken numbers and names; do not depend on default pronunciation. Mix validation includes the full export, not only source narration WAVs.

Track stable object IDs across scenes. Preserve exact mathematical state independently from drawing coordinates. Validate transformations against that state. Provide a semantic timeline of appearance, movement, comparison and reveal so automated checks can flag simultaneous competing events.

Implement a phone-scale review preset with UI overlays, captions and typical viewing area. A high-resolution render can still be unreadable at actual size. Color must not be the only identity cue; use letters, position, shapes or outlines as well.

Do not require generative video for exact geometry, counts, labels or equations. Use code-controlled assets for those. Generated textures or decorative environments are optional; they must not change the mathematical claim. Two-dimensional motion can be excellent; three-dimensional realism is a creative option with costs, not a quality gate.

**Resource allocation**

Spend early on uncertainty that could invalidate the whole episode. A failed opening or representation should be discovered in a rough animatic. Cache stable narration phrases and reusable assets. Render changed scenes only; remix audio separately. Preserve successful states and stop revision loops when further changes lack a concrete hypothesis.

Suggested development order: (1) claim and beat contracts, (2) full animatic with review provenance, (3) independent sound planning and mixing, (4) flexible scene composition and object continuity, (5) experiment/analytics records, (6) channel vocabulary refined from repeated evidence. These are priorities for implementation, not changes already made.

**Experiments and analytics**

First use a formative test for major failures. Then use independently assigned viewers for learning comparisons. A preference study that shows both variants has carryover and should not be presented as a first-exposure learning experiment.

Useful initial questions:

- Does a choice-driven dice story improve voluntary watching without reducing explanation accuracy?
- Does a sparse soundtrack improve enjoyment relative to voice-only, while preserving numerical comprehension?
- Do stable objects across scene changes reduce reorientation failures?
- Does showing a small case before a dense diagram help novices more than knowledgeable viewers?
- Can viewers recognize the channel across different topics when title and logo are hidden?
- Does a complete 4–5 minute explanation outperform a compressed version for the intended learning goal, and at what cost in voluntary viewing?

Duration comparisons change time available to learn. Record that tradeoff rather than interpreting them as a pure pacing effect. Do not compare raw completion percentages between a 60-second Short and a 5-minute regular video as if they measure the same performance.

Store observations at declared checkpoints with exposure counts, metric definitions, content version and platform context. Distinguish impression-based rates, engaged-view metrics and all-view totals. Test reports must distinguish random assignment, organic observations and model predictions.

Collect only necessary participant information. Keep responses and account analytics private by default; publish aggregated findings. Research evidence and original general-purpose design files may be public. No OAuth material, emails or local user paths belong in the repository.

**Definition of completion for the next prototype**

A single episode has an explicit purpose, defensible mathematics, a coherent visual explanation, deliberate audio, recorded review evidence, and an honest account of what is still unknown about audience response. It is not 'validated' merely because it renders or uploads. The next system milestone is proving this workflow on one redesigned episode before scaling production volume.
