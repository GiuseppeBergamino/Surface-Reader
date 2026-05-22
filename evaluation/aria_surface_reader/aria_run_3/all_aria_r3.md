Prompt: Represent the whole instrument as Surface ARIA structure.

Response: 

I’ll build this as a static Surface ARIA model, not as a live state report. I’ll include regions, groups, controls, indicators, ports, possible states, and tactile map anchors.

Ragionato per 14s

Below is a static Surface ARIA representation of the Korg monotribe. It describes the instrument’s documented surface and possible states, not its current knob positions, switch positions, LED states, cable connections, or sounding state. Current-state fields are therefore marked as requiring situated evidence.

The mapping follows the Surface Model / Surface Map pipeline: manual extraction, static layout extraction, semantic typing, model construction, map construction, and non-visual guidance. The schema explicitly says the surface model represents controls, regions, indicators, displays, ports, functions, possible states, and current-state requirements, while the surface map represents physical layout and tactile navigation without inferring live state. Surface ARIA role assignment treats rotary knobs as slider, pressable controls as button, discrete-position controls as switch, LEDs as indicator, physical jacks as port, and the ribbon as keyboard.

surface_aria_model:
  node_id: monotribe
  role: instrument
  name: Korg monotribe Analog Ribbon Station
  description: >
    Analog ribbon station with analog synthesizer, three-part analog drum
    sound generator, eight-step sequencer, ribbon keyboard, external audio input,
    sync input/output, internal speaker, battery or optional AC adapter power.
  current_state: requires_situated_evidence
  source_grounding:
    manual_function: monotribe_manual.pdf
    visual_layout: monotribe_manual_p10.png, monotribe_manual_p13.png, foto_pannello.jpeg
    visual_index: monotribe_manual_visual_index.json
  children:

    - node_id: synthesis_region
      role: region
      name: Synthesizer section
      description: >
        Sound-generation control area for VCO, VCF, VCA, EG, LFO, and ribbon keyboard.
        The manual describes the synth sound generator as VCO → VCF → VCA, with EG and
        LFO modulation, and with the ribbon keyboard or sequence data producing synth notes.
      citation: ":contentReference[oaicite:2]{index=2}"
      spatial_map:
        approximate_position: main upper/top-panel control area
        landmarks:
          - rotary knob groups
          - small discrete selector switches
          - long ribbon keyboard along the lower part of the synthesizer area
        source: "manual page 10 panel overview via visual index :contentReference[oaicite:3]{index=3}"
      children:

        - node_id: vco_group
          role: group
          name: VCO
          description: >
            Oscillator/noise group. Generates sawtooth, triangle, or square waveform;
            mixes white noise and external audio input before the signal continues
            through the filter and amplifier.
          citation: ":contentReference[oaicite:4]{index=4}"
          children:
            - node_id: vco_octave
              role: switch
              name: OCTAVE selector
              physical_type: discrete selector, exact tactile form from static panel sources
              description: Specifies VCO pitch in octave steps.
              possible_states:
                type: documented_discrete_positions
                examples: includes 64' setting; full set should be read from panel/manual diagram
              current_state: requires_situated_evidence

            - node_id: vco_wave
              role: switch
              name: WAVE select switch
              physical_type: slide or discrete selector, confirmed as discrete panel control from static layout
              description: Selects VCO waveform.
              possible_states:
                - sawtooth wave
                - triangle wave
                - square wave
              current_state: requires_situated_evidence
              citation: ":contentReference[oaicite:5]{index=5}"

            - node_id: vco_noise
              role: slider
              name: NOISE knob
              physical_type: rotary knob
              description: Adjusts the level of white noise mixed with the VCO output.
              possible_states: continuous_range_not_numerically_documented
              current_state: requires_situated_evidence
              citation: ":contentReference[oaicite:6]{index=6}"

            - node_id: keyboard_range
              role: switch
              name: RANGE select switch
              physical_type: discrete selector
              description: Specifies the ribbon keyboard playing mode.
              possible_states:
                WIDE: continuous pitch, about six times NARROW range; OCTAVE selector ignored
                NARROW: continuous pitch according to printed ribbon keyboard
                KEY: chromatic stepped pitch according to printed ribbon keyboard
              current_state: requires_situated_evidence
              citation: ":contentReference[oaicite:7]{index=7}"

        - node_id: vcf_group
          role: group
          name: VCF
          description: >
            Filter group. Modifies timbre using a 12 dB/oct low-pass filter derived
            from the Korg MS-20 filter circuit.
          citation: ":contentReference[oaicite:8]{index=8}"
          spatial_map:
            tactile_anchor: vertical pair of rotary knobs
            relation: CUTOFF above PEAK, according to the schema’s example mapping pattern
            citation: ":contentReference[oaicite:9]{index=9}"
          children:
            - node_id: vcf_cutoff
              role: slider
              name: CUTOFF knob
              physical_type: rotary knob
              description: Adjusts VCF cutoff frequency; left darkens the sound, right brightens it.
              possible_states: continuous_range_not_numerically_documented
              current_state: requires_situated_evidence
              citation: ":contentReference[oaicite:10]{index=10}"

            - node_id: vcf_peak
              role: slider
              name: PEAK knob
              physical_type: rotary knob
              description: Adjusts VCF resonance, emphasizing the cutoff frequency.
              possible_states: continuous_range_not_numerically_documented
              current_state: requires_situated_evidence
              citation: ":contentReference[oaicite:11]{index=11}"

        - node_id: vca_eg_group
          role: group
          name: VCA and EG
          description: >
            Amplifier and envelope group. VCA varies volume; EG selects the envelope
            shape applied to the VCA.
          citation: ":contentReference[oaicite:12]{index=12}"
          children:
            - node_id: vca_level
              role: slider
              name: LEVEL knob
              physical_type: rotary knob
              description: Adjusts synth volume.
              possible_states: continuous_range_not_numerically_documented
              current_state: requires_situated_evidence

            - node_id: eg_select
              role: switch
              name: EG select switch
              physical_type: discrete selector
              description: Selects one of three modulation waveforms for the EG applied to the VCA.
              possible_states:
                DECAY: volume starts at maximum when note sounds, then decays
                GATE: volume remains at maximum while note is played
                ATTACK: volume rises when note sounds, then remains at maximum while note is played
              current_state: requires_situated_evidence
              citation: ":contentReference[oaicite:13]{index=13}"

        - node_id: lfo_group
          role: group
          name: LFO
          description: >
            Low Frequency Oscillator group. Applies cyclical modulation to pitch,
            filter cutoff, or both; 1SHOT mode can make the LFO behave like an EG.
          citation: ":contentReference[oaicite:14]{index=14}"
          children:
            - node_id: lfo_rate
              role: slider
              name: RATE knob
              physical_type: rotary knob
              description: Adjusts modulation speed; clockwise gives faster modulation.
              possible_states: continuous_range_not_numerically_documented
              current_state: requires_situated_evidence

            - node_id: lfo_intensity
              role: slider
              name: INT. knob
              physical_type: rotary knob
              description: Adjusts modulation intensity/depth; fully left applies no modulation.
              possible_states: continuous_range_not_numerically_documented
              current_state: requires_situated_evidence

            - node_id: lfo_target
              role: switch
              name: TARGET select switch
              physical_type: discrete selector
              description: Selects what the LFO modulates.
              possible_states:
                VCO: VCO pitch changes
                VCO+VCF: VCO pitch and VCF cutoff frequency change
                VCF: VCF cutoff frequency changes
              current_state: requires_situated_evidence
              citation: ":contentReference[oaicite:15]{index=15}"

            - node_id: lfo_mode
              role: switch
              name: MODE select switch
              physical_type: discrete selector
              description: Selects modulation rate range or 1SHOT behavior.
              possible_states:
                FAST: approximately 1 Hz to 5 kHz
                SLOW: approximately 0.05 Hz to 18 Hz
                1SHOT: first half-cycle applies when note begins, then LFO stops
              current_state: requires_situated_evidence
              citation: ":contentReference[oaicite:16]{index=16}"

            - node_id: lfo_wave
              role: switch
              name: WAVE select switch
              physical_type: discrete selector
              description: Selects LFO modulation waveform.
              possible_states:
                - sawtooth wave
                - triangle wave
                - square wave
              current_state: requires_situated_evidence

        - node_id: ribbon_keyboard
          role: keyboard
          name: Ribbon keyboard
          physical_type: ribbon touch surface
          description: Touch with a finger to play synth sounds.
          possible_states:
            touch_position: requires_situated_evidence
            pitch_behavior: determined by RANGE mode and OCTAVE setting where applicable
          current_state: requires_situated_evidence
          citation: ":contentReference[oaicite:17]{index=17}"
          spatial_map:
            approximate_position: lower performance area of top panel
            tactile_description: long horizontal ribbon strip; useful bottom-panel landmark

    - node_id: sequencer_region
      role: region
      name: Sequencer section
      description: >
        Eight-step sequencer controlling the synthesizer and drum sound generator.
        Includes part selection, active-step editing, playback, recording, gate time,
        tempo, rhythm volume, step buttons, and step/part/transport indicators.
      citation: ":contentReference[oaicite:18]{index=18}"
      spatial_map:
        approximate_position: right/lower top-panel sequencer control area
        landmarks:
          - row of eight step buttons
          - row or cluster of part buttons
          - transport controls
        source: "manual page 13 sequencer overview via visual index :contentReference[oaicite:19]{index=19}"
      children:

        - node_id: part_selection_group
          role: group
          name: Part selection
          children:
            - node_id: part_leds
              role: indicator
              name: PART LEDs
              physical_type: LEDs
              description: Light when a PART button selects a part; all four blink for low battery warning.
              possible_states:
                lit: selected part, if observed
                blinking_all_four: low battery warning, if observed
                unlit: not selected or inactive, depending on context
              current_state: requires_situated_evidence
              citation: ":contentReference[oaicite:20]{index=20}"

            - node_id: part_synth
              role: button
              name: SYNTH button
              physical_type: button
              description: Selects the SYNTH part for editing.
              possible_states:
                selected: indicated by SYNTH part LED, requires situated evidence
              current_state: requires_situated_evidence

            - node_id: part_bd
              role: button
              name: BD button
              physical_type: button
              description: Selects the BD bass drum part for editing.
              possible_states:
                selected: indicated by BD part LED, requires situated evidence
              current_state: requires_situated_evidence

            - node_id: part_sn
              role: button
              name: SN button
              physical_type: button
              description: Selects the SN snare drum part for editing.
              possible_states:
                selected: indicated by SN part LED, requires situated evidence
              current_state: requires_situated_evidence

            - node_id: part_hh
              role: button
              name: HH button
              physical_type: button
              description: Selects the HH hi-hat part for editing.
              possible_states:
                selected: indicated by HH part LED, requires situated evidence
              current_state: requires_situated_evidence

        - node_id: active_step_group
          role: group
          name: Active Step
          children:
            - node_id: active_step_button
              role: button
              name: ACTIVE STEP button
              physical_type: button
              description: >
                While held, enabled step LEDs light; hold it and press a step button
                to enable or disable that step. Disabled steps are skipped during playback
                and recording.
              possible_states:
                pressed: requires_situated_evidence
                step_enabled_or_disabled: indicated by step LEDs while held; requires situated evidence
              current_state: requires_situated_evidence

        - node_id: transport_group
          role: group
          name: Transport and recording
          children:
            - node_id: play_button
              role: button
              name: PLAY button
              physical_type: button
              description: Starts or stops the sequence; playback starts from the beginning.
              possible_states:
                playing: PLAY LED lit, requires situated evidence
                stopped: PLAY LED unlit, requires situated evidence
              current_state: requires_situated_evidence

            - node_id: play_led
              role: indicator
              name: PLAY LED
              physical_type: LED
              description: Lit during playback.
              possible_states:
                lit: playback
                unlit: not playback
              current_state: requires_situated_evidence

            - node_id: rec_button
              role: button
              name: REC button
              physical_type: button
              description: >
                During playback, enters record mode. While stopped, enters record-ready mode.
                Press again to exit. Also used to save a sequence when stopped and not producing sound.
              possible_states:
                recording: REC LED lit, requires situated evidence
                record_ready: REC LED blinking, requires situated evidence
                inactive: REC LED dark, requires situated evidence
              current_state: requires_situated_evidence

            - node_id: rec_led
              role: indicator
              name: REC LED
              physical_type: LED
              description: Lit in record mode; blinking in record-ready mode; dark when inactive.
              possible_states:
                lit: record mode
                blinking: record-ready mode or saving sequence context
                unlit: inactive or after save complete
              current_state: requires_situated_evidence

        - node_id: tempo_group
          role: group
          name: Tempo
          children:
            - node_id: tempo_knob
              role: slider
              name: TEMPO knob
              physical_type: rotary knob
              description: >
                Sets sequencer speed. Global menu can set NARROW 60–180 BPM or WIDE 10–600 BPM.
                Disabled when SYNC IN is connected.
              possible_states:
                value: continuous_position_requires_situated_evidence
                range_mode:
                  - NARROW
                  - WIDE
              current_state: requires_situated_evidence

        - node_id: synth_sequence_group
          role: group
          name: Synthesizer sequence controls
          children:
            - node_id: flux_button
              role: button
              name: FLUX button
              physical_type: button
              description: Turns FLUX mode on or off.
              possible_states:
                ON: synth part recorded and played back as continuous data
                OFF: one note plays back for each step
              current_state: requires_situated_evidence

            - node_id: gate_time_button
              role: button
              name: GATE TIME button
              physical_type: button
              description: >
                Hold it and use the ribbon keyboard during sequence playback to change
                synth-note gate time. Far left of ribbon is 1.4%; far right is 100%.
              possible_states:
                pressed: requires_situated_evidence
                gate_time_value: depends on ribbon touch position, requires situated evidence
              current_state: requires_situated_evidence
              citation: ":contentReference[oaicite:21]{index=21}"

        - node_id: step_sequence_group
          role: group
          name: Step sequence
          spatial_map:
            tactile_anchor: row of eight repeated step buttons
            tactile_description: repeated button row; strong landmark for sequencer navigation
          children:
            - node_id: step_leds
              role: indicator
              name: STEP LEDs
              physical_type: LEDs
              description: >
                Light or go dark with corresponding step buttons; blink during playback to
                indicate the current step. At startup they also indicate remaining battery power.
              possible_states:
                lit: step on or startup battery indication, context-dependent
                unlit: step off or lower battery indication, context-dependent
                blinking: current playback step, if observed
              current_state: requires_situated_evidence
              citation: ":contentReference[oaicite:22]{index=22}"

            - node_id: step_buttons_1_to_8
              role: group
              name: STEP buttons 1–8
              description: >
                Eight pressable step buttons. For synth sequence, each step can be on/off.
                For selected drum part BD, SN, or HH, each step can be on/off. Holding a part
                button while turning on a step places that drum sound halfway through the step,
                effectively providing 16 rhythm positions.
              citation: ":contentReference[oaicite:23]{index=23}"
              children:
                - { node_id: step_button_1, role: button, name: STEP button 1, physical_type: button, possible_states: [ON, OFF], current_state: requires_situated_evidence }
                - { node_id: step_button_2, role: button, name: STEP button 2, physical_type: button, possible_states: [ON, OFF], current_state: requires_situated_evidence }
                - { node_id: step_button_3, role: button, name: STEP button 3, physical_type: button, possible_states: [ON, OFF], current_state: requires_situated_evidence }
                - { node_id: step_button_4, role: button, name: STEP button 4, physical_type: button, possible_states: [ON, OFF], current_state: requires_situated_evidence }
                - { node_id: step_button_5, role: button, name: STEP button 5, physical_type: button, possible_states: [ON, OFF], current_state: requires_situated_evidence }
                - { node_id: step_button_6, role: button, name: STEP button 6, physical_type: button, possible_states: [ON, OFF], current_state: requires_situated_evidence }
                - { node_id: step_button_7, role: button, name: STEP button 7, physical_type: button, possible_states: [ON, OFF], current_state: requires_situated_evidence }
                - { node_id: step_button_8, role: button, name: STEP button 8, physical_type: button, possible_states: [ON, OFF], current_state: requires_situated_evidence }

        - node_id: drum_mix_group
          role: group
          name: Drum sound generator sequence controls
          children:
            - node_id: rhythm_knob
              role: slider
              name: RHYTHM knob
              physical_type: rotary knob
              description: Adjusts the volume of the drum sound generator.
              possible_states: continuous_range_not_numerically_documented
              current_state: requires_situated_evidence
              citation: ":contentReference[oaicite:24]{index=24}"

    - node_id: connection_region
      role: region
      name: Connections and power
      description: Rear/edge connection area for power, audio, headphones, sync, and grounding.
      citation: ":contentReference[oaicite:25]{index=25}"
      spatial_map:
        approximate_position: rear/upper edge connection row
        landmarks:
          - row of jacks along the edge
          - power switch at one end of the connection row
          - grounding screw
        source: "manual page 8 connection diagram via visual index :contentReference[oaicite:26]{index=26}"
      children:
        - node_id: power_switch
          role: button
          name: Power switch
          physical_type: power switch/button
          description: Turns power on/off; hold to turn power off.
          possible_states:
            on: requires_situated_evidence
            off: requires_situated_evidence
          current_state: requires_situated_evidence
          citation: ":contentReference[oaicite:27]{index=27}"

        - node_id: dc9v_jack
          role: port
          name: DC 9V jack
          physical_type: power jack
          description: Connect optional specified AC adapter.
          possible_states:
            connected: requires_situated_evidence
            disconnected: requires_situated_evidence
          safety_notes:
            - Turn off power before connecting the AC adapter.
            - Use only the specified AC adapter.
          citation: ":contentReference[oaicite:28]{index=28}"

        - node_id: audio_in_jack
          role: port
          name: AUDIO IN jack
          physical_type: 3.5 mm stereo mini-phone jack
          description: >
            External audio source is mixed with the VCO and sent through the VCF and VCA;
            stereo input is mixed to mono.
          possible_states:
            connected: requires_situated_evidence
            disconnected: requires_situated_evidence
          citation: ":contentReference[oaicite:29]{index=29}"

        - node_id: output_jack
          role: port
          name: OUTPUT jack
          physical_type: 6.3 mm phone jack
          description: >
            Monaural output to mixer or powered monitors; accepts mono or stereo unbalanced plugs.
          possible_states:
            connected: requires_situated_evidence
            disconnected: requires_situated_evidence
          citation: ":contentReference[oaicite:30]{index=30}"

        - node_id: headphones_jack
          role: port
          name: HEADPHONES jack
          physical_type: 3.5 mm stereo mini-phone jack
          description: Connect stereo mini-plug headphones.
          possible_states:
            connected: requires_situated_evidence
            disconnected: requires_situated_evidence
          citation: ":contentReference[oaicite:31]{index=31}"

        - node_id: sync_out_jack
          role: port
          name: SYNC OUT jack
          physical_type: 3.5 mm monaural mini-phone jack
          description: Outputs 5 V, 15 ms pulse at the beginning of each step.
          possible_states:
            polarity:
              - rise at beginning of each step
              - fall at beginning of each step
            connected: requires_situated_evidence
          citation: ":contentReference[oaicite:32]{index=32}"

        - node_id: sync_in_jack
          role: port
          name: SYNC IN jack
          physical_type: 3.5 mm monaural mini-phone jack
          description: >
            When connected, internal step clock is ignored and sequencer steps follow incoming pulses.
          possible_states:
            polarity:
              - advance when input signal rises
              - advance when input signal falls
            connected: requires_situated_evidence
          current_state: requires_situated_evidence
          citation: ":contentReference[oaicite:33]{index=33}"

        - node_id: grounding_screw
          role: port
          name: Grounding Screw
          physical_type: grounding screw
          description: Used to ground the unit by attaching a grounding wire.
          possible_states:
            grounded: requires_situated_evidence
            not_grounded: requires_situated_evidence
          safety_notes:
            - Do not use the unit if the screw is removed.
          citation: ":contentReference[oaicite:34]{index=34}"

    - node_id: global_menu_region
      role: region
      name: Global menu
      description: >
        Settings mode using step buttons 1–7. Enter by holding ACTIVE STEP and GATE TIME
        while turning power on. Save with REC; cancel with FLUX.
      citation: ":contentReference[oaicite:35]{index=35}"
      current_state: requires_situated_evidence
      children:
        - node_id: global_step_1_auto_power_off
          role: switch
          name: Step button 1 — Auto power-off
          physical_type: step button plus LED state
          possible_states:
            LED_unlit: auto power-off disabled
            LED_lit: auto power-off enabled, factory default
          current_state: requires_situated_evidence

        - node_id: global_step_2_battery_type
          role: switch
          name: Step button 2 — Battery type selection
          possible_states:
            LED_unlit: alkaline batteries, factory default
            LED_lit: nickel-metal hydride batteries
          current_state: requires_situated_evidence

        - node_id: global_step_3_sync_out_polarity
          role: switch
          name: Step button 3 — SYNC OUT polarity
          possible_states:
            LED_unlit: output rises at beginning of each step, factory default
            LED_lit: output falls at beginning of each step
          current_state: requires_situated_evidence

        - node_id: global_step_4_sync_in_polarity
          role: switch
          name: Step button 4 — SYNC IN polarity
          possible_states:
            LED_unlit: step advances when input signal rises, factory default
            LED_lit: step advances when input signal falls
          current_state: requires_situated_evidence

        - node_id: global_step_5_startup_sequence
          role: switch
          name: Step button 5 — Sequence settings at start-up
          possible_states:
            LED_unlit: initial sequence loaded at power-on
            LED_blinking: saved sequence loaded at power-on
            LED_lit: demo sequence loaded at power-on, factory default
          current_state: requires_situated_evidence

        - node_id: global_step_6_drum_preview
          role: switch
          name: Step button 6 — Drum preview
          possible_states:
            LED_unlit: drum part buttons do not preview sound
            LED_lit: corresponding drum sound is heard when drum part button is pressed, factory default
          current_state: requires_situated_evidence

        - node_id: global_step_7_tempo_range
          role: switch
          name: Step button 7 — TEMPO knob range
          possible_states:
            LED_unlit: TEMPO range narrow
            LED_lit: TEMPO range wide, factory default
          current_state: requires_situated_evidence

    - node_id: power_battery_region
      role: region
      name: Battery and power status
      description: Battery compartment and battery indication behavior.
      children:
        - node_id: battery_compartment
          role: region
          name: Battery compartment
          physical_type: compartment under/rear side
          description: Holds six AA alkaline or nickel-metal hydride batteries.
          safety_notes:
            - Turn off power before replacing batteries.
            - Remove depleted batteries immediately.
            - Do not mix partially used and new batteries.
            - Do not mix battery types.
          citation: ":contentReference[oaicite:36]{index=36}"

        - node_id: startup_battery_indicator
          role: indicator
          name: Step LEDs as battery level indicator
          physical_type: STEP LEDs
          description: At startup, more lit step LEDs mean more remaining battery power.
          possible_states:
            all_step_leds_lit: batteries full
            fewer_step_leds_lit: lower battery level
            inaccurate_when_ac_adapter_connected: documented limitation
          current_state: requires_situated_evidence
          citation: ":contentReference[oaicite:37]{index=37}"

        - node_id: low_battery_warning
          role: indicator
          name: Low battery warning
          physical_type: PART LEDs and Step 1 LED
          description: Four part LEDs blink simultaneously when batteries run low; Step 1 LED blinks before automatic power-off when batteries run down completely.
          current_state: requires_situated_evidence
          citation: ":contentReference[oaicite:38]{index=38}"

Static tactile map summary: from the performer’s perspective, treat the monotribe as four main navigable zones. The upper/main control field is the synthesizer section: VCO/noise/range, filter pair, VCA/EG, and LFO. The long ribbon keyboard is a strong lower-panel landmark. The sequencer is anchored by the repeated row of eight step buttons and associated LEDs. The rear/upper edge is the connection row: power, DC 9V, AUDIO IN, OUTPUT, HEADPHONES, SYNC OUT, SYNC IN, plus the grounding screw. The static panel diagram and visual index identify the synthesizer page, sequencer page, and connection diagram as the layout sources.

[Trace]
Sources used: monotribe_manual.pdf pages 6–16; monotribe_manual_visual_index.json entries for pages 6, 8, 10, 13, 14, 15, 16; foto_pannello.jpeg; 01_surface_aria_store.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 20%; Surface Model/Map Schema 15%.
Evidence confidence: High.
Confidence rationale: Official names/functions and possible states come from the manual; roles and current-state limits come from the Surface ARIA and schema stores; physical layout is static, not live.
Unsupported-current-state risk: Low.
[/Trace]