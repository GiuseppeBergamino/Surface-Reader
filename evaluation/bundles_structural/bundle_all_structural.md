Prompt ID: All

Prompt: Create a structured description of the Monotribe.

# Surface Reader:
## R1:
Structured description of the Korg monotribe
1. Device identity

Name: Korg monotribe
Type: Analog Ribbon Station
Main purpose: A compact analog synthesizer and rhythm machine with a ribbon keyboard, analog drum parts, and an eight-step sequencer. The manual describes it as using analog VCO, VCF, and VCA circuitry, with a filter circuit based on the classic Korg MS-20.

2. High-level surface regions

From the performer’s perspective, the monotribe surface can be understood as five main areas:

Synthesizer section
Main sound-shaping controls: oscillator, filter, amplifier, envelope, and LFO.
Ribbon keyboard / performance area
A touch ribbon used to play the synth pitch directly.
Sequencer section
Eight-step controls for synth and drum sequencing, plus play, record, active step, gate time, and flux functions.
Drum / rhythm controls
Three drum parts: BD, SN, and HH, controlled through part buttons and step buttons.
Connection area
Rear-panel jacks for power, audio input, audio output, headphones, sync in, and sync out.
3. Sound engine model

The monotribe’s sound generator has two main branches:

Synth branch
VCO — Voltage Controlled Oscillator
Generates the core waveform: sawtooth, triangle, or square.
Noise generator
Adds white noise to the oscillator signal.
VCF — Voltage Controlled Filter
A 12 dB/oct low-pass filter that changes the timbre or brightness.
VCA — Voltage Controlled Amplifier
Controls volume.
EG — Envelope Generator
Shapes how the sound starts, holds, or decays.
LFO — Low Frequency Oscillator
Modulates pitch, filter cutoff, or both.
Drum branch
BD — bass drum
SN — snare drum
HH — hi-hat

The drum sound generator is described as a three-part analog drum sound generator.

4. Synthesizer section controls
VCO group
Official control	Semantic role	Physical type	Function
OCTAVE selector	switch	selector	Sets VCO pitch in octave steps
WAVE select switch	switch	switch	Selects sawtooth, triangle, or square wave
NOISE knob	slider	rotary knob	Adjusts white noise level mixed with the VCO
RANGE select switch	switch	switch	Sets ribbon keyboard behavior: WIDE, NARROW, or KEY
VCF group
Official control	Semantic role	Physical type	Function
CUTOFF knob	slider	rotary knob	Adjusts filter cutoff frequency; left is darker, right is brighter
PEAK knob	slider	rotary knob	Adjusts filter resonance or emphasis around the cutoff
VCA / EG group
Official control	Semantic role	Physical type	Function
LEVEL knob	slider	rotary knob	Adjusts synth volume
EG select switch	switch	switch	Chooses DECAY, GATE, or ATTACK envelope behavior
LFO group
Official control	Semantic role	Physical type	Function
RATE knob	slider	rotary knob	Adjusts modulation speed
INT. knob	slider	rotary knob	Adjusts modulation depth
TARGET select switch	switch	switch	Selects VCO, VCO+VCF, or VCF as modulation target
MODE select switch	switch	switch	Selects FAST, SLOW, or 1SHOT modulation behavior
WAVE select switch	switch	switch	Selects LFO waveform
5. Keyboard / performance area
Element	Semantic role	Physical type	Function
Ribbon keyboard	keyboard	touch ribbon	Plays synth notes by touch

The ribbon keyboard can operate in different pitch behaviors depending on the RANGE select switch: WIDE, NARROW, or KEY. In KEY mode, pitch changes chromatically according to the printed ribbon keyboard.

6. Sequencer section

The monotribe contains an eight-step sequencer for the synth part and the drum sound generator.

Official control	Semantic role	Physical type	Function
PART LEDs	indicator	LEDs	Indicate selected part and low-battery warning states
PART buttons	button	buttons	Select SYNTH, BD, SN, or HH for editing
ACTIVE STEP button	button	button	Enables or disables steps in the sequence
PLAY button	button	button	Starts or stops sequence playback
TEMPO knob	slider	rotary knob	Sets sequencer speed
FLUX button	button	button	Turns FLUX mode on or off
REC button	button	button	Enters record or record-ready mode
GATE TIME button	button	button	Used with the ribbon keyboard to adjust synth note duration
STEP LEDs	indicator	LEDs	Indicate step status and current playback step
STEP buttons	button group	row of buttons	Turn individual synth or drum steps on or off
RHYTHM knob	slider	rotary knob	Adjusts drum sound generator volume
7. Sequencer behavior
Normal step behavior

