Prompt ID: s2

Prompt: Create a structured description of the VCO wave selector.

# Surface Reader:
## R1:
VCO WAVE select switch — structured description

Official name: WAVE select switch
Device section: Synthesizer section
Group: VCO — Voltage Controlled Oscillator
Semantic role: switch
Physical type: three-position waveform selector switch
Purpose: selects the oscillator waveform that becomes the basic sound source of the synth voice.

Documented possible positions
Position	Meaning	Sound source
Sawtooth wave	Selects sawtooth oscillator waveform	bright, harmonically rich VCO tone
Triangle wave	Selects triangle oscillator waveform	smoother, simpler VCO tone
Square wave	Selects square oscillator waveform	hollow/pulse-like VCO tone

The manual states that the VCO generates “the waveform that’s the basis of the sound: a sawtooth wave, triangle wave, or square wave,” and that the WAVE select switch chooses between those three waveforms.

Non-visual location and orientation

From the performer’s perspective, the VCO controls are in the upper-left synthesizer area of the panel. The WAVE select switch is part of the VCO group, near the OCTAVE selector and NOISE knob. Use the VCO area as a small oscillator cluster: octave selection, waveform selection, and noise level all belong together.

Surface model node
node_id: synth.vco.wave_select
role: switch
name: WAVE select switch
region: Synthesizer section
group: VCO
physical_type: three-position selector switch
description: Selects the VCO waveform used as the basis of the synth sound.
possible_states:
  - sawtooth wave
  - triangle wave
  - square wave
actions:
  - select sawtooth wave
  - select triangle wave
  - select square wave
current_state: unknown
current_state_note: Static sources cannot determine the switch’s present position.
Current-state limitation

I can describe the possible settings and static location, but I cannot know which waveform is currently selected without live evidence from the physical instrument.

[Trace]
Sources used: monotribe_manual.pdf; monotribe_manual_visual_index.json; 01_surface_aria_store.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 15%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 5%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names the WAVE select switch and its three possible waveform settings; layout is supported by the panel overview index.
Unsupported-current-state risk: Low.
[/Trace]

## R2:
Structured description: VCO WAVE select switch

Official name: WAVE select switch
Surface node ID: monotribe.vco.wave_select
Parent region: Synthesizer section
Group: VCO, or Voltage Controlled Oscillator
Semantic role: switch
Physical type: Three-position slide switch
Control purpose: Selects the VCO waveform. The manual says the VCO waveform can be sawtooth, triangle, or square.

Possible settings
Position / value	Meaning
Sawtooth wave	Selects sawtooth as the oscillator waveform
Triangle wave	Selects triangle as the oscillator waveform
Square wave	Selects square as the oscillator waveform

Current state: Unknown. A manual, diagram, or static panel photo can identify the switch and its possible positions, but cannot confirm which waveform is selected on your physical unit right now.

Non-visual location and tactile map

From the performer’s perspective, the WAVE select switch is in the upper-left synthesizer area, inside the VCO group.

Use this mental anchor:

VCO group = octave selector, waveform switch, noise knob, range switch.

A tactile route:

Start in the upper-left control area of the panel.
Find the VCO controls.
The WAVE select switch is a small three-position switch near the OCTAVE selector and above/near the NOISE knob area.
It is not a continuous knob; it has three discrete stops.
Surface model entry
node_id: monotribe.vco.wave_select
name: WAVE select switch
role: switch
physical_type: three-position slide switch
region: Synthesizer section
group: VCO
parent: monotribe.vco
description: Selects the VCO waveform used as the basis of the synth sound.
possible_states:
  - sawtooth wave
  - triangle wave
  - square wave
current_state: unknown
actions:
  - move switch to one of three waveform positions
state_rule: current selected waveform requires situated evidence
sources:
  - monotribe_manual.pdf, panel description and VCO section
  - monotribe_manual_visual_index.json, page 10 panel overview
  - foto_pannello static panel reference

[Trace]
Sources used: monotribe_manual.pdf p.10–11; monotribe_manual_visual_index.json entry for p.10; foto_pannello static panel reference; 01_surface_aria_store.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 05_surface_model_map_schema.md; 04_routing_and_uncertainty_policy.md.
Routing weights: Device manual 35%; Visual/static layout 25%; Surface ARIA Store 15%; Surface Model/Map Schema 15%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names the WAVE select switch and its three waveform settings, while the panel diagram/photo support static location and physical grouping.
Unsupported-current-state risk: Medium.
[/Trace]

## R3:
Structured description: VCO WAVE select switch

Official name: WAVE select switch
Section: Synthesizer section
Group: VCO, or Voltage Controlled Oscillator
Semantic role: switch
Physical type: multi-position slide switch, based on the panel diagram/static layout
Purpose: Selects the VCO waveform. The manual states that the oscillator generates the waveform that forms the basis of the sound, and the WAVE select switch chooses between sawtooth, triangle, and square waves.

Possible settings
Sawtooth wave
A selectable VCO waveform.
Triangle wave
A selectable VCO waveform.
Square wave
A selectable VCO waveform.
Surface model node
{
  "node_id": "synth.vco.wave_select",
  "role": "switch",
  "name": "WAVE select switch",
  "region": "Synthesizer section",
  "group": "VCO",
  "physical_type": "slide switch",
  "description": "Selects the VCO waveform used as the basis of the synth sound.",
  "possible_states": [
    "sawtooth wave",
    "triangle wave",
    "square wave"
  ],
  "current_state": null,
  "actions": [
    "move switch to sawtooth",
    "move switch to triangle",
    "move switch to square"
  ]
}
Non-visual/tactile guidance

