Prompt ID: b3

Prompt: Create a structured description of the sequencer section.

# Surface Reader:
## R1:
Sequencer section — structured description

The monotribe sequencer section is an eight-step sequencer that controls both the SYNTH part and the three drum parts: BD, SN, and HH. The manual states that the sequencer controls the synthesizer and drum sound generator, and that the instrument has 8 steps.

1. Region

Name: Sequencer section
Role: region
Purpose: Create and play back step-based patterns for the synth and drum parts.
Physical area: From the performer’s perspective, this section is concentrated in the lower half and right side of the top panel, with the row of step buttons acting as the main tactile landmark.

2. Main groups inside the sequencer
A. Part selection group

Controls:

SYNTH button
BD button
SN button
HH button
PART LEDs

Role: group containing button controls and indicator LEDs.
Function: Select which part is being edited. The manual says each PART button selects the corresponding part, and its PART LED lights when selected. The part LEDs also blink together as a low-battery warning.

Non-visual note: The LEDs indicate possible states, but their current state cannot be known from the manual or static panel image alone.

B. Transport and recording group

Controls:

PLAY button
REC button

Roles: button controls with associated indicator LEDs.
Function:

PLAY starts or stops the sequence. Playback always starts from the beginning, and the PLAY LED is lit during playback.
REC enters record mode during playback, or record-ready mode while stopped. The REC LED lights in record mode and blinks in record-ready mode.

Non-visual note: These controls are mode-sensitive. The same REC button behaves differently depending on whether the sequencer is stopped or playing.

C. Step-sequencer group

Controls:

STEP buttons
STEP LEDs
ACTIVE STEP button

Roles:

STEP buttons: button
STEP LEDs: indicator
ACTIVE STEP button: button

Function:
The step buttons turn individual steps on or off. During playback, the step LEDs blink to indicate the current step. Holding ACTIVE STEP lets you enable or disable steps; disabled steps are skipped during playback and recording. The manual also notes that all steps are on at power-up and that all steps cannot be turned off at the same time.

Tactile landmark: The row of eight step buttons is the strongest landmark in this section. Think of it as the sequencer’s “timeline,” running left to right from step 1 to step 8.

D. Synth sequence group

Controls:

FLUX button
GATE TIME button
REC button
Ribbon keyboard, used with recording and gate-time entry

Roles: button controls plus the ribbon keyboard as keyboard.

Function:

FLUX switches synth sequencing between continuous recording/playback and one-note-per-step playback.
GATE TIME changes the duration of synth notes while the sequence plays; touching farther left on the ribbon gives shorter gate time, and farther right gives longer gate time.
In REC mode, gate time changes can be recorded per step.

Mental model: FLUX affects how pitch movement is captured. GATE TIME affects how long synth notes last.

E. Drum sequence group

Controls:

BD, SN, HH PART buttons
STEP buttons
RHYTHM knob

Roles:

Drum part buttons: button
Step buttons: button
RHYTHM knob: slider, physical type rotary knob

Function:
The step buttons turn steps on or off for the selected drum part. The RHYTHM knob adjusts the volume of the drum sound generator. The manual also describes a half-step drum entry behavior: if you turn on a step button while holding a part button, that drum sounds halfway through the step, effectively allowing 16 rhythmic positions across the 8 step buttons.

3. Surface model summary
Sequencer section [region]
├─ Part selection group [group]
│  ├─ SYNTH button [button]
│  ├─ BD button [button]
│  ├─ SN button [button]
│  ├─ HH button [button]
│  └─ PART LEDs [indicators]
├─ Transport / recording group [group]
│  ├─ PLAY button [button]
│  └─ REC button [button]
├─ Step-sequencer group [group]
│  ├─ ACTIVE STEP button [button]
│  ├─ STEP buttons 1–8 [buttons]
│  └─ STEP LEDs 1–8 [indicators]
├─ Synth sequence group [group]
│  ├─ FLUX button [button]
│  ├─ GATE TIME button [button]
│  └─ Ribbon keyboard interaction [keyboard input]
└─ Drum sequence group [group]
   ├─ BD / SN / HH part selection [buttons]
   ├─ STEP buttons 1–8 [buttons]
   └─ RHYTHM knob [slider / rotary knob]