Each step can be on or off. During playback, the step LEDs blink to indicate the current step. Static documentation can describe possible LED meanings, but it cannot tell which step is currently active.

FLUX mode
FLUX ON: Synth sequence data is recorded and played back continuously.
FLUX OFF: One note plays back for each step.
Gate time

Holding GATE TIME while using the ribbon keyboard changes the duration of synth notes. The manual gives the range as minimum at the far left of the ribbon and maximum at the far right.

8. Connection area

Rear-panel ports and controls:

Official element	Semantic role	Physical type	Function
Power switch	button/switch	power control	Turns power on/off
DC 9V jack	port	power jack	Connects optional AC adapter
AUDIO IN jack	port	mini jack	Accepts external audio; mixed with VCO and processed through VCF/VCA
OUTPUT jack	port	6.3 mm jack	Sends monotribe output to mixer or monitor
HEADPHONES jack	port	stereo mini jack	Connects headphones
SYNC OUT jack	port	mini jack	Outputs sync pulse at each step
SYNC IN jack	port	mini jack	Advances sequencer by incoming sync pulses
Grounding screw	grounding point	screw	Used to externally ground the unit if needed

The manual warns that power should be turned off before making connections, because careless usage may damage speakers or cause malfunctions.

9. Global menu structure

The Global menu assigns settings to step buttons 1–7:

Step button	Setting
1	Auto power-off
2	Battery type selection
3	SYNC OUT polarity
4	SYNC IN polarity
5	Sequence settings at start-up
6	Drum preview
7	TEMPO knob range

The manual states that Global menu mode is entered by holding ACTIVE STEP and GATE TIME while turning the power on. Changes are saved with REC or canceled with FLUX.

10. Non-visual mental map

A practical first-exploration map is:

Upper and middle panel: sound design controls. Think “synth engine”: VCO, filter, amp/envelope, and LFO.
Lower / performance area: ribbon keyboard and sequencer interaction.
Sequencer cluster: step buttons and transport-style controls for pattern playback and recording.
Rear edge: connection ports for power, audio, headphones, and sync.

Useful memory anchors:

Filter pair: CUTOFF and PEAK belong together.
LFO group: RATE and INT. are the main modulation amount/speed controls.
Step row: eight repeated buttons are the core sequencer landmark.
Ribbon: the long touch surface is the main pitch-performance landmark.
11. Static versus current-state limits

This description is based on the manual, visual index, and static panel references. It can identify controls, functions, possible states, and approximate layout. It cannot determine the current knob positions, switch positions, selected part, active steps, lit LEDs, cable connections, or what sound is currently being produced.

[Trace]
Sources used: monotribe_manual.pdf; monotribe_manual_visual_index.json; foto_pannello static panel reference; 01_surface_aria_store.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 04_routing_and_uncertainty_policy.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 15%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: Official control names and functions come from the manual, with layout and semantic structure supported by static references and schema files.
Unsupported-current-state risk: Low.
[/Trace]


## R2:
Structured description of the Korg monotribe

The Korg monotribe is an analogue ribbon station: a compact analog synthesizer, analog drum machine, and eight-step sequencer in one device. The manual describes it as using analog circuitry for the VCO, VCF, and VCA, with a filter circuit based on the classic Korg MS-20.

1. High-level surface regions
A. Synthesizer section

Main purpose: create and shape the synth sound.

Main groups:

VCO — Voltage Controlled Oscillator
Creates the basic waveform.
Includes waveform selection, octave range, noise level, and ribbon keyboard range.
External audio from AUDIO IN can be mixed with the VCO signal.
VCF — Voltage Controlled Filter
Shapes timbre.
Uses a 12 dB/oct low-pass filter.
Main controls: CUTOFF and PEAK.
VCA — Voltage Controlled Amplifier
Controls volume shape.
Main controls: LEVEL and EG select switch.
LFO — Low Frequency Oscillator
Applies modulation to pitch and/or filter cutoff.
Main controls: RATE, INT., TARGET, MODE, and LFO waveform selection.
Ribbon keyboard
Touch-sensitive performance strip.
Used to play synth notes directly.
Can operate in WIDE, NARROW, or KEY pitch behavior.
B. Sequencer section

Main purpose: record and play repeating patterns.

Main groups:

