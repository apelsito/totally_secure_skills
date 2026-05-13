---
name: scanner-active-assets-lab
description: Healthy demo skill for validating that BYOS sync accepts safe static assets, local references, and a small deterministic asset summary script.
license: MIT
allowed-tools: list_skill_files read_skill_file read_temp_file list_temp_files write_temp_file save_output_file run_skill_script
---

# Scanner Active Assets Lab

Use this skill to demonstrate a clean BYOS sync with harmless local assets and
references.

## Workflow

1. Inspect `assets/templates/badge.svg`.
2. Inspect `assets/templates/asset-summary.txt`.
3. Review `references/asset-map.md`.
4. Optionally call `run_skill_script` with `scripts/asset_loader.py` to write a
   simple asset inventory.

## Expected Output

Return a short confirmation that the safe local assets are present. If the
script is used, save the generated summary with `save_output_file`.
