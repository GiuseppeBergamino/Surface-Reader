Prompt: Create a structured description of the headphones out.

Response: 

HEADPHONES jack — structured description

Official name: HEADPHONES jack

Surface role: port

Physical type: 3.5 mm stereo mini-phone jack

Region: connection area / rear-panel jacks

Purpose: Connect stereo headphones to monitor the monotribe directly. The manual states: “Connect your headphones (stereo mini-plug) here.”

Connector specification: ø3.5 mm stereo mini-phone jack

Input/output direction: audio output to headphones

Current-state note: I cannot determine from the manual or static panel references whether headphones are currently plugged in, whether audio is present, or what the headphone volume level is.

Non-visual location guidance:
From the performer’s perspective, treat this as part of the rear connection row, not the top control surface. It sits among the rear-panel jacks near the OUTPUT, SYNC, AUDIO IN, DC power, and power switch connections. Use the row of physical sockets as the tactile landmark; the HEADPHONES jack is a small mini-jack rather than a large quarter-inch output jack.

Safety / use note:
Before connecting headphones or powering on connected audio equipment, lower the monotribe’s LEVEL knob and RHYTHM knob to avoid unexpectedly loud sound. The manual also warns to turn off power before making connections because careless use may damage speakers or cause malfunctions.

node_id: port.headphones
name: HEADPHONES jack
role: port
physical_type: 3.5 mm stereo mini-phone jack
region: connection area
group: rear-panel audio connections
direction: output
function: Connect stereo headphones for direct monitoring.
connector: ø3.5 mm stereo mini-phone jack
nearby_elements:
  - OUTPUT jack
  - SYNC OUT jack
  - SYNC IN jack
  - AUDIO IN jack
  - DC 9V jack
current_state: unknown; requires situated evidence
source:
  - monotribe_manual.pdf, English manual, Connections section, page 8
  - monotribe_manual.pdf, Specifications section, page 17

[Trace]
Sources used: monotribe_manual.pdf pages 8 and 17; monotribe_manual_visual_index.json entry for page 8; 01_surface_aria_store.md; 02_interaction_guidance_store.md; 05_surface_model_map_schema.md; 04_routing_and_uncertainty_policy.md.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 15%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Routing/Uncertainty Policy 5%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names the HEADPHONES jack, its use, and its connector type; layout is supported by the rear-panel connection diagram.
Unsupported-current-state risk: Low.
[/Trace]
