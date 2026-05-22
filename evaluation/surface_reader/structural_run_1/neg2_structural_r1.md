Prompt: Create a structured description of the distortion mode.

Respose: 

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