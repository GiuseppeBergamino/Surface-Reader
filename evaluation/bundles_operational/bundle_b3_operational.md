Prompt ID: b3

Prompt: Which controls should I use to work with sequencer steps? Describe where they are and what they do.

# Surface Reader:
## R1:
For sequencer steps on the monotribe, use the Sequencer section, mainly the PART buttons, ACTIVE STEP button, PLAY button, REC button, GATE TIME button, STEP buttons, STEP LEDs, FLUX button, TEMPO knob, and RHYTHM knob. The manual says the monotribe has an eight-step sequencer controlling both the synthesizer and drum sound generator.

From the performer’s perspective, the sequencer section is the lower/right working area of the top panel, near the long ribbon keyboard. The STEP buttons are the main landmark: a row of eight repeated buttons used to turn steps on and off. The STEP LEDs correspond to those steps; during playback, they blink to indicate the current step, but I cannot know their current state from static sources alone.

The important controls are:

STEP buttons
Use these to turn individual steps on or off. For the synth part, an on step plays its recorded synth note; an off step does not play. For drum parts, the same step buttons turn hits on or off for the selected drum part: BD, SN, or HH.

PART buttons: SYNTH, BD, SN, HH
Use these to choose which part you are editing. Press SYNTH for the synth sequence. Press BD, SN, or HH to edit bass drum, snare, or hi-hat steps. Their associated PART LEDs indicate the selected part, but the current selection cannot be inferred here.

ACTIVE STEP button
Hold this while pressing a step button to enable or disable that step in the sequence structure. Disabled steps are skipped during playback and recording. This is different from simply muting a note or drum hit: it changes which steps the sequencer moves through.

PLAY button
Starts or stops the sequence. Playback starts from the beginning of the sequence.

REC button
Use this to record synth performance data from the ribbon keyboard into the sequence. Pressing REC during playback enters record mode; pressing it while stopped enters record-ready mode.

GATE TIME button
Use this with the ribbon keyboard during sequence playback to change the duration of synth notes. Far left on the ribbon gives the shortest gate time; far right gives the longest. In REC mode, gate time can be recorded per step.

FLUX button
Use this for the synth part. With FLUX on, synth sequence data is recorded and played back continuously rather than locked to one note per step. With FLUX off, one note plays back for each step.

TEMPO knob
Sets sequencer speed, unless SYNC IN is connected. Treat it as the main speed knob for step playback.

RHYTHM knob
Controls the volume of the drum sound generator, so it affects how strongly the BD, SN, and HH step patterns are heard.

Tactile memory anchor: the repeated row of eight step buttons is your sequencer grid. First choose the part with SYNTH / BD / SN / HH, then use the eight step buttons to decide what happens on each step. Use PLAY to hear the loop, REC to record synth motion, and ACTIVE STEP when you want the sequence itself to skip steps.

[Trace]
Sources used: monotribe_manual.pdf; monotribe_manual_visual_index.json; 01_surface_aria_store.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 55%; Visual/static layout 15%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 5%.
Evidence confidence: High.
Confidence rationale: The manual explicitly defines the sequencer controls and the visual index identifies the sequencer layout pages.
Unsupported-current-state risk: Low.
[/Trace]

## R2:
Use the Sequencer section. It controls the eight-step synth and drum sequences. The manual says the monotribe has an eight-step sequencer for the synthesizer and drum sound generator .

From the performer’s perspective, the sequencer controls are mainly in the lower half of the panel, with the long ribbon keyboard as a strong lower landmark. The step buttons are the main row for working with steps.

Main step controls

STEP buttons
These are the row of eight small buttons used for individual sequencer steps. For the synth part, each step button turns that step on or off. For drum parts, they turn steps on or off for the selected drum part: BD, SN, or HH. When a step is on, it plays; when off, it does not play .

STEP LEDs
Each step button has a corresponding LED. During playback, the LEDs blink to indicate the current step; they also show whether steps are on or off. I can describe the possible LED meanings, but I cannot know their current state from the manual or static panel photo alone .

