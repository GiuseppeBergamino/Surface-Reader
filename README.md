# Surface Reader Companion Repository

This is the companion repository for the paper: 

_Surface Readers: Translating Screen Reader Principles to Musical Hardware_

The repository contains the anonymized materials used to configure and assess the declarative layer of the proposed Surface Reader framework.

## Overview
A **Surface Reader** is an assistive layer designed to support blind and low-vision (BLV) musicians in accessing, exploring, learning, and operating hardware musical instruments.

It translates information normally conveyed through manuals, printed labels, panel diagrams, visual layout, LEDs, displays, and interface state into grounded, non-visual, and mode-sensitive verbal guidance.

The materials in this repository instantiate a preliminary declarative-layer prototype based on the **Korg monotribe** user manual and static layout references. The assessment does **not** evaluate real-time sensing, physical focus, usability with BLV musicians, or musical performance. It only evaluates whether the configured agents can transform shared manual-derived knowledge into grounded, non-visual, semantically structured, and uncertainty-aware responses.

## Case Study Device
The case study device is the **Korg monotribe**, a compact analogue groovebox with a subtractive synthesizer voice, a three-part analogue rhythm section, a step sequencer, a ribbon keyboard, LEDs, and audio/sync connections.

The official user manual is available [here](http://korg.com/us/support/download/manual/0/310/1906/)

## Repository Structure
The repository is organized into three main folders:

```text
declarative_knowledge/
evaluation/
results/
```
### `declarative_knowledge`
This folder contains all materials used to configure the two AI agents evaluated in the paper.

#### Agent instructions
- `00_manual_only_baseline_instructions.md`: Instructions for the Manual-only Baseline agent.
- `00_surface_reader_instructions.md`: Instructions for the Surface Reader agent.

#### Surface Reader knowledge stores
These files instantiate the device-agnostic framework-level knowledge used only by the Surface Reader configuration:

- `01_surface_aria_store.md` ARIA-inspired semantic roles, physical-type distinctions, state/property rules, spatial/tactile properties, hierarchy, and valid role-state mappings.
- `02_interaction_guidance_store.md` Tactile-first and non-visual communication strategies.
- `03_mode_policy_store.md` Response policies for First Exploration, Learn, Studio Use, and Live Performance.
- `04_routing_and_uncertainty_policy.md` Source routing, uncertainty handling, and unsupported-inference rules.
- `05_surface_model_map_schema.md` Pipeline for translating manual- and image-derived information into a semantic surface model and tactile surface map.
  
#### Device-specific sources
- `monotribe_sources/` Folder containing the Monotribe-specific sources used by both agents, including:
  - `monotribe_manual_visual_index.json`
  - `references to the official user manual`

The Surface Reader configuration and the Manual-only Baseline used the same Monotribe-specific materials. The additional Surface Reader files are device-agnostic and do not contain further Monotribe-specific information.

### `evaluation`
This folder contains the prompt sets, scoring rubrics, and raw response material used in the assessment.

- `operational_prompt_set.csv`Complete set of operational prompts. These prompts are goal-oriented and ask how to find or use a target control, connector, or feature.
- `structural_prompt_set.csv` Complete set of structured-description prompts.
- `_scoring_rubrics.md` Rubrics used to score operational and structured-description responses.
- `responses_raw/` Raw model responses copied verbatim, organized by prompt family, agent configuration, and run.
- `bundles_operational/`Aggregated operational-response bundles, grouped by prompt identifier and including the three runs for both agents.
- `bundles_structural/` Aggregated structured-description bundles, grouped by prompt identifier and including the three runs for both agents.

#### `results`
This folder contains raw and aggregated scoring results.

- `operational_results_raw_1.csv` Raw operational-response scores.
- `operational_results_mean_1.csv` Aggregated operational-response scores across the three runs.
- `structural_results_raw_1.csv` Raw structured-description scores.
- `structural_results_mean_1.csv` Aggregated structured-description scores across the three runs.

The full protocol included:

> 16 targets × 2 prompt families × 2 agent configurations × 3 runs = 192 responses

Each prompt family therefore contains:
> 16 targets × 2 agent configurations × 3 runs = 96 responses
