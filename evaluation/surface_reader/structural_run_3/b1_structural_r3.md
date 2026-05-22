Prompt: Create a structured description of the play button.

Response: 

Structured description: PLAY button

Official name: PLAY button
Device: Korg monotribe
Region: Sequencer section
Group: Basic controls / transport controls
Semantic role: button
Physical type: Pressable button
Primary action: Press
Documented function: Pressing the PLAY button starts or stops the sequence. Playback always starts from the beginning of the sequence. The PLAY LED is lit during playback.

Surface model entry
node_id: sequencer.play_button
name: PLAY button
role: button
physical_type: button
region: Sequencer section
group: Basic controls / transport
description: Starts or stops sequence playback.
actions:
  - press: start sequence playback if stopped
  - press: stop sequence playback if playing
possible_indicators:
  - PLAY LED lit: playback is running
current_state: unknown
state_note: Current playback state and LED state cannot be inferred from the manual or static panel references alone.
Surface map entry
node_id: sequencer.play_button
approximate_position: sequencer section, upper central transport area
landmarks:
  - sequencer controls cluster
  - nearby REC button
  - step button row below
neighbours:
  - REC button nearby in the same sequencer-control area
  - TEMPO knob nearby in the sequencer section
  - step buttons below in the lower sequencer area
navigation_hint: From the lower step-button row, move upward into the sequencer control cluster; the PLAY button is the transport button used to start and stop playback.
Non-visual description

The PLAY button is the monotribe’s main transport control for sequence playback. Treat it as a toggle-style action button: one press starts the sequence, and another press stops it. The manual says playback starts from the beginning of the sequence, and the PLAY LED indicates playback, but I cannot know whether it is currently lit from static sources alone.

[Trace]
Sources used: monotribe_manual.pdf, manual page 14; monotribe_manual_visual_index.json, sequencer section entry for page 13; static panel photo reference; 01_surface_aria_store.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 04_routing_and_uncertainty_policy.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 45%; Visual/static layout 25%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: Medium.
Confidence rationale: The PLAY function is manual-grounded; exact tactile placement is based on static layout references, not live observation.
Unsupported-current-state risk: Low.
[/Trace]
