Prompt: Create a structured description of the Monotribe.

Response:

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