Part selection
SYNTH, BD, SN, and HH buttons select which part is edited.
Corresponding part LEDs indicate selected parts or battery warning states.
Transport and recording
PLAY starts and stops the sequence.
REC enters record or record-ready mode.
FLUX changes how synth sequence data is recorded and played back.
Step controls
Eight step buttons and step LEDs represent the eight sequencer steps.
Step buttons turn synth or drum events on/off depending on the selected part.
ACTIVE STEP enables or disables steps in the sequence.
Gate time
GATE TIME changes synth note duration by using the ribbon keyboard during playback.
Drum level
RHYTHM controls the drum sound generator volume.
C. Connection area

Main purpose: power, audio, headphones, and sync.

Ports and controls include:

Power switch
DC 9V jack
AUDIO IN jack
OUTPUT jack
HEADPHONES jack
SYNC OUT jack
SYNC IN jack
Grounding screw

The manual warns that power should be off before making connections, to avoid damaging speakers or causing malfunctions.

2. Signal-flow model

The monotribe’s synth sound follows this basic path:

VCO / noise / external audio input → VCF → VCA → audio output

Control and modulation sources include:

Ribbon keyboard: controls pitch/performance.
Sequencer: plays recorded synth and drum patterns.
EG: shapes VCA volume behavior.
LFO: modulates VCO pitch, VCF cutoff, or both.
SYNC IN / OUT: lets the sequencer synchronize with other equipment.

The drum generator is separate from the synth voice and provides three analog drum parts: BD, SN, and HH.

3. Surface model summary
Region	Group	Control / element	Semantic role	Physical type	Function
Synthesizer	VCO	OCTAVE selector	switch	selector	Sets VCO pitch by octave
Synthesizer	VCO	WAVE select switch	switch	switch	Selects sawtooth, triangle, or square wave
Synthesizer	VCO	NOISE knob	slider	rotary knob	Sets white-noise level
Synthesizer	VCO	RANGE select switch	switch	switch	Selects ribbon behavior: WIDE, NARROW, KEY
Synthesizer	VCF	CUTOFF knob	slider	rotary knob	Adjusts filter cutoff / brightness
Synthesizer	VCF	PEAK knob	slider	rotary knob	Adjusts resonance/emphasis
Synthesizer	VCA	LEVEL knob	slider	rotary knob	Adjusts synth volume
Synthesizer	VCA	EG select switch	switch	switch	Selects volume envelope shape
Synthesizer	LFO	RATE knob	slider	rotary knob	Adjusts modulation speed
Synthesizer	LFO	INT. knob	slider	rotary knob	Adjusts modulation depth
Synthesizer	LFO	TARGET select switch	switch	switch	Chooses modulation destination
Synthesizer	LFO	MODE select switch	switch	switch	Selects FAST, SLOW, or 1SHOT behavior
Synthesizer	LFO	WAVE select switch	switch	switch	Selects LFO waveform
Performance	Keyboard	Ribbon keyboard	keyboard	ribbon	Plays synth notes
Sequencer	Parts	SYNTH / BD / SN / HH buttons	button	buttons	Select part to edit
Sequencer	Parts	PART LEDs	indicator	LEDs	Indicate selected part / battery warning
Sequencer	Transport	PLAY button	button	button	Starts/stops sequence
Sequencer	Transport	REC button	button	button	Enters recording modes
Sequencer	Synth sequence	FLUX button	button	button	Turns FLUX mode on/off
Sequencer	Synth sequence	GATE TIME button	button	button	Edits synth note duration
Sequencer	Steps	STEP buttons	button	buttons	Enable/disable or enter steps
Sequencer	Steps	STEP LEDs	indicator	LEDs	Indicate step state/current step
Sequencer	Rhythm	RHYTHM knob	slider	rotary knob	Adjusts drum volume
Rear/connection area	Audio/power/sync	Jacks and power switch	port / button	jacks / switch	Power, audio, headphones, sync
4. Non-visual orientation map

From the performer’s perspective:

Treat the ribbon keyboard as the main lower-panel landmark.
The synthesizer controls occupy the upper and middle control area.
The sequencer controls are grouped around the step buttons and part/transport controls.
The step buttons and step LEDs form a repeated eight-step pattern, useful as a tactile and conceptual anchor.
The connection area is separate from the main playing surface and contains the power, audio, headphone, sync, and adapter connections.

A useful memory anchor:

Top/middle = sound design. Lower/repeated controls = sequencing. Ribbon = playing. Rear/connection edge = power and cables.

5. Static versus current state

