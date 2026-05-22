Prompt: Represent the whole instrument as Surface ARIA structure.

Response: 
I’ll build this as a static Surface ARIA model: semantic hierarchy plus physical/tactile map. I’ll mark possible states separately from current state so it does not imply live observation.

Below is a static Surface ARIA representation of the Korg monotribe as a non-visual control-surface model. It is grounded in the manual, visual index, static panel/photo references, and the Surface ARIA/model guidance stores. It does not include current knob values, switch positions, LED states, cables, or playback state, because those require live evidence.

surface:
  node_id: monotribe
  role: instrument
  name: Korg monotribe analogue ribbon station
  description: Analog ribbon synthesizer with VCO, VCF, VCA, LFO, three-part drum generator, eight-step sequencer, ribbon keyboard, sync, audio input, and audio output.
  current_state: unavailable_from_static_sources
  children:
    - top_panel
    - rear_connection_area
    - global_menu_model
    - internal_sound_engine

top_panel:
  node_id: top_panel
  role: region
  name: Top panel
  description: Main performance and editing surface.
  map:
    perspective: performer
    top: farthest edge from performer
    bottom: closest edge to performer
    left: performer left
    right: performer right
    major_landmarks:
      - ribbon_keyboard_lower_area
      - step_button_row_in_sequencer
      - knob_and_switch_clusters_in_synth_section
  children:
    - synthesizer_section
    - sequencer_section
    - ribbon_keyboard_region

synthesizer_section:
  node_id: synthesizer_section
  role: region
  name: Synthesizer section
  description: Controls the analog synth voice: VCO pitch/wave/noise, VCF timbre, VCA level/envelope, and LFO modulation.
  source: manual panel description, page 10–13; visual index page 10
  map:
    approximate_position: upper_and_middle_panel_area
    tactile_summary: Multiple rotary knobs and small selector switches grouped by sound function.
  children:
    - vco_group
    - vcf_group
    - vca_group
    - lfo_group
    - ribbon_keyboard_region

vco_group:
  node_id: vco_group
  role: group
  name: VCO
  description: Oscillator group. Generates the basic waveform and mixes white noise or external audio before filtering.
  children:
    - octave_selector
    - vco_wave_select_switch
    - noise_knob
    - range_select_switch

octave_selector:
  node_id: octave_selector
  role: switch
  name: OCTAVE selector
  physical_type: discrete selector
  description: Specifies VCO pitch in octave steps.
  possible_states:
    - octave settings including 64-foot range, where the ribbon keyboard range is A0–D2
  current_state: unavailable_from_static_sources

vco_wave_select_switch:
  node_id: vco_wave_select_switch
  role: switch
  name: WAVE select switch
  physical_type: slide_or_multi-position_switch_from_static_layout
  description: Selects the VCO waveform.
  possible_states:
    - sawtooth wave
    - triangle wave
    - square wave
  current_state: unavailable_from_static_sources

noise_knob:
  node_id: noise_knob
  role: slider
  name: NOISE knob
  physical_type: rotary knob
  description: Adjusts the level of white noise mixed with the VCO output.
  actions:
    - turn counterclockwise to decrease
    - turn clockwise to increase
  current_state: unavailable_from_static_sources

range_select_switch:
  node_id: range_select_switch
  role: switch
  name: RANGE select switch
  physical_type: multi-position switch
  description: Specifies the ribbon keyboard playing mode.
  possible_states:
    - WIDE: extended continuous pitch range, octave selector ignored
    - NARROW: continuous pitch according to the printed ribbon keyboard
    - KEY: chromatic pitch steps according to the printed ribbon keyboard
  current_state: unavailable_from_static_sources

vcf_group:
  node_id: vcf_group
  role: group
  name: VCF
  description: Filter group. Changes timbre using a 12 dB/oct low-pass filter.
  map:
    tactile_anchor: two related rotary knobs
    memory_anchor: Cutoff shapes brightness; Peak shapes emphasis.
  children:
    - cutoff_knob
    - peak_knob

