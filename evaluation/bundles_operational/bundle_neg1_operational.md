Prompt ID: neg1

Prompt: Which control should I use to change delay time? Describe where it is and what it does.

# Surface Reader:
## R1:
The monotribe manual does not document a delay effect or a “delay time” control. So there is no official delay-time knob on the monotribe.

The closest time-related sound control is the LFO RATE knob:

Official control: RATE knob
Section: LFO section
What it does: adjusts the speed of LFO modulation. Turning it right makes the modulation faster. The manual says this can create effects ranging from vibrato to sound effects.
Where it is: in the synthesizer section, in the LFO group. From the performer’s perspective, it is in the upper-right area of the main synth controls, near the INT. knob, TARGET select switch, MODE select switch, and LFO WAVE select switch. The RATE knob is the first knob in the LFO pair: RATE then INT.

If you are using an external delay pedal or DAW effect, its delay time will be controlled on that external device, not from the monotribe panel.

[Trace]
Sources used: monotribe_manual.pdf, monotribe_manual_visual_index.json, 02_interaction_guidance_store.md, 03_mode_policy_store.md, 04_routing_and_uncertainty_policy.md, 05_surface_model_map_schema.md, 01_surface_aria_store.md.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 10%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: The manual lists LFO RATE but no delay-time control in the documented panel functions.
Unsupported-current-state risk: None.
[/Trace]

## R2:
The monotribe manual does not identify any dedicated “delay time” control or built-in delay effect. The control that might sound closest is LFO RATE, but it changes modulation speed, not audio delay time.

Control to use: RATE knob in the LFO section.
The manual says the RATE knob “adjusts the speed of modulation”; turning it right makes the modulation faster.

Where it is:
From the performer’s perspective, use the upper-right synthesizer area as your target. The LFO group is the cluster on the right side of the synth section. The RATE knob is the first knob in that LFO group, paired with the INT. knob nearby. RATE sets speed; INT. sets depth.

What it does:
It controls how fast the LFO cycles. Depending on the TARGET select switch, that modulation can affect VCO pitch, VCO pitch plus VCF cutoff, or VCF cutoff. So RATE can create slow sweeps, vibrato-like movement, fast modulation, or one-shot envelope-like motion, but it is not a delay-time control.

[Trace]
Sources used: monotribe_manual.pdf, panel overview/manual page uncertain; monotribe_manual_visual_index.json; Surface ARIA Store; Surface Model/Map Schema; Interaction Guidance Store; Mode Policy Store; Routing/Uncertainty Policy.
Routing weights: Device manual 45%; Visual/static layout 25%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: Medium.
Confidence rationale: Manual clearly documents LFO RATE but available sources do not show any dedicated delay effect/control.
Unsupported-current-state risk: Low.
[/Trace]

## R3:
The monotribe does not have a delay effect or a dedicated “delay time” control in the manual.

The closest control for a time-based change is the LFO RATE knob. It changes the speed of modulation: turning it right makes the modulation faster; turning it left makes it slower. The manual describes RATE as adjusting modulation speed, not audio delay time.

Tactile location: from the performer’s perspective, use the ribbon keyboard along the bottom as your lower landmark. Move up into the right half of the synthesizer section. The LFO group has two rotary knobs side by side above a row of small selector switches. RATE is the left knob of that pair; INT. is the knob immediately to its right.

What it does: RATE controls how fast the LFO cycles. Depending on the LFO TARGET setting, that movement can affect VCO pitch, VCF cutoff, or both. So it can create slow sweeps, vibrato-like movement, or faster sound effects, but it is not a delay-time knob.

[Trace]
Sources used: monotribe_manual.pdf, manual page 10 panel diagram, manual page 12 LFO RATE description, monotribe_manual_visual_index.json, 01_surface_aria_store.md, 02_interaction_guidance_store.md, 03_mode_policy_store.md, 05_surface_model_map_schema.md, 04_routing_and_uncertainty_policy.md.
Routing weights: Device manual 45%; Visual/static layout 25%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 7%; Mode Policy Store 2%; Routing/Uncertainty Policy 1%.
Evidence confidence: High.
Confidence rationale: The manual explicitly defines LFO RATE and contains no delay-time control in the cited panel/function sections.
Unsupported-current-state risk: Low.
[/Trace]

# Baseline:
## R1:
The monotribe manual does not document a delay effect or a delay-time control. So there is no official “delay time” control to use.

The closest documented control is the LFO RATE knob, but it changes modulation speed, not audio delay time. It is in the Synthesizer section, in the LFO group: the upper of the two small LFO knobs, immediately left of the INT. knob. The manual says the RATE knob adjusts the speed of modulation, with faster modulation as you turn it to the right.

[Trace]
Sources used: monotribe_manual.pdf, Synthesizer section pages 10–12; static panel photo for control placement.
Routing weights: Device manual 80%; Visual/static layout 20%.
Evidence confidence: High.
Confidence rationale: The manual lists LFO RATE but does not list any delay-time control.
Unsupported-current-state risk: None.
[/Trace]

## R2:
There is no documented delay time control on the monotribe. The manual does not describe a delay effect or a delay-time parameter.

The closest time-related controls are not delay controls:

RATE knob in the LFO section: changes the speed of LFO modulation.
TEMPO knob in the sequencer section: changes sequencer speed.
GATE TIME button: changes the duration of synth notes in a sequence.

Where the closest control is: the RATE knob is in the LFO area of the synthesizer section, toward the right side of the top panel, paired with the INT. knob. It is the left knob of that LFO pair.

What it does: RATE adjusts modulation speed; turning it right makes modulation faster. This is not documented as delay time.

[Trace]
Sources used: monotribe manual pages 10–12, 14–15; static panel photo.
Routing weights: Device manual 85%; Visual/static layout 15%.
Evidence confidence: High.
Confidence rationale: The manual documents RATE, TEMPO, and GATE TIME but no delay-time control.
Unsupported-current-state risk: None.
[/Trace]

## R3:
Use the RATE knob in the LFO section to change the time-related speed of modulation. The manual does not document a dedicated “delay time” control on the monotribe.

Where it is: on the top panel’s synthesizer section, the LFO controls are in the lower-right area of that section. The RATE knob is the left knob of the two LFO knobs, with INT. immediately to its right.

What it does: RATE adjusts the speed of LFO modulation; turning it right makes the modulation faster. The manual describes this as modulation speed, not delay time. The nearby MODE switch changes the modulation-rate range or how modulation is applied: FAST, SLOW, or 1SHOT.

[Trace]
Sources used: monotribe_manual.pdf, synthesizer section pages 10–12; static panel photo.
Routing weights: Device manual 80%; Visual/static layout 20%.
Evidence confidence: High.
Confidence rationale: The manual explicitly identifies RATE as the LFO speed control and does not document a delay-time control.
Unsupported-current-state risk: None.
[/Trace]