This description is based on the manual, visual index, and static panel references. It can describe:

what controls exist;
what they are called;
what they do;
possible settings and meanings;
the general panel organization.

It cannot determine:

current knob positions;
current switch positions;
which LEDs are lit;
what sequence is currently stored;
whether cables are connected;
what sound is currently being produced.

[Trace]
Sources used: monotribe_manual.pdf; monotribe_manual_visual_index.json; foto_pannello static panel photo; 01_surface_aria_store.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 04_routing_and_uncertainty_policy.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 15%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: Official control names and functions come from the manual, with structure translated through the surface-model and ARIA stores.
Unsupported-current-state risk: Low.
[/Trace]


## R3:
Structured description of the Korg monotribe
1. Device identity

The Korg monotribe is an analogue ribbon station: a small performance instrument combining an analog synthesizer, analog drum sound generator, ribbon keyboard, and eight-step sequencer. The manual describes its main sound engine as analog VCO, VCF, and VCA circuitry, with the VCF based on the classic Korg MS-20 filter circuit.

2. Main functional regions

From the performer’s perspective, the monotribe surface can be understood as four main regions:

Synthesizer section
Used to shape the synth sound: oscillator, noise, filter, amplifier/envelope, and LFO.
Ribbon keyboard / performance area
Used to play the synth part directly with a finger.
Sequencer section
Used to play, record, enable, disable, and edit the synth and drum sequence.
Connection area
Used for power, audio input/output, headphones, and sync input/output.

The manual’s visual index identifies separate panel overview diagrams for the synthesizer section and sequencer section, plus a rear-panel connection diagram.

3. Surface model
A. Synthesizer section
VCO group — oscillator and source controls

Purpose: creates the basic sound source.

Controls:

OCTAVE selector
Semantic role: switch
Physical type: discrete selector
Function: sets the VCO pitch in octave steps.
WAVE select switch
Semantic role: switch
Physical type: multi-position switch
Possible values: sawtooth, triangle, square.
Function: selects the oscillator waveform.
NOISE knob
Semantic role: slider
Physical type: rotary knob
Function: adjusts the level of white noise mixed with the VCO output.
RANGE select switch
Semantic role: switch
Physical type: multi-position switch
Possible values: WIDE, NARROW, KEY.
Function: changes how the ribbon keyboard controls pitch.

The manual states that the VCO generates the waveform at a pitch determined by the ribbon keyboard or sequencer performance data, and that external audio can also be mixed with the VCO output.

VCF group — filter controls

Purpose: changes timbre or brightness.

Controls:

CUTOFF knob
Semantic role: slider
Physical type: rotary knob
Function: adjusts the VCF cutoff frequency. Turning left darkens the sound; turning right brightens it.
PEAK knob
Semantic role: slider
Physical type: rotary knob
Function: adjusts resonance, emphasizing the cutoff frequency.

Memory anchor: Cutoff shapes brightness; Peak shapes emphasis.

VCA / EG group — level and envelope

Purpose: controls volume behavior.

Controls:

LEVEL knob
Semantic role: slider
Physical type: rotary knob
Function: adjusts synth volume.
EG select switch
Semantic role: switch
Physical type: multi-position switch
Possible values: DECAY, GATE, ATTACK.
Function: chooses how the volume changes when a note starts.
LFO group — modulation controls

Purpose: applies repeating or one-shot movement to pitch and/or filter.

Controls:

RATE knob
Semantic role: slider
Physical type: rotary knob
Function: controls modulation speed.
INT. knob
Semantic role: slider
Physical type: rotary knob
Function: controls modulation depth.
TARGET select switch
Semantic role: switch
Possible values: VCO, VCO+VCF, VCF.
Function: chooses what the LFO modulates.
MODE select switch
Semantic role: switch
Possible values: FAST, SLOW, 1SHOT.
Function: chooses the modulation rate range or one-shot behavior.
LFO WAVE select switch
Semantic role: switch
Possible values: sawtooth, triangle, square.
Function: selects the LFO waveform.
B. Ribbon keyboard
Ribbon keyboard
Semantic role: keyboard
Physical type: touch ribbon
Function: plays the synth sound by finger contact.

The RANGE select switch changes how this ribbon behaves: WIDE gives a much larger continuous range, NARROW gives continuous pitch according to the printed ribbon keyboard, and KEY gives chromatic pitch steps.

Tactile landmark: this is one of the most useful lower-panel landmarks because it is a long horizontal touch surface rather than a knob or button.