cutoff_knob:
  node_id: cutoff_knob
  role: slider
  name: CUTOFF knob
  physical_type: rotary knob
  description: Adjusts the cutoff frequency of the VCF. Left darkens the sound; right brightens it.
  actions:
    - turn counterclockwise for darker sound
    - turn clockwise for brighter sound
  current_state: unavailable_from_static_sources

peak_knob:
  node_id: peak_knob
  role: slider
  name: PEAK knob
  physical_type: rotary knob
  description: Adjusts VCF resonance, emphasizing the cutoff frequency.
  actions:
    - turn counterclockwise to decrease emphasis
    - turn clockwise to increase emphasis
  current_state: unavailable_from_static_sources

vca_group:
  node_id: vca_group
  role: group
  name: VCA
  description: Amplifier group. Controls synth voice volume and envelope behavior.
  children:
    - level_knob
    - eg_select_switch

level_knob:
  node_id: level_knob
  role: slider
  name: LEVEL knob
  physical_type: rotary knob
  description: Adjusts the synth volume.
  safety_note: Manual instructs turning LEVEL fully left before powering on or off.
  current_state: unavailable_from_static_sources

eg_select_switch:
  node_id: eg_select_switch
  role: switch
  name: EG select switch
  physical_type: multi-position switch
  description: Selects one of three envelope shapes applied to the VCA.
  possible_states:
    - DECAY: volume starts at maximum and decays
    - GATE: volume remains at maximum while note is played
    - ATTACK: volume rises after note begins and remains at maximum while note is played
  current_state: unavailable_from_static_sources

lfo_group:
  node_id: lfo_group
  role: group
  name: LFO
  description: Low Frequency Oscillator group. Applies cyclic or one-shot modulation to pitch and/or filter cutoff.
  children:
    - lfo_rate_knob
    - lfo_int_knob
    - lfo_target_select_switch
    - lfo_mode_select_switch
    - lfo_wave_select_switch

lfo_rate_knob:
  node_id: lfo_rate_knob
  role: slider
  name: RATE knob
  physical_type: rotary knob
  description: Adjusts modulation speed. Turning right makes modulation faster.
  current_state: unavailable_from_static_sources

lfo_int_knob:
  node_id: lfo_int_knob
  role: slider
  name: INT. knob
  physical_type: rotary knob
  description: Adjusts modulation intensity or depth. Fully left applies no modulation.
  current_state: unavailable_from_static_sources

lfo_target_select_switch:
  node_id: lfo_target_select_switch
  role: switch
  name: TARGET select switch
  physical_type: multi-position switch
  description: Selects the destination affected by LFO modulation.
  possible_states:
    - VCO: VCO pitch changes
    - VCO+VCF: VCO pitch and VCF cutoff frequency change
    - VCF: VCF cutoff frequency changes
  current_state: unavailable_from_static_sources

lfo_mode_select_switch:
  node_id: lfo_mode_select_switch
  role: switch
  name: MODE select switch
  physical_type: multi-position switch
  description: Selects LFO speed range or one-shot behavior.
  possible_states:
    - FAST: approximately 1 Hz to 5 kHz
    - SLOW: approximately 0.05 Hz to 18 Hz
    - 1SHOT: first half-cycle plays at note start, then stops
  current_state: unavailable_from_static_sources

lfo_wave_select_switch:
  node_id: lfo_wave_select_switch
  role: switch
  name: WAVE select switch
  physical_type: multi-position switch
  description: Selects the LFO modulation waveform.
  possible_states:
    - sawtooth wave
    - triangle wave
    - square wave
  current_state: unavailable_from_static_sources

