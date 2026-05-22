Prompt: Create a structured description of the sequencer section.

Response: 

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