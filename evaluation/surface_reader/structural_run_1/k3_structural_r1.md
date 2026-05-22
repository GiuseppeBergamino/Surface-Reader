Prompt: Create a structured description of the rythm level.

Response: 
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

