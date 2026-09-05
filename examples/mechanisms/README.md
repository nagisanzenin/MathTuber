# Mechanism-first workshop examples

The two references remake earlier topics locally; the batch contains five new upload topics. Each example is one continuous scene, with a pinned workshop 0.2 profile. Original vectors and narration are editable under the repository license; fonts and speech model assets retain their own licenses.

Initialize a production folder with `engine.py init --project /local/production --manifest manifest.json`, copy `scenes` and `assets` into it, then run audio, compile_cues.py, preview render, inspection, final render, assemble and verify. Use native rendering only for trusted source. If the manifest references score.wav, run `score.py --project /local/production` after audio and cue compilation, before rendering. WAVs and generated media are deliberately excluded from source control. Follow the skill for evidence-based final review. Publication additionally needs an explicitly authorized intent and credentials outside the repository.

References are mechanism prototypes, not audience-validated gold standards. See docs/research/MECHANISM-DIRECTION.md for annotations, anti-examples and viewer-test protocol. A sampled visual inspection and technical audio check do not establish that the result is enjoyable.
