# Linked representations and deliberate pauses

Research update: 6 September 2026. This extends, rather than replaces, [mechanism direction](MECHANISM-DIRECTION.md). Our last batch improved continuity but still asked viewers to translate between pictures without enough help. Its text morphs also briefly distorted words. These are editorial observations, not measured audience effects.

## What the evidence supports

| Source | Finding and boundary | Production inference |
| --- | --- | --- |
| [Ainsworth (2006), DeFT](https://doi.org/10.1016/j.learninstruc.2006.03.001) | Framework for the design, functions and learner tasks of multiple representations. Extra representations impose interpretation and translation work; they are not automatically helpful. | Keep a shared object, position or quantity visible across the transition. Introduce one correspondence at a time. |
| [Fyfe et al. (2014), systematic review](https://doi.org/10.1007/s10648-014-9249-3) | Abstract reviewed: concreteness fading connects concrete and abstract representations. This is not a universal sequence proven for Shorts. | Remove incidental detail after the relation is grounded; do not suddenly replace a physical example with an unexplained graph. |
| [Lowe & Boucheix (2016), author manuscript](https://lead.ube.fr/wp-content/uploads/2023/09/001168-principled-animation-design-improves-comprehension-of-complex-dynamics.pdf) | In a piano-mechanism learning experiment, contiguous presentation of interacting relation pairs improved mental-model quality. Local kinematics and transfer did not significantly differ. | Build an explanation around successive relationships, preserving the shared part. More motion is not itself the goal. |
| [Spanjers et al. (2012), university abstract](https://cris.maastrichtuniversity.nl/en/publications/explaining-the-segmentation-effect-in-learning-from-animations-th/) | 161 secondary students studied probability animations in four conditions. Results suggest pauses and temporal cues both contribute to segmentation, in different ways. No claim here about optimal pause duration or Shorts retention. | Hold a consequential comparison long enough to inspect. Distinguish an inference pause from a diagram left unchanged while narration introduces new ideas. |
| [Hekkert et al. (2003), design research](https://research.tue.nl/en/publications/most-advanced-yet-acceptable-typicality-and-novelty-as-joint-pred/) | Typicality and novelty jointly relate to aesthetic preference in industrial design. Adjacent evidence, not a channel-branding experiment. | Familiar material and motion grammar, different topic-specific compositions. Treat recognition and appeal as separate hypotheses. |

## Decisions for profile 0.3

1. **One control, visible consequences.** A moving contact point updates both a route and its reflected counterpart. A game position maps to a probability height. Explain the mapping before demanding inference from it. Two views are an option, not an obligatory dashboard.
2. **Name the relationship after showing it.** Short object-attached labels; replace whole phrases with a fade, never interpolate unrelated letter shapes.
3. **Pause with a question to answer.** The viewer should know what to compare or predict. No universal cut interval and no penalty for stillness that supports thinking.
4. **A family of settings.** Paper workbench, dark plotting field, river map, token board and dissection table. Exact geometry and consistent color roles remain recognizable. Keep decorative detail away from the active relation.
5. **Prototype risky passages.** At minimum inspect the actual transition from example to explanation. Final review samples opening, every authored cue, distributed frames, and every declared critical interval through its end. A successful opening does not certify a late rearrangement.
6. **Sound has a job.** Keep difficult inferences dry. Boundary tones may mark entry and resolution. An untested music bed is not a default quality upgrade. Technical ASR and signal checks do not establish pleasant listening.

## Portable review plan

Put `assets/review-plan.json` in the project with `intervals`: each item has `id`, `start_cue`, `end_cue`, optional `start_offset` and `end_offset` in seconds, `samples` (at least 3), and `purpose`. Cues must exist in the compiled timing map. `mathtuber.review_sampling.interval_samples` resolves and validates the entire interval; it does not silently clip an invalid range. Include all difficult mappings, rearrangements and the ending, not only the first transformation. A host may use these times with FFmpeg or its own video tools. The sampler produces evidence locations, never an acceptance decision.

## Next batch and evaluation

Five different mechanisms: random halfway hops, four equal-speed pursuers, a route unfolded by reflection, a bounded fair random walk, and a missing-square dissection. Verify each mathematical argument independently. A finite simulation is an illustration, not a probability proof.

Before release, write a per-film judgment of opening, mechanism, readability, pacing, sound scope and remaining weaknesses. Review the complete batch before the first upload. After release, compare early exits and retention around the mapping with previous episodes, accounting for topic and audience differences. Ask actual viewers to explain the key relation and predict a changed case. Neither retention nor an agent's enthusiasm alone proves learning. We have not performed these audience tests; no causal lift is claimed.
