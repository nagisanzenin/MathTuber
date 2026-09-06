# Small mechanical recipes

These are intentionally short Manim constructions, not complete film templates. Adapt composition and mathematical meaning to the problem. Run with the configured media Python:

```sh
python -m manim -ql outline_restore.py OutlineRestore
python -m manim -ql attached_marker.py AttachedMarker
```

- `outline_restore.py`: change stroke opacity without turning an unfilled outline into a solid shape. Assertions check the fill after both transitions.
- `attached_marker.py`: include the marker and label in the group passed to `UpdateFromAlphaFunc`, so the renderer tracks every changed object. Assertions check their final correspondence.

Each example still needs visual inspection. A geometry assertion cannot detect every rendering artifact. In a production scene, use measured narration timing and the project profile; these standalone examples contain neither speech nor publication logic.

Both recipes were executed with Manim 0.20.1 on the existing macOS runtime; their assertions passed and five sampled frames from each were inspected. See `verification.json` for source hashes and limits. This is evidence about these primitives, not a lower-model filmmaking evaluation.