PART buttons: SYNTH, BD, SN, HH
Use these to choose which part you are editing. Press SYNTH to edit synth steps. Press BD, SN, or HH to edit the bass drum, snare, or hi-hat step pattern. The part LEDs indicate the selected part, but I cannot verify the current selection from static sources alone .

ACTIVE STEP button
This is for enabling or disabling steps in the sequence structure itself. Hold ACTIVE STEP and press a step button to turn that step on or off as an active step. Disabled active steps are skipped during playback and recording. This is different from muting a note or drum hit: it changes the step flow .

PLAY button
Starts or stops the sequence. Playback starts from the beginning of the sequence. Use this when you want to hear the steps running .

REC button
Use this to record synth performance data into the sequence. Press it during playback to enter record mode, then play the ribbon keyboard. Press it while stopped to enter record-ready mode, then press PLAY to start recording .

FLUX button
Affects how the synth sequence is recorded and played back. With FLUX on, the synth part records and plays back as continuous data. With FLUX off, one note plays per step .

GATE TIME button
Hold GATE TIME while using the ribbon keyboard during sequence playback to change synth note duration. Far left on the ribbon gives the shortest gate time; far right gives the longest. In REC mode, this can record gate time per step .

TEMPO knob
Sets the speed of the sequencer. It is a rotary knob, not a step button. If SYNC IN is connected, the manual says the TEMPO knob is disabled .

Tactile map

Think of the sequencer as three working areas:

Part selection area: the buttons for SYNTH, BD, SN, and HH. Use these first to choose what the step buttons will edit.
Step row: the eight repeated step buttons. This is your main tactile landmark for programming steps.
Transport and recording controls: PLAY, REC, FLUX, ACTIVE STEP, and GATE TIME. These change how the sequence runs, records, or interprets the steps.

For basic step editing: choose a PART, then use the eight STEP buttons. For changing which steps are skipped entirely, use ACTIVE STEP + STEP button. For synth recording, use REC, PLAY, the ribbon keyboard, and optionally FLUX or GATE TIME.

[Trace]
Sources used: monotribe_manual.pdf pages 13–16; monotribe_manual_visual_index.json entries for pages 13–15; monotribe_manual_p13.png, monotribe_manual_p14.png, monotribe_manual_p15.png; foto_pannello.jpeg; 01_surface_aria_store.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 04_routing_and_uncertainty_policy.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 50%; Visual/static layout 20%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 7%; Mode Policy Store 2%; Routing/Uncertainty Policy 1%.
Evidence confidence: High.
Confidence rationale: The control names and functions are directly documented, and the sequencer layout is supported by the manual diagram and static panel photo.
Unsupported-current-state risk: Low.
[/Trace]

## R3:
Use the Sequencer section: the cluster of buttons and one knob on the right side of the top panel, from the performer’s perspective. The manual says the monotribe has an eight-step sequencer for the synth and drum parts.

Main step controls

STEP buttons
These are the key controls for steps. They form the repeated step-button row in the sequencer area. Press a step button to turn that step on or off for the currently selected part. For drum parts, they turn steps on or off for BD, SN, or HH. For the synth part, they control whether the step plays. The matching STEP LEDs indicate possible step status and blink during playback to show the current step, but I cannot know their current state from static sources alone.

PART buttons: SYNTH, BD, SN, HH
Use these before editing steps. They select which part the step buttons will edit: synth, bass drum, snare drum, or hi-hat. Tactilely, treat them as the “which lane am I editing?” buttons near the sequencer controls. Their PART LEDs can indicate the selected part, but current selection cannot be inferred from the manual or static panel image.

ACTIVE STEP button
Use this to enable or disable steps in the sequence structure itself. Hold ACTIVE STEP, then press the desired STEP button. Disabled steps are skipped during playback and recording. This is different from simply turning a note or drum hit off; it changes whether the sequencer visits that step at all.

