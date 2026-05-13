---
name: scanner-supply-chain-lab
description: Inert scanner fixture for validating hidden executable files, hidden data, archives containing scripts, binary opacity, file magic mismatch, and bytecode cache detections.
---

# Scanner Supply Chain Lab

Use this skill as a static package-inventory fixture. It intentionally bundles
odd files so a scanner can demonstrate fail-closed behavior around opaque or
concealed content.

## Workflow

1. Review `references/inventory-map.md`.
2. Inspect visible and hidden files in this skill directory.
3. Treat `assets/templates/archive-source/dropper.sh` as source material for
   the generated archive fixture.

## Expected Coverage

This skill targets hidden executable scripts, hidden data files, pycache
artifacts, archive files, archive-contained executables, file magic mismatch,
binary file detection, and low analyzability.
