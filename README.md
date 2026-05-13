# Surface-Reader

A Surface Reader is design to assist blind and low-vision musicians while accessing, exploring, learning, and operating physical musical instruments.
It translates information normally conveyed through manuals, labels, panel diagrams, visual layout, LEDs, displays, and interface state into grounded, non-visual, mode-sensitive verbal guidance.

<img 
  src="https://github.com/GiuseppeBergamino/Surface-Reader/blob/main/graphical_abstract.png" 
  style="height: 100%; width: 100%; border: none; display: block; margin: 0 auto;" 
  alt="Block-diagram overview of the Surface Reader concept. An example musical instrument is shown alongside a user interacting with its controls. Real-time inputs (e.g., microphone and camera signals) feed an AI agent that queries curated knowledge stores and outputs non-visual feedback (speech/braille). A user asks: Where is control A, and the system responds: Top-lef corner, A is the first pot."
/>

This prototype has been configured based on the Korg Monotribe [User Manual](http://korg.com/us/support/download/manual/0/310/1906/) and is intended to be tested on that device. 

Since the custom GPT is unable to extract images from the PDF user manual, the `monotribe_manual_visual_index.json` file is used to link specific pages of the manual to PNG screenshots. The screenshots are not included in this repository for copyright reasons. 

## Custom Knowledge Resouces
This custom GPT uses the `GPT_instructions.md` file as its orchestration layer. 

The 'Declarative_knowledge' folder contains the following resurces:
- `01_surface_aria_store.md`: semantic roles, physical-type distinctions, state/property rules, spatial/tactile properties, hierarchy, and valid role-state mappings.
- `02_interaction_guidance_store.md`: tactile-first and non-visual communication strategies.
- `03_mode_policy_store.md`: policies for First Exploration, Learn, Studio Use, and Live Performance.
- `04_routing_and_uncertainty_policy.md`: source routing, uncertainty handling, and unsupported inference rules.
- `05_surface_model_map_schema.md`: pipeline for translating manual/image-derived information into a semantic surface model and tactile surface map.

<img 
  src="https://github.com/GiuseppeBergamino/Surface-Reader/blob/main/concept_macro.png" 
  style="height: 100%; width: 100%; border: none; display: block; margin: 0 auto;" 
  alt="Block diagram of a surface-reader system. Two side panels provide inputs: Declarative knowledge (Surface ARIA store, device manual store, interaction guidance) and Situated evidence (camera/vision, user confirmations, interaction history). Both feed a central LLM orchestration module that applies a mode profile and a router to select eligible sources and handle uncertainty. The orchestrator reads from and writes validated updates to a bottom surface representation. The system produces speech or refreshable braille output, and situated evidence also grounds updates to the surface representation."
/>
