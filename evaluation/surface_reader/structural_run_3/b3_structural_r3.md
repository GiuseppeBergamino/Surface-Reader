Prompt: Create a structured description of the sequencer section.

Response: 

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

