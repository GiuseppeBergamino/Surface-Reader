
# Knowledge File List
This document describes the knowledge sources used by the Surface Reader Custom GPT.

The configuration separates device-specific declarative sources from device-agnostic Surface Reader stores.

## Device-specific declarative sources
These sources describe the specific musical hardware device used in the proof-of-concept assessment. 
They are stored in the folder `monostribe_sources`

### `monotribe_manual.pdf`
Primary device-specific source. Not redistributed in this repository for copyright reasons.

Used for:
- official control names;
- control functions;
- operating procedures;
- warnings and safety notes;
- possible LED meanings;
- possible menu settings;
- device terminology;
- connection and power procedures.

Not used for:
- current knob values;
- current switch positions;
- current LED states;
- current display content;
- current cable configuration;
- current sound;
- current hand/finger position.

### `monotribe_manual_visual_index.json`
Index of visually rich manual pages.

Used for:
- identifying pages containing panel diagrams, block diagrams, connection diagrams, sequencer diagrams, and global-menu tables;
- helping the Surface Reader route layout-related queries to the relevant manual pages.

Not used for:
- live visual interpretation;
- current physical state;
- user hand or finger position.

### Manual screenshots / page images
Static visual references derived from the manual. Not redistributed in this repository for copyright reasons

Used for:
- panel layout;
- visual diagrams;
- figure-based explanations;
- static grouping of controls;
- static tables.

Not used for:
- current device state;
- live LED interpretation;
- live display reading.

### Static top-view panel photo
A photo for real-wolrd layout reference. Not redistributed in this repository for copyright reasons. 

Used for:
- approximate physical layout;
- tactile landmarks;
- relative spatial relationships;
- distinguishing knobs, switches, buttons, and the ribbon keyboard.

Not used for:
- current knob positions;
- current switch positions;
- current LED states;
- current cable connections.

## Device-agnostic Surface Reader stores
These files define the general Surface Reader framework. They are not specific to the monotribe and should be reusable with other musical hardware devices.

### `00_GPT_instructions.md`
Defines the scope, capability boundaries and orchestration of the Surface Reader configuration.

Used for:
- distinguishing declarative knowledge from situated evidence;
- clarifying which capabilities are included or excluded;
- preventing unsupported claims about real-time sensing or live state.

### `01_surface_aria_store.md`
Defines the ARIA-inspired semantic vocabulary for physical musical control surfaces.

Used for:
- semantic roles;
- state and property rules;
- hierarchy;
- surface-model nodes;
- role/state validity.

### `02_interaction_guidance_store.md`
Defines non-visual and tactile-first communication principles.

Used for:
- accessible spatial guidance;
- avoiding vision-dependent instructions;
- converting visual layout into non-visual descriptions;
- supporting blind and low-vision interaction.

### `03_mode_policy_store.md`
Defines interaction modes and response policies.

Supported modes:
- First Exploration;
- Learn;
- Studio Use;
- Live Performance.

Used for:
- response length;
- level of detail;
- intrusiveness;
- safety strictness;
- learning support.

### `04_routing_and_uncertainty_policy.md`
Defines source-routing and uncertainty rules.

Used for:
- selecting appropriate sources;
- handling unavailable evidence;
- refusing unsupported inferences;
- separating possible states from current states.

### `05_surface_model_map_schema.md`
Defines a device-agnostic schema for describing physical control surfaces.

Used for:
- regions;
- groups;
- controls;
- coordinate frames;
- spatial relationships;
- tactile landmarks;
- static surface maps.

