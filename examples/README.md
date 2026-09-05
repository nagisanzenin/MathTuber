# Editable films

Each directory contains a standalone manifest, scene sources and measured cue assets. Initialize a separate production directory with the engine, then copy both `scenes/` and `assets/` into it. Run audio generation before rendering. These examples use Kokoro English narration at the speed specified in their manifests.

`python3 <plugin>/scripts/compile_cues.py --project <production>` regenerates literal `self.at("spoken phrase")` timings from the current audio word timestamps. It refuses missing or ambiguous phrases. If you change narration/provider, regenerate the audio and cues before rendering. The prisoner-cycle scene also contains explicitly measured per-number animation cues; review/re-time those when changing the voice or script.

The diagrams are computed, not stock footage. Exact enumeration verifies Efron's four 24/36 matchups and the urn's uniform distribution after four draws. The triangle mesh respects Sperner's boundary rule; the illustrated doorway path terminates at a rainbow. The examples demonstrate explanations, not replacements for the skill's media review requirements.

Generated audio, rendered videos, publishing intents, channel inventories and credentials are intentionally excluded from these examples.
