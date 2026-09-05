# Captioned scene prototypes

Render a current scene preview, then run:

```sh
python3 "$MATHTUBER_ROOT/scripts/caption_preview.py" --project ./video-project --scene s01
```

The output combines the current preview and narration with the same caption phrasing and style functions used in final assembly. It is stored separately under `reviews/captioned-previews` and a `prototype:captioned:<scene>` artifact key. It never records a final export or acceptance. It includes no soundtrack and does not replace final-resolution or full-timeline review.

This makes early inspection of phrase boundaries, caption placement and intermediate animation states inexpensive. A local 92.27-second Bézier preview at 360×640 took 1.08 seconds to mux and burn captions after the base preview existed. One run is not a general speed benchmark. The resulting frame was visually inspected and the existing final export record was verified unchanged.

The helper requires a current preview fingerprint; changed sources or audio cannot silently reuse stale video. Its output is cached against render, audio, settings, profile style and caption implementation. Authored phrases still must contain the current spoken words in order.

Related authoring support: `WorkshopScene.focus_outline(target)` draws attention without changing the target's fill or geometry. Read [attention and inference](research/ATTENTION-AND-INFERENCE.md) for the research boundaries and the editorial motivation.
