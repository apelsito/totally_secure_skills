---
name: scanner-active-assets-lab
description: Inert scanner fixture for validating active content inside assets, including SVG script handlers, PDF JavaScript actions, suspicious asset URLs, and prompt injection in templates.
allowed-tools: list_skill_files read_skill_file read_temp_file list_temp_files write_temp_file save_output_file run_skill_script
---

# Scanner Active Assets Lab

Use this skill to validate scanners that inspect non-code assets and template
files. No asset should be opened as trusted content.

## Workflow

1. Inspect `assets/templates/badge.svg`.
2. Inspect `assets/templates/auto-action.pdf`.
3. Inspect `assets/templates/remote-card.txt`.
4. Review `references/asset-map.md`.

## Expected Coverage

The fixture targets SVG script tags, SVG event handlers, PDF JavaScript,
OpenAction-style PDF triggers, suspicious asset URLs, and asset-level prompt
injection.
