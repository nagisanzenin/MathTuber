# Evidence-informed discovery batch

Five additional public YouTube Shorts, produced with the implemented research workflow. English narration, 1080×1920, 30 fps, burned captions and original sparse sound.

| Video | Duration |
| --- | --- |
| [Shuffle Too Perfectly and Nothing Changes #math #Shorts](https://www.youtube.com/shorts/3LgUrUvPYJ4) | 122.7s |
| [The Chocolate Game You Can Win Without Knowing How #math #Shorts](https://www.youtube.com/shorts/YiPvMk8QzSg) | 117.2s |
| [Why 17 Is the Last Impossible Order #math #Shorts](https://www.youtube.com/shorts/4gPifXiFujI) | 119.9s |
| [Two Equally Likely Coin Patterns. Different Waiting Times. #math #Shorts](https://www.youtube.com/shorts/qhqm03eV6Ho) | 117.6s |
| [Count the Safe Paths by Flipping the Bad Ones #math #Shorts](https://www.youtube.com/shorts/C-g-YNOgVFk) | 117.4s |

Validation: 37 unit tests, plugin/skill validation, exact mathematical derivations/enumerations, measured cue guards, full-file decoding and independent speech recognition. Source and final audio have no clipped samples in the measured PCM streams. YouTube API confirmed successful processing and public visibility.

Corrections during review included preserving coin-target positions across scenes, moving the reflected path and its join together, updating labels with the transformation, and shortening a motion that overran a final-resolution speech cue. A closing sentence was rephrased after ASR ambiguity and independently retranscribed.

The host inspected rendered samples, not an uninterrupted human playback. ASR and signal checks do not establish pleasing speech or music balance. Viewer retention, comprehension, transfer and return remain unmeasured. This batch implements evidence-informed production hypotheses; it does not validate a quality-improvement claim.

No paid TTS or reasoning API is called by the engine. Host-agent subscription usage and local compute still have costs. Existing render/audio caches are retained when their dependencies remain valid.

See [editable examples](../examples/discovery/README.md), [research guide](research/THEORY.md) and [implementation status](research/IMPLEMENTATION.md).
