Prompt: Create a structured description of the sequencer section.

Response: 

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
