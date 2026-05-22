Prompt ID: s1

Prompt: Create a structured description of the keyboard range selector.

# Surface Reader:
## R1:
Structured description: keyboard range selector

Official control name: RANGE select switch
Surface model role: switch
Physical type: three-position slide switch
Region: Synthesizer section
Group: VCO / keyboard control group
Related control: Ribbon keyboard

Function

The RANGE select switch sets the ribbon keyboard’s playing mode. The manual defines three possible positions: WIDE, NARROW, and KEY.

Possible positions
Position	Documented behavior
WIDE	Extends the pitch range to about six times the NARROW setting. Pitch changes continuously, and the OCTAVE selector is ignored.
NARROW	Pitch changes continuously according to the printed ribbon keyboard.
KEY	Pitch changes in chromatic steps according to the printed ribbon keyboard.
Non-visual description

From the performer’s perspective, the RANGE select switch is in the upper-left synthesizer area, near the VCO controls and related to the ribbon keyboard. It is not a knob; it is a discrete selector with three possible settings. Use it as a mode switch for how the ribbon responds when touched.

State limitation

This describes the control and its possible settings only. I cannot determine the current physical position of the RANGE switch from the manual or static panel references alone.

[Trace]
Sources used: monotribe_manual.pdf, manual page 11; monotribe_manual_visual_index.json entry for manual page 10; foto_pannello; 01_surface_aria_store.md; 05_surface_model_map_schema.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 04_routing_and_uncertainty_policy.md.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 15%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names the control and its three documented settings; layout and role are supported by static references.
Unsupported-current-state risk: Low.
[/Trace]

## R2:
Keyboard range selector — structured description

Official name: RANGE select switch
Device area: Synthesizer section → VCO / keyboard control area
Semantic role: switch
Physical type: three-position slide switch
Purpose: Sets how the ribbon keyboard controls pitch. The manual says it “specifies the ribbon keyboard’s playing mode” .

Possible positions

WIDE
Extends the pitch range to approximately six times the NARROW setting. Pitch change is continuous, and the OCTAVE selector is ignored.

NARROW
Pitch changes continuously according to the printed ribbon keyboard range.

KEY
Pitch changes in chromatic steps according to the printed ribbon keyboard, making it behave more like a conventional keyboard.

Surface model node
{
  "node_id": "monotribe.synth.vco.range_select",
  "role": "switch",
  "name": "RANGE select switch",
  "region": "Synthesizer section",
  "group": "VCO / ribbon keyboard pitch control",
  "physical_type": "three-position slide switch",
  "description": "Selects the ribbon keyboard playing mode.",
  "possible_states": ["WIDE", "NARROW", "KEY"],
  "current_state": null,
  "actions": ["move to WIDE", "move to NARROW", "move to KEY"],
  "state_notes": {
    "WIDE": "Continuous pitch; range extended to about six times NARROW; OCTAVE selector ignored.",
    "NARROW": "Continuous pitch according to the printed ribbon keyboard.",
    "KEY": "Chromatic stepped pitch according to the printed ribbon keyboard."
  }
}
Non-visual orientation

From the performer’s perspective, this switch belongs to the synthesizer section, near the ribbon keyboard controls. Treat it as the keyboard-behavior switch: it decides whether the ribbon plays freely across a wide range, freely across a narrower range, or in chromatic note steps.

I cannot determine its current position from the manual, diagram, or static panel photo alone.

[Trace]
Sources used: monotribe_manual.pdf, manual page 11; monotribe_manual_visual_index.json entry for page 10; foto_pannello static panel photo; 01_surface_aria_store.md; 05_surface_model_map_schema.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 04_routing_and_uncertainty_policy.md.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 15%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: The manual directly defines the RANGE select switch and its three documented positions; static layout sources support its physical/surface role.
Unsupported-current-state risk: Low.
[/Trace]

## R3:
Keyboard range selector — structured description

Official name: RANGE select switch

Surface model role: switch

Physical type: three-position slide switch, based on the panel reference and manual layout.

Region: Synthesizer section

Group: VCO / ribbon keyboard control group

Function: It specifies the ribbon keyboard’s playing mode. The manual defines three possible settings:

Position	Meaning
WIDE	Extends the pitch range to about six times the NARROW setting. Pitch change is continuous. The OCTAVE selector is ignored.
NARROW	Pitch changes continuously according to the printed ribbon keyboard.
KEY	Pitch changes in chromatic steps according to the printed ribbon keyboard.

Tactile location: From the performer’s perspective, the RANGE select switch is in the upper-left synthesizer area, near the ribbon keyboard controls. It belongs with the VCO controls rather than the sequencer. Use the long ribbon keyboard as a lower-panel landmark, then move upward toward the synth controls; the RANGE switch is one of the small discrete-position switches associated with how the ribbon responds.

