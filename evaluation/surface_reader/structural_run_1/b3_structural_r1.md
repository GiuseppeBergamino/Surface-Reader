Prompt: Create a structured description of the sequencer section.

Response: 

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