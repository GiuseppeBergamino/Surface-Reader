Prompt ID: p2

Prompt: Which port should I use for headphones? Describe where it is and what it does.

# Surface Reader:
## R1:
Use the HEADPHONES jack. The manual says to connect headphones with a stereo mini-plug there.

From the performer’s perspective, it is in the connection row along the top/rear edge of the monotribe. In that row, the HEADPHONES jack is the fifth connection from the left:

Power switch
DC 9V
AUDIO IN
OUTPUT
HEADPHONES
SYNC OUT
SYNC IN

Tactilely, find the row of jacks along the back edge. The headphones port is a small 3.5 mm stereo mini jack, immediately to the right of the larger OUTPUT jack and immediately to the left of SYNC OUT.

What it does: it sends the monotribe’s audio to headphones for private listening. Use the LEVEL knob for synth volume and RHYTHM knob for drum volume.

[Trace]
Sources used: monotribe_manual.pdf, page 8 connections; monotribe_manual_visual_index.json page 8 entry; Surface ARIA Store; Surface Model/Map Schema; Interaction Guidance Store; Mode Policy Store.
Routing weights: Device manual 45%, Visual/static layout 25%, Surface ARIA Store 10%, Surface Model/Map Schema 10%, Interaction Guidance Store 5%, Mode Policy Store 5%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names the HEADPHONES jack and the connection diagram provides its order in the rear connection row.
Unsupported-current-state risk: Low.
[/Trace]

## R2:
Use the HEADPHONES jack. The manual says it is for headphones with a stereo mini-plug.

From the performer’s perspective, it is on the rear connection edge, in the row of jacks. In the manual’s connection diagram, it is jack 5: immediately to the right of the OUTPUT jack and to the left of SYNC OUT.

What it does: it sends the monotribe’s sound to your headphones, so you can listen privately without using the built-in speaker or external monitor speakers. It is separate from the larger OUTPUT jack, which is meant for a mixer or powered speakers.

Tactile cue: along the back edge, feel for the small 3.5 mm mini-jacks. The headphones port is the mini-jack just after the larger output jack, before the sync jacks.

[Trace]
Sources used: monotribe_manual.pdf p.8 Connections; monotribe_manual_visual_index.json entry for p.8; static panel/photo reference available for rear/panel orientation; Interaction Guidance Store; Mode Policy Store; Surface ARIA Store; Surface Model/Map Schema; Routing/Uncertainty Policy.
Routing weights: Device manual 45%; Visual/static layout 25%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names the HEADPHONES jack and the connection diagram gives its order among rear-panel ports.
Unsupported-current-state risk: Low.
[/Trace]

## R3:
Use the HEADPHONES jack. It accepts headphones with a stereo mini-plug, which means a 3.5 mm stereo headphone plug. The manual lists it as item 5 in the connection section: “Connect your headphones (stereo mini-plug) here.”

From the performer’s perspective, find the row of connection ports along the top/back edge of the monotribe. Move left to right through the jack area:

Power switch, DC 9V, AUDIO IN, OUTPUT, HEADPHONES, SYNC OUT, SYNC IN.

So the headphone port is the small mini-jack just to the right of the larger OUTPUT jack and just to the left of SYNC OUT. Use it when you want to listen directly on headphones instead of using the built-in speaker or connecting the OUTPUT jack to speakers or a mixer.

The manual warns to turn off the power before connecting anything, because careless connection can damage speakers or cause malfunctions.

[Trace]
Sources used: monotribe_manual.pdf page 8; monotribe_manual_visual_index.json entry for page 8; static panel photo foto_pannello; 01_surface_aria_store.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 45%; Visual/static layout 25%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 5%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names the HEADPHONES jack and the connection diagram supports its position in the jack row.
Unsupported-current-state risk: Low.
[/Trace]

# Baseline:
## R1:
Use the HEADPHONES jack for headphones. It accepts a stereo mini-plug.

It is on the connector side of the monotribe, in the row of jacks shown in the manual’s connection diagram. In that row, it is port number 5, between the OUTPUT jack on its left and the SYNC OUT jack on its right.

What it does: it sends the monotribe’s sound to your headphones, so you can listen without using powered monitor speakers. The manual separately says the OUTPUT jack is for a mixer or powered monitor speakers, while the HEADPHONES jack is specifically for headphones.

[Trace]
Sources used: monotribe Owner’s manual, Connections page 8; static panel photo.
Routing weights: Device manual 90%; Visual/static layout 10%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names the HEADPHONES jack and its plug type.
Unsupported-current-state risk: None.
[/Trace]

## R2:
Use the HEADPHONES jack for headphones. It accepts a stereo mini-plug.

It is on the rear connection row, near the right side of the unit. In the manual’s connection diagram, the rear jacks are numbered left to right: power switch, DC 9V, AUDIO IN, OUTPUT, HEADPHONES, SYNC OUT, SYNC IN. So the headphones port is the fifth item from the left, between OUTPUT on its left and SYNC OUT on its right.

What it does: it sends the monotribe’s sound to your headphones for listening. The manual separately lists OUTPUT for mixer or powered speakers, so use HEADPHONES, not OUTPUT, when plugging in normal headphones.

[Trace]
Sources used: monotribe_manual.pdf, Connections page 8; static panel photo for rear-row spatial layout.
Routing weights: Device manual 80%; Visual/static layout 20%.
Evidence confidence: High.
Confidence rationale: The manual explicitly identifies “HEADPHONES jack” and says to connect headphones there.
Unsupported-current-state risk: None.
[/Trace]

## R3:
Use the HEADPHONES jack for headphones. It accepts a stereo mini-plug.

It is on the connector edge in the row of jacks, numbered 5 in the manual’s connection diagram. Moving across that connector row, it is to the right of the OUTPUT jack and to the left of the SYNC OUT jack.

What it does: it sends the monotribe’s audio to your headphones. The manual separately says the OUTPUT jack is for a mixer or powered monitor speakers, so for headphones use the dedicated HEADPHONES jack, not OUTPUT.

[Trace]
Sources used: monotribe_manual.pdf, Connections page 8; Specifications page 17.
Routing weights: Device manual 90%; Visual/static layout 10%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names the HEADPHONES jack and states “Connect your headphones (stereo mini-plug) here.”
Unsupported-current-state risk: None.
[/Trace]