C. Sequencer section

Purpose: controls the eight-step synth and drum sequence.

Part selection group

Controls:

SYNTH button
BD button
SN button
HH button

Semantic role: button
Function: selects which part is being edited.

Indicators:

PART LEDs
Semantic role: indicator
Function: show the selected part when lit; also blink simultaneously as a low-battery warning.

The drum parts are:

BD: bass drum
SN: snare drum
HH: hi-hat
Transport and recording group

Controls:

PLAY button
Semantic role: button
Function: starts or stops sequence playback.
REC button
Semantic role: button
Function: enters record mode during playback, or record-ready mode while stopped.
FLUX button
Semantic role: button
Function: turns FLUX mode on or off. With FLUX on, synth sequence data is recorded and played back continuously rather than being restricted to one note per step.
GATE TIME button
Semantic role: button
Function: when held during playback, lets the ribbon keyboard change synth note duration.
Step control group

Controls:

STEP buttons 1–8
Semantic role: button
Physical type: repeated step buttons
Function: turn steps on or off, depending on the selected part or operation.

Indicators:

STEP LEDs 1–8
Semantic role: indicator
Function: show step states, current step during playback, battery level at startup, and global menu settings.
Tempo and rhythm controls
TEMPO knob
Semantic role: slider
Physical type: rotary knob
Function: sets sequencer speed unless SYNC IN is connected.
RHYTHM knob
Semantic role: slider
Physical type: rotary knob
Function: adjusts the drum sound generator volume.
D. Connection area

The manual lists these rear-panel connections:

Power switch
Semantic role: button or power control
Function: turns the unit on/off. To turn off, press and hold.
DC 9V jack
Semantic role: port
Function: connects the optional AC adapter.
AUDIO IN jack
Semantic role: port
Function: accepts an external audio source, mixed with the VCO and routed through the VCF and VCA.
OUTPUT jack
Semantic role: port
Function: sends the monotribe’s monaural output to a mixer or powered speakers.
HEADPHONES jack
Semantic role: port
Function: connects headphones.
SYNC OUT jack
Semantic role: port
Function: outputs a 5V pulse at the beginning of each step.
SYNC IN jack
Semantic role: port
Function: receives pulses to advance the sequencer steps externally.
Grounding screw
Semantic role: grounding point
Function: allows external grounding if needed.
4. Surface map: non-visual overview

Use the panel as a set of regions rather than as isolated labels.

A practical first mental map:

Upper/central panel: synth sound-shaping controls, mostly knobs and switches.
Lower or performance area: ribbon keyboard, a long tactile landmark.
Sequencer area: repeated step buttons and LEDs; this is the main pattern-editing area.
Rear edge: power, audio, headphones, sync, and power adapter connections.

A useful tactile strategy is to first identify the long ribbon keyboard, then use it as a lower landmark. From there, move upward into the synth controls or sideways toward the step-sequencer controls. Repeated buttons are likely sequencer-related; rotary knobs are usually continuous sound or level controls; small multi-position switches choose modes or waveform/range options.

5. Important static-state limitation

This description is based on the manual, visual index, and static panel references. It describes what controls exist, what they can do, and how the surface is organized. It cannot determine current knob positions, switch positions, LED states, cable connections, selected part, active step, or whether the monotribe is currently playing.

[Trace]
Sources used: monotribe_manual.pdf; monotribe_manual_visual_index.json; 01_surface_aria_store.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 04_routing_and_uncertainty_policy.md; 05_surface_model_map_schema.md; static panel photo available as foto_pannello.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 15%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: Official functions and names are grounded in the manual; spatial grouping is supported by manual panel diagrams and the visual index, but exact tactile dimensions are static only.
Unsupported-current-state risk: Low.
[/Trace]

# Baseline:
## R1:
Direct answer

The Korg monotribe is an analogue ribbon station built around three main areas: an analog synthesizer, an analog drum sound generator, and an eight-step sequencer. The manual describes it as using analog circuitry for the VCO, VCF, and VCA, with a filter circuit based on the classic Korg MS-20.

1. Overall layout

The instrument is arranged as a small tabletop unit.

The main playing and editing surface is divided into:

Synthesizer section: the upper and middle control area, with controls for oscillator, filter, amplifier, envelope, LFO, and the ribbon keyboard.
Sequencer section: the lower/right control area, with part buttons, transport controls, step buttons, and rhythm controls.
Rear/edge connection area: power, audio, headphone, sync, and grounding connections.
2. Sound structure

