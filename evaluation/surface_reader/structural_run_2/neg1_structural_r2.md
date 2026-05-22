Prompt: Create a structured description of the delay time.

Respose: 

Structured description: “Delay Time”

Device: Korg monotribe
Control/entity status: No dedicated Delay Time control is documented in the monotribe owner’s manual. The monotribe manual describes VCO, VCF, VCA, LFO, EG, sequencer, rhythm, sync, and global settings, but not an audio delay effect or a delay-time parameter.

Surface model entry
name: Delay Time
documented_on_monotribe: false
role: unsupported / not present in documented surface model
physical_type: none documented
region: none documented
group: none documented
function: not applicable
possible_values: none documented
current_state: unavailable
Non-visual guidance

Do not look for a Delay Time knob, switch, button, or menu item on the monotribe itself. If you are hearing repeats or echoes, that is likely coming from external equipment, a mixer, a pedal, a DAW effect, or another connected device—not from a documented monotribe delay parameter.

Related documented controls that might be confused with delay

The closest time-related controls on the monotribe are:

TEMPO knob:
  role: slider
  physical_type: rotary knob
  region: Sequencer section
  function: Sets sequencer speed.
  delay_related: false

LFO RATE knob:
  role: slider
  physical_type: rotary knob
  region: Synthesizer section / LFO group
  function: Adjusts modulation speed.
  delay_related: false

GATE TIME button:
  role: button
  physical_type: button
  region: Sequencer section
  function: Used with the ribbon keyboard to change synth note duration in the sequence.
  delay_related: false

[Trace]
Sources used: monotribe_manual.pdf, manual page uncertain; 04_routing_and_uncertainty_policy.md; 01_surface_aria_store.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 55%; Routing/Uncertainty Policy 15%; Surface ARIA Store 15%; Surface Model/Map Schema 15%.
Evidence confidence: Medium.
Confidence rationale: The available manual text lists documented controls and functions but contains no Delay Time parameter in the shown English section.
Unsupported-current-state risk: Low.
[/Trace]