ribbon_keyboard_region:
  node_id: ribbon_keyboard_region
  role: keyboard
  name: Ribbon keyboard
  physical_type: ribbon touch surface
  description: Touch surface used to play synth notes. Its pitch behavior depends on the RANGE select switch.
  map:
    approximate_position: lower_panel_performance_area
    tactile_role: strong horizontal landmark
    navigation_hint: Use the long ribbon surface as a lower-panel reference point for locating nearby sequencer and synth controls.
  actions:
    - touch to play
    - touch while holding GATE TIME during playback to set gate time
  current_state: unavailable_from_static_sources

sequencer_section:
  node_id: sequencer_section
  role: region
  name: Sequencer section
  description: Eight-step sequencer controlling the synth part and three drum parts.
  source: manual panel description, page 13–15; visual index pages 13–15
  map:
    approximate_position: lower_and_right_panel_area
    tactile_summary: Button-heavy area with part buttons, transport buttons, step buttons, and related LEDs.
  children:
    - part_selection_group
    - transport_group
    - synth_sequence_group
    - step_sequence_group
    - rhythm_group

part_selection_group:
  node_id: part_selection_group
  role: group
  name: PART controls
  description: Selects which part is edited.
  children:
    - part_leds
    - synth_part_button
    - bd_part_button
    - sn_part_button
    - hh_part_button

part_leds:
  node_id: part_leds
  role: indicator
  name: PART LEDs
  physical_type: LEDs
  description: Light when the corresponding PART button is selected; all four blink simultaneously as a low-battery warning.
  possible_states:
    - lit: corresponding part selected
    - blinking_together: low battery warning
  current_state: unavailable_from_static_sources

synth_part_button:
  node_id: synth_part_button
  role: button
  name: SYNTH button
  physical_type: button
  description: Selects the SYNTH part for editing.
  current_state: unavailable_from_static_sources

bd_part_button:
  node_id: bd_part_button
  role: button
  name: BD button
  physical_type: button
  description: Selects the bass drum part for editing.
  current_state: unavailable_from_static_sources

sn_part_button:
  node_id: sn_part_button
  role: button
  name: SN button
  physical_type: button
  description: Selects the snare drum part for editing.
  current_state: unavailable_from_static_sources

hh_part_button:
  node_id: hh_part_button
  role: button
  name: HH button
  physical_type: button
  description: Selects the hi-hat part for editing.
  current_state: unavailable_from_static_sources

transport_group:
  node_id: transport_group
  role: group
  name: Transport controls
  description: Controls sequence playback and recording.
  children:
    - play_button
    - play_led
    - rec_button
    - rec_led

play_button:
  node_id: play_button
  role: button
  name: PLAY button
  physical_type: button
  description: Starts or stops the sequence. Playback starts from the beginning.
  current_state: unavailable_from_static_sources

play_led:
  node_id: play_led
  role: indicator
  name: PLAY LED
  physical_type: LED
  description: Lit during playback.
  possible_states:
    - lit: playback is active
    - unlit: playback is not indicated
  current_state: unavailable_from_static_sources

rec_button:
  node_id: rec_button
  role: button
  name: REC button
  physical_type: button
  description: Enters or exits record mode or record-ready mode; also used to save a sequence when held while stopped and silent.
  actions:
    - press during playback to enter record mode
    - press while stopped to enter record-ready mode
    - press again to exit record or record-ready mode
    - hold while stopped and silent to save sequence
  safety_note: Do not turn off power while data is being saved.
  current_state: unavailable_from_static_sources

rec_led:
  node_id: rec_led
  role: indicator
  name: REC LED
  physical_type: LED
  description: Indicates record status.
  possible_states:
    - lit: record mode
    - blinking: record-ready mode or saving sequence until it stops blinking and goes dark
    - unlit: not in record or record-ready mode
  current_state: unavailable_from_static_sources

synth_sequence_group:
  node_id: synth_sequence_group
  role: group
  name: Synthesizer sequence controls
  description: Controls synth-part recording behavior and gate time.
  children:
    - flux_button
    - flux_led
    - gate_time_button
    - active_step_button
    - tempo_knob

