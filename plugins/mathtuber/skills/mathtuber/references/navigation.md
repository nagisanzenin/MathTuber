# Find the next useful action

Start from the current project state, not the history of this conversation. Resolve the full plugin root first. For an existing project, run `engine.py status --project PROJECT`; its findings and `next_actions` distinguish missing work from cached work.

| Situation | Read or run | Evidence needed before proceeding |
|---|---|---|
| New environment | `engine.py doctor`; setup only missing dependencies | Capability-specific dependency report; authentication and model downloads remain separate |
| New idea | Editorial mix, channel profile, closest prior learning goals | One correct, distinct mathematical insight and its assumptions |
| Hard visual inference | Production guide; a small scene prototype | The transformation can be followed at phone scale |
| Literal speech cues written | `compile_cues.py --check-only` | Each cue uniquely matches the authored narration |
| Narration synthesized | `audio_review.py`; read the transcript and mathematical discrepancies | Current speech says the intended quantities; listening limits remain explicit |
| Speech approved for rendering | Compile measured cues, then render preview/final | Current timing and source; no concurrent job owns this project |
| All scene renders current | Assemble, verify, then `visual_review.py` and `audio_review.py --final` | Current export, complete decoding, inspectable evidence |
| Final review | Inspect actual returned media and critical transitions | Honest current-hash attestations, including limitations |
| Authorized publication | Publishing guide, batch plan, then publish | Every batch member approved before the first upload |
| Upload attempted | `publication_status.py` | Actual requested visibility and successful processing; preserve uncertain receipts |

The command names above refer to scripts under the resolved plugin root; full syntax is in [commands](commands.md) and [production](production.md). These stages express dependencies, not mandatory creative personas or a fixed visual template.

For technically valid but confusing animation, read [annotated production decisions](annotated-decisions.md).

For a static concluding summary, consider an optional [new-case ending](ending-case.md). For changing inputs, inspect [transition consistency](transition-consistency.md).

When stuck, retrieve at most a few concrete repair notes:

```sh
python3 "$ROOT/scripts/knowledge.py" --query "Manim opacity fill"
python3 "$ROOT/scripts/knowledge.py" --query "ambiguous number speech" --stage speech
python3 "$ROOT/scripts/knowledge.py" --id project-busy
```

Read the symptom before applying the repair. A superficially similar error can have a different cause. If no note fits, inspect the error and the smallest relevant source. After repeated identical failures, simplify the construction or seek stronger reasoning; never bypass review to finish a retry budget.

Prefer tested primitives for mechanical operations, such as `WorkshopScene.replace_label` and `focus_outline`. Their implementation is in `components.py`. Small runnable constructions are also bundled in `<root>/recipes/`; read their README for scope. They are building blocks, not complete explanatory designs. Mathematics, object correspondence and visual composition still need authored judgment.

Knowledge status: repair notes reflect observed failures; primitives have the tests documented in the repository. This guide has not established autonomous competence for any lower-capability model. A fresh model handoff must be evaluated independently using the installed package alone.
