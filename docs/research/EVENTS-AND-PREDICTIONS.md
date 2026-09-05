# From narrated diagrams to events viewers can reason about

The linked batch made relationships clearer, but several openings presented a board before anything happened. Our hypothesis for the next batch is that a legible event, an answerable prediction, and a visible explanation can make a stronger viewing experience. This is an editorial hypothesis, not a measured retention result.

## Evidence and boundaries

- Kim, Reinecke and Hullman (CHI 2017), [Explaining the Gap](https://idl.cs.washington.edu/files/2017-ExplainingTheGap-CHI.pdf), tested prediction and self-explanation around data. Their experiments support eliciting prior expectations and showing feedback; effects differed between visual and text conditions. These were interactive tasks, not passive Shorts. A spoken question is a weaker intervention than a recorded prediction.
- Brod, Hasselhorn and Bunge (2018), [When generating a prediction boosts learning](https://escholarship.org/uc/item/0qn99739), report learning benefits associated with surprise after predictions. This entry uses the university abstract, not inaccessible full text. We infer a design opportunity; we do not infer a universal engagement gain.
- Gerber-Morón and Szarkowska (2018), [Line breaks in subtitling](https://discovery.ucl.ac.uk/10051115/1/Line%20breaks%20in%20subtitling_AfterReview_APA_FINAL.pdf), found preferences for syntactic segmentation in paired subtitle screenshots. Eye-movement effects depended on linguistic category and viewer group. This supports respecting phrases, not claiming a fixed optimal word count or guaranteed comprehension improvement.
- Phan (2023), [Effects of Background Music in Instructional Videos on Learners’ Retention](https://www.thejeo.com/archive/2023_20_3/van_thanh_phan), reports that classical music in pretraining improved retention in that experiment, whereas embedding music in narrated content did not have a remarkable influence. It does not establish that background music always helps, nor evaluate our short synthesized event sounds.

## Production changes

1. Show a concrete action before abstract rules when the topic permits it. The viewer must be able to describe the question from the picture.
2. Offer a prediction with clear alternatives before the reveal. Leave a purposeful beat; do not imply the viewer actually answered.
3. Spend the most screen area and motion on the hardest inference. Preserve a small orientation cue when zooming or changing representations.
4. Author caption sense units in `captions.phrases`, keyed by scene ID. They must preserve every spoken word in order. Exact validation rejects stale phrases. The fallback avoids some dangling English function words; it is not a multilingual parser.
5. Optional sparse sounds come from `assets/sound-events.json`, resolved against measured speech cues by `scripts/score_events.py`. A cue plus offset must match the visible action landing, not merely the start of a sentence. Kinds are `tap`, `settle`, and `reveal`. Original local synthesis has no API or stock-license cost. Silence remains appropriate for reasoning.
6. Review captioned final motion samples, independent math checks, and speech alignment. Signal checks and ASR do not constitute subjective listening. Record that limitation until a listening-capable review is available.

## How this hypothesis could fail

A prediction can be empty suspense if the alternatives are impossible to judge. Sounds can distract or imply false counts. A large close-up can destroy orientation. Excessive segmentation can make captions feel fragmented. Five polished examples cannot establish audience causality.

For each release, record the first likely skip point, the exact inference most likely to lose a novice, whether the reveal answers the opening, and a change for the next cycle. Separate defects observed in media from hypotheses about viewers. If available, use actual retention and comments alongside these observations; do not substitute subjective scores for measured results.
