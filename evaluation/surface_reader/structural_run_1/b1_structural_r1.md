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
  - press: starts sequence playback from the beginning
  - press_again: stops sequence playback
indicator:
  name: PLAY LED
  possible_state:
    - lit during playback
current_state: unknown from static sources
manual_grounding: The manual states that the PLAY button plays or stops the sequence, playback always starts from the beginning, and the PLAY LED is lit during playback. :contentReference[oaicite:0]{index=0}
surface_map:
  approximate_position: sequencer section, among the basic sequencer controls
  tactile_landmark: part of the sequencer control area, separate from the ribbon keyboard and synth knobs
  neighbouring_controls:
    - ACTIVE STEP button
    - TEMPO knob
    - REC button
non_visual_guidance: Find the sequencer section, then locate the small transport/control cluster rather than the long ribbon keyboard or the rotary synth knobs. The PLAY button is a pressable control used as the main start/stop control for the sequence.
state_limitation: Static sources can describe what the PLAY LED means, but cannot tell whether it is currently lit.

[Trace]
Sources used: monotribe_manual.pdf, sequencer section/basic controls; monotribe_manual_visual_index.json, sequencer section layout entry; Surface ARIA Store; Surface Model/Map Schema; Interaction Guidance Store; Mode Policy Store.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 15%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 5%.
Evidence confidence: High.
Confidence rationale: The PLAY button function and LED meaning are explicitly documented in the manual, with layout supported by the sequencer panel diagram index.
Unsupported-current-state risk: Low.
[/Trace]
