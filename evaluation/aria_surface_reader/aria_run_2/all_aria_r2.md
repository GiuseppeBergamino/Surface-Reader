Prompt: Represent the whole instrument as Surface ARIA structure.

Response: 

I’ll build this as a static Surface ARIA model, not a live state report: controls, possible states, hierarchy, and tactile layout, with current states left unknown unless observed.

Ragionato per 21s

Below is a static Surface ARIA representation of the Korg monotribe. It uses the manual for official names/functions and possible states, and static layout sources for regions/control grouping. It does not report current knob values, switch positions, LEDs, cables, or sequence content. The model follows the Surface Model rule that a surface model represents controls, roles, possible states, and hierarchy, while current state requires situated evidence. Surface ARIA roles are assigned according to the store rules: knobs as slider, pressable controls as button, discrete selectors as switch, LEDs as indicator, ribbon as keyboard, and jacks as port.

{
  "node_id": "korg_monotribe",
  "role": "instrument",
  "name": "Korg monotribe analogue ribbon station",
  "description": "Analog synthesizer with VCO, VCF, VCA, EG, LFO, ribbon keyboard, three-part analog drum generator, eight-step sequencer, sync I/O, audio I/O, internal speaker, and battery or AC power.",
  "current_state": "requires situated evidence",
  "children": [
    {
      "node_id": "top_panel",
      "role": "region",
      "name": "Top panel",
      "spatial_description": "Main playing and editing surface, described from the performer's perspective: top is farthest away, bottom is closest.",
      "children": [
        {
          "node_id": "synthesizer_section",
          "role": "region",
          "name": "Synthesizer section",
          "description": "Controls the analog synth sound generator: VCO pitch/source, VCF timbre, VCA volume/envelope, LFO modulation, and ribbon keyboard.",
          "source": "Manual pp.10-13; panel overview screenshot p.10; static panel photo",
          "children": [
            {
              "node_id": "vco_group",
              "role": "group",
              "name": "VCO",
              "description": "Voltage Controlled Oscillator group. Generates the waveform that forms the basis of the synth sound; external AUDIO IN is mixed with the VCO output when connected.",
              "children": [
                {
                  "node_id": "octave_selector",
                  "role": "switch",
                  "name": "OCTAVE selector",
                  "physical_type": "discrete selector",
                  "description": "Specifies VCO pitch in octave steps.",
                  "possible_values": ["documented octave positions including 64'"],
                  "current_state": "requires situated evidence"
                },
                {
                  "node_id": "vco_wave_select",
                  "role": "switch",
                  "name": "WAVE select switch",
                  "physical_type": "multi-position switch",
                  "description": "Selects the VCO waveform.",
                  "possible_values": ["sawtooth wave", "triangle wave", "square wave"],
                  "current_state": "requires situated evidence"
                },
                {
                  "node_id": "noise_knob",
                  "role": "slider",
                  "name": "NOISE knob",
                  "physical_type": "rotary knob",
                  "description": "Adjusts the level of white noise mixed with the VCO output.",
                  "possible_states": "continuous value",
                  "current_state": "requires situated evidence"
                },
                {
                  "node_id": "range_select",
                  "role": "switch",
                  "name": "RANGE select switch",
                  "physical_type": "multi-position switch",
                  "description": "Specifies the ribbon keyboard playing mode.",
                  "possible_values": [
                    {
                      "name": "WIDE",
                      "meaning": "Pitch range is extended to approximately six times NARROW; pitch change is continuous; OCTAVE selector is ignored."
                    },
                    {
                      "name": "NARROW",
                      "meaning": "Pitch changes continuously according to the printed ribbon keyboard."
                    },
                    {
                      "name": "KEY",
                      "meaning": "Pitch changes in chromatic steps according to the printed ribbon keyboard."
                    }
                  ],
                  "current_state": "requires situated evidence"
                }
              ]
            },
            {
              "node_id": "vcf_group",
              "role": "group",
              "name": "VCF",
              "description": "Voltage Controlled Filter group. Low-pass filter that modifies timbre by boosting or cutting frequency regions; based on the Korg MS-20 filter circuit.",
              "children": [
                {
                  "node_id": "cutoff_knob",
                  "role": "slider",
                  "name": "CUTOFF knob",
                  "physical_type": "rotary knob",
                  "description": "Adjusts the VCF cutoff frequency; left darkens the sound, right brightens it.",
                  "possible_states": "continuous value",
                  "current_state": "requires situated evidence",
                  "spatial_properties": {
                    "tactile_description": "upper knob in the filter pair",
                    "near": ["PEAK knob"]
                  }
                },
                {
                  "node_id": "peak_knob",
                  "role": "slider",
                  "name": "PEAK knob",
                  "physical_type": "rotary knob",
                  "description": "Adjusts VCF resonance, emphasizing the cutoff frequency.",
                  "possible_states": "continuous value",
                  "current_state": "requires situated evidence",
                  "spatial_properties": {
                    "tactile_description": "lower knob in the filter pair",
                    "near": ["CUTOFF knob"]
                  }
                }
              ]
            },
            {
              "node_id": "vca_group",
              "role": "group",
              "name": "VCA",
              "description": "Voltage Controlled Amplifier group. Controls synth volume and envelope behaviour.",
              "children": [
                {
                  "node_id": "level_knob",
                  "role": "slider",
                  "name": "LEVEL knob",
                  "physical_type": "rotary knob",
                  "description": "Adjusts synth volume.",
                  "possible_states": "continuous value",
                  "current_state": "requires situated evidence"
                },
                {
                  "node_id": "eg_select",
                  "role": "switch",
                  "name": "EG select switch",
                  "physical_type": "multi-position switch",
                  "description": "Selects the envelope generator behaviour applied to the VCA.",
                  "possible_values": [
                    {
                      "name": "DECAY",
                      "meaning": "Volume starts at maximum when the note sounds, then decays."
                    },
                    {
                      "name": "GATE",
                      "meaning": "Volume remains at maximum while the note is played."
                    },
                    {
                      "name": "ATTACK",
                      "meaning": "Volume begins increasing when the note sounds and remains at maximum while the note is played."
                    }
                  ],
                  "current_state": "requires situated evidence"
                }
              ]
            },
            {
              "node_id": "lfo_group",
              "role": "group",
              "name": "LFO",
              "description": "Low Frequency Oscillator group. Applies cyclic or one-shot modulation to pitch and/or filter cutoff.",
              "children": [
                {
                  "node_id": "rate_knob",
                  "role": "slider",
                  "name": "RATE knob",
                  "physical_type": "rotary knob",
                  "description": "Adjusts modulation speed; turning right produces faster modulation.",
                  "possible_states": "continuous value",
                  "current_state": "requires situated evidence"
                },
                {
                  "node_id": "int_knob",
                  "role": "slider",
                  "name": "INT. knob",
                  "physical_type": "rotary knob",
                  "description": "Adjusts modulation intensity/depth; fully left applies no modulation.",
                  "possible_states": "continuous value",
                  "current_state": "requires situated evidence"
                },
                {
                  "node_id": "target_select",
                  "role": "switch",
                  "name": "TARGET select switch",
                  "physical_type": "multi-position switch",
                  "description": "Selects what the LFO modulates.",
                  "possible_values": [
                    {
                      "name": "VCO",
                      "meaning": "VCO pitch changes."
                    },
                    {
                      "name": "VCO+VCF",
                      "meaning": "VCO pitch and VCF cutoff frequency change."
                    },
                    {
                      "name": "VCF",
                      "meaning": "VCF cutoff frequency changes."
                    }
                  ],
                  "current_state": "requires situated evidence"
                },
                {
                  "node_id": "mode_select",
                  "role": "switch",
                  "name": "MODE select switch",
                  "physical_type": "multi-position switch",
                  "description": "Switches modulation-rate range or changes how modulation is applied.",
                  "possible_values": [
                    {
                      "name": "FAST",
                      "meaning": "Modulation rate approximately 1 Hz to 5 kHz."
                    },
                    {
                      "name": "SLOW",
                      "meaning": "Modulation rate approximately 0.05 Hz to 18 Hz."
                    },
                    {
                      "name": "1SHOT",
                      "meaning": "When the note begins, the first half-cycle of modulation is applied, then the LFO stops."
                    }
                  ],
                  "current_state": "requires situated evidence"
                },
                {
                  "node_id": "lfo_wave_select",
                  "role": "switch",
                  "name": "WAVE select switch",
                  "physical_type": "multi-position switch",
                  "description": "Selects the LFO modulation waveform.",
                  "possible_values": ["sawtooth wave", "triangle wave", "square wave"],
                  "current_state": "requires situated evidence"
                }
              ]
            },
            {
              "node_id": "ribbon_keyboard",
              "role": "keyboard",
              "name": "Ribbon keyboard",
              "physical_type": "ribbon touch surface",
              "description": "Playable touch surface for synth pitch; pitch behaviour depends on RANGE and OCTAVE settings.",
              "actions": ["touch", "slide", "hold"],
              "current_state": "requires situated evidence",
              "spatial_properties": {
                "landmark": "long horizontal tactile/performance surface on the lower part of the top panel"
              }
            }
          ]
        },
        {
          "node_id": "sequencer_section",
          "role": "region",
          "name": "Sequencer section",
          "description": "Eight-step sequencer controlling the synthesizer and drum sound generator.",
          "source": "Manual pp.13-15; panel overview screenshot p.13; static panel photo",
          "children": [
            {
              "node_id": "part_selection_group",
              "role": "group",
              "name": "Part selection",
              "description": "Selects which part is edited.",
              "children": [
                {
                  "node_id": "part_leds",
                  "role": "indicator",
                  "name": "PART LEDs",
                  "physical_type": "LEDs",
                  "description": "Indicate selected part; all four blink simultaneously when batteries run low.",
                  "possible_states": ["lit", "unlit", "blinking"],
                  "current_state": "requires situated evidence"
                },
                {
                  "node_id": "synth_part_button",
                  "role": "button",
                  "name": "SYNTH button",
                  "physical_type": "button",
                  "description": "Selects the SYNTH part for editing.",
                  "possible_states": ["pressed", "not pressed", "selected indicated by associated PART LED"],
                  "current_state": "requires situated evidence"
                },
                {
                  "node_id": "bd_part_button",
                  "role": "button",
                  "name": "BD button",
                  "physical_type": "button",
                  "description": "Selects the BD bass drum part for editing.",
                  "possible_states": ["pressed", "not pressed", "selected indicated by associated PART LED"],
                  "current_state": "requires situated evidence"
                },
                {
                  "node_id": "sn_part_button",
                  "role": "button",
                  "name": "SN button",
                  "physical_type": "button",
                  "description": "Selects the SN snare drum part for editing.",
                  "possible_states": ["pressed", "not pressed", "selected indicated by associated PART LED"],
                  "current_state": "requires situated evidence"
                },
                {
                  "node_id": "hh_part_button",
                  "role": "button",
                  "name": "HH button",
                  "physical_type": "button",
                  "description": "Selects the HH hi-hat part for editing.",
                  "possible_states": ["pressed", "not pressed", "selected indicated by associated PART LED"],
                  "current_state": "requires situated evidence"
                }
              ]
            },
            {
              "node_id": "transport_and_tempo_group",
              "role": "group",
              "name": "Transport and tempo",
              "description": "Playback control and sequence speed.",
              "children": [
                {
                  "node_id": "active_step_button",
                  "role": "button",
                  "name": "ACTIVE STEP button",
                  "physical_type": "button",
                  "description": "Used with step buttons to enable or disable each sequence step. Disabled steps are skipped during playback and recording.",
                  "actions": ["press", "hold while pressing a STEP button"],
                  "possible_states": ["pressed", "not pressed"],
                  "current_state": "requires situated evidence"
                },
                {
                  "node_id": "play_button",
                  "role": "button",
                  "name": "PLAY button",
                  "physical_type": "button",
                  "description": "Starts or stops the sequence; playback starts from the beginning.",
                  "possible_states": ["pressed", "not pressed"],
                  "current_state": "requires situated evidence"
                },
                {
                  "node_id": "play_led",
                  "role": "indicator",
                  "name": "PLAY LED",
                  "physical_type": "LED",
                  "description": "Lit during playback.",
                  "possible_states": ["lit", "unlit"],
                  "current_state": "requires situated evidence"
                },
                {
                  "node_id": "tempo_knob",
                  "role": "slider",
                  "name": "TEMPO knob",
                  "physical_type": "rotary knob",
                  "description": "Sets sequencer speed. The range is set in the Global menu; disabled when SYNC IN is connected.",
                  "possible_values": [
                    "NARROW global range: 60–180 BPM",
                    "WIDE global range: 10–600 BPM"
                  ],
                  "current_state": "requires situated evidence"
                }
              ]
            },
            {
              "node_id": "synth_sequence_group",
              "role": "group",
              "name": "Synthesizer sequence controls",
              "description": "Controls synth-part sequence recording, playback mode, and gate time.",
              "children": [
                {
                  "node_id": "flux_button",
                  "role": "button",
                  "name": "FLUX button",
                  "physical_type": "button",
                  "description": "Turns FLUX mode on or off.",
                  "possible_states": [
                    {
                      "name": "ON",
                      "meaning": "Synth sequence is recorded and played back as continuous data."
                    },
                    {
                      "name": "OFF",
                      "meaning": "One note plays back for each step."
                    }
                  ],
                  "current_state": "requires situated evidence"
                },
                {
                  "node_id": "rec_button",
                  "role": "button",
                  "name": "REC button",
                  "physical_type": "button",
                  "description": "Enters or exits record mode or record-ready mode; also used to save a sequence when stopped and not producing sound.",
                  "actions": ["press", "press again", "hold to save sequence when stopped"],
                  "current_state": "requires situated evidence"
                },
                {
                  "node_id": "rec_led",
                  "role": "indicator",
                  "name": "REC LED",
                  "physical_type": "LED",
                  "description": "Indicates recording state.",
                  "possible_states": [
                    {
                      "state": "lit",
                      "meaning": "Record mode during playback."
                    },
                    {
                      "state": "blinking",
                      "meaning": "Record-ready mode while stopped, or saving sequence until it stops blinking and goes dark."
                    },
                    {
                      "state": "unlit",
                      "meaning": "Not in record mode / save complete, depending on procedure context."
                    }
                  ],
                  "current_state": "requires situated evidence"
                },
                {
                  "node_id": "gate_time_button",
                  "role": "button",
                  "name": "GATE TIME button",
                  "physical_type": "button",
                  "description": "When held while using the ribbon keyboard during sequence playback, changes synth note gate time; in REC mode, records gate time per step.",
                  "actions": ["hold while touching ribbon keyboard"],
                  "possible_values": ["1.4% at far left of ribbon", "100% at far right of ribbon"],
                  "current_state": "requires situated evidence"
                }
              ]
            },
            {
              "node_id": "step_sequence_group",
              "role": "group",
              "name": "Step controls",
              "description": "Eight step buttons and associated step LEDs used for synth and drum step editing, active-step editing, battery indication at startup, and global menu settings.",
              "children": [
                {
                  "node_id": "step_leds",
                  "role": "indicator",
                  "name": "STEP LEDs",
                  "physical_type": "row of LEDs",
                  "description": "Indicate step on/off state and current playback step; at startup, indicate remaining battery power.",
                  "possible_states": [
                    "lit: corresponding step on, or enabled during Active Step hold, or battery-level indication at startup",
                    "unlit: corresponding step off, depending on mode",
                    "blinking: current playback step, or step 1 blinking before automatic power-off when batteries run down completely"
                  ],
                  "current_state": "requires situated evidence"
                },
                {
                  "node_id": "step_buttons_1_to_8",
                  "role": "group",
                  "name": "STEP buttons 1–8",
                  "description": "Eight pressable step buttons.",
                  "children": [
                    {
                      "node_id": "step_button_1",
                      "role": "button",
                      "name": "STEP button 1",
                      "physical_type": "button",
                      "description": "Turns step 1 on/off; also used for Global menu Auto power-off setting.",
                      "current_state": "requires situated evidence"
                    },
                    {
                      "node_id": "step_button_2",
                      "role": "button",
                      "name": "STEP button 2",
                      "physical_type": "button",
                      "description": "Turns step 2 on/off; also used for Global menu Battery type selection.",
                      "current_state": "requires situated evidence"
                    },
                    {
                      "node_id": "step_button_3",
                      "role": "button",
                      "name": "STEP button 3",
                      "physical_type": "button",
                      "description": "Turns step 3 on/off; also used for Global menu SYNC OUT polarity.",
                      "current_state": "requires situated evidence"
                    },
                    {
                      "node_id": "step_button_4",
                      "role": "button",
                      "name": "STEP button 4",
                      "physical_type": "button",
                      "description": "Turns step 4 on/off; also used for Global menu SYNC IN polarity.",
                      "current_state": "requires situated evidence"
                    },
                    {
                      "node_id": "step_button_5",
                      "role": "button",
                      "name": "STEP button 5",
                      "physical_type": "button",
                      "description": "Turns step 5 on/off; also used for Global menu Sequence settings at start-up.",
                      "current_state": "requires situated evidence"
                    },
                    {
                      "node_id": "step_button_6",
                      "role": "button",
                      "name": "STEP button 6",
                      "physical_type": "button",
                      "description": "Turns step 6 on/off; also used for Global menu Drum preview.",
                      "current_state": "requires situated evidence"
                    },
                    {
                      "node_id": "step_button_7",
                      "role": "button",
                      "name": "STEP button 7",
                      "physical_type": "button",
                      "description": "Turns step 7 on/off; also used for Global menu TEMPO knob range.",
                      "current_state": "requires situated evidence"
                    },
                    {
                      "node_id": "step_button_8",
                      "role": "button",
                      "name": "STEP button 8",
                      "physical_type": "button",
                      "description": "Turns step 8 on/off.",
                      "current_state": "requires situated evidence"
                    }
                  ]
                }
              ]
            },
            {
              "node_id": "drum_sequence_group",
              "role": "group",
              "name": "Drum sound generator sequence controls",
              "description": "Controls sequencing and volume of the three-part drum sound generator.",
              "children": [
                {
                  "node_id": "rhythm_knob",
                  "role": "slider",
                  "name": "RHYTHM knob",
                  "physical_type": "rotary knob",
                  "description": "Adjusts the volume of the drum sound generator.",
                  "possible_states": "continuous value",
                  "current_state": "requires situated evidence"
                },
                {
                  "node_id": "drum_step_editing",
                  "role": "group",
                  "name": "Drum step editing",
                  "description": "With BD, SN, or HH selected, STEP buttons turn steps of that drum part on/off. Holding a part button while turning on a step places the sound halfway through the step, effectively providing 16 rhythm positions.",
                  "children": ["bd_part_button", "sn_part_button", "hh_part_button", "step_buttons_1_to_8", "step_leds"]
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "node_id": "connection_area",
      "role": "region",
      "name": "Connection area",
      "description": "Power, audio, headphones, sync, and grounding connections.",
      "source": "Manual p.8 connection diagram; visual index p.8",
      "children": [
        {
          "node_id": "power_switch",
          "role": "button",
          "name": "Power switch",
          "physical_type": "press switch",
          "description": "Turns power on/off. To turn power off, press and hold.",
          "actions": ["press", "press and hold"],
          "current_state": "requires situated evidence"
        },
        {
          "node_id": "dc_9v_jack",
          "role": "port",
          "name": "DC 9V jack",
          "physical_type": "power jack",
          "description": "Connection for optional AC adapter.",
          "possible_states": ["connected", "not connected"],
          "current_state": "requires situated evidence",
          "safety_notes": ["Turn off power before connecting the AC adapter.", "Use only the specified AC adapter."]
        },
        {
          "node_id": "audio_in_jack",
          "role": "port",
          "name": "AUDIO IN jack",
          "physical_type": "3.5 mm stereo mini-phone jack",
          "description": "External audio source input; signal is mixed with the VCO output and sent through VCF and VCA. Stereo input is mixed to mono.",
          "possible_states": ["connected", "not connected"],
          "current_state": "requires situated evidence"
        },
        {
          "node_id": "output_jack",
          "role": "port",
          "name": "OUTPUT jack",
          "physical_type": "6.3 mm stereo phone jack, unbalanced",
          "description": "Main monaural output to mixer or powered monitor speakers; accepts mono or stereo phone plugs.",
          "possible_states": ["connected", "not connected"],
          "current_state": "requires situated evidence"
        },
        {
          "node_id": "headphones_jack",
          "role": "port",
          "name": "HEADPHONES jack",
          "physical_type": "3.5 mm stereo mini-phone jack",
          "description": "Headphone output.",
          "possible_states": ["connected", "not connected"],
          "current_state": "requires situated evidence"
        },
        {
          "node_id": "sync_out_jack",
          "role": "port",
          "name": "SYNC OUT jack",
          "physical_type": "3.5 mm monaural mini-phone jack",
          "description": "Outputs a 5 V pulse of 15 ms at the beginning of each step; polarity is set in the Global menu.",
          "possible_states": ["connected", "not connected"],
          "current_state": "requires situated evidence"
        },
        {
          "node_id": "sync_in_jack",
          "role": "port",
          "name": "SYNC IN jack",
          "physical_type": "3.5 mm monaural mini-phone jack",
          "description": "Receives sync pulses. If connected, the internal step clock is ignored and the sequencer advances according to incoming pulses; polarity is set in the Global menu.",
          "possible_states": ["connected", "not connected"],
          "current_state": "requires situated evidence"
        },
        {
          "node_id": "grounding_screw",
          "role": "port",
          "name": "Grounding Screw",
          "physical_type": "screw terminal",
          "description": "Used to ground the unit by attaching a grounding wire.",
          "possible_states": ["ground wire attached", "not attached"],
          "current_state": "requires situated evidence",
          "safety_notes": ["Do not use the unit if the screw is removed."]
        }
      ]
    },
    {
      "node_id": "power_and_battery_area",
      "role": "region",
      "name": "Power and battery area",
      "description": "Battery compartment, battery indication behaviour, and power-related settings.",
      "children": [
        {
          "node_id": "battery_compartment",
          "role": "group",
          "name": "Battery compartment",
          "physical_type": "rear-panel battery compartment",
          "description": "Holds six AA batteries, alkaline or nickel-metal hydride.",
          "possible_states": ["batteries installed", "batteries not installed", "battery type selected in Global menu"],
          "current_state": "requires situated evidence",
          "safety_notes": [
            "Turn off power before replacing batteries.",
            "Remove depleted batteries immediately.",
            "Do not mix partially used batteries with new batteries.",
            "Do not mix batteries of differing types."
          ]
        },
        {
          "node_id": "battery_level_indication",
          "role": "indicator_group",
          "name": "Battery level indication",
          "description": "At startup, the STEP LEDs indicate remaining battery power. During operation, the four PART LEDs blink simultaneously when batteries are running low; if batteries run down completely, STEP 1 LED blinks and power turns off automatically.",
          "children": ["step_leds", "part_leds"],
          "current_state": "requires situated evidence"
        }
      ]
    },
    {
      "node_id": "global_menu",
      "role": "region",
      "name": "Global menu",
      "description": "Configuration mode entered by holding ACTIVE STEP and GATE TIME while turning power on. Step buttons 1–7 select settings; their LEDs indicate values.",
      "source": "Manual p.16",
      "children": [
        {
          "node_id": "global_auto_power_off",
          "role": "switch",
          "name": "Auto power-off",
          "controlled_by": "STEP button 1",
          "indicator": "STEP 1 LED",
          "possible_values": [
            "LED unlit: Auto power-off disabled",
            "LED lit: Auto power-off enabled, factory default"
          ],
          "current_state": "requires situated evidence"
        },
        {
          "node_id": "global_battery_type",
          "role": "switch",
          "name": "Battery type selection",
          "controlled_by": "STEP button 2",
          "indicator": "STEP 2 LED",
          "possible_values": [
            "LED unlit: alkaline batteries, factory default",
            "LED lit: nickel-metal hydride batteries"
          ],
          "current_state": "requires situated evidence"
        },
        {
          "node_id": "global_sync_out_polarity",
          "role": "switch",
          "name": "SYNC OUT polarity",
          "controlled_by": "STEP button 3",
          "indicator": "STEP 3 LED",
          "possible_values": [
            "LED unlit: output rises at beginning of each step, factory default",
            "LED lit: output falls at beginning of each step"
          ],
          "current_state": "requires situated evidence"
        },
        {
          "node_id": "global_sync_in_polarity",
          "role": "switch",
          "name": "SYNC IN polarity",
          "controlled_by": "STEP button 4",
          "indicator": "STEP 4 LED",
          "possible_values": [
            "LED unlit: step advances when input signal rises, factory default",
            "LED lit: step advances when input signal falls"
          ],
          "current_state": "requires situated evidence"
        },
        {
          "node_id": "global_startup_sequence",
          "role": "switch",
          "name": "Sequence settings at start-up",
          "controlled_by": "STEP button 5",
          "indicator": "STEP 5 LED",
          "possible_values": [
            "LED unlit: initial sequence loaded at power-on",
            "LED blinking: saved sequence loaded at power-on",
            "LED lit: demo sequence loaded at power-on, factory default"
          ],
          "current_state": "requires situated evidence"
        },
        {
          "node_id": "global_drum_preview",
          "role": "switch",
          "name": "Drum preview",
          "controlled_by": "STEP button 6",
          "indicator": "STEP 6 LED",
          "possible_values": [
            "LED unlit: no sound when pressing drum part buttons",
            "LED lit: corresponding drum sound heard when pressing drum part buttons, factory default"
          ],
          "current_state": "requires situated evidence"
        },
        {
          "node_id": "global_tempo_range",
          "role": "switch",
          "name": "TEMPO knob range",
          "controlled_by": "STEP button 7",
          "indicator": "STEP 7 LED",
          "possible_values": [
            "LED unlit: TEMPO range narrow",
            "LED lit: TEMPO range wide, factory default"
          ],
          "current_state": "requires situated evidence"
        }
      ]
    },
    {
      "node_id": "audio_engine",
      "role": "region",
      "name": "Sound generator structure",
      "description": "Internal signal-flow model rather than a physical control group. Synth sound generator consists of VCO, VCF, and VCA; drum sound generator provides BD, SN, and HH; sequencer controls synth and drum playback.",
      "children": [
        {
          "node_id": "vco_engine",
          "role": "group",
          "name": "VCO engine",
          "controlled_by": ["OCTAVE selector", "WAVE select switch", "NOISE knob", "RANGE select switch", "Ribbon keyboard", "LFO"]
        },
        {
          "node_id": "vcf_engine",
          "role": "group",
          "name": "VCF engine",
          "controlled_by": ["CUTOFF knob", "PEAK knob", "LFO TARGET/MODE/WAVE/RATE/INT."]
        },
        {
          "node_id": "vca_engine",
          "role": "group",
          "name": "VCA engine",
          "controlled_by": ["LEVEL knob", "EG select switch"]
        },
        {
          "node_id": "drum_engine",
          "role": "group",
          "name": "3-part drums",
          "description": "Analog drum sound generator with BD, SN, and HH parts.",
          "controlled_by": ["BD button", "SN button", "HH button", "STEP buttons", "RHYTHM knob"]
        }
      ]
    }
  ],
  "global_current_state_rule": "All current control values, switch positions, LED states, cable connections, sequence contents, and sounding state require situated evidence and are not inferred from the manual, screenshots, or static panel photo."
}

Core grounding: the manual identifies the monotribe as an analog synth with VCO/VCF/VCA, ribbon keyboard, three-part drum generator, eight-step sequencer, LFO, external input, internal speaker, and battery/AC power. It documents the VCO, VCF, VCA, LFO, and ribbon controls in the synthesizer section. It documents sequencer controls such as ACTIVE STEP, PLAY, TEMPO, FLUX, REC, GATE TIME, STEP LEDs/buttons, and RHYTHM. It documents rear connections and their functions: DC 9V, AUDIO IN, OUTPUT, HEADPHONES, SYNC OUT, and SYNC IN. The visual index identifies the relevant layout pages for the block diagram, rear-panel connections, synthesizer panel, sequencer panel, and global menu.

[Trace]
Sources used: monotribe_manual.pdf pp.5–16; monotribe_manual_visual_index.json entries for pp.6, 8, 10, 13, 14, 15, 16; foto_pannello.jpeg static panel photo; 01_surface_aria_store.md; 03_mode_policy_store.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 20%; Surface Model/Map Schema 10%; Mode Policy Store 5%.
Evidence confidence: High.
Confidence rationale: Official control names and functions come from the manual; role mapping follows the Surface ARIA store; current-state claims are explicitly excluded.
Unsupported-current-state risk: Low.
[/Trace]