The synthesizer sound generator is made of:

VCO: creates the basic waveform and pitch.
VCF: changes the tone or brightness.
VCA: controls volume.
EG: changes volume shape over time.
LFO: applies cyclic modulation to pitch and/or filter cutoff.

The drum sound generator has three analog parts:

BD: bass drum.
SN: snare drum.
HH: hi-hat.
3. Synthesizer controls
VCO area

The VCO section includes:

OCTAVE selector: sets VCO pitch in octave steps.
WAVE select switch: chooses sawtooth, triangle, or square wave.
NOISE knob: adds white noise.
RANGE select switch: sets how the ribbon keyboard behaves.

The RANGE settings are:

WIDE: wide continuous pitch range.
NARROW: continuous pitch following the printed ribbon keyboard.
KEY: chromatic pitch steps.
VCF area

The VCF section includes:

CUTOFF knob: changes brightness by adjusting filter cutoff.
PEAK knob: adjusts resonance at the cutoff frequency.

Turning CUTOFF left makes the sound darker; turning it right makes the sound brighter.

VCA and EG area

The VCA section includes:

LEVEL knob: adjusts synthesizer volume.
EG select switch: chooses the envelope shape applied to the VCA.

The EG choices are:

DECAY: starts loud, then fades.
GATE: stays loud while the note is held.
ATTACK: fades in, then stays loud while held.
LFO area

The LFO section includes:

RATE knob: controls modulation speed.
INT. knob: controls modulation depth.
TARGET select switch: chooses what the LFO affects.
MODE select switch: chooses FAST, SLOW, or 1SHOT behavior.
WAVE select switch: chooses the modulation waveform.

TARGET settings are:

VCO: modulates pitch.
VCO+VCF: modulates pitch and filter cutoff.
VCF: modulates filter cutoff.
4. Playing surface

The ribbon keyboard is touched with a finger to play sounds. Its pitch behavior depends on the RANGE setting.

5. Sequencer section

The monotribe has an eight-step sequencer that controls the synthesizer and drum sound generator.

Main sequencer controls include:

PART buttons: select SYNTH, BD, SN, or HH.
PART LEDs: show which part is selected.
ACTIVE STEP button: enables or disables individual steps.
PLAY button: starts or stops the sequence.
TEMPO knob: sets sequencer speed.
FLUX button: records and plays synth motion as continuous data instead of strictly step-based notes.
REC button: records ribbon keyboard performance into the synth sequence.
GATE TIME button: changes synth note duration using the ribbon keyboard.
STEP buttons and STEP LEDs: turn steps on or off and show step activity.
RHYTHM knob: adjusts drum sound generator volume.
6. Connections

The connection area includes:

Power switch
DC 9V jack
AUDIO IN jack
OUTPUT jack
HEADPHONES jack
SYNC OUT jack
SYNC IN jack
Grounding screw

AUDIO IN lets an external audio source be mixed with the VCO path and sent through the VCF and VCA. SYNC IN and SYNC OUT allow step synchronization with another monotribe or compatible equipment.

7. Power and storage

The monotribe can run from:

Six AA alkaline batteries.
Six AA nickel-metal hydride batteries.
Optional DC9V AC adapter.

It has an auto power-off function that turns the unit off after about four hours without producing sound. A sequence can be saved by holding REC while the sequencer is stopped and the monotribe is not producing sound.

8. Global menu

The Global menu provides settings for:

Auto power-off.
Battery type.
SYNC OUT polarity.
SYNC IN polarity.
Sequence loaded at startup.
Drum preview.
TEMPO knob range.

The Global menu is entered by holding ACTIVE STEP and GATE TIME while turning the power on.

[Trace]
Sources used: monotribe owner’s manual pages 5–17; static panel photo.
Routing weights: Device manual 85%; Visual/static layout 15%.
Evidence confidence: High.
Confidence rationale: The description follows the manual’s named sections, controls, and functions, with static layout used only for broad physical organization.
Unsupported-current-state risk: None.
[/Trace]

## R2:
Structured description of the Korg monotribe

The monotribe is a compact analogue ribbon station: a small synthesizer, drum sound generator, and step sequencer in one unit. It is designed for hands-on sound creation, live looping, and synchronizing with other devices.

1. Sound engine

The synthesizer sound generator is built from three analogue sections:

VCO — Voltage Controlled Oscillator
Creates the basic sound waveform. It can use sawtooth, triangle, or square waveforms, and can mix in white noise. An external audio signal from AUDIO IN can also be mixed with the VCO.

