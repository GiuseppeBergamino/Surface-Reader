Prompt ID: k3

Prompt: Create a structured description of the rythm level.

# Surface Reader:
## R1:
The RHYTHM knob controls the volume level of the monotribe’s drum sound generator. In other words, it is the level control for the rhythm/drum part, not for the synth part. The manual identifies it as item 11 in the sequencer section and states: “This knob adjusts the volume of the drum sound generator.”

Structured description:

node_id: sequencer.rhythm_level
name: RHYTHM knob
role: slider
physical_type: rotary knob
region: Sequencer section
group: Drum sound generator sequence controls
function: Adjusts the volume of the drum sound generator
controlled_sound_source:
  - BD: bass drum
  - SN: snare drum
  - HH: hi-hat
actions:
  - turn counterclockwise to decrease drum/rhythm level
  - turn clockwise to increase drum/rhythm level
current_state: unknown
current_state_note: Static sources cannot determine the knob’s present position or actual output level.
related_controls:
  - PART buttons: select SYNTH, BD, SN, or HH for editing
  - STEP buttons: turn steps on or off for the selected drum part
  - LEVEL knob: adjusts the synth/audio output level separately
non_visual_anchor: Use it as the drum-volume control in the sequencer area; it balances the rhythm/drum generator against the synth level.

Tactile/mental-map note: treat LEVEL and RHYTHM as the two main volume concepts: LEVEL for the synth/output level, RHYTHM for the drum generator level.

[Trace]
Sources used: monotribe_manual.pdf, manual page 15; monotribe_manual_visual_index.json, page 13/15 sequencer layout entries; 01_surface_aria_store.md; 05_surface_model_map_schema.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md.
Routing weights: Device manual 55%; Visual/static layout 15%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 5%.
Evidence confidence: High.
Confidence rationale: The manual explicitly defines the RHYTHM knob as the drum sound generator volume control.
Unsupported-current-state risk: Low.
[/Trace]

## R2:
Structured description: RHYTHM level

Official control name: RHYTHM knob
Likely user term: “rhythm level”
Region: Sequencer section
Group: Drum sound generator sequence controls
Semantic role: slider
Physical type: rotary knob
Function: Adjusts the volume of the drum sound generator. The monotribe’s drum sound generator includes BD, SN, and HH parts, played by sequence data.

{
  "node_id": "sequencer_rhythm_level",
  "role": "slider",
  "name": "RHYTHM knob",
  "physical_type": "rotary knob",
  "region": "Sequencer section",
  "group": "Drum sound generator sequence controls",
  "description": "Adjusts the volume of the drum sound generator.",
  "affected_parts": ["BD", "SN", "HH"],
  "actions": ["turn clockwise to raise drum level", "turn counterclockwise to lower drum level"],
  "possible_states": "continuous volume value",
  "current_state": "requires situated evidence",
  "nearby_controls": {
    "related": ["PART buttons", "STEP buttons"],
    "same_functional_area": "drum sequence controls"
  },
  "safety_notes": [
    "Before turning the power on, the manual instructs turning LEVEL and RHYTHM all the way left.",
    "For power-off, the manual also instructs turning LEVEL and RHYTHM all the way left."
  ]
}
Non-visual use

Treat RHYTHM as the drum level knob. It does not set the synth volume; it controls the drum sound generator level. The manual also uses it during startup and shutdown: turn both LEVEL and RHYTHM fully left before powering on or off, then turn RHYTHM clockwise to an appropriate level after power-on.

Current-state limitation

I can describe what RHYTHM does and how it should be represented, but I cannot know its current knob position from the manual or static panel references alone. A continuous rotary knob may be modeled as a slider, but valuenow requires situated evidence.

[Trace]
Sources used: monotribe_manual.pdf pages 5, 9, 15; 01_surface_aria_store.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 55%; Surface ARIA Store 20%; Surface Model/Map Schema 15%; Interaction Guidance Store 10%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names RHYTHM knob and states its function; semantic mapping follows the provided surface-model rules.
Unsupported-current-state risk: Low.
[/Trace]


## R3:
Structured description: RHYTHM level control
node_id: monotribe.sequencer.rhythm_level
name: RHYTHM knob
role: slider
physical_type: rotary knob
region: Sequencer section
group: Drum sound generator sequence controls
official_function: Adjusts the volume of the drum sound generator.
manual_source: monotribe Owner's Manual, Sequencer section, page 15
possible_user_actions:
  - turn counterclockwise to decrease drum level
  - turn clockwise to increase drum level
controls_audio_from:
  - BD bass drum part
  - SN snare drum part
  - HH hi-hat part
does_not_control:
  - synthesizer VCO level
  - overall output level
  - headphone/output jack level directly
