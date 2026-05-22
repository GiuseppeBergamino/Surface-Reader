Prompt: Create a structured description of the play button.

Response: 

Structured description: PLAY button
node_id: monotribe.sequencer.play_button
name: PLAY button
role: button
physical_type: pressable button
region: Sequencer section
group: Basic controls / transport controls
official_function: Press to play or stop the sequence.
actions:
  - press: starts sequence playback
  - press_again: stops sequence playback
documented_behavior:
  - Playback always starts from the beginning of the sequence.
  - The PLAY LED is lit during playback.
possible_indicators:
  - PLAY LED lit: playback is active
current_state: unknown
current_state_note: Static sources cannot tell whether the PLAY LED is currently lit or whether playback is running.
surface_map:
  approximate_position: upper area of the Sequencer section
  nearby_controls:
    - ACTIVE STEP button
    - TEMPO knob
    - REC button
    - FLUX button
    - STEP buttons
  tactile_guidance: >
    From the performer’s perspective, work in the sequencer area rather than the synth-control area.
    The PLAY button belongs to the transport/basic-control cluster, near REC and the tempo control.
    Treat it as the main start/stop button for the eight-step sequencer.

The manual identifies the PLAY button as basic control number 4 in the sequencer section and says: “Press this button to play or stop the sequence. Playback always starts from the beginning of the sequence. The PLAY LED will be lit during playback.” The visual index points to the sequencer-section panel diagram on manual page 13, which is the layout source for this control’s region and neighbors.

[Trace]
Sources used: monotribe_manual.pdf, sequencer section/basic controls; monotribe_manual_visual_index.json, page 13 sequencer panel overview; 01_surface_aria_store.md; 05_surface_model_map_schema.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 04_routing_and_uncertainty_policy.md.
Routing weights: Device manual 40%; Visual/static layout 20%; Surface ARIA Store 15%; Surface Model/Map Schema 15%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: The PLAY button name, function, LED meaning, and sequencer-region placement are directly supported by the manual and visual index.
Unsupported-current-state risk: Low.
[/Trace]