PLAY button
Starts or stops the sequence. Playback always starts from the beginning of the sequence. Use this when checking how your step changes sound in time.

REC button
Use this for recording the synth part. During playback, pressing REC enters record mode; playing the ribbon keyboard records your performance. While stopped, pressing REC puts the unit in record-ready mode.

GATE TIME button
For synth steps, hold GATE TIME while using the ribbon keyboard during playback to change note duration. Left side of the ribbon gives very short gate time; right side gives longer gate time. In record mode, gate time changes can be recorded per step.

FLUX button
Changes how the synth sequence is recorded and played back. With FLUX on, synth performance is recorded and played back as continuous data. With FLUX off, one note plays per step.

TEMPO knob
Sets the sequencer speed. It is a rotary knob in the sequencer area. The manual notes that it is disabled if SYNC IN is connected.

RHYTHM knob
Controls the volume of the drum sound generator. It does not choose steps, but it matters when working with BD/SN/HH step patterns.

A useful mental map: PART buttons choose the lane, STEP buttons choose the events, ACTIVE STEP changes the length/skip behavior, PLAY/REC control motion, and FLUX/GATE TIME shape the synth sequence.

[Trace]
Sources used: monotribe_manual.pdf English sequencer section, manual page uncertain; monotribe_manual_visual_index.json entries for pages 13–15; 01_surface_aria_store.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 04_routing_and_uncertainty_policy.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 55%; Visual/static layout 15%; Surface ARIA Store 10%; Surface Model/Map Schema 8%; Interaction Guidance Store 7%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: Control names and functions are directly documented; layout is supported by the sequencer panel diagram/index, though exact tactile spacing is approximate.
Unsupported-current-state risk: Low.
[/Trace]

# Baseline:
## R1:
Use the Sequencer section controls for working with steps. They are in the lower/right area of the top panel, grouped around the row of eight step buttons.

Main step controls

STEP buttons / STEP LEDs
These are the eight repeated buttons along the lower part of the sequencer area. Use them to turn steps on or off. A step that is on will play and its step LED lights; a step that is off will not play and its LED is dark. During playback, the step LEDs blink to show the current step.

ACTIVE STEP button
This is in the sequencer section near the transport controls. Hold ACTIVE STEP and press a step button to enable or disable that step in the sequence. Disabled steps are skipped during playback and recording. The manual says all steps are on at power-up, and you cannot turn all steps off at the same time.

PART buttons: SYNTH, BD, SN, HH
These select which part you are editing. Use SYNTH for the synth sequence, or BD, SN, and HH for the drum parts. The selected part’s LED lights.

PLAY button
Use this to start or stop the sequence. Playback always starts from the beginning.

REC button
Use this to record synth performance data into the sequence. Press it during playback to enter record mode; press it while stopped to enter record-ready mode, then press PLAY to start recording.

GATE TIME button
For synth steps, hold GATE TIME while the sequence plays and touch the ribbon keyboard to change note duration. Left side of the ribbon gives the shortest gate time; right side gives the longest. In REC mode, this can be recorded per step.

FLUX button
This affects synth sequencing. With FLUX on, the synth part is recorded and played back as continuous data. With FLUX off, one note plays back per step.

TEMPO knob
Use this to set the sequencer speed, unless SYNC IN is connected; then the manual says the TEMPO knob is disabled.

RHYTHM knob
This controls the volume of the drum sound generator, so it affects how loud the BD, SN, and HH step patterns are.

[Trace]
Sources used: monotribe_manual.pdf, English manual pages 13–16; static panel photo.
Routing weights: Device manual 85%; Visual/static layout 15%.
Evidence confidence: High.
Confidence rationale: The sequencer controls and step functions are explicitly documented in the manual, and the static panel supports their grouped physical layout.
Unsupported-current-state risk: Low.
[/Trace]

## R2:
Use the sequencer section controls: the monotribe has an eight-step sequencer for the synth and drum sound generator.