4. Tactile-first orientation

From the performer’s perspective, use the row of eight step buttons as the main sequencer landmark. They form the horizontal time line of the pattern. Nearby buttons modify what those steps mean: part buttons choose the lane, PLAY starts and stops the pattern, REC captures synth performance, ACTIVE STEP changes which steps are skipped, and GATE TIME changes synth note length.

The RHYTHM knob belongs to the drum side of the sequencer because it controls the drum sound generator’s volume, not the synth volume.

5. Static vs current-state note

This description is based on the manual and static layout references. It can describe official functions, possible LED meanings, and physical grouping, but it cannot determine which part is currently selected, whether PLAY or REC is active, which LEDs are lit, or which steps are currently on.

[Trace]
Sources used: monotribe_manual.pdf, especially sequencer section pages 13–16; monotribe_manual_visual_index.json entries for pages 13, 14, and 15; foto_pannello static top-panel reference; 01_surface_aria_store.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 04_routing_and_uncertainty_policy.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 15%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: The sequencer controls and behaviors are explicitly documented in the manual, with static layout support from the panel diagram and panel photo.
Unsupported-current-state risk: Low.
[/Trace]

## R2:
Sequencer section — structured surface description

The monotribe sequencer section is an eight-step sequencer region that controls both the SYNTH part and the three drum parts: BD, SN, and HH. The manual states that the sequencer “controls the synthesizer and drum sound generator” and that the monotribe has an “eight-step sequencer.”

1. Region

Name: Sequencer section
Role: region
Purpose: Create and play looped patterns for the synth and drum sound generator.
Approximate location: On the right/lower-right area of the top panel, grouped around the step buttons, part buttons, transport controls, and rhythm/tempo controls.
Main tactile landmark: The row of eight step buttons is the strongest landmark for this section.

2. Main groups inside the sequencer section
A. Part selection group

Controls:

SYNTH button
BD button
SN button
HH button
PART LEDs

Roles:

PART buttons: button
PART LEDs: indicator

Function: The PART buttons choose which part is being edited. The corresponding PART LED lights when a part is selected. The manual also says the PART LEDs blink together when the batteries are running low.

Non-visual note: Static sources can tell us what the LEDs mean, but they cannot tell which PART LED is currently lit.

B. Transport and recording group

Controls:

PLAY button
REC button

Roles:

PLAY: button
REC: button
PLAY LED / REC LED: indicator

Function:

PLAY starts or stops the sequence. Playback always starts from the beginning of the sequence, and the PLAY LED is lit during playback.
REC enters record mode during playback. When stopped, pressing REC enters record-ready mode; pressing PLAY then starts recording.
C. Step control group

Controls:

STEP buttons
STEP LEDs
ACTIVE STEP button

Roles:

STEP buttons: button
STEP LEDs: indicator
ACTIVE STEP: button

Function:

STEP buttons turn steps on or off.
STEP LEDs light or go dark with the corresponding step button.
During playback, STEP LEDs blink to indicate the current step.
ACTIVE STEP lets you enable or disable steps in the sequence; disabled steps are skipped during playback and recording.

Tactile structure: Treat the eight STEP buttons as a horizontal counted row: step 1 at the left of the row, step 8 at the right.

D. Synth sequence group

Controls:

FLUX button
GATE TIME button
REC button
Ribbon keyboard, used during synth recording and gate-time editing

Roles:

FLUX: button
GATE TIME: button
REC: button
Ribbon keyboard: keyboard

Function:

