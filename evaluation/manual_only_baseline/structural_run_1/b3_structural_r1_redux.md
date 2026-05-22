Prompt: Create a structured description of the sequencer section.

Response: 

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