Prompt: Create a structured description of the Monotribe.

Response:

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