FLUX changes how synth sequence data is recorded and played back. With FLUX on, synth sequence data is continuous; with FLUX off, one note plays back per step.
GATE TIME changes the duration of synth notes while the sequence plays. Holding GATE TIME and touching the ribbon keyboard sets gate time from minimum at the far left to maximum at the far right.
In REC mode, gate time changes can be recorded into the sequence.
E. Drum sequence group

Controls:

BD / SN / HH part buttons
STEP buttons
RHYTHM knob

Roles:

Drum part buttons: button
STEP buttons: button
RHYTHM knob: slider, physical type rotary knob

Function:

Select BD, SN, or HH, then use the STEP buttons to turn steps for that drum part on or off.
Holding a drum part button while turning on a step places the drum sound halfway through the step, effectively allowing 16 rhythmic positions across the 8 step buttons.
RHYTHM adjusts the volume of the drum sound generator.
F. Tempo group

Control:

TEMPO knob

Role: slider, physical type rotary knob

Function: Sets the sequencer speed. The manual says the range can be changed in the Global menu: NARROW gives 60–180 BPM, WIDE gives 10–600 BPM. TEMPO is disabled when SYNC IN is connected.

3. Compact surface-model representation
Sequencer section [region]
├─ Part selection group [group]
│  ├─ SYNTH button [button]
│  ├─ BD button [button]
│  ├─ SN button [button]
│  ├─ HH button [button]
│  └─ PART LEDs [indicators]
├─ Transport / record group [group]
│  ├─ PLAY button [button]
│  └─ REC button [button]
├─ Step control group [group]
│  ├─ ACTIVE STEP button [button]
│  ├─ STEP buttons 1–8 [buttons]
│  └─ STEP LEDs 1–8 [indicators]
├─ Synth sequence group [group]
│  ├─ FLUX button [button]
│  ├─ GATE TIME button [button]
│  └─ Ribbon keyboard interaction [keyboard]
├─ Drum sequence group [group]
│  ├─ BD / SN / HH part buttons [buttons]
│  ├─ STEP buttons 1–8 [buttons]
│  └─ RHYTHM knob [slider / rotary knob]
└─ Tempo group [group]
   └─ TEMPO knob [slider / rotary knob]
4. Non-visual memory anchor

Think of the sequencer as three layers around the eight step buttons:

Choose the part — SYNTH, BD, SN, or HH.
Choose the steps — the eight step buttons form the main row.
Control playback and recording — PLAY, REC, FLUX, ACTIVE STEP, GATE TIME, TEMPO, and RHYTHM shape how the pattern runs.

Static sources describe the layout and possible LED meanings, but they do not reveal the current sequence, current selected part, current LED state, or current knob positions.

[Trace]
Sources used: monotribe_manual.pdf, monotribe_manual_visual_index.json, monotribe_manual_p13.png, monotribe_manual_p14.png, monotribe_manual_p15.png, foto_pannello.jpeg, 01_surface_aria_store.md, 02_interaction_guidance_store.md, 03_mode_policy_store.md, 04_routing_and_uncertainty_policy.md, 05_surface_model_map_schema.md.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 15%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: The control names and functions are directly documented, and the layout is supported by the sequencer diagram and static panel references.
Unsupported-current-state risk: Low.
[/Trace]

## R3:
Sequencer section — structured surface description

The Sequencer section is the lower performance/control area for creating and playing the monotribe’s eight-step sequence. It controls both the SYNTH part and the three drum parts: BD, SN, and HH. The manual defines it as an eight-step sequencer that controls the synthesizer and drum sound generator.

1. Region: Sequencer section

Role: region
Purpose: Create, play, record, enable, disable, and edit sequencer steps.
Main contents: Part selection, transport, active-step editing, tempo, synth-sequence controls, step buttons, step LEDs, and rhythm volume.

From the performer’s perspective, treat this as a step-and-transport region. The most useful tactile landmark is the row of eight STEP buttons/LEDs, because many sequencer operations are organized around those eight positions.

