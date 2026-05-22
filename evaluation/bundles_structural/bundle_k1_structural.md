Prompt ID: k1

Prompt: Create a structured description of the cutoff.

# Surface Reader:
## R1:
Cutoff — structured description

Official name: CUTOFF knob
Section: Synthesizer section
Group: VCF, or Voltage Controlled Filter
Semantic role: slider
Physical type: rotary knob
Current value: Not knowable from the manual or static panel references alone.

Function: The CUTOFF knob adjusts the cutoff frequency of the VCF. This changes the brightness of the synth sound: turning it left darkens the sound, and turning it right brightens the sound.

Related control: PEAK knob. Cutoff sets the filter frequency; Peak adds resonance or emphasis around that cutoff frequency.

Non-visual location: From the performer’s perspective, Cutoff is in the synthesizer section, in the filter area. It is the upper knob in the VCF pair, with PEAK directly below it. Think of the pair as: Cutoff above, Peak below.

Surface model entry:

node_id: vcf_cutoff
name: CUTOFF knob
role: slider
physical_type: rotary knob
region: Synthesizer section
group: VCF
description: Adjusts the VCF cutoff frequency, affecting sound brightness.
actions:
  - turn counterclockwise to darken the sound
  - turn clockwise to brighten the sound
related_controls:
  - PEAK knob
current_state: unavailable from static sources

[Trace]
Sources used: monotribe_manual.pdf, manual page 10/11 content; monotribe_manual_visual_index.json entry for panel overview; Surface ARIA Store; Surface Model/Map Schema; Interaction Guidance Store; Mode Policy Store.
Routing weights: Device manual 45%, Visual/static layout 20%, Surface ARIA Store 15%, Surface Model/Map Schema 10%, Interaction Guidance Store 5%, Mode Policy Store 5%.
Evidence confidence: High.
Confidence rationale: The manual directly documents the CUTOFF function and the panel diagram supports its placement in the VCF group.
Unsupported-current-state risk: Low.
[/Trace]

## R2:
Cutoff control — structured description

Official name: CUTOFF knob

Region: Synthesizer section

Group: VCF, or Voltage Controlled Filter

Semantic role: slider

Physical type: rotary knob

Function: The CUTOFF knob adjusts the cutoff frequency of the VCF. In practical sound terms, it changes the brightness of the synth sound. Turning it left makes the sound darker; turning it right makes it brighter.

Related control: PEAK knob. Cutoff sets the filter’s cutoff point; Peak emphasizes the sound around that cutoff frequency.

Non-visual location: From the performer’s perspective, the Cutoff knob is in the upper-middle synth-control area, in the filter group. It is the upper knob of the filter pair, with Peak directly below it.

Possible values: Continuous knob range; the manual describes left as darker and right as brighter, but does not provide numeric values.

Current state: Unknown. A manual or static panel photo cannot tell where the Cutoff knob is currently set.

node_id: synth.vcf.cutoff
name: CUTOFF knob
role: slider
physical_type: rotary knob
region: Synthesizer section
group: VCF
actions:
  - turn counterclockwise to lower cutoff / darken sound
  - turn clockwise to raise cutoff / brighten sound
possible_states:
  - lower cutoff / darker sound
  - higher cutoff / brighter sound
current_state: unavailable from static sources
neighbours:
  below: PEAK knob
semantic_relationships:
  - part of VCF filter group
  - affects timbre / brightness

[Trace]
Sources used: monotribe Owner’s Manual, panel description and functions; manual visual index, panel overview for synthesizer section; Surface ARIA Store; Surface Model/Map Schema; Interaction Guidance Store; Mode Policy Store; Routing and Uncertainty Policy.
Routing weights: Device manual 45%, Visual/static layout 20%, Surface ARIA Store 15%, Surface Model/Map Schema 10%, Interaction Guidance Store 5%, Mode Policy Store 3%, Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: The function and neighbouring filter context are documented in the manual, and the layout is supported by the panel overview/static references.
Unsupported-current-state risk: Low.
[/Trace]

