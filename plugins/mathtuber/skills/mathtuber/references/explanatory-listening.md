# Optional explanatory listening

Use sound when it demonstrates the relationship. First establish what to compare, let the listener hear it without narration, then show a changed condition. Keep the mathematical comparison visible for muted viewing. Label slowed diagrams and synthesized illustrations honestly.

After speech synthesis and cue compilation, create `assets/listening-windows.json`:

```json
[
  {
    "id": "full-cavity",
    "scene": "s01",
    "paragraph_pause": 0,
    "offset": 0.15,
    "duration": 2.5,
    "fade_seconds": 0.05,
    "tones": [{"frequency_hz": 220, "amplitude": 0.1}],
    "meaning": "Reference resonance before the air volume changes"
  }
]
```

`paragraph_pause` is a zero-based boundary index. Give that scene sufficient explicit `paragraph_pauses` duration. Run `python3 <root>/scripts/score_events.py --project <path>`; this compiles both action events and listening windows into the same score. Re-run after any narration, pause or sound-plan edit, then reassemble. The script uses current speech metadata and frame-rounded scene offsets. Windows must fit the measured inserted silence; nonoverlapping windows may share one boundary. Action sounds cannot overlap them.

Tones are original sine synthesis with raised-cosine edges, not recorded instruments. Frequency range is 30–8000 Hz; amplitude is linear peak, not a guarantee of perceived loudness. Match model frequencies to the authored plan and verify the final decoded mix. Inspect visual transitions and captions throughout each listening interval. Numerical audio QA does not establish pleasantness, natural prosody or audience understanding. Consult `docs/research/EXPLANATORY-LISTENING.md` for bounded evidence and model sources.