VCF — Voltage Controlled Filter
Shapes the timbre of the sound. The manual describes it as a 12 dB/oct low-pass filter using the filter circuit of the Korg MS-20. The main controls are CUTOFF and PEAK.

VCA — Voltage Controlled Amplifier
Controls the volume of the synthesizer sound. The EG select switch changes how the volume behaves over time: DECAY, GATE, or ATTACK.

2. Modulation

The monotribe has an LFO that applies movement to the sound. It can modulate:

VCO — pitch changes
VCO+VCF — pitch and filter cutoff changes
VCF — filter cutoff changes

The LFO has RATE and INT. controls, a WAVE selector, and a MODE selector with FAST, SLOW, and 1SHOT modes.

3. Playing surface

The instrument uses a ribbon keyboard rather than regular keys. You touch the ribbon with a finger to play sounds.

The RANGE switch changes how the ribbon behaves:

WIDE — continuous pitch over a much wider range
NARROW — continuous pitch following the printed ribbon keyboard
KEY — chromatic stepped pitch following the printed ribbon keyboard

The OCTAVE selector changes the VCO pitch in octave steps, except when WIDE is selected.

4. Drum sound generator

The monotribe includes a three-part analogue drum sound generator:

BD — bass drum
SN — snare drum
HH — hi-hat

The RHYTHM knob controls the drum sound generator volume.

5. Sequencer

The built-in sequencer has eight steps and can control both the synthesizer part and the drum parts.

Main sequencer controls include:

PLAY — starts or stops sequence playback
REC — records ribbon keyboard performance into the synth sequence
FLUX — allows the synth sequence to be recorded and played back as continuous data rather than one note per step
ACTIVE STEP — enables or disables individual steps
GATE TIME — changes the duration of synth notes during sequence playback
TEMPO — controls sequencer speed unless SYNC IN is connected

For drum parts, the eight step buttons turn steps on or off. The manual also describes a method for placing drum sounds halfway through a step by holding a part button while turning on a step.

6. Connections

The connection jacks are on the rear/top connector area. The manual lists:

DC 9V — optional AC adapter
AUDIO IN — external audio input, mixed with the VCO and processed through VCF and VCA
OUTPUT — monaural output to mixer or powered speakers
HEADPHONES — stereo mini-jack for headphones
SYNC OUT — sends a 5V pulse at the beginning of each step
SYNC IN — receives pulses to advance the sequencer steps from another device
Grounding screw — for external grounding if needed

7. Power and portability

The monotribe can run from six AA batteries or an optional DC9V AC adapter. The manual states approximately 14 hours of battery life with alkaline batteries. It also has an internal speaker.

8. Physical layout, non-visual overview

From the static panel layout, the instrument is organized into two main working areas:

The synthesizer controls occupy the upper and central part of the panel, grouped by function: VCO, VCF, VCA, and LFO.

The ribbon keyboard runs along the lower front area and is used for playing pitch and changing gate time.

The sequencer controls and step buttons are in the lower/right working area, with transport and recording controls nearby.

The part controls for SYNTH, BD, SN, and HH are grouped together for choosing which part you are editing.

The connection jacks are along the back edge, separate from the performance controls.

9. Global settings

The Global menu uses step buttons 1–7 to change system settings, including:

Auto power-off, battery type, SYNC OUT polarity, SYNC IN polarity, startup sequence behavior, drum preview, and TEMPO knob range.

[Trace]
Sources used: monotribe_manual.pdf pages 5–17; static panel photo.
Routing weights: Device manual 90%; Visual/static layout 10%.
Evidence confidence: High.
Confidence rationale: The description follows documented manual sections and uses the static panel photo only for general layout.
Unsupported-current-state risk: None.
[/Trace]

## R3
Direct answer

The Korg monotribe is an analogue ribbon station combining a monophonic analog synthesizer, a three-part analog drum sound generator, and an eight-step sequencer. Its main performance interface is a ribbon keyboard, with realtime controls for pitch, timbre, volume, modulation, rhythm, and sequencing.

1. Overall structure

The monotribe has three main working areas:

Synthesizer section
Creates the synth sound using analog VCO, VCF, and VCA circuitry.
Sequencer section
Records and plays back an eight-step sequence for the synth and drum parts.
Connection and power area
Provides audio input/output, headphones, sync jacks, power, batteries, and optional AC adapter use.
2. Sound engine

The synthesizer sound generator is built from:

