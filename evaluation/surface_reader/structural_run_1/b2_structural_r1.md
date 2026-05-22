Prompt: Create a structured description of the rec button.

Response: 

Structured description: REC button
node_id: monotribe.sequencer.synth_sequence.rec
name: REC button
role: button
physical_type: pressable button
region: Sequencer section
group: Synthesizer sequence controls
official_manual_number: 7
function:
  primary: Enters or exits recording for the synth sequence.
  during_playback: Pressing REC puts the monotribe into record mode.
  while_stopped: Pressing REC puts the monotribe into record-ready mode.
actions:
  - press
  - press again to exit record or record-ready mode
  - hold while stopped to save a sequence
indicators:
  related_indicator: REC LED
  possible_states:
    - lit: record mode during playback
    - blinking: record-ready mode while stopped
    - dark: not in record mode or record-ready mode
recording_behavior:
  when_recording: Playing the ribbon keyboard records performance data.
  record_ready_transition: In record-ready mode, pressing PLAY starts playback and activates record mode.
save_behavior:
  condition: Sequencer is stopped and monotribe is not producing sound.
  action: Hold REC until the REC LED stops blinking and goes dark.
  result: The sequence is saved and loaded at next power-up.
spatial_map:
  perspective: performer’s perspective
  approximate_position: sequencer section, upper-middle/right area of the top panel
  nearby_controls:
    - FLUX button nearby in the same synth sequence control group
    - GATE TIME button nearby in the same group
    - PLAY button nearby in the sequencer basic controls
  tactile_hint: Find the sequencer control cluster above the step-button row; REC is one of the small pressable buttons used for synth-sequence recording, grouped with FLUX and GATE TIME.
current_state:
  value: unknown
  note: Static manual and panel references cannot determine whether REC is currently lit, blinking, pressed, or active.
safety_notes:
  - Never turn off the power while data is being saved, because doing so may destroy internal data.

The manual states that pressing REC during playback enters record mode and lights the REC LED; pressing it while stopped enters record-ready mode and makes the REC LED blink. Pressing REC again exits either state and makes the REC LED go dark.

For saving, the manual says to hold REC while the sequencer is stopped and the monotribe is not producing sound, until the REC LED stops blinking and goes dark. It also warns not to turn off power while data is being saved.

[Trace]
Sources used: monotribe_manual.pdf pages 13–16; monotribe_manual_visual_index.json entry for page 13; foto_pannello static panel photo; Surface ARIA Store; Surface Model/Map Schema; Interaction Guidance Store; Routing and Uncertainty Policy; Mode Policy Store.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 15%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: REC function and LED meanings are directly documented; location is supported by static panel layout sources.
Unsupported-current-state risk: Low.
[/Trace]