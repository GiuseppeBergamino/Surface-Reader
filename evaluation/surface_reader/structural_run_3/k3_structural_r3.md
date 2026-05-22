Prompt: Create a structured description of the rythm level.

Response: 

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

