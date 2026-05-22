Prompt: Create a structured description of the distortion mode.

Respose: 

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