2. Basic controls group
PART LEDs

Role: indicator
Physical type: LEDs
Function: Light when a PART button is selected. They can also blink together for low battery warning.
Current-state note: Static sources cannot tell which PART LED is currently lit.

PART buttons

Role: button
Physical type: pressable buttons
Official controls:

SYNTH button
BD button
SN button
HH button

Function: Select the part to edit. The selected part’s LED lights. BD is bass drum, SN is snare drum, and HH is hi-hat.

Tactile concept: Think of these as the part-choice buttons. They decide whether the step buttons edit the synth sequence or one of the drum sequences.

3. Transport and timing group
PLAY button

Role: button
Function: Starts or stops the sequence. Playback always starts from the beginning of the sequence. The PLAY LED is lit during playback.
Current-state note: I cannot determine whether playback is currently running from static sources.

TEMPO knob

Role: slider
Physical type: rotary knob
Function: Sets the sequencer speed. The manual says the range can be changed in the Global menu: NARROW gives 60–180 BPM, and WIDE gives 10–600 BPM. The tempo knob is disabled if the SYNC IN jack is connected.

Tactile concept: This is the sequencer’s speed control.

4. Step control group
STEP LEDs

Role: indicator
Physical type: LEDs associated with steps
Function: Light or go dark according to the corresponding step button. During playback, they blink to indicate the current step.
Current-state note: Static sources cannot confirm which step is currently active or lit.

STEP buttons

Role: button
Physical type: repeated step buttons
Count: 8
Function for synth and drums: Turn each step on or off.

Possible documented states:

ON: the step will be played, and its step LED will light.
OFF: the step will not be played, and its step LED will not light.

Tactile concept: This is the core eight-step row. Use it as a landmark: step 1 at the left end, step 8 at the right end.

5. Active Step group
ACTIVE STEP button

Role: button
Function: Enables or disables steps in the sequence. While holding ACTIVE STEP, enabled step LEDs light. Hold ACTIVE STEP and press a step button to turn that step on or off. Disabled steps are skipped during playback and recording.

Important documented limits:

When power is turned on, all steps are on.
It is not possible to turn all steps off at the same time.

Tactile concept: This button changes the length/shape of the loop by deciding which steps are included.

6. Synthesizer sequence controls group
FLUX button

Role: button
Function: Turns FLUX mode on or off.

Possible documented states:

ON: the synth part sequence is recorded and played back as continuous data.
OFF: one note plays back for each step.

Musical meaning: FLUX ON is freer and less grid-bound; FLUX OFF is step-based.

REC button

Role: button
Function: Controls recording.

Documented behavior:

Press during playback: enters record mode; REC LED lights.
Press while stopped: enters record-ready mode; REC LED blinks.
Press PLAY from record-ready mode: starts recording.
Press REC again: exits record or record-ready mode.

Current-state note: I cannot tell whether REC is lit or blinking without current evidence.

GATE TIME button

Role: button
Function: Used with the ribbon keyboard during sequence playback to change synth note duration. Far left on the ribbon gives minimum gate time, 1.4%; far right gives maximum gate time, 100%. In REC mode, gate time per step can be recorded.

Tactile concept: Hold this button, then use the ribbon as a duration control: left is shorter, right is longer.

7. Drum sound generator sequence controls
RHYTHM knob

Role: slider
Physical type: rotary knob
Function: Adjusts the volume of the drum sound generator.

Drum STEP buttons

Role: button
Function: With BD, SN, or HH selected, the eight step buttons turn that drum part on or off per step.

Additional rhythm behavior: If you turn on a step while holding a part button, the drum part sounds halfway through the step, effectively providing 16 steps for the rhythm sequence.

Tactile concept: Select BD, SN, or HH first, then use the same eight-step row to place drum hits.

