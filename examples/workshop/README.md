# Workshop batch: five candidate profile applications

These original scenes exercise the same pinned profile with different mathematical mechanisms. They are production examples, not validated audience experiments. The manifests include project-local profile snapshots; no credentials or generated speech/video files are distributed.

Copy an example directory into a working directory outside the repository. Initialize it using its manifest, then synthesize audio, compile measured cues, generate its original score, and render scenes. Use absolute paths for ENGINE, PROJECT and this score script.

```sh
python3 "$ENGINE" init --project "$PROJECT" --manifest "$PROJECT/manifest.json"
python3 "$ENGINE" plan-check --project "$PROJECT"
python3 "$ENGINE" audio --project "$PROJECT"
python3 "$PLUGIN_ROOT/scripts/compile_cues.py" --project "$PROJECT"
"$MEDIA_PYTHON" "$REPO/examples/workshop/score.py" --project "$PROJECT"
python3 "$ENGINE" render --project "$PROJECT" --scene s01 --quality preview --execution native
```

Inspect and revise previews; render s01 through s04 at final quality, then assemble, verify and review before publishing. The engine supplies the profile to WorkshopScene. Profile, timing and score assets must be present before rendering; regenerate cues and score after narration changes. Existing mathematical reports describe the authored examples and are not fresh attestations for modified work.

The lattice episode demonstrates the formula, explains additivity and explicitly labels its proof as a sketch; the linked source supplies the full derivation. The ring comparison uses axonometric illustrations. The graph episode uses line style as well as color; crossings do not represent people. No learning or retention improvement is claimed.
