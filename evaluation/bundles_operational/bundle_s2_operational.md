Prompt ID: s2

Prompt: Which control should I use to change the oscillator waveform? Describe where it is and what it does.

# Surface Reader:
## R1:
Use the WAVE select switch in the VCO section. The manual says it selects the VCO waveform: sawtooth, triangle, or square.

From the performer’s perspective, it is in the upper-left synthesizer area, near the oscillator controls. Treat the VCO area as your oscillator group: the OCTAVE selector is nearby, the NOISE knob is also in that group, and the WAVE select switch is the discrete-position control used to choose the oscillator’s basic tone shape.

What it does: it changes the raw waveform that the oscillator generates before the sound goes through the filter and amplifier. Sawtooth, triangle, and square have different basic timbres, so this is one of the first controls to use when changing the character of the synth sound.

I cannot tell which waveform is currently selected from the manual or static panel references alone.

[Trace]
Sources used: monotribe Owner’s Manual, synthesizer section / VCO description; monotribe_manual_visual_index.json panel overview entry; static panel photo reference.
Routing weights: Device manual 55%; Visual/static layout 25%; Surface ARIA Store 10%; Surface Model/Map Schema 5%; Interaction Guidance Store 5%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names the WAVE select switch and its three waveform choices; layout is supported by the panel overview/static reference.
Unsupported-current-state risk: Low.
[/Trace]

## R2:
Use the WAVE select switch in the VCO section.

It selects the oscillator waveform: sawtooth, triangle, or square. The manual says the VCO is the oscillator that generates the basic waveform of the sound, and the WAVE select switch chooses which of those three waveforms it uses.

From the performer’s perspective, it is in the upper-left synthesizer area, near the VCO controls. Use the OCTAVE selector as a nearby landmark: the WAVE select switch is the small discrete-position switch just to the right/below that upper-left VCO area in the manual’s synthesizer panel diagram. The visual index identifies manual page 10 as the top-panel layout for the synthesizer section, including the VCO controls.

Functionally:

Sawtooth: brighter, buzzy oscillator tone.
Triangle: softer, rounder oscillator tone.
Square: hollow, pulse-like oscillator tone.

I can describe the possible positions, but I cannot know which waveform your unit is currently set to from the manual or static photo alone.

[Trace]
Sources used: monotribe_manual.pdf p.10–11; monotribe_manual_visual_index.json entry for p.10; Surface ARIA Store; Surface Model/Map Schema; Interaction Guidance Store; Mode Policy Store.
Routing weights: Device manual 45%; Visual/static layout 25%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 7%; Mode Policy Store 3%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names the WAVE select switch and its three waveform choices, and the panel diagram supports its location in the VCO area.
Unsupported-current-state risk: Low.
[/Trace]

## R3:
Use the WAVE select switch in the VCO section. The manual says it selects the oscillator waveform: sawtooth, triangle, or square.

From the performer’s perspective, it is in the upper-left synthesizer area, near the top edge. Find the VCO group: the OCTAVE selector is at the far upper-left, and the WAVE select switch is immediately to its right. It is a small three-position switch, not a knob.

What it does: it changes the basic waveform produced by the oscillator, which changes the raw tone before it goes through the filter and amplifier. Think of it as choosing the synth’s starting sound shape.

[Trace]
Sources used: monotribe_manual.pdf, page 10 panel diagram and page 11 VCO description; monotribe_manual_visual_index.json page 10 entry; foto_pannello static panel photo; 01_surface_aria_store.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 45%; Visual/static layout 25%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 5%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names the WAVE select switch and its three waveform choices, and the static layout sources support its upper-left VCO placement.
Unsupported-current-state risk: Low.
[/Trace]

# Baseline:
## R1:
Use the WAVE select switch in the VCO section. It selects the VCO waveform: sawtooth, triangle, or square.

It is in the synthesizer section, near the upper-left area of the panel. In the manual’s numbered panel diagram, it is control 2, next to the OCTAVE selector and above the NOISE knob.

What it does: the VCO is the oscillator that generates the basic waveform of the synth sound. Moving the WAVE select switch changes that basic oscillator shape between:

sawtooth wave
triangle wave
square wave

[Trace]
Sources used: monotribe_manual.pdf, pages 10–11; panel description entry “2. WAVE select switch.”
Routing weights: Device manual 90%; Visual/static layout 10%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names the control and its three waveform choices.
Unsupported-current-state risk: None.
[/Trace]

## R2:
Use the WAVE select switch in the VCO section. It selects the oscillator waveform: sawtooth, triangle, or square.

Where it is: on the top panel’s synthesizer section, it is control number 2 in the manual’s panel diagram. It sits near the top of the synth controls, to the right of the OCTAVE selector and above the RANGE select switch.

What it does: it changes the VCO waveform, which is the basic raw sound before filtering and amplification. The manual lists the choices as sawtooth wave, triangle wave, and square wave.

[Trace]
Sources used: monotribe manual, English pages 10–11; static panel photo.
Routing weights: Device manual 85%; Visual/static layout 15%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names control 2 as the WAVE select switch and states its waveform choices.
Unsupported-current-state risk: None.
[/Trace]

## R3:
Use the WAVE select switch in the VCO section.

It is in the synthesizer section, near the upper left area of the top panel. In the manual’s synth panel diagram, it is control number 2, immediately near the OCTAVE selector and above the NOISE knob.

What it does: it selects the VCO oscillator waveform. The three choices are:

sawtooth wave, triangle wave, or square wave.

Changing this switch changes the basic tone source before it goes through the filter and amplifier.

[Trace]
Sources used: monotribe_manual.pdf, English manual pages 10–11; static panel photo.
Routing weights: Device manual 80%; Visual/static layout 20%.
Evidence confidence: High.
Confidence rationale: The manual explicitly identifies control 2 as the VCO WAVE select switch and lists its three waveform choices.
Unsupported-current-state risk: None.
[/Trace]


