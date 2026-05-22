Prompt: Create a structured description of the rec button.

Response: 

Structured description: REC button

Official name: REC button
Surface role: button
Physical type: pressable button
Region: Sequencer section
Group: Synthesizer sequence controls / transport-related recording controls
Related indicator: REC LED

Function

The REC button controls recording for the monotribe sequencer. According to the manual, pressing it during playback puts the monotribe into record mode, and the REC LED lights up. Playing the ribbon keyboard then records your performance data into the sequence.

Pressing REC while the sequencer is stopped puts the monotribe into record-ready mode; the REC LED blinks. Pressing PLAY after that starts playback and activates record mode. Press REC again to leave record mode or record-ready mode; the REC LED goes dark.

Possible states

These are documented possible states, not current observed states:

State	Meaning
REC LED lit	Record mode during playback
REC LED blinking	Record-ready mode while stopped
REC LED dark	Not in record mode or record-ready mode
Actions
Press REC during playback: enter record mode.
Press REC while stopped: enter record-ready mode.
Press PLAY while REC is blinking: begin playback and activate record mode.
Press REC again: exit recording or record-ready mode.
Hold REC while stopped and silent: save the sequence until the REC LED stops blinking and goes dark. The manual warns not to turn off the power while data is being saved.
Non-visual location guidance

From the performer’s perspective, the REC button is in the sequencer section, near the PLAY button and close to the FLUX and GATE TIME controls. Use the lower sequencer area as your landmark: find the cluster of pressable sequencer buttons rather than the rotary knobs. REC is part of the recording/playback control area, not the row of eight step buttons.

I cannot determine whether the REC LED is currently lit, blinking, or dark from the manual or static panel references alone.

node_id: monotribe.sequencer.rec_button
name: REC button
role: button
physical_type: pressable button
region: Sequencer section
group: Synthesizer sequence controls
related_indicator: REC LED
actions:
  - press
  - press_again
  - hold_while_stopped_and_silent_for_save
possible_states:
  - rec_led_lit: record mode
  - rec_led_blinking: record-ready mode
  - rec_led_dark: not recording / not record-ready
current_state: unknown_static_sources_only

[Trace]
Sources used: monotribe_manual.pdf, manual page 15 and page 16; monotribe_manual_visual_index.json entry for page 13; Surface ARIA Store; Surface Model/Map Schema; Interaction Guidance Store; Mode Policy Store; Routing and Uncertainty Policy.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 15%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: Function and possible LED meanings are explicitly documented; location is supported by the sequencer layout diagram.
Unsupported-current-state risk: Low.
[/Trace]