Actions:
Move the switch to one of three discrete positions: WIDE, NARROW, or KEY.

Current state: Not available from static sources. I can describe the possible settings, but I cannot know which position your physical switch is currently in without live evidence.

Compact semantic node:

{
  "node_id": "synth.vco.range_select",
  "name": "RANGE select switch",
  "role": "switch",
  "physical_type": "three-position slide switch",
  "region": "Synthesizer section",
  "group": "VCO / ribbon keyboard controls",
  "description": "Specifies the ribbon keyboard's playing mode.",
  "possible_states": ["WIDE", "NARROW", "KEY"],
  "current_state": null,
  "actions": ["move to WIDE", "move to NARROW", "move to KEY"],
  "unsupported_current_state_risk": "High"
}

[Trace]
Sources used: monotribe_manual.pdf p.11; monotribe_manual_visual_index.json entry for p.10; static panel photo foto_pannello; 01_surface_aria_store.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 04_routing_and_uncertainty_policy.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 15%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: Medium.
Confidence rationale: Function and possible states are manual-grounded; tactile location is based on static layout rather than live inspection.
Unsupported-current-state risk: High.
[/Trace]

# Baseline:
## R1:
The keyboard range selector is the RANGE select switch. It sets how the ribbon keyboard controls pitch.

Where it is

It is in the Synthesizer section, listed as control 4 in the panel diagram. It sits near the VCO controls, below or near the OCTAVE selector, WAVE select switch, and NOISE knob, and above the ribbon keyboard area.

What it does

The RANGE select switch has three settings:

Setting	Result
WIDE	Extends the pitch range to approximately six times the NARROW setting. Pitch changes continuously. The OCTAVE selector is ignored.
NARROW	Pitch changes continuously according to the printed ribbon keyboard.
KEY	Pitch changes in chromatic steps according to the printed ribbon keyboard.
Practical meaning

Use WIDE for broad, continuous pitch sweeps.
Use NARROW for smaller continuous pitch movement across the ribbon.
Use KEY when you want stepped, chromatic notes rather than a smooth glide.

[Trace]
Sources used: monotribe_manual.pdf, English manual pp. 10–11; static panel photo.
Routing weights: Device manual 85%; Visual/static layout 15%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names the RANGE select switch and defines all three settings.
Unsupported-current-state risk: None.
[/Trace]

## R2:
Direct answer: The keyboard range selector is the RANGE select switch. It sets how the ribbon keyboard controls pitch.

Where it is: It is in the Synthesizer section, listed as control 4 in the panel description. It is near the VCO controls, associated with the ribbon keyboard’s pitch behavior.

What it does:

WIDE: Extends the pitch range to approximately six times the NARROW setting. Pitch changes continuously. The OCTAVE selector is ignored.
NARROW: Pitch changes continuously according to the printed ribbon keyboard.
KEY: Pitch changes in chromatic steps according to the printed ribbon keyboard.

How to use it: Move the RANGE select switch to choose between broad continuous pitch control, narrower continuous pitch control, or stepped chromatic pitch control.

Limitation: The manual describes the possible settings, but it cannot tell which setting your physical switch is currently on.

[Trace]
Sources used: monotribe_manual.pdf, English manual pages 5, 10–11; static panel photo for layout context.
Routing weights: Device manual 90%; Visual/static layout 10%.
Evidence confidence: High.
Confidence rationale: The RANGE select switch and its three settings are directly documented in the manual.
Unsupported-current-state risk: Low.
[/Trace]

## R3:
Keyboard range selector
Direct answer

The keyboard range selector is the RANGE select switch. It specifies the ribbon keyboard’s playing mode.

Where it is

It is in the Synthesizer section, listed as control 4 in the manual’s panel diagram. It sits near the VCO controls, below/near the OCTAVE selector, WAVE select switch, and NOISE knob, and above the ribbon keyboard area.

What it does

The RANGE select switch has three documented settings:

Setting	Function
WIDE	Extends the pitch range to approximately six times the NARROW setting. Pitch change is continuous. The OCTAVE selector is ignored.
NARROW	Pitch changes continuously according to the printed ribbon keyboard.
KEY	Pitch changes in chromatic steps according to the printed ribbon keyboard.
Use note

Use WIDE for a broad continuous pitch sweep, NARROW for a smaller continuous ribbon range, and KEY when you want chromatic stepped pitches like a conventional keyboard.

[Trace]
Sources used: monotribe_manual.pdf, English manual pages 10–11, “Synthesizer section,” item 4 “RANGE select switch”; static panel photo for approximate layout.
Routing weights: Device manual 85%; Visual/static layout 15%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names the control and defines all three settings.
Unsupported-current-state risk: Low.
[/Trace]