flux_button:
  node_id: flux_button
  role: button
  name: FLUX button
  physical_type: button
  description: Turns FLUX mode on or off.
  possible_states:
    - ON: synth sequence is recorded and played back as continuous data
    - OFF: one note plays back for each step
  current_state: unavailable_from_static_sources

flux_led:
  node_id: flux_led
  role: indicator
  name: FLUX LED
  physical_type: LED
  description: Indicates possible FLUX button state if observed.
  current_state: unavailable_from_static_sources

gate_time_button:
  node_id: gate_time_button
  role: button
  name: GATE TIME button
  physical_type: button
  description: While held during sequence playback, the ribbon keyboard changes synth note gate time.
  possible_values:
    - far left of ribbon: minimum gate time, 1.4%
    - far right of ribbon: maximum gate time, 100%
  current_state: unavailable_from_static_sources

active_step_button:
  node_id: active_step_button
  role: button
  name: ACTIVE STEP button
  physical_type: button
  description: Held with step buttons to enable or disable sequence steps.
  actions:
    - hold ACTIVE STEP and press a step button to turn that step on or off
  possible_states:
    - enabled step: step LED lit while ACTIVE STEP is held
    - disabled step: skipped during playback and recording
  constraints:
    - all steps cannot be turned off at the same time
    - all steps are on at power-up
  current_state: unavailable_from_static_sources

tempo_knob:
  node_id: tempo_knob
  role: slider
  name: TEMPO knob
  physical_type: rotary knob
  description: Sets sequencer speed unless SYNC IN is connected.
  possible_ranges:
    - NARROW global setting: 60–180 BPM
    - WIDE global setting: 10–600 BPM
  current_state: unavailable_from_static_sources

step_sequence_group:
  node_id: step_sequence_group
  role: group
  name: STEP controls
  description: Eight step buttons and LEDs used for synth and rhythm sequence programming.
  map:
    tactile_anchor: repeated row of eight step buttons
    memory_anchor: This repeated row is the main sequencer landmark.
  children:
    - step_leds
    - step_buttons_1_to_8

step_leds:
  node_id: step_leds
  role: indicator_set
  name: STEP LEDs
  physical_type: row_of_LEDs
  description: Show step on/off status and current step during playback; also show battery level at startup.
  possible_states:
    - lit: corresponding step on, or enabled depending on context
    - unlit: corresponding step off, depending on context
    - blinking_during_playback: current step
    - startup_count: approximate battery level
    - step_1_blinking_before_power_off: battery completely depleted
  current_state: unavailable_from_static_sources

step_buttons_1_to_8:
  node_id: step_buttons_1_to_8
  role: button_set
  name: STEP buttons 1–8
  physical_type: row_of_buttons
  description: Turn sequencer steps on or off; also act as global menu setting buttons.
  children:
    - step_button_1
    - step_button_2
    - step_button_3
    - step_button_4
    - step_button_5
    - step_button_6
    - step_button_7
    - step_button_8

step_button_1:
  role: button
  name: STEP button 1
  global_menu_assignment: Auto power-off

step_button_2:
  role: button
  name: STEP button 2
  global_menu_assignment: Battery type selection

step_button_3:
  role: button
  name: STEP button 3
  global_menu_assignment: SYNC OUT polarity

step_button_4:
  role: button
  name: STEP button 4
  global_menu_assignment: SYNC IN polarity

step_button_5:
  role: button
  name: STEP button 5
  global_menu_assignment: Sequence settings at start-up

step_button_6:
  role: button
  name: STEP button 6
  global_menu_assignment: Drum preview

step_button_7:
  role: button
  name: STEP button 7
  global_menu_assignment: TEMPO knob range

step_button_8:
  role: button
  name: STEP button 8
  global_menu_assignment: no documented global assignment in English manual table

