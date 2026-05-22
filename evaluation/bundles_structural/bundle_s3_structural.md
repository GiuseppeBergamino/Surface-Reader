Prompt ID: s3

Prompt: Create a structured description of the octave selector.

# Surface Reader:
## R1:
Octave selector — structured surface description

Official name: OCTAVE selector

Surface model role: switch

Physical type: Discrete multi-position selector, visually/static-layout supported as a selector in the VCO area. I will not infer its current position from the static photo or manual.

Region: Synthesizer section

Group: VCO, or Voltage Controlled Oscillator

Function: The OCTAVE selector specifies the VCO pitch in octave steps. The manual gives one documented reference point: with the 64' setting, the ribbon keyboard pitch range is A0–D2.

Possible values: The manual page identifies octave settings, including 64'. The exact current selected octave cannot be determined from static sources alone.

Actions:
Move/select one of the octave positions to shift the VCO pitch range by octave steps.

Non-visual location:
From the performer’s perspective, the OCTAVE selector is in the upper-left synthesizer area, inside the VCO group. Use the ribbon keyboard as a lower-panel landmark, then move upward and left into the synth control area. The OCTAVE selector is the first numbered control in the synthesizer panel diagram, near the VCO waveform selector and noise control.

Nearby controls for confirmation:
It is grouped with VCO controls: the WAVE select switch, NOISE knob, and RANGE select switch. The VCO group is the part of the synth section that determines the basic pitch and waveform before filtering and amplification.

Current-state limitation:
I can describe what the OCTAVE selector can do and where it is, but I cannot know which octave setting is currently selected without live tactile, visual, or device-state evidence.

[Trace]
Sources used: monotribe_manual.pdf, especially English synthesizer section / VCO description; monotribe_manual_visual_index.json entry for page 10 panel overview; static panel photo foto_pannello; 01_surface_aria_store.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 04_routing_and_uncertainty_policy.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 35%; Visual/static layout 25%; Surface ARIA Store 15%; Surface Model/Map Schema 10%; Interaction Guidance Store 10%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: Medium.
Confidence rationale: The function and VCO grouping are manual-grounded, while tactile placement is based on static layout references rather than live observation.
Unsupported-current-state risk: Low.
[/Trace]

## R2:
Octave selector — structured surface description

Official name: OCTAVE selector.
Region: Synthesizer section.
Group: VCO, or Voltage Controlled Oscillator.
Semantic role: switch.
Physical type: discrete selector control; the static panel sources support it as a multi-position selector, not a continuous knob.
Function: It specifies the VCO pitch in octave steps. The manual gives one documented example: at the 64' setting, the ribbon keyboard pitch range is A0–D2.
Important interaction note: The OCTAVE selector is ignored when the RANGE select switch is set to WIDE; in WIDE mode the ribbon keyboard uses an extended continuous pitch range instead.

Possible states

The manual identifies the OCTAVE selector as an octave-step control, but the available text here does not expose the full list of printed octave positions. Therefore:

node_id: monotribe.synth.vco.octave_selector
name: OCTAVE selector
role: switch
physical_type: multi-position selector
region: Synthesizer section
group: VCO
description: Specifies the VCO pitch in octave steps.
possible_states:
  - documented_example: "64'"
    effect: "Ribbon keyboard range is A0–D2"
current_state: unknown
state_limitation: Current selector position cannot be inferred from the manual, diagram, or static panel photo alone.
Non-visual location and orientation

From the performer’s perspective, place the monotribe with the ribbon keyboard closest to you. The OCTAVE selector belongs to the upper-left synthesizer area, inside the VCO group. Use the left side of the panel as the main landmark: the OCTAVE selector is near the top-left VCO controls, above the lower ribbon-keyboard area and before the filter and LFO controls farther to the right.

Do not rely on the printed octave marking to determine its current setting unless you have sighted assistance or a separate tactile marking. Static sources can identify the control and its function, but not where it is currently set.

[Trace]
Sources used: monotribe_manual.pdf, manual page 10 panel overview via visual index, monotribe_manual_visual_index.json, foto_pannello, 01_surface_aria_store.md, 02_interaction_guidance_store.md, 03_mode_policy_store.md, 04_routing_and_uncertainty_policy.md, 05_surface_model_map_schema.md.
Routing weights: Device manual 35%; Visual/static layout 25%; Surface ARIA Store 15%; Surface Model/Map Schema 10%; Interaction Guidance Store 10%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: Medium.
Confidence rationale: Function and region are manual-grounded; exact tactile form and printed positions are only partially supported by static layout evidence.
Unsupported-current-state risk: Medium.
[/Trace]

## R3:
Structured description: OCTAVE selector

Official name: OCTAVE selector
Device: Korg monotribe
Region: Synthesizer section
Group: VCO, or Voltage Controlled Oscillator
Semantic role: switch
Physical type: rotary selector, based on the panel layout/static panel references
Interaction: turn/select one of the octave positions
Current state: unknown from static sources alone

Function

The OCTAVE selector specifies the VCO pitch in octave steps. The manual states that with the 64' setting, the ribbon keyboard pitch range is A0–D2.

Possible values

The manual identifies it as an octave selector for the VCO. The visible panel layout shows multiple discrete octave positions around the selector; these are possible positions, not current state. Static sources cannot tell which octave is selected now.

Non-visual location

From the performer’s perspective, the OCTAVE selector is in the upper-left area of the synthesizer section, at the start of the VCO controls. Use it as an early landmark for the synth controls: it sits before the waveform and range-related controls, and belongs to the pitch/source area rather than the filter or sequencer area.

Surface model node
node_id: monotribe.vco.octave_selector
name: OCTAVE selector
role: switch
physical_type: rotary selector
region: Synthesizer section
group: VCO
description: Specifies the VCO pitch in octave steps.
actions:
  - turn/select octave position
possible_states:
  - documented octave selector positions; current selected position requires situated evidence
current_state: unknown
Surface map entry
node_id: monotribe.vco.octave_selector
approximate_position: upper-left synthesizer area
landmarks:
  - upper-left VCO control group
  - nearby waveform/range controls
tactile_description: discrete rotary selector used for octave selection
navigation_hint: start at the upper-left control area of the synth section; the octave selector is the VCO pitch-range selector there.

[Trace]
Sources used: monotribe_manual.pdf p.10–11; monotribe_manual_visual_index.json entry for panel overview p.10; static panel photo foto_pannello; Surface ARIA Store; Surface Model/Map Schema; Interaction Guidance Store; Mode Policy Store; Routing and Uncertainty Policy.
Routing weights: Device manual 35%; Visual/static layout 25%; Surface ARIA Store 15%; Surface Model/Map Schema 15%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: Medium.
Confidence rationale: The function and section are manual-grounded; physical type and location are based on static layout references, not live observation.
Unsupported-current-state risk: Low.
[/Trace]

# Baseline:
## R1:
The OCTAVE selector sets the VCO pitch in octave steps. It affects the pitch range used by the ribbon keyboard, except when the RANGE select switch is set to WIDE, because the manual says WIDE ignores the OCTAVE selector.

Where it is:
It is in the Synthesizer section, at the upper-left area of the main control panel. In the manual’s synthesizer-section diagram, it is control 1, immediately left of the VCO WAVE select switch.

What it does:
The manual says: “This specifies the VCO pitch in steps of an octave.” With the 64' setting, the ribbon keyboard pitch range is A0–D2.

Related control:
The nearby RANGE select switch changes how the ribbon keyboard behaves:

WIDE: continuous pitch over a much wider range; OCTAVE selector is ignored.
NARROW: continuous pitch according to the printed ribbon keyboard.
KEY: chromatic pitch steps according to the printed ribbon keyboard.

[Trace]
Sources used: monotribe_manual.pdf, English manual p.10 synthesizer section diagram; p.11 VCO/OCTAVE selector and RANGE select switch; static panel photo for approximate physical layout.
Routing weights: Device manual 85%; Visual/static layout 15%.
Evidence confidence: High.
Confidence rationale: The OCTAVE selector function and WIDE limitation are explicitly documented in the manual.
Unsupported-current-state risk: None.
[/Trace]

## R2
Direct answer: The OCTAVE selector sets the VCO pitch in octave steps. It changes the pitch range used by the synthesizer sound generator. In the manual’s example, when set to “64’”, the ribbon keyboard pitch range is A0–D2.

Where it is: It is in the Synthesizer section, listed as control 1 in the panel diagram. On the top panel, it is at the upper-left area of the synth controls, immediately left of the VCO WAVE select switch and above the NOISE knob and RANGE select switch.

What it does:

It belongs to the VCO (Voltage Controlled Oscillator) section.
It changes the oscillator pitch by octaves.
The manual states that the VCO pitch is determined by the ribbon keyboard or sequence data, and that the OCTAVE selector specifies the VCO pitch in octave steps.
The manual also states that when the RANGE select switch is set to WIDE, the OCTAVE selector is ignored.

Limitation: The manual describes the selector’s function and one example pitch range, but from the manual and static panel photo alone I cannot determine the selector’s current physical position on your unit.

[Trace]
Sources used: monotribe_manual.pdf, English manual pp. 10–11; static panel photo.
Routing weights: Device manual 80%; Visual/static layout 20%.
Evidence confidence: High.
Confidence rationale: The manual directly names the OCTAVE selector and describes its function; the panel diagram and photo support its location.
Unsupported-current-state risk: Low.
[/Trace]

## R3:
Direct answer: The OCTAVE selector sets the VCO pitch in octave steps. It affects the pitch range used by the ribbon keyboard, except when the RANGE select switch is set to WIDE, because WIDE ignores the OCTAVE selector.

Where it is: It is in the Synthesizer section, at the upper-left area of the main control panel. In the manual’s numbered panel diagram it is control 1, immediately near the WAVE select switch labeled as control 2.

What it does: The manual says: “This specifies the VCO pitch in steps of an octave.” With the 64' setting, the ribbon keyboard pitch range is A0–D2. The VCO pitch is otherwise determined by the touched position on the ribbon keyboard or recorded sequence data.

Interaction with RANGE:

NARROW: OCTAVE selector applies; pitch changes continuously according to the printed ribbon keyboard.
KEY: OCTAVE selector applies; pitch changes in chromatic steps according to the printed ribbon keyboard.
WIDE: OCTAVE selector is ignored; pitch range is extended to about six times NARROW and changes continuously.

Limitation: The manual and static panel photo can identify the selector and describe its function, but they cannot tell what octave position your physical unit is currently set to.

[Trace]
Sources used: monotribe_manual.pdf, English manual pages 10–11; static panel photo.
Routing weights: Device manual 85%; Visual/static layout 15%.
Evidence confidence: High.
Confidence rationale: The OCTAVE selector is explicitly named and described in the manual’s synthesizer section.
Unsupported-current-state risk: Low.
[/Trace]