From the performer’s perspective, the WAVE select switch is in the upper-left synthesizer area, inside the VCO group. It is near the OCTAVE selector, the NOISE knob, and the RANGE select switch. Use this as a memory anchor: VCO starts the sound; WAVE chooses the raw shape before filtering and amplification.

I cannot determine the switch’s current position from the manual, screenshots, or static panel photo alone.

[Trace]
Sources used: monotribe_manual.pdf, manual page 10 panel overview, manual page 11 VCO description, monotribe_manual_visual_index.json, foto_pannello, 01_surface_aria_store.md, 02_interaction_guidance_store.md, 03_mode_policy_store.md, 04_routing_and_uncertainty_policy.md, 05_surface_model_map_schema.md.
Routing weights: Device manual 35%; Visual/static layout 25%; Surface ARIA Store 15%; Surface Model/Map Schema 15%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: The manual gives the official name, function, and possible settings; static layout sources support placement and physical type.
Unsupported-current-state risk: Low.
[/Trace]

# Baseline:
## R1:
The VCO wave selector is the WAVE select switch in the VCO section. It selects the oscillator waveform used as the basis of the synth sound.

Where it is:
It is control 2 in the synthesizer section diagram. It sits near the top-left area of the panel, to the right of the OCTAVE selector and above the RANGE select switch.

What it controls:
The manual says the VCO generates the waveform that forms the basis of the sound. The WAVE select switch chooses one of three VCO waveforms:

Switch choice	Manual waveform name	Effect
Sawtooth wave	Sawtooth wave	Selects a sawtooth oscillator waveform
Triangle wave	Triangle wave	Selects a triangle oscillator waveform
Square wave	Square wave	Selects a square oscillator waveform

How to use it:
Move the WAVE select switch to one of its three positions to choose the VCO waveform. The selected waveform is then sent onward through the rest of the synth path, including the VCF and VCA.

Limitation:
The manual documents the available waveform choices and the switch function, but it cannot tell which waveform is currently selected on your physical unit.

[Trace]
Sources used: monotribe_manual.pdf, Panel description and functions, Synthesizer section, manual pages 10–11; static panel photo for layout relation.
Routing weights: Device manual 85%; Visual/static layout 15%.
Evidence confidence: High.
Confidence rationale: The manual explicitly identifies control 2 as the VCO WAVE select switch and lists its three waveform choices.
Unsupported-current-state risk: Low.
[/Trace]

## R2:
VCO WAVE select switch

Direct answer:
The WAVE select switch chooses the VCO waveform: sawtooth wave, triangle wave, or square wave.

Where it is:
In the Synthesizer section, it is item 2 in the manual’s panel diagram. It sits near the top-left area of the panel, in the VCO group. It is next to the OCTAVE selector and above the NOISE knob and RANGE select switch.

What it does:
The VCO is the oscillator that creates the basic sound waveform. The WAVE select switch changes that basic waveform between:

Sawtooth wave
Triangle wave
Square wave

These waveforms are the starting tone source before the sound is further shaped by the VCF, VCA, EG, and LFO.

How to use it:
Move the switch to one of its three positions to choose the waveform you want. The manual documents the three waveform choices, but it does not describe the exact physical order of the three switch positions in text.

Limitation:
The manual and static panel photo can identify the control and its documented function, but they cannot tell which waveform your unit is currently set to.

[Trace]
Sources used: monotribe_manual.pdf, English manual pp. 10–11; static panel photo.
Routing weights: Device manual 80%; Visual/static layout 20%.
Evidence confidence: High.
Confidence rationale: The manual directly names item 2 as the WAVE select switch and lists its three VCO waveform choices.
Unsupported-current-state risk: Low.
[/Trace]


## R3:
The VCO WAVE select switch chooses the basic oscillator waveform for the monotribe’s synth sound. It has three positions: sawtooth wave, triangle wave, and square wave.

Where it is:
It is in the Synthesizer section, near the upper-left area of the top panel. In the manual’s Synthesizer section diagram, it is control 2, placed to the right of the OCTAVE selector and above the NOISE knob.

What it does:
The VCO generates the waveform that forms the basis of the synth sound. The WAVE select switch selects one of these VCO waveforms:

Position	Waveform	Basic role
Sawtooth	Sawtooth wave	One of the three available VCO source waves
Triangle	Triangle wave	One of the three available VCO source waves
Square	Square wave	One of the three available VCO source waves

The selected waveform is then part of the sound path that continues through the VCF and VCA. The manual does not describe the tonal character of each waveform beyond naming the three waveform types.

[Trace]
Sources used: monotribe_manual.pdf, Synthesizer section pages 10–11; static panel photo.
Routing weights: Device manual 85%; Visual/static layout 15%.
Evidence confidence: High.
Confidence rationale: The manual explicitly identifies control 2 as the VCO WAVE select switch and lists its three waveform choices.
Unsupported-current-state risk: None.
[/Trace]