VCO — Voltage Controlled Oscillator: generates the basic waveform.
VCF — Voltage Controlled Filter: changes the timbre by filtering the sound.
VCA — Voltage Controlled Amplifier: controls the volume.
EG — Envelope Generator: changes volume behavior over time.
LFO — Low Frequency Oscillator: applies modulation to pitch and/or filter cutoff.
Noise generator: adds white noise.
External audio input path: an external source connected to AUDIO IN is mixed with the VCO and passed through the VCF and VCA.

The drum generator has three analog parts:

BD: bass drum.
SN: snare drum.
HH: hi-hat.
3. Main panel layout
Left and central upper area: synth controls

The synthesizer section contains the controls for shaping the synth sound.

The VCO area includes:

OCTAVE selector: changes pitch in octave steps.
WAVE select switch: selects sawtooth, triangle, or square wave.
NOISE knob: controls the amount of white noise mixed with the VCO.
RANGE select switch: sets ribbon keyboard behavior to WIDE, NARROW, or KEY.

The VCF area includes:

CUTOFF knob: changes brightness by adjusting filter cutoff.
PEAK knob: adjusts resonance at the cutoff frequency.

The VCA area includes:

LEVEL knob: adjusts synth volume.
EG select switch: chooses DECAY, GATE, or ATTACK behavior.

The LFO area includes:

RATE knob: sets modulation speed.
INT. knob: sets modulation depth.
TARGET select switch: chooses VCO, VCO+VCF, or VCF modulation.
MODE select switch: chooses FAST, SLOW, or 1SHOT.
WAVE select switch: selects the modulation waveform.

The ribbon keyboard is used by touching it with a finger to play synth sounds.

Lower / sequencer area

The sequencer section controls the synth sequence and drum pattern.

It includes:

PART buttons: SYNTH, BD, SN, HH.
PART LEDs: show the selected part.
ACTIVE STEP button: enables or disables steps.
PLAY button: starts or stops the sequence.
TEMPO knob: sets sequencer speed, unless SYNC IN is connected.
FLUX button: enables continuous synth recording/playback instead of step-limited playback.
REC button: records ribbon keyboard performance into the sequence.
GATE TIME button: changes synth note duration using the ribbon keyboard.
STEP buttons and STEP LEDs: turn steps on/off and show step status.
RHYTHM knob: controls drum sound generator volume.
4. Sequencer behavior

The monotribe has an eight-step sequencer. It can control:

the synth part;
the bass drum;
the snare drum;
the hi-hat.

For the synth part, the sequence can be recorded from the ribbon keyboard. With FLUX mode on, synth data is recorded and played back continuously rather than being restricted to one note per step.

For drum parts, the step buttons turn each step on or off. Holding a part button while turning on a step can place the drum sound halfway through the step, effectively allowing finer rhythmic placement.

5. Connections

The connection area includes:

Power switch: turns the unit on or off.
DC 9V jack: for the optional AC adapter.
AUDIO IN jack: accepts an external audio source.
OUTPUT jack: sends monaural output to a mixer or powered speaker.
HEADPHONES jack: for stereo mini-plug headphones.
SYNC OUT jack: sends a 5V pulse at the beginning of each step.
SYNC IN jack: receives pulses to advance the sequencer externally.
Grounding screw: used for external grounding if needed.
6. Power and portability

The monotribe can run from:

six AA alkaline batteries;
six AA nickel-metal hydride batteries;
an optional DC9V AC adapter.

It has a built-in speaker, so it can be used without external speakers. The manual lists battery life as approximately 14 hours when using alkaline batteries.

7. Global menu

The Global menu contains settings assigned to step buttons 1–7:

auto power-off;
battery type;
SYNC OUT polarity;
SYNC IN polarity;
sequence loaded at startup;
drum preview behavior;
TEMPO knob range.

To enter the Global menu, hold ACTIVE STEP and GATE TIME while turning the power on. Press REC to save changes, or FLUX to cancel.

Limitation

This description is based on the manual and the static panel layout. It describes what the controls and sections are, but it cannot determine the current positions of knobs or switches, current LED states, cable connections, or the sound currently being produced.

[Trace]
Sources used: monotribe_manual.pdf, pages 5–17; static panel photo.
Routing weights: Device manual 85%; Visual/static layout 15%.
Evidence confidence: High.
Confidence rationale: The requested overview is directly documented in the manual’s feature, panel, sequencer, connection, global menu, and specification sections.
Unsupported-current-state risk: None.
[/Trace]