# Explanatory listening, not an automatic music bed

## Why this experiment

The physical-context batch remained speech-heavy despite recognizable subjects. The earlier beats film already included local mathematical tones. This iteration makes that capability reusable: let an acoustic relationship be heard during a selected speech-free interval, keep the same relationship visible, and return to it after changing one condition. This is an editorial hypothesis about these films, not a proven retention intervention.

## Relevant primary evidence

[Kucinkas et al., 2026, npj Science of Learning](https://www.nature.com/articles/s41539-025-00385-4) studied sixty sighted adults learning auditory mappings of simple visual stimuli. Both structured pitch/time mappings outperformed an arbitrary-tone control on recognition. The two structured mappings did not differ significantly; that does not establish equivalence. Novel-item performance exceeded the nominal five-choice chance rate, although the authors describe a strategy that raises a conservative chance baseline. The control also differed in acoustic complexity and instructions. This short laboratory training task does not establish effects on Shorts, calmness, mathematics learning or enjoyment. It supports treating sound mappings as something to explain and learn, rather than assuming that a chosen pitch/space association is self-evident.

This extends the bounded evidence in [recognition and listening](RECOGNITION-AND-LISTENING.md) and [quiet beats](QUIET-BEATS.md). No tested universal optimum for pause length, background music or narration density follows from those studies.

## Production decisions

- Use actual modeled acoustic frequencies when demonstrating pitch. State that synthesized tones are illustrations, not field recordings or complete instrument simulations.
- Give each listening interval one explicit meaning. Establish the object and comparison before the sound begins. Avoid explaining over the demonstration.
- Preserve a visible equivalent: a labeled frequency comparison, elapsed-time path, repeating waveform, or selected spectral component. Muted viewing must still reveal the relationship.
- Keep exact times linked to measured speech pauses. Recompile after narration changes. Do not manually paste stale timestamps into the score.
- Use smooth tone edges and bounded amplitudes. Signal checks establish neither pleasantness nor comfortable playback loudness on every device.
- A slowed vibration diagram must say it is slowed; audio remains at the labeled frequency. Do not imply that a 30-fps movie literally resolves audible vibration.
- Review the captioned final mixture and the entire listening interval. Transcription and spectrum checks cannot substitute for subjective listening or viewer feedback.

## Candidate scientific models

[Bottle resonance, UNSW](https://phys.unsw.edu.au/jw/Helmholtz.html): a small neck-air mass interacts with compressible cavity air. With fixed neck geometry and effective length, frequency scales as inverse square root of air volume. Wavelength must greatly exceed cavity dimensions; end corrections matter. Pure tones only illustrate the resonance change.

[Wind chimes, Stepanishen, ASA author presentation](https://acoustics.org/2psa9-acoustic-transients-from-the-impact-force-excitation-of-beams-and-wind-chimes-peter-stepanishen/): a free-free beam approximates a slender chime. With material and cross-section fixed, corresponding bending-mode frequencies scale as inverse length squared. Higher modes are not generally harmonic. Use a selected mode, not a purported complete chime recording.

[Echo timing, OpenStax](https://openstax.org/books/college-physics-2e/pages/17-2-speed-of-sound-frequency-and-wavelength): a pulse makes an outward and return journey. For a stationary source beside its receiver and a stationary reflector, distance is half sound speed times delay. Temperature changes sound speed. Show the two legs and preserve their timing.

[Frequency and perceived pitch, UNSW](https://phys.unsw.edu.au/jw/musFAQ.html): a periodic mixture can suggest a pitch corresponding to an absent fundamental component. Show which frequencies are physically present and distinguish waveform repetition from a claim about every listener's percept. Playback systems and listeners differ.

[Pluck position, Daniel Russell, Penn State](https://www.acs.psu.edu/drussell/Demos/Pluck-Fourier/Pluck-Fourier.html): an ideal string released from a triangular displacement has modal coefficients containing sin(nπd/L). At d=L/3, modes divisible by three are absent. Moving the pluck changes excitation weights without changing the allowed frequencies. Sound radiation and pickup position add further weighting. Produce original geometry and tones; do not reuse the source's licensed animations.

## Novelty boundaries

The channel already has Chladni patterns, equal-tempered tuning and Fourier synthesis. Those are excluded as central lessons. Earlier authored films cover beats, Doppler shifts, circle/spring projection and counterpropagating waves. The proposed new operations are cavity-volume scaling, bending-length scaling, round-trip timing, absence of a fundamental spectral component despite period repetition, and initial-condition selection of string modes. The latter two need especially clear boundaries from generic Fourier and standing-wave explanations. Earlier unavailable transcripts prevent an exhaustive historical novelty claim.

## Implementation and evidence

The opt-in `assets/listening-windows.json` plan is compiled by `scripts/score_events.py` alongside existing action events. Windows refer to measured scene paragraph pauses. Validation rejects invalid numbers, missing references, speech spill, overlapping windows and action sounds that mask listening. Raised-cosine fades and deterministic local sine synthesis require no API or stock-audio fee. The default remains the existing sparse score when no listening plan exists.

Tests verify actual PCM silence, stable-tone zero-crossing frequency, fade endpoints, deterministic output, and rejection cases. These establish mechanical behavior, not artistry. A prototype and final batch review remain required before publication. No audience outcome or quality plateau has been established.