8. Compact surface-model outline
Sequencer section [region]
├─ Part selection group [group]
│  ├─ PART LEDs [indicator group]
│  ├─ SYNTH button [button]
│  ├─ BD button [button]
│  ├─ SN button [button]
│  └─ HH button [button]
├─ Transport/timing group [group]
│  ├─ PLAY button [button]
│  └─ TEMPO knob [slider / rotary knob]
├─ Active-step group [group]
│  └─ ACTIVE STEP button [button]
├─ Synth sequence group [group]
│  ├─ FLUX button [button]
│  ├─ REC button [button]
│  └─ GATE TIME button [button]
├─ Step row [group]
│  ├─ STEP LEDs 1–8 [indicator group]
│  └─ STEP buttons 1–8 [button group]
└─ Drum sequence group [group]
   └─ RHYTHM knob [slider / rotary knob]
9. Static/current-state boundary

This description is based on the manual and static layout references. It can describe what controls exist, what they do, where they belong conceptually, and what states are possible. It cannot determine current playback, selected part, LED state, active step, knob position, saved sequence, or whether SYNC IN is connected.

[Trace]
Sources used: monotribe_manual.pdf, especially English Sequencer section pages 13–16; monotribe_manual_visual_index.json entry for “Panel overview (Sequencer section)” and related sequencer behavior diagrams; Surface ARIA Store; Surface Model/Map Schema; Interaction Guidance Store; Mode Policy Store; Routing and Uncertainty Policy.
Routing weights: Device manual 50%; Visual/static layout 15%; Surface ARIA Store 15%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: Official control names and functions come from the manual, while semantic roles follow the uploaded surface-model stores.
Unsupported-current-state risk: Low.
[/Trace]

# Baseline:
## R1:
The sequencer section is the lower-right performance/control area of the monotribe. It contains the controls for the built-in eight-step sequencer, which controls both the synthesizer part and the drum sound generator.

Physical layout

The sequencer section is arranged around these groups:

1. Part selection area

On the left side of the sequencer section are the PART buttons and PART LEDs.

They select which part you are editing:

SYNTH — synthesizer part
BD — bass drum
SN — snare drum
HH — hi-hat

The corresponding PART LED lights when a part is selected. The manual also says the part LEDs blink together when the batteries are running low.

2. Playback and timing controls

Near the upper/middle area are the main sequencer controls:

PLAY button — starts or stops the sequence. Playback always starts from the beginning.
TEMPO knob — sets sequencer speed.
ACTIVE STEP button — enables or disables individual steps.

The TEMPO knob range can be set in the Global menu:

NARROW: 60–180 BPM
WIDE: 10–600 BPM

The TEMPO knob is disabled when SYNC IN is connected.

3. Synth sequence controls

The synth sequence controls are:

FLUX button
REC button
GATE TIME button

FLUX changes how synth notes are recorded and played back:

FLUX ON: synth performance is recorded and played back as continuous data.
FLUX OFF: one note plays back per step.

REC records ribbon-keyboard performance into the synth sequence.

GATE TIME changes the duration of synth notes while the sequence plays. Hold GATE TIME and touch the ribbon keyboard:

far left = minimum gate time, 1.4%
far right = maximum gate time, 100%

In REC mode, gate time changes can be recorded per step.

4. Step area

Along the lower part of the sequencer section are the STEP LEDs and STEP buttons.

The STEP LEDs show step status and blink to indicate the current step during playback.

The STEP buttons turn steps on or off:

ON: the step plays and its LED lights.
OFF: the step does not play and its LED is unlit.

For the synth part, recording onto an off step automatically turns that step on and erases any previous data in that step.

5. Drum sequence controls

For drums, the selected part is one of:

BD
SN
HH

The same step buttons turn steps on or off for the selected drum part.

The RHYTHM knob adjusts the volume of the drum sound generator.

There is also a documented half-step rhythm function: if you turn on a step while holding a part button, that drum part sounds halfway through the step. The manual says this effectively provides 16 steps for the rhythm sequence, using the 8 step buttons.

