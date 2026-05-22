Prompt: Create a structured description of the Monotribe.

Response:

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

