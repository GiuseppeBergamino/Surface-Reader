Prompt ID: p1

Prompt: Which port should I use to connect an external audio source? Describe where it is and what it does.

# Surface Reader:
## R1:
Use the AUDIO IN jack for an external audio source. It is a 3.5 mm stereo mini-phone input. The manual says audio connected there is mixed with the VCO, then sent through the VCF and VCA, so you can process an external source through the monotribe’s filter/amplifier path or use the monotribe as an effect processor. A stereo input is summed to mono.

From the performer’s perspective, it is in the rear connection row along the top edge, among the jacks. In the manual’s connection diagram it is item 3, positioned after the power/DC area and before the main OUTPUT jack. Use the row of rear ports as your landmark: the AUDIO IN is one of the small mini-jacks in that top-edge connection group, not the larger quarter-inch OUTPUT jack.

Turn the monotribe and connected gear off before cabling; the manual warns that careless connection may damage speakers or cause malfunction.

[Trace]
Sources used: monotribe_manual.pdf p.8 connections; monotribe_manual_visual_index.json entry for p.8; Surface ARIA Store; Surface Model/Map Schema; Interaction Guidance Store; Mode Policy Store.
Routing weights: Device manual 55%; Visual/static layout 20%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 0%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names the AUDIO IN jack, describes its function, and the connection diagram supports its rear-panel location.
Unsupported-current-state risk: Low.
[/Trace]

## R2:
Use the AUDIO IN jack for an external audio source.

From the performer’s perspective, it is on the rear connection edge, in the row of connectors. In the manual’s rear-panel connection diagram it is connector 3, between the DC 9V jack and the OUTPUT jack.

What it does: audio plugged into AUDIO IN is mixed with the monotribe’s VCO, then sent through the VCF filter and VCA amplifier. That means you can run another sound source through the monotribe to color it with the synth/filter path, or use the monotribe as an effect processor. A stereo input is mixed down to mono.

Tactile cue: start along the rear edge where the cable jacks are. Find the power adapter jack first if it is present; the AUDIO IN mini-jack is immediately to its right, before the larger OUTPUT jack.

[Trace]
Sources used: monotribe_manual.pdf page 8; monotribe_manual_visual_index.json entry for page 8; Surface ARIA Store; Surface Model/Map Schema; Interaction Guidance Store; Mode Policy Store; Routing/Uncertainty Policy.
Routing weights: Device manual 45%; Visual/static layout 25%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names AUDIO IN and describes its function; the connection diagram supports the rear-panel location.
Unsupported-current-state risk: Low.
[/Trace]

## R3:
Use the AUDIO IN jack. It is the port for connecting an external audio source. The manual says audio connected there is mixed with the VCO, then sent through the VCF filter and VCA amp, so you can process the external sound through the monotribe or use it as an effect processor. A stereo input is mixed down to mono.

From the performer’s perspective, the connection ports are along the top edge / rear edge of the monotribe. The AUDIO IN jack is a small 3.5 mm mini-jack in that rear connection row. In the manual’s connection diagram it is item 3, between the DC 9V jack and the OUTPUT jack. Use the top edge as your landmark: find the row of rear jacks, then locate the mini-jack just to the right of the power/adapter area and before the larger output jack.

Important: turn the monotribe and connected equipment off before making connections; the manual warns careless connection can damage speakers or cause malfunctions.

[Trace]
Sources used: monotribe_manual.pdf p.8 connections and p.11 VCO description; monotribe_manual_visual_index.json p.8 connection diagram entry; foto_pannello static panel photo; 01_surface_aria_store.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 45%; Visual/static layout 25%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 5%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names AUDIO IN and describes both its function and connection position.
Unsupported-current-state risk: Low.
[/Trace]


# Baseline:
## R1:
Use the AUDIO IN jack for an external audio source.

It is on the connector edge in the row of rear-panel ports. In the manual’s connection diagram, it is port 3, between the DC 9V jack on its left and the OUTPUT jack on its right.

What it does: audio plugged into AUDIO IN is mixed with the VCO, then sent through the VCF filter and VCA amp. The manual says this can expand the monotribe’s sound possibilities or let you use it as an effect processor for an external audio source. A stereo input signal is mixed to mono.

[Trace]
Sources used: monotribe manual p. 8 “Connections”; monotribe manual p. 11 “VCO”; static panel photo.
Routing weights: Device manual 85%; Visual/static layout 15%.
Evidence confidence: High.
Confidence rationale: The manual explicitly identifies AUDIO IN as the external audio input and describes its signal path.
Unsupported-current-state risk: None.
[/Trace]

## R2:
Use the AUDIO IN jack for an external audio source.

It is on the rear connection edge, in the row of jacks. In the manual’s connection diagram it is connector 3, between the DC 9V jack on its left and the OUTPUT jack on its right.

What it does: audio connected to AUDIO IN is mixed with the VCO, then sent through the VCF and VCA. This lets you process an external sound through the monotribe’s synth path, or use the monotribe as an effect processor for an external audio source. A stereo input signal is mixed to mono.

[Trace]
Sources used: monotribe_manual.pdf, Connections p.8; static panel photo.
Routing weights: Device manual 85%; Visual/static layout 15%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names AUDIO IN and explains its signal path and placement in the connector diagram.
Unsupported-current-state risk: None.
[/Trace]

## R3:
Use the AUDIO IN jack for an external audio source.

It is on the connection side of the monotribe, in the row of rear/edge connectors. In the manual’s connection diagram it is connector number 3, between the DC 9V jack on its left and the OUTPUT jack on its right.

What it does: an external audio source plugged into AUDIO IN is mixed with the VCO, then sent through the VCF and VCA. The manual says this can expand the monotribe’s sound possibilities or let you use the monotribe as an effect processor for a separate audio source. A stereo input signal is mixed down to mono.

[Trace]
Sources used: monotribe_manual.pdf, Connections p.8; Synthesizer section/VCO p.11.
Routing weights: Device manual 90%; Visual/static layout 10%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names AUDIO IN and describes its connection and signal path.
Unsupported-current-state risk: None.
[/Trace]