## R3:
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

# Baseline:
## R1:
The CUTOFF knob controls the monotribe’s VCF cutoff frequency, which changes the brightness or darkness of the synth sound. Turning it left darkens the sound; turning it right brightens the sound.

Where it is
The CUTOFF knob is in the Synthesizer section, within the VCF group. In the manual’s numbered synthesizer panel diagram, it is control 5. It sits below the VCO controls and above the lower keyboard area, with the PEAK knob nearby as the other VCF control.

What it affects
The VCF is the filter. It changes the sound’s timbre by boosting or cutting frequency regions from the oscillator sound. The monotribe uses a 12 dB/oct low-pass filter, based on the Korg MS-20 filter circuit.

How to use it
Turn CUTOFF left for a more muted, darker tone. Turn it right for a brighter, more open tone. The LFO can also modulate the VCF cutoff frequency over time when its TARGET is set to affect the VCF.

Not current state
The manual and static panel sources describe what the CUTOFF knob does and where it is, but they cannot tell its current physical position on your unit.

[Trace]
Sources used: monotribe_manual.pdf, English manual pages 10–12; static panel photo for layout support.
Routing weights: Device manual 85%; Visual/static layout 15%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names the CUTOFF knob, places it in the VCF section, and describes its effect.
Unsupported-current-state risk: Low.
[/Trace]

## R2:
The CUTOFF control is the monotribe’s filter cutoff frequency control. It changes the brightness of the synthesizer sound by adjusting the cutoff frequency of the VCF. Turning it left makes the sound darker; turning it right makes the sound brighter.

Where it is:
The CUTOFF knob is in the Synthesizer section, in the VCF area. In the manual’s panel diagram, it is control 5, positioned below the VCO controls and above the lower row of LFO/keyboard-related controls.

What it affects:
The monotribe uses a 12 dB/oct low-pass filter (LPF) in the VCF. The filter changes the timbre by boosting or cutting frequency regions of the sound produced by the oscillator. The CUTOFF knob sets the point where that filtering happens.

Related controls:
The nearby PEAK knob adjusts the VCF resonance, emphasizing the cutoff frequency. The LFO can also modulate the VCF cutoff over time when the LFO TARGET is set to VCF or VCO+VCF.

Current-state limitation:
The manual and static panel layout can identify the CUTOFF control and describe what it does, but they cannot tell the current physical position of your CUTOFF knob.

[Trace]
Sources used: monotribe_manual.pdf, English owner’s manual pages 10–12; static panel layout reference.
Routing weights: Device manual 85%; Visual/static layout 15%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names the CUTOFF knob and describes its effect on VCF cutoff frequency and brightness.
Unsupported-current-state risk: Low.
[/Trace]

## R3:
The CUTOFF knob controls the cutoff frequency of the monotribe’s VCF, or Voltage Controlled Filter. It changes the brightness of the synth sound. Turning it left makes the sound darker; turning it right makes the sound brighter.

Where it is:
The CUTOFF knob is in the Synthesizer section, in the VCF area. In the manual’s front-panel diagram, it is control number 5, placed below the VCO controls and above the VCA/LEVEL area.

What it does:
The monotribe uses a 12 dB/oct low-pass filter, described as the same traditional filter type used on the Korg MS-20. The filter shapes the timbre by cutting or emphasizing frequency regions of the sound from the oscillator. The CUTOFF knob sets the point where that filtering happens.

Related control:
The nearby PEAK knob adjusts the VCF resonance, adding emphasis around the cutoff frequency. The LFO can also modulate the VCF cutoff over time when its TARGET switch is set to VCF or VCO+VCF.

[Trace]
Sources used: monotribe_manual.pdf, English manual pages 10–12; static panel photo for control-location context.
Routing weights: Device manual 85%; Visual/static layout 15%.
Evidence confidence: High.
Confidence rationale: The manual explicitly identifies CUTOFF as VCF control number 5 and describes its effect.
Unsupported-current-state risk: None.
[/Trace]