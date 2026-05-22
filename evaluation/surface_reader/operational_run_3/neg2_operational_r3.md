Prompt: Which control should I use to change distortion mode? Describe where it is and what it does.

Respose: 

The monotribe manual does not document a control called “distortion mode.” The closest officially named “mode” control is the MODE select switch in the LFO section. It changes how LFO modulation is applied: FAST, SLOW, or 1SHOT—not distortion.

From the performer’s perspective, find it in the upper-right synth area, in the LFO group. Use the two LFO knobs as landmarks: RATE and INT. are the pair of knobs. Just below/near them are the LFO’s small select switches. The MODE select switch is the one for FAST / SLOW / 1SHOT. The manual’s panel overview identifies this as part of the Synthesizer section layout.

What it does:

FAST: LFO modulation rate range is about 1 Hz to 5 kHz.
SLOW: LFO modulation rate range is about 0.05 Hz to 18 Hz.
1SHOT: when a note begins, only the first half-cycle of modulation is applied, then the LFO stops.

For a harsher or more aggressive sound, the manual-grounded controls to explore are more likely PEAK in the VCF section, CUTOFF, and possibly LFO modulation, but the manual does not call any of these “distortion mode.”

[Trace]
Sources used: monotribe_manual.pdf, English panel/function section around Synthesizer section; monotribe_manual_visual_index.json entry for page 10 panel overview; 04_routing_and_uncertainty_policy.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 05_surface_model_map_schema.md; 01_surface_aria_store.md.
Routing weights: Device manual 50%; Visual/static layout 20%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: Medium.
Confidence rationale: The manual clearly documents MODE as LFO mode, but no official “distortion mode” control appears in the available manual text.
Unsupported-current-state risk: Low.
[/Trace]