current_state: unknown
current_state_note: Static sources cannot tell the present knob position or current drum volume.
Non-visual/tactile description

The RHYTHM knob is the drum level control for the rhythm/drum generator. It is a rotary knob, so treat it as a continuous level control rather than an on/off button.

From the performer’s perspective, it belongs to the sequencer area, near the drum part and step controls. Use it as the drum-volume counterpart to the synth LEVEL knob: LEVEL adjusts the synth volume, while RHYTHM adjusts the drum sound generator volume. The manual states that the RHYTHM knob “adjusts the volume of the drum sound generator” .

Surface model meaning

In Surface ARIA terms, RHYTHM should be represented as:

role: slider
physical_type: rotary knob
value_type: continuous audio level
current_value_supported: false_without_situated_evidence

Do not expose a current value such as “50%” unless there is live evidence of the actual knob position.

[Trace]
Sources used: monotribe_manual.pdf page 15; monotribe_manual_visual_index.json entry for sequencer section/page 13; 01_surface_aria_store.md; 05_surface_model_map_schema.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 04_routing_and_uncertainty_policy.md.
Routing weights: Device manual 45%; Visual/static layout 15%; Surface ARIA Store 15%; Surface Model/Map Schema 15%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: The function is directly documented in the manual; spatial detail is static and approximate.
Unsupported-current-state risk: Low.
[/Trace]

# Baseline:
## R1:
The RHYTHM knob is the drum-level control: it adjusts the volume of the monotribe’s drum sound generator.

Structured description

Official name: RHYTHM knob
Section: Sequencer section, under “Drum sound generator sequence controls”
Function: Raises or lowers the volume of the drum sound generator.
Affected parts: BD, SN, and HH drum parts, as a combined drum level.
Use: Turn it left to reduce the drum volume; turn it right to increase the drum volume.
Related power-on/off caution: The manual says to turn both the LEVEL knob and RHYTHM knob all the way left before turning the monotribe on or off.

Where it is: In the sequencer section. In the manual’s sequencer control diagram, it is item 11, positioned in the lower-right area of the sequencer controls, near the step buttons.

[Trace]
Sources used: monotribe_manual.pdf, pages 9 and 15; sequencer section diagram page 13; static panel photo.
Routing weights: Device manual 90%; Visual/static layout 10%.
Evidence confidence: High.
Confidence rationale: The manual directly defines the RHYTHM knob as controlling the drum sound generator volume.
Unsupported-current-state risk: None.
[/Trace]

## R2:
The RHYTHM knob is the rhythm level control. It adjusts the volume of the drum sound generator. The drum sound generator includes the three rhythm parts: BD bass drum, SN snare drum, and HH hi-hat.

Where it is:
It is in the Sequencer section, near the lower-right area of the panel controls. In the manual’s sequencer diagram, it is item 11, placed near the step-button area and the drum sequence controls.

What it does:
Turn the RHYTHM knob to change the overall volume level of the drum sound generator. It affects the rhythm/drum parts as a group, not an individual BD, SN, or HH level.

How to use it:
Before turning the monotribe on or off, the manual says to turn both the LEVEL knob and RHYTHM knob all the way left. After powering on, turn the RHYTHM knob clockwise to an appropriate level.

Limitation:
The manual documents this as a volume control for the drum sound generator. It does not document separate level controls for BD, SN, and HH.

[Trace]
Sources used: monotribe_manual.pdf, English manual pages 9 and 15; static panel photo.
Routing weights: Device manual 85%; Visual/static layout 15%.
Evidence confidence: High.
Confidence rationale: The manual directly defines the RHYTHM knob as adjusting drum sound generator volume.
Unsupported-current-state risk: None.
[/Trace]

## R3:
The RHYTHM knob controls the volume level of the drum sound generator. It affects the drum parts: BD bass drum, SN snare drum, and HH hi-hat.

Where it is:
It is in the sequencer section, near the lower-right area of the main control panel. In the manual’s sequencer diagram, it is item 11, positioned just above or near the step-button area used for drum sequencing.

What it does:
Turning the RHYTHM knob changes the overall drum sound generator volume. The manual also says that when powering on or off, the RHYTHM knob should be turned all the way left before adjusting it to an appropriate level.

Related controls:
The RHYTHM level works with the drum parts selected by the BD, SN, and HH PART buttons, and with the STEP buttons that turn drum steps on or off.

[Trace]
Sources used: monotribe_manual.pdf, English manual pages 9, 13–15; static panel photo.
Routing weights: Device manual 85%; Visual/static layout 15%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names the RHYTHM knob and says it adjusts the drum sound generator volume.
Unsupported-current-state risk: None.
[/Trace]