Prompt ID: neg2

Prompt: Which control should I use to change distortion mode? Describe where it is and what it does.

# Surface Reader:
## R1:
The monotribe manual does not document a “distortion mode” control. The closest official control named MODE is the LFO MODE select switch, and it changes how the LFO modulation behaves, not distortion.

From the performer’s perspective, find the right side of the synthesizer section. Use the two LFO knobs as a landmark: RATE above, INT. below. Just below that LFO area is a small three-position switch: MODE. It selects:

FAST: faster LFO modulation, about 1 Hz to 5 kHz.
SLOW: slower LFO modulation, about 0.05 Hz to 18 Hz.
1SHOT: applies only the first half-cycle of modulation when a note begins, then stops.

For a harsher or more aggressive sound, use the VCF CUTOFF and PEAK knobs instead: Cutoff changes brightness, and Peak emphasizes the cutoff frequency. That is filter tone shaping, not a documented distortion mode.

[Trace]
Sources used: monotribe_manual.pdf, page 11–12/manual page uncertain; monotribe_manual_visual_index.json panel overview entry; static panel photo foto_pannello; Surface ARIA Store; Surface Model/Map Schema; Interaction Guidance Store; Mode Policy Store; Routing/Uncertainty Policy.
Routing weights: Device manual 45%; Visual/static layout 25%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: Medium.
Confidence rationale: The manual clearly documents LFO MODE and filter controls, but no official distortion mode appears in the searched manual text.
Unsupported-current-state risk: Low.
[/Trace]

## R2:
The monotribe manual does not document a “distortion mode” control. The closest control with the official word MODE is the LFO MODE select switch, but it changes LFO modulation behavior, not distortion. Its three settings are FAST, SLOW, and 1SHOT: FAST and SLOW set the modulation-rate range, while 1SHOT applies the first half-cycle of modulation when a note begins, then stops.

From the performer’s perspective, find the LFO section in the upper-right area of the synth controls. The MODE select switch is a small three-position switch in the lower part of that LFO group, near the TARGET select switch and the LFO WAVE select switch. Use it when you want to change how the LFO behaves, for example vibrato-like movement, filter movement, or one-shot envelope-like movement depending on the TARGET setting.

If you are trying to make the sound more aggressive, the manual-grounded control to try is PEAK, the lower knob in the VCF/filter pair. It increases resonance by emphasizing the cutoff frequency, but the manual does not call this a distortion mode.

I cannot determine the current switch position or knob setting from the manual or static panel references alone.

[Trace]
Sources used: monotribe_manual.pdf pages 10–13; monotribe_manual_visual_index.json entry for page 10; foto_pannello.jpeg; 01_surface_aria_store.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 04_routing_and_uncertainty_policy.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 45%; Visual/static layout 25%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: Medium.
Confidence rationale: The MODE control and PEAK function are documented, but “distortion mode” is not documented in the manual.
Unsupported-current-state risk: Low.
[/Trace]

## R3:
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

# Baseline:
## R1:
There is no documented “distortion mode” control on the monotribe. The manual does not list a distortion mode, distortion switch, or distortion setting.

The closest documented control with “MODE” in its name is the LFO MODE select switch, but it changes how LFO modulation is applied, not distortion.

It is in the synthesizer section, in the LFO area, below the RATE and INT. knobs, near the TARGET and WAVE select switches. It selects FAST, SLOW, or 1SHOT modulation behavior.

[Trace]
Sources used: monotribe_manual.pdf, Panel description and functions, Synthesizer section, LFO MODE select switch.
Routing weights: Device manual 100%; Visual/static layout 0%.
Evidence confidence: High.
Confidence rationale: The manual documents LFO MODE but no distortion mode.
Unsupported-current-state risk: None.
[/Trace]

## R2:
The monotribe manual does not document a “distortion mode” control. There is no listed distortion mode setting or distortion-mode switch in the official panel functions.

The closest documented “MODE” control is the LFO MODE select switch, but it changes how LFO modulation is applied, not distortion. It is in the Synthesizer section, near the lower-right of that section: below the LFO RATE and INT. knobs, between the LFO TARGET select switch and the LFO WAVE select switch.

The LFO MODE select switch has three settings: FAST, SLOW, and 1SHOT. FAST and SLOW change the modulation-rate range; 1SHOT applies the first half-cycle of modulation when a note begins, then stops.

Limitation: distortion mode is not documented in the manual or static panel source, so I can’t identify a distortion-mode control from these sources.

[Trace]
Sources used: monotribe_manual.pdf, Synthesizer section pages 10–13; static panel photo.
Routing weights: Device manual 85%; Visual/static layout 15%.
Evidence confidence: High.
Confidence rationale: The manual’s panel description lists controls and functions, and no distortion mode control is documented.
Unsupported-current-state risk: None.
[/Trace]

## R3:
There is no documented “distortion mode” control in the monotribe manual. The closest documented control named “MODE” is the LFO MODE select switch, but it changes LFO behavior, not distortion.

Where it is: in the Synthesizer section, in the LFO area near the lower-right part of the synth controls. It is control 12, between the TARGET select switch and the WAVE select switch in the manual’s panel diagram.

What it does: the MODE select switch chooses how the LFO modulation is applied:

FAST: modulation rate range is about 1 Hz to 5 kHz.
SLOW: modulation rate range is about 0.05 Hz to 18 Hz.
1SHOT: when a note begins, the first half-cycle of modulation is applied, then the LFO stops.

[Trace]
Sources used: monotribe_manual.pdf, English manual pp. 10–12; static panel photo for general layout.
Routing weights: Device manual 85%; Visual/static layout 15%.
Evidence confidence: High.
Confidence rationale: The manual documents the LFO MODE select switch and does not document a distortion mode.
Unsupported-current-state risk: None.
[/Trace]

