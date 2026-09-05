# Process and inspection: move for change, hold for structure

Cycle five follows the [quiet batch reflection](../quiet-batch.md). A physical rhythm should not speed up, restart or stop merely because the next sentence has arrived. Conversely, a construction can benefit from a stable state. This is an authoring distinction, not a demand for constant motion.

## Evidence

Ploetzner, Berney and Bétrancourt (2021), [When learning from animations is more successful than learning from static pictures](https://link.springer.com/article/10.1007/s11251-021-09541-w), randomly assigned 88 university students to one picture, four pictures or an animation of a six-bar linkage. Animation supported recognition of its motions; one picture supported recognition of spatial arrangements. Reported differences were large. The tasks concerned perceptual recognition, not conceptual understanding, and the authors explicitly distinguish these. The study does not establish Shorts retention, pleasure, transfer or an optimal moving/still ratio. Full open-access methods, results and discussion were read.

## Production inference

Choose the perceptual task first. If the viewer needs to see a wave propagating, preserve its propagation rate across captions, labels and narration gaps. If the viewer needs to compare two lengths, deliberately freeze the relevant state and make the pause understandable. Keep a key object in the same coordinate frame when possible. A beautiful transformation can appear in the opening before its rule is introduced; it must be an honest preview of the actual explanation.

`NarratedScene.process_clock(rate=1, initial=0)` provides an optional phase independent of individual `play` calls. Read `clock.value` from object updaters; use `clock.pause()` and `clock.resume()` for deliberate inspection. Units are chosen by the author. The helper is presentation timing, not a physics integrator. Add the clock before its dependent objects, and remember that clearing a scene removes its invisible driver too.

The driver reads absolute renderer time. An initial implementation accumulated updater `dt`, but a real Manim test found a frame missing at each animation boundary. The absolute clock fixes that loss, including across `play`, `wait` and inspection pauses. Unit tests cover time partitioning, invalid inputs, overflow and pause boundaries; a real four-second render checks phase 2, 4, 4, 6 at successive seconds. Render fingerprints include the helper.

For cycle five, use a shorter inserted paragraph pause (0.45 seconds) as a new creative hypothesis. Cycle four's 1.1-second insertion produced approximately two-second full quiet gaps once synthesized silence was included. Measure the new audio and inspect it; neither setting is a research optimum. Narration silence and physical motion are separate decisions.

## Acceptance questions

- Does the phenomenon appear before a lengthy explanation of its vocabulary?
- Is motion carrying an observable relationship, with a stable rate where the model requires it?
- Can a viewer identify what a deliberate freeze asks them to compare?
- Does the same object remain attached to the explanation?
- Are idealizations stated without overwhelming the main idea?

Image sequences and ASR can locate defects but cannot certify enjoyment or learning. No plateau or claim of audience impact follows from implementation alone.
