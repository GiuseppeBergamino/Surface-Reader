Prompt ID: b2

Prompt: Create a structured description of the rec button.

# Surface Reader:
## R1:
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

## R2:
Structured description: REC button

Control name: REC button
Semantic role: button
Physical type: pressable button
Region: Sequencer section
Group: Synthesizer sequence controls / recording controls
Related indicator: REC LED

Documented function:
The REC button controls recording for the synthesizer sequence. During playback, pressing REC puts the monotribe into record mode; the REC LED lights, and ribbon keyboard performance data is recorded. When stopped, pressing REC puts the unit into record-ready mode; the REC LED blinks. Pressing PLAY from that state starts playback and activates record mode. Press REC again to exit record or record-ready mode, making the REC LED go dark.

Possible states described by the manual:

REC LED lit: record mode during playback.
REC LED blinking: record-ready mode while stopped.
REC LED dark: not in record mode or record-ready mode.

Additional documented use:
When the sequencer is stopped and the monotribe is not producing sound, holding REC until the REC LED stops blinking and goes dark saves the sequence. Do not turn off the power while data is being saved, because this may destroy internal data.

Non-visual location guidance:
From the performer’s perspective, the REC button is in the sequencer section, near the PLAY button and the FLUX and GATE TIME controls. Use the lower/right sequencer control area as the working region, then identify the small transport/recording cluster rather than relying on printed labels. The manual’s sequencer panel diagram identifies REC as item 7 in that section.

Current-state limitation:
I can describe what the REC LED states mean, but I cannot determine whether the REC LED is currently lit, blinking, or dark from the manual or static panel references alone.

[Trace]
Sources used: monotribe_manual.pdf, sequencer section pages 13–16; monotribe_manual_visual_index.json entry for page 13; Surface ARIA Store; Surface Model/Map Schema; Interaction Guidance Store; Mode Policy Store; Routing and Uncertainty Policy.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 15%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: The REC function and LED meanings are explicitly documented, and the sequencer diagram identifies its control grouping.
Unsupported-current-state risk: Low.
[/Trace]


## R3:
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


# Baseline:
## R1:
REC button — structured description

Direct answer:
The REC button controls recording for the monotribe’s synthesizer sequence. Pressing it changes between record, record-ready, and off states.

Where it is:
It is in the Sequencer section, among the Synthesizer sequence controls. In the manual’s sequencer diagram, it is item 7, positioned near the FLUX button and GATE TIME button.

What it does:

During playback: press REC to enter record mode. The REC LED lights up. Playing the ribbon keyboard records your performance data.
While stopped: press REC to enter record-ready mode. The REC LED blinks. Then press PLAY to start playback and activate record mode.
To exit: press REC again. The REC LED goes dark.

Related function:
When the sequencer is stopped and the monotribe is not producing sound, holding REC saves the sequence. Keep holding until the REC LED stops blinking and goes dark.

Limitation:
The manual describes possible REC LED meanings, but it cannot tell whether your unit is currently recording, record-ready, or saved.

[Trace]
Sources used: monotribe_manual.pdf, Sequencer section, “REC button” and “Saving a sequence”; sequencer panel diagram item 7.
Routing weights: Device manual 90%; Visual/static layout 10%.
Evidence confidence: High.
Confidence rationale: The REC button behavior is explicitly documented in the manual.
Unsupported-current-state risk: Medium.
[/Trace]

## R2:
REC button — structured description

Direct answer:
The REC button controls recording for the monotribe’s synth sequence. It can enter record mode, enter record-ready mode, exit either mode, and save a sequence in a separate stopped-state procedure.

Where it is:
In the Sequencer section, the REC button is item 7 in the manual’s sequencer layout. It is in the upper row of synth sequence controls, near the FLUX button and GATE TIME button.

What it does:

Situation	Action	Result
Sequence is playing	Press REC	Enters record mode; the REC LED lights up. Playing the ribbon keyboard records your performance data.
Sequence is stopped	Press REC	Enters record-ready mode; the REC LED blinks. Pressing PLAY then starts playback and activates record mode.
In record or record-ready mode	Press REC again	Exits that mode; the REC LED goes dark.
Sequencer stopped and monotribe not producing sound	Hold REC until the REC LED stops blinking and goes dark	Saves the sequence.

Important limitation:
The manual describes what the REC LED can mean, but from the manual and static panel photo alone I cannot determine whether your actual unit is currently recording, record-ready, saved, or stopped.

[Trace]
Sources used: monotribe_manual.pdf, sequencer section pages 13–16; static panel photo for general panel-layout grounding.
Routing weights: Device manual 90%; Visual/static layout 10%.
Evidence confidence: High.
Confidence rationale: The REC button behavior is explicitly documented in the sequencer section.
Unsupported-current-state risk: High.
[/Trace]

## R3:
REC button — structured description

Direct answer:
The REC button controls recording for the monotribe’s synthesizer sequence. Pressing it changes between normal, record-ready, and record modes.

Where it is:
In the sequencer section, the REC button is in the upper row of synth sequence controls. It sits near the FLUX button and GATE TIME button, above the step-button area.

What it does:

During playback: press REC to enter record mode. The REC LED lights up. Playing the ribbon keyboard records your performance data into the sequence.
While stopped: press REC to enter record-ready mode. The REC LED blinks. Press PLAY to start playback and activate recording.
To exit: press REC again. The REC LED goes dark.

Related function:
When the sequencer is stopped and the monotribe is not producing sound, holding down REC saves the sequence. Keep holding until the REC LED stops blinking and goes dark.

Limitation:
The manual describes what the REC LED means in these modes, but it cannot tell the current state of your unit from the manual or static photo alone.

[Trace]
Sources used: monotribe Owner’s manual, sequencer section pages 13–16; static panel layout reference.
Routing weights: Device manual 85%; Visual/static layout 15%.
Evidence confidence: High.
Confidence rationale: The REC button behavior and LED states are directly documented in the sequencer section.
Unsupported-current-state risk: Low.
[/Trace]