rhythm_group:
  node_id: rhythm_group
  role: group
  name: Drum sound generator sequence controls
  description: Controls the three analog drum parts and their sequence steps.
  children:
    - rhythm_knob
    - bd_part_button
    - sn_part_button
    - hh_part_button
    - step_buttons_1_to_8

rhythm_knob:
  node_id: rhythm_knob
  role: slider
  name: RHYTHM knob
  physical_type: rotary knob
  description: Adjusts the volume of the drum sound generator.
  safety_note: Manual instructs turning RHYTHM fully left before powering off.
  current_state: unavailable_from_static_sources

rear_connection_area:
  node_id: rear_connection_area
  role: region
  name: Connection area
  description: Rear-panel power, audio, sync, headphone, and grounding connections.
  source: manual connections section, page 8–9; visual index page 8
  map:
    approximate_position: rear_or_top_edge_connection_row
    tactile_summary: Jacks and power switch arranged as the connection area.
  children:
    - power_switch
    - dc_9v_jack
    - audio_in_jack
    - output_jack
    - headphones_jack
    - sync_out_jack
    - sync_in_jack
    - grounding_screw

power_switch:
  node_id: power_switch
  role: button
  name: Power switch
  physical_type: power switch/button
  description: Turns power on or off. Hold to turn power off.
  current_state: unavailable_from_static_sources

dc_9v_jack:
  node_id: dc_9v_jack
  role: port
  name: DC 9V jack
  physical_type: power jack
  description: Connects the optional AC adapter.
  safety_note: Turn off power before connecting the AC adapter; use only the specified adapter.
  current_state: cable_connection_unavailable_from_static_sources

audio_in_jack:
  node_id: audio_in_jack
  role: port
  name: AUDIO IN jack
  physical_type: 3.5 mm stereo mini-phone jack
  description: Accepts external audio, mixed with the VCO output and routed through VCF and VCA. Stereo input is mixed to mono.
  current_state: cable_connection_unavailable_from_static_sources

output_jack:
  node_id: output_jack
  role: port
  name: OUTPUT jack
  physical_type: 6.3 mm phone jack
  description: Monaural output to mixer or powered monitor speaker input; accepts mono or stereo unbalanced phone plugs.
  current_state: cable_connection_unavailable_from_static_sources

headphones_jack:
  node_id: headphones_jack
  role: port
  name: HEADPHONES jack
  physical_type: 3.5 mm stereo mini-phone jack
  description: Connects headphones.
  current_state: cable_connection_unavailable_from_static_sources

sync_out_jack:
  node_id: sync_out_jack
  role: port
  name: SYNC OUT jack
  physical_type: 3.5 mm monaural mini-phone jack
  description: Outputs a 5V, 15 ms pulse at the beginning of each step.
  possible_settings:
    - polarity set by Global menu step button 3
  current_state: cable_connection_unavailable_from_static_sources

sync_in_jack:
  node_id: sync_in_jack
  role: port
  name: SYNC IN jack
  physical_type: 3.5 mm monaural mini-phone jack
  description: When connected, internal step clock is ignored and sequencer advances according to incoming pulses.
  possible_settings:
    - polarity set by Global menu step button 4
  note: TEMPO knob is disabled when SYNC IN is connected.
  current_state: cable_connection_unavailable_from_static_sources

grounding_screw:
  node_id: grounding_screw
  role: port
  name: Grounding Screw
  physical_type: screw_terminal
  description: Used to ground the unit externally.
  safety_note: Do not use the unit if the screw is removed.
  current_state: unavailable_from_static_sources

