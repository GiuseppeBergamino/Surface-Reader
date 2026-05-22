Prompt: Create a structured description of the noise level.

Response:

Noise level — structured description

Official control name: NOISE knob
Surface role: slider
Physical type: rotary knob
Region: Synthesizer section
Group: VCO / oscillator group
Function: Adjusts the level of white noise mixed with the VCO output. The manual states: “This knob adjusts the level of white noise that’s mixed with the VCO output.”

What it controls

The NOISE knob controls how much white noise is added to the oscillator sound before the signal continues through the filter and amplifier. In the block diagram, the noise generator is part of the VCO-side sound source path feeding the VCF and VCA.

Non-visual meaning

Think of it as a continuous “noise amount” control:

Turn left: less white noise mixed into the synth sound.
Turn right: more white noise mixed into the synth sound.
Fully left likely means no or minimal noise, but the manual does not give an exact numeric range.
Surface-model entry
node_id: synth.vco.noise_level
name: NOISE knob
role: slider
physical_type: rotary knob
region: Synthesizer section
group: VCO
parameter: white noise level
action:
  - turn counterclockwise to decrease noise level
  - turn clockwise to increase noise level
possible_values: continuous range, exact values not documented
current_state: unknown
current_state_reason: static sources cannot reveal the present knob position
source: monotribe Owner's manual, Synthesizer section / VCO description
Current-state limitation

I can describe what the NOISE knob does, but I cannot determine the current noise level setting from the manual, screenshots, or static panel photo alone.

[Trace]
Sources used: monotribe_manual.pdf, Synthesizer section / VCO description; monotribe_manual.pdf, block diagram; Surface ARIA Store; Surface Model/Map Schema; Interaction Guidance Store; Routing and Uncertainty Policy.
Routing weights: Device manual 55%, Surface ARIA Store 15%, Surface Model/Map Schema 15%, Interaction Guidance Store 10%, Routing/Uncertainty Policy 5%.
Evidence confidence: High.
Confidence rationale: The manual directly defines the NOISE knob function; semantic role and current-state limitation are supported by the stores.
Unsupported-current-state risk: Low.
[/Trace]