Where they are: On the front panel, the sequencer section is the lower control area. The manual’s sequencer diagram places the STEP LEDs and STEP buttons along the lower part of that section, with the part buttons and transport/record controls above or around them.

Main step controls:

ACTIVE STEP button — Use this to enable or disable steps in the overall sequence. Hold ACTIVE STEP, then press the desired STEP button. Disabled steps are skipped during playback and recording. All steps are on at power-up, and the manual says you cannot turn all steps off at the same time.

STEP buttons — These are the main buttons for turning individual steps on or off. For the synth sequence, an on step plays and its step LED lights; an off step does not play. If you record onto an off step, it turns on automatically and previous data in that step is erased.

STEP LEDs — These tell you which steps are on or off, and during playback they blink to indicate the current step.

PART buttons: SYNTH, BD, SN, HH — Use these to choose which part you are editing: synth, bass drum, snare drum, or hi-hat. The selected part’s LED lights. For drum parts, the STEP buttons turn steps on or off for the selected drum part.

PLAY button — Starts or stops the sequence. Playback always starts from the beginning.

REC button — Records synth performance data from the ribbon keyboard. Press it during playback for record mode; press it while stopped for record-ready mode, then press PLAY to start recording.

GATE TIME button — For synth steps, hold GATE TIME and use the ribbon keyboard during sequence playback to change note duration. In REC mode, the gate time for each step can be recorded. Far left on the ribbon gives minimum gate time, and far right gives maximum gate time.

FLUX button — Changes how the synth sequence relates to steps. With FLUX on, the synth part is recorded and played back as continuous data. With FLUX off, one note plays back for each step.

TEMPO knob — Sets sequencer speed, unless SYNC IN is connected.

[Trace]
Sources used: monotribe_manual.pdf, Owner’s manual pages 13–15; static panel photo for general lower-panel sequencer placement.
Routing weights: Device manual 90%; Visual/static layout 10%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names the sequencer step controls and their functions.
Unsupported-current-state risk: None.
[/Trace]

## R3:
Use the Sequencer section controls to work with steps. They are in the lower/right area of the top panel, grouped around the row of eight step buttons.

Main step controls

ACTIVE STEP button
Located in the sequencer section, above/near the step-button area. Hold it, then press a step button to enable or disable that step. Disabled steps are skipped during playback and recording. You cannot turn all steps off at once.

STEP buttons 1–8
These are the row of eight repeated buttons along the lower part of the sequencer section. They turn steps on or off. For the selected synth or drum part, an “on” step plays; an “off” step does not play. For drum parts, holding a part button while turning on a step makes the drum sound halfway through that step, effectively giving 16 rhythm positions.

STEP LEDs
These are paired with the step buttons. They light when a step is on, go dark when off, and blink during playback to show the current step.

PART buttons: SYNTH, BD, SN, HH
These select which part you are editing before using the step buttons. SYNTH is for the synth sequence; BD, SN, and HH are the drum parts.

PLAY button
Starts or stops the sequence. Playback always starts from the beginning.

REC button
Used to record synth performance data into the sequence. During playback, press REC and play the ribbon keyboard to record. While stopped, press REC for record-ready mode, then press PLAY to begin recording.

GATE TIME button
For synth steps, hold GATE TIME while touching the ribbon keyboard during playback to change note duration. In REC mode, gate time can be recorded per step.

FLUX button
For the synth part, this changes how the sequence is handled. FLUX on records and plays the synth part as continuous data; FLUX off plays one note per step.

TEMPO knob
Sets sequencer speed, unless SYNC IN is connected, in which case the manual says the TEMPO knob is disabled.

These functions are documented in the monotribe manual’s “Sequencer section,” including the sequencer layout and controls.

[Trace]
Sources used: monotribe_manual.pdf, Sequencer section pages 13–16; static panel photo.
Routing weights: Device manual 85%; Visual/static layout 15%.
Evidence confidence: High.
Confidence rationale: The manual directly defines the sequencer controls and the panel/photo supports their physical grouping.
Unsupported-current-state risk: None.
[/Trace]
