# A pattern that becomes understandable

Cycle 13 made geometric causes easier to track, but its isolated mechanisms still felt visually interchangeable. The next experiment gives the image more presence: a complete original pattern, a close examination of its local rule, then a return to the same whole with something newly understandable. This is an editorial hypothesis, not measured viewer improvement.

## Evidence and limits

[Muth and Carbon (2013)](https://www.experimental-psychology.de/ccc/docs/pubs/MuthCarbon2013.pdf) studied 30 people repeatedly viewing two-tone face/nonface images. Liking increased after the largest reported recognition change for faces; repetition alone did not raise overall liking. Recognition was inferred from ratings, not experimentally assigned. Face recognition is not mathematical understanding. Their regressions on rating-level means do not predict individual viewer behavior. The methods, results and beginning of discussion informed this reading.

[Muth, Raab and Carbon (2015)](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2015.00365/full) used one 7-minute-18-second artwork, watched twice by 60 participants in gallery/laboratory settings. Interest rose before, and liking around/after, inferred insight windows. Windows came from group rating changes; different dimensions involved different groups. Repeated ratings, one artwork and setting differences limit generalization. JPEG size as a complexity proxy and an inspection-chosen temporal adjustment do not establish an ideal complexity level or pacing interval. The complete main article was read.

Our inference is modest: let viewers discover an organizing relationship in something already worth looking at. Do not manufacture confusion to imitate laboratory recognition, promise an aesthetic response, or prolong uncertainty to force retention. Aesthetic satisfaction, comprehension, desire to explore and completion rate remain separate outcomes.

## Production decisions

1. Design the complete image first. Its richness must come from the mathematical subject: tile paths, interlaced threads, packing, a ruled surface, or a repeating curve. Extra particles are not an explanation.
2. Identify one small rule and the global consequence it supports. Write the reason in everyday language before adding notation.
3. Preserve correspondence. Lift an identified unit from the field, keep muted context, investigate it, and return it to the same place. A zoom is a mapping that the viewer must understand.
4. Make the essential join or comparison large enough to inspect on a phone. Whole-pattern beauty does not compensate for a tiny proof.
5. Return to the whole and trace the consequence. Give a changed case that tests the rule, not five further facts.
6. Keep color meanings stable and add position, marks, motion or labels. Avoid presenting a randomly selected route as every route.
7. Use a quiet, unhurried voice; meaningful pauses need visible work to notice. A silent prototype cannot validate the eventual voice or music.

The channel profile remains a material and editorial language, not a compulsory layout. Pattern films may be denser than isolated constructions while preserving space for captions. Do not claim that a higher object count is inherently more beautiful.

## Truchet reference: topology before ornament

[Reimann (2011), Decorating Regular Tiles with Arcs](https://archive.bridgesmathart.org/2011/bridges2011-581.pdf) describes regular polygon tiles with uniformly located edge endpoints and paired arcs, including crossing-free decorations. Its introduction and methods support using shared endpoints for continuous patterns. Our square-quarter-circle construction and graph traversal are independently implemented; no paper artwork is copied.

Each square contains two disjoint quarter-circles. Either orientation uses exactly one endpoint at each edge midpoint. Neighboring endpoints coincide, and quarter-circle tangents agree across the seam. Every interior join therefore has two incident arc segments, while each boundary endpoint has one. A finite connected component is a closed loop or a path between boundary endpoints. This does **not** imply every component closes or that one path visits every tile.

`mathtuber.tiled_paths` uses doubled integer coordinates for exact graph joins, partitions every arc once, and orients each traversal continuously. Its path parameter is proportional to distance because all component arcs have the same length. This special case does not change the general `CurveTrace` parameter-space contract. Tests exhaust all 512 3×3 fields, including boundary endpoints, arc coverage and directed tangent continuity.

The first rendered prototype exposed an opacity bug: changing overall VMobject opacity filled open paths. Change stroke opacity explicitly. Inspect the return-to-whole transition as well as the opening. Sampling proves only the inspected frames; it cannot establish uninterrupted audiovisual experience or viewer delight.

## Next-batch novelty scope

Compared all 175 stored archive titles and all 75 authored learning goals. Candidate lessons: midpoint connectivity; square versus triangular packing cell areas; staggered 2/2 weave repeats; straight rulings of a hyperboloid; odd/even polar-rose retracing. Related old titles include honeycomb geometry, Penrose tiling, moiré, circular projection and saddle points. Those relationships are not the proposed mechanisms. Older unavailable transcripts leave a residual uncertainty; this is not a claim to have watched every historical film.

## Review questions

Can a novice point to the organizing unit? Can they see why neighboring units work together? Does the final whole now mean something different? Is the changed case genuinely predicted by the rule? Are texture, motion and sound helping this particular relationship? Record visible evidence and predicted reactions separately. If the prototype remains confusing, revise it before producing a batch.