Saving a sequence

When the sequencer is stopped and the monotribe is not producing sound, hold REC until the REC LED stops blinking and goes dark. The saved sequence will be loaded at the next power-up, depending on the Global menu startup setting.

Do not turn off the power while data is being saved.

Limitation

The manual and static panel layout describe the controls and their functions, but they cannot tell which part is currently selected, which steps are currently on, whether FLUX or REC is active, or the current tempo setting.

[Trace]
Sources used: monotribe_manual.pdf, “Main features” p.5; “Sequencer section” pp.13–16; static panel photo.
Routing weights: Device manual 85%; Visual/static layout 15%.
Evidence confidence: High.
Confidence rationale: The sequencer controls and functions are explicitly documented in the manual.
Unsupported-current-state risk: Low.
[/Trace]

## R2:
The sequencer section is the lower performance-control area for the monotribe’s eight-step sequencer. It controls both the synthesizer part and the three drum parts: BD, SN, and HH. The manual says the monotribe contains “an eight-step sequencer that controls the synthesizer and drum sound generator.”

Overall layout

The sequencer section is arranged along the lower half of the panel.

From left to right, it contains:

Part selection controls
Active Step and transport controls
Synth sequence controls
Step LEDs and step buttons
Rhythm volume control
1. Part selection

The PART buttons select which part you are editing.

Available parts:

SYNTH: synthesizer part
BD: bass drum part
SN: snare drum part
HH: hi-hat part

The PART LEDs show which part is selected. The same part LEDs also blink together when the batteries are running low.

2. Active Step control

The ACTIVE STEP button enables or disables steps in the sequence.

To use it:

Hold ACTIVE STEP, then press a step button.

Enabled steps play normally. Disabled steps are skipped during playback and recording. When the monotribe is powered on, all steps are enabled. The manual says it is not possible to turn all steps off at the same time.

3. Transport and tempo

The PLAY button starts or stops the sequence. Playback always starts from the beginning of the sequence.

The TEMPO knob sets sequencer speed. Its range depends on the Global menu setting:

NARROW: 60–180 BPM
WIDE: 10–600 BPM

The TEMPO knob is disabled when SYNC IN is connected.

4. Synthesizer sequence controls

The synth sequence has three main controls:

FLUX button: Turns FLUX mode on or off.
When FLUX is on, the synth sequence is recorded and played back as continuous data. When FLUX is off, one note plays back for each step.

REC button: Enters record mode or record-ready mode.
During playback, pressing REC starts recording. While stopped, pressing REC enters record-ready mode; pressing PLAY then begins recording.

GATE TIME button: Changes the duration of synth notes.
Hold GATE TIME while the sequence plays, then touch the ribbon keyboard. Far left gives the shortest gate time, 1.4%; far right gives the longest, 100%. In REC mode, gate time can be recorded per step.

5. Step LEDs and step buttons

There are eight step positions.

The STEP LEDs show which steps are on or off, and blink during playback to indicate the current step.

For the synth part, the STEP buttons turn each step on or off. If you record onto a step that is off, it turns on automatically and previously recorded data for that step is erased.

For drum parts, the same step buttons turn steps on or off for the selected drum part: BD, SN, or HH.

6. Drum sequence controls

The RHYTHM knob controls the volume of the drum sound generator.

For drum sequencing, select BD, SN, or HH, then use the step buttons to turn hits on or off.

The manual also documents a half-step drum function: if you turn on a step button while holding down a part button, that drum part sounds halfway through the step. This gives the rhythm sequence an effective 16-step feel using the eight step buttons.

7. Saving a sequence

To save a sequence:

Stop sequencer playback and make sure the monotribe is not producing sound. Then hold REC until the REC LED stops blinking and goes dark.

The saved sequence can be loaded at the next power-up, depending on the Global menu sequence start-up setting.

