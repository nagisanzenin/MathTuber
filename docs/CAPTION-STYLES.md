# Channel caption styles

A pinned profile may define `identity.captions`. Projects may override individual fields with `captions.style`. Missing fields retain the legacy appearance. Sizes and margins use a 1080×1920 reference and scale with the actual export.

```json
{
  "captions": {
    "burn_in": true,
    "style": {
      "font": "DejaVu Sans",
      "font_size": 48,
      "color": "#243944",
      "outline_color": "#F3ECDD",
      "outline": 1,
      "bold": false,
      "margin_bottom": 270,
      "margin_side": 108,
      "wrap_width": 34
    },
    "phrases": {
      "s01": ["A curve can grow\nfrom straight lines."]
    }
  }
}
```

Supply all narration phrases in order. Their lexical content must match current speech timing words. A newline preserves a chosen line boundary in SRT and ASS. Explicit captions allow at most two nonempty lines, each no longer than `wrap_width`; without a newline, the existing phrase-wrap heuristic applies. This is a character limit, not a font-width measurement.

Use installed font families and inspect renderer fallback on each host. Review caption contrast against the actual scene, reserve space for platform UI, and do not assume a profile that worked on paper will work over a dark background. Font files are not distributed. Invalid values, unknown fields and ASS syntax in a font name are rejected. Caption changes invalidate assembled exports and their reviews.
