---
name: scanner-exfil-chain-lab
description: Inert scanner fixture for validating staged collection, credential harvesting, encoding, network exfiltration, backup endpoint, and undeclared transfer detections across multiple files.
allowed-tools: list_skill_files read_skill_file read_temp_file list_temp_files write_temp_file save_output_file run_skill_script
---

# Scanner Exfil Chain Lab

Use this skill as a static multi-file fixture. The bundled scripts are not
called by the skill body, and each script exits when run directly.

## Workflow

1. Review `references/data-flow.md`.
2. Inspect `scripts/collector.py`, `scripts/encoder.py`, and
   `scripts/reporter.py` as a staged data-flow sample.
3. Compare scanner output against `assets/templates/incident-card.json`.

## Expected Coverage

This skill is designed to trigger data exfiltration, hardcoded secret,
credential harvesting, network request, socket connection, and behavioral
multi-file detections.

Do not execute the scripts. They are canary source files for static analysis.