global_menu_model:
  node_id: global_menu_model
  role: menu
  name: Global menu
  description: Hidden settings mode accessed at startup using ACTIVE STEP and GATE TIME.
  source: manual global menu, page 16
  entry_procedure:
    - Hold ACTIVE STEP and GATE TIME.
    - Turn power on.
    - Press the step button for the setting to change.
    - Press REC to save and start normally, or FLUX to cancel.
  safety_note: Never turn off power while data is being saved.
  children:
    - global_auto_power_off
    - global_battery_type
    - global_sync_out_polarity
    - global_sync_in_polarity
    - global_startup_sequence
    - global_drum_preview
    - global_tempo_range

global_auto_power_off:
  node_id: global_auto_power_off
  role: switch
  name: Auto power-off
  controlled_by: STEP button 1
  possible_states:
    - LED unlit: disabled
    - LED lit: enabled, factory default

global_battery_type:
  node_id: global_battery_type
  role: switch
  name: Battery type selection
  controlled_by: STEP button 2
  possible_states:
    - LED unlit: alkaline batteries, factory default
    - LED lit: nickel-metal hydride batteries

global_sync_out_polarity:
  node_id: global_sync_out_polarity
  role: switch
  name: SYNC OUT polarity
  controlled_by: STEP button 3
  possible_states:
    - LED unlit: output rises at beginning of each step, factory default
    - LED lit: output falls at beginning of each step

global_sync_in_polarity:
  node_id: global_sync_in_polarity
  role: switch
  name: SYNC IN polarity
  controlled_by: STEP button 4
  possible_states:
    - LED unlit: step advances when input rises, factory default
    - LED lit: step advances when input falls

global_startup_sequence:
  node_id: global_startup_sequence
  role: switch
  name: Sequence settings at start-up
  controlled_by: STEP button 5
  possible_states:
    - LED unlit: initial sequence loaded at power-on
    - LED blinking: saved sequence loaded at power-on
    - LED lit: demo sequence loaded at power-on, factory default

global_drum_preview:
  node_id: global_drum_preview
  role: switch
  name: Drum preview
  controlled_by: STEP button 6
  possible_states:
    - LED unlit: drum part buttons do not sound preview
    - LED lit: corresponding drum sound heard when pressing drum part button, factory default

global_tempo_range:
  node_id: global_tempo_range
  role: switch
  name: TEMPO knob range
  controlled_by: STEP button 7
  possible_states:
    - LED unlit: narrow tempo range
    - LED lit: wide tempo range, factory default

internal_sound_engine:
  node_id: internal_sound_engine
  role: region
  name: Internal sound engine
  description: Semantic signal-flow model, not a tactile surface area.
  source: manual block diagram, page 6; visual index page 6
  children:
    - synth_voice_path
    - drum_generator
    - sequencer_engine
    - sync_engine

synth_voice_path:
  node_id: synth_voice_path
  role: group
  name: Synth voice path
  description: VCO plus noise and external audio feed the VCF, then the VCA, then audio output.
  signal_flow:
    - VCO
    - NOISE generator
    - AUDIO IN mixed with VCO output
    - VCF
    - VCA
    - AUDIO OUT

drum_generator:
  node_id: drum_generator
  role: group
  name: Three-part drum sound generator
  description: Discrete analog drum generator with BD, SN, and HH parts.
  parts:
    - BD bass drum
    - SN snare drum
    - HH hi-hat

sequencer_engine:
  node_id: sequencer_engine
  role: group
  name: Eight-step sequencer
  description: Controls synth and drum parts using step, transport, and recording controls.

sync_engine:
  node_id: sync_engine
  role: group
  name: Sync engine
  description: Sends and receives step clock pulses through SYNC OUT and SYNC IN.

[Trace]
Sources used: monotribe_manual.pdf; monotribe_manual_visual_index.json; static panel photo foto_pannello; 01_surface_aria_store.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 04_routing_and_uncertainty_policy.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 15%; Surface Model/Map Schema 12%; Interaction Guidance Store 4%; Mode Policy Store 2%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: Official control names/functions come from the manual, while roles and static mapping follow the provided schema and ARIA store.
Unsupported-current-state risk: Low.
[/Trace]