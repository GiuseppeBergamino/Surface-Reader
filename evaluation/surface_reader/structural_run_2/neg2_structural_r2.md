Prompt: Create a structured description of the distortion mode.

Respose: 

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