[Trace]
Sources used: monotribe_manual.pdf, English owner’s manual pages 13–16; static panel photo for broad lower-panel layout.
Routing weights: Device manual 90%; Visual/static layout 10%.
Evidence confidence: High.
Confidence rationale: The sequencer section is explicitly documented in the manual with numbered controls and functions.
Unsupported-current-state risk: None.
[/Trace]

## R3:
The sequencer section is the monotribe’s eight-step control area for playing, recording, editing, and saving synth and drum sequences. It controls both the synthesizer part and the three drum parts: BD, SN, and HH.

Where it is

On the top panel, the sequencer section is the lower control area beneath the synthesizer controls. It includes the transport and edit buttons, the row of step buttons and step LEDs, the part buttons, the TEMPO knob, and the RHYTHM knob.

Structured description
1. Basic part selection

The sequencer has four editable parts:

SYNTH: synthesizer part.
BD: bass drum part.
SN: snare drum part.
HH: hi-hat part.

Press a PART button to choose which part you are editing. The corresponding PART LED lights when selected. The same PART LEDs also blink together as a low-battery warning.

2. Playback and tempo

The PLAY button starts or stops the sequence. Playback always starts from the beginning of the sequence, and the PLAY LED lights during playback.

The TEMPO knob sets sequencer speed. Its range is set in the Global menu:

NARROW: 60–180 BPM for finer adjustment.
WIDE: 10–600 BPM.

If SYNC IN is connected, the TEMPO knob is disabled, because the sequencer follows incoming sync pulses instead.

3. Active Step control

The ACTIVE STEP button enables or disables steps in the sequence.

To change active steps, hold ACTIVE STEP and press a step button. Disabled steps are skipped during playback and recording. At power-on, all steps are enabled. The manual states that all steps cannot be turned off at the same time.

4. Synthesizer sequence controls

The FLUX button switches FLUX mode on or off.

FLUX ON: the synth part is recorded and played back as continuous data.
FLUX OFF: one note plays for each step.

The REC button controls recording. Pressing REC during playback enters record mode, and playing the ribbon keyboard records your performance. Pressing REC while stopped enters record-ready mode; then pressing PLAY starts recording.

The GATE TIME button changes the duration of synth notes. Hold GATE TIME and touch the ribbon keyboard while the sequence plays. Far left gives the minimum gate time, 1.4%; far right gives the maximum, 100%. In REC mode, gate time changes can be recorded per step.

5. Step LEDs and step buttons

The STEP LEDs show step status. They light or go dark when the matching step button is pressed. During playback, they blink to indicate the current step.

The STEP buttons turn steps on or off.

For the synth part:

ON: the step plays and its LED lights.
OFF: the step does not play and its LED is dark.
Recording onto an off step automatically turns it on and erases any previous data in that step.

For drum parts:

Select BD, SN, or HH.
Press step buttons to turn that drum part on or off at each step.
Holding a part button while turning on a step places that drum sound halfway through the step, giving an effective 16-step rhythm resolution from the 8 step buttons.
6. Drum level

The RHYTHM knob adjusts the volume of the drum sound generator.

7. Saving a sequence

When the sequencer is stopped and the monotribe is not producing sound, hold REC until the REC LED stops blinking and goes dark. The saved sequence can be loaded at the next power-up depending on the Global menu start-up sequence setting.

Do not turn off the power while saving, because the manual warns this may damage internal data.

Limitation

The manual and static panel layout describe what the sequencer controls do, but they cannot reveal the current selected part, current LED states, current tempo, current sequence contents, or whether any steps are presently active.

[Trace]
Sources used: monotribe_manual.pdf, English manual pages 13–16; static panel photo for general lower-panel sequencer location.
Routing weights: Device manual 90%; Visual/static layout 10%.
Evidence confidence: High.
Confidence rationale: The sequencer controls and procedures are explicitly documented in the manual section “Sequencer section.”
Unsupported-current-state risk: Low.
[/Trace]