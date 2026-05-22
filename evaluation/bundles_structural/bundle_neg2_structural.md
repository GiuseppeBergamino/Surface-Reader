Prompt ID: neg2

Prompt: Create a structured description of the distortion mode.

# Surface Reader:
## R1:
Distortion mode — structured description

Official status: I do not find a documented “Distortion mode” in the monotribe owner’s manual. The manual describes the sound path as VCO → VCF → VCA, with noise, external audio input, EG, and LFO modulation, but it does not name a distortion mode or a distortion control.

Closest documented related feature: The AUDIO IN jack can mix an external audio source with the VCO, then route it through the VCF and VCA. The manual says this can expand the monotribe’s sonic possibilities or let the monotribe work as an effect processor for an external audio source.

Surface-model entry
{
  "node_id": "mode_distortion",
  "name": "Distortion mode",
  "status": "not documented in the available monotribe manual",
  "role": "unsupported_or_absent_mode",
  "region": "synthesizer / signal path",
  "documented_related_nodes": [
    "AUDIO IN jack",
    "VCO",
    "VCF",
    "VCA",
    "CUTOFF knob",
    "PEAK knob",
    "LEVEL knob"
  ],
  "possible_function": "No manual-grounded function can be assigned.",
  "current_state": "not available from static sources",
  "non_visual_note": "Do not look for a dedicated distortion switch or mode button based on the provided manual; none is documented."
}
Practical non-visual guidance

Treat “distortion mode” as unsupported unless you have another source, such as a firmware update note, modification guide, or user-created hack. On the stock manual-grounded monotribe, the closest sound-shaping path is: external audio or VCO sound enters the filter, then the amp. The CUTOFF, PEAK, and LEVEL controls may change brightness, resonance, and volume, but the manual does not define these as distortion.

[Trace]
Sources used: monotribe_manual.pdf pages 5–8/11 signal path and AUDIO IN descriptions; 04_routing_and_uncertainty_policy.md; 01_surface_aria_store.md; 05_surface_model_map_schema.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md.
Routing weights: Device manual 55%; Routing/Uncertainty Policy 20%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 3%; Mode Policy Store 2%.
Evidence confidence: Medium.
Confidence rationale: The manual search found no documented distortion mode, but absence is based on the provided manual rather than every possible firmware/mod source.
Unsupported-current-state risk: Low.
[/Trace]

## R2:
Structured description: “distortion mode”

The available monotribe owner’s manual does not document an official control, menu item, or operating state named Distortion mode. So this should not be represented as a confirmed monotribe mode unless another source or live evidence identifies it.

A safer structured representation is:

{
  "node_id": "unsupported_distortion_mode",
  "name": "Distortion mode",
  "role": "unsupported_or_unverified_feature",
  "device": "Korg monotribe",
  "status": "not documented in the available owner’s manual",
  "current_state": "unknown; static sources cannot determine whether any distortion-like condition is active",
  "related_documented_features": [
    {
      "name": "VCF / filter timbre shaping",
      "role": "group",
      "description": "The manual documents the VCF as changing timbre by boosting or cutting frequency regions. The CUTOFF knob changes brightness, and the PEAK knob adds resonance at the cutoff frequency."
    },
    {
      "name": "AUDIO IN as effect-processing path",
      "role": "port",
      "description": "External audio can be mixed with the VCO and passed through the VCF and VCA, allowing the monotribe to process an external source."
    },
    {
      "name": "LFO sound effects",
      "role": "group",
      "description": "The LFO can create modulation from subtle movement to sound effects, but the manual does not call this distortion."
    }
  ],
  "unsupported_inferences": [
    "Do not claim that the monotribe has a distortion mode based on the available manual alone.",
    "Do not infer distortion from knob positions, switch positions, LED states, or a static photo.",
    "Do not label high resonance, high level, external input processing, or modulation as distortion unless the source explicitly says so."
  ],
  "non_visual_guidance": {
    "summary": "Treat distortion as an auditory result, not a documented mode, unless confirmed by another source.",
    "verification_strategy": "Use listening: if the sound becomes rough, clipped, saturated, or overdriven, describe that as an observed sound quality, not as a confirmed device mode."
  }
}

Non-visually: think of this as an unverified sound character, not a surface control. The manual-grounded controls that could affect roughness or intensity are mainly the filter pair—CUTOFF and PEAK—and the external AUDIO IN path, but the manual does not name any of these “distortion mode.”

[Trace]
Sources used: monotribe_manual.pdf; 01_surface_aria_store.md; 04_routing_and_uncertainty_policy.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 55%; Routing/Uncertainty Policy 20%; Surface ARIA Store 15%; Surface Model/Map Schema 10%.
Evidence confidence: Medium.
Confidence rationale: The manual search did not surface a documented “distortion mode,” but related sound-shaping paths are documented.
Unsupported-current-state risk: High.
[/Trace]

## R3:
Structured description: Distortion mode

Status: No documented “Distortion mode” is present in the uploaded Korg monotribe owner’s manual. I should not invent a mode that the manual does not define.

What the manual does document instead

Related sound-shaping areas:

VCF / filter shaping
The monotribe uses a 12 dB/oct low-pass filter based on the Korg MS-20 filter circuit.
The CUTOFF knob changes brightness: left is darker, right is brighter.
The PEAK knob adds resonance/emphasis around the cutoff frequency.
External audio processing
Audio connected to AUDIO IN is mixed with the VCO, then sent through the VCF and VCA.
The manual says this can expand sonic possibilities or let the monotribe act as an effect processor for an external audio source.
LFO sound effects
The LFO can modulate VCO pitch and/or VCF cutoff.
Its wide RATE and INTENSITY range can create anything from subtle modulation to sound effects.
Surface-model representation
node_id: mode_distortion
name: Distortion mode
role: unsupported / not documented
region: not assigned
group: not assigned
physical_control: none documented
possible_states: none documented
current_state: unavailable
manual_status: not found in owner’s manual
Safe interpretation

Use “distortion mode” only as an unsupported user label, not as an official monotribe mode. For manual-grounded sound design, describe it instead as:

External audio or VCO signal → VCF filtering/resonance → VCA output

The closest documented controls for aggressive or distorted-like tone are CUTOFF, PEAK, LEVEL, NOISE, and possibly external audio through AUDIO IN, but the manual does not call this distortion.

[Trace]
Sources used: monotribe_manual.pdf pages 5–8, 11–12; 04_routing_and_uncertainty_policy.md; 01_surface_aria_store.md.
Routing weights: Device manual 65%; Routing/Uncertainty Policy 15%; Surface ARIA Store 20%.
Evidence confidence: Medium.
Confidence rationale: The manual search did not find an official distortion mode, but related sound-shaping functions are documented.
Unsupported-current-state risk: Low.
[/Trace]

# Baseline:
## R1:
The monotribe owner’s manual does not document a distortion mode as a named mode or switchable function. The manual describes analog synthesis using VCO, VCF, VCA, EG, and LFO, plus external audio input, but no official “distortion mode” entry appears in the documented controls, modes, or Global menu.

Structured description:

Name: Distortion mode
Manual status: Not documented.
Control location: No distortion control or distortion mode switch is documented.
How to enable it: No manual procedure is given.
Related but not identical documented features:
The AUDIO IN jack can mix an external audio source with the VCO and route it through the VCF and VCA, allowing the monotribe to be used as an effect processor. This is documented, but the manual does not call it distortion.
The VCF CUTOFF and PEAK controls change the sound’s timbre and resonance, but the manual describes these as filter controls, not distortion controls.
The LFO can create changes from subtle modulation to sound effects, but again this is not described as distortion mode.

So, based only on the manual and static panel source, “distortion mode” should be treated as unsupported or undocumented for the monotribe.

[Trace]
Sources used: monotribe_manual.pdf, English owner’s manual pages 5–6, 8, 10–12, 16; static panel photo not used.
Routing weights: Device manual 100%; Visual/static layout 0%.
Evidence confidence: High.
Confidence rationale: The manual documents the sound engine, input routing, filter, LFO, and Global menu, but contains no documented distortion mode.
Unsupported-current-state risk: None.
[/Trace]

## R2:
Direct answer: The monotribe manual does not document a “distortion mode.” It documents analog synthesis, the VCO/VCF/VCA signal path, LFO, EG, sequencer, and AUDIO IN processing, but no control, switch, menu item, or procedure named “distortion mode” appears in the manual.

Where it would be expected: There is no documented panel control or Global menu setting for distortion mode. The Global menu only lists settings such as auto power-off, battery type, SYNC polarity, startup sequence, drum preview, and TEMPO knob range.

Related documented feature: The manual says the AUDIO IN jack can mix an external audio source with the VCO, then send it through the VCF and VCA. It also says this can let the monotribe act as an effect processor for an external audio source. That is documented, but it is not described as distortion mode.

Limitation: I cannot describe steps for enabling distortion mode because the uploaded manual does not document such a mode.

[Trace]
Sources used: monotribe_manual.pdf, pages 5, 8, 16; manual panel description pages 10–13.
Routing weights: Device manual 100%; Visual/static layout 0%.
Evidence confidence: High.
Confidence rationale: The manual’s feature list, panel controls, connection section, and Global menu do not document a distortion mode.
Unsupported-current-state risk: None.
[/Trace]

## R3:
The monotribe manual does not document a “distortion mode” as a named mode, switch position, menu item, or procedure.

Structured description, based only on documented functions:

Name: Distortion mode
Manual status: Not documented.

Closest documented sound-shaping path:
The synth sound is generated by the VCO, then shaped by the VCF, then controlled in volume by the VCA. The manual describes the VCF as a low-pass filter whose settings can significantly change the character of the sound, with CUTOFF controlling brightness and PEAK adding resonance emphasis at the cutoff frequency.

External audio processing:
The manual says an external audio source connected to AUDIO IN is mixed with the VCO and sent through the VCF and VCA. It also says this can let the monotribe act as an effect processor for an external audio source. This is documented as external audio processing, not as a distortion mode.

Where relevant controls are:
On the top panel, the VCF controls are in the synthesizer section: CUTOFF and PEAK are in the middle area of that section, below the VCO controls and above/near the VCA and LFO controls. The AUDIO IN jack is on the rear connection row, listed as connector 3 in the manual’s connection diagram.

Unsupported items:
The manual does not document a distortion on/off control, distortion amount, distortion type, distortion LED, or distortion-specific saved setting.

[Trace]
Sources used: monotribe_manual.pdf, English manual pages 5–6, 8, 10–12; static panel photo for general top-panel layout.
Routing weights: Device manual 90%; Visual/static layout 10%.
Evidence confidence: High.
Confidence rationale: The manual documents synthesis, filtering, and audio input processing, but no named distortion mode.
Unsupported-current-state risk: None.
[/Trace]


