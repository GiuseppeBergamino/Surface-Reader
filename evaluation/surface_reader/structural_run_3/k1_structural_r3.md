Prompt: Create a structured description of the cutoff.

Response: 

Structured description: CUTOFF

Official name: CUTOFF knob
Region: Synthesizer section
Group: VCF, Voltage Controlled Filter
Semantic role: slider
Physical type: rotary knob
Function: Adjusts the cutoff frequency of the VCF. The manual says turning it left darkens the sound, and turning it right brightens the sound.

Surface model node
node_id: synth_vcf_cutoff
role: slider
name: CUTOFF knob
region: Synthesizer section
group: VCF
physical_type: rotary knob
description: Adjusts the cutoff frequency of the low-pass filter, changing the brightness of the sound.
actions:
  - turn counterclockwise to lower cutoff / darken sound
  - turn clockwise to raise cutoff / brighten sound
possible_values:
  - continuous range, exact numeric range not documented
current_state: unknown from static sources
neighbours:
  - PEAK knob in the same VCF group
  - VCO and VCA controls nearby in the Synthesizer section
state_caution: Do not report a current cutoff value without live/situated evidence.
Surface map description

From the performer’s perspective, the CUTOFF knob is in the upper-middle synthesizer area, in the filter pair. Use the VCF group as a memory anchor: CUTOFF is the brightness knob; PEAK is the emphasis knob.

Tactile cue: find the pair of related rotary knobs in the filter area. The CUTOFF knob is the one documented as controlling filter brightness; PEAK is its partner for resonance/emphasis.

Non-visual use

Turn CUTOFF left for a darker, more muted synth sound. Turn it right for a brighter, more open sound. This describes the control’s possible effect, not its current position.

[Trace]
Sources used: monotribe Owner’s manual, Synthesizer section / VCF description; monotribe manual visual index, panel overview page 10; Surface ARIA Store; Surface Model/Map Schema; Interaction Guidance Store; Routing and Uncertainty Policy.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 15%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Routing/Uncertainty Policy 5%.
Evidence confidence: High.
Confidence rationale: The manual directly names CUTOFF and documents its function; static layout sources support its placement in the synthesizer/VCF area.
Unsupported-current-state risk: Low.
[/Trace]
