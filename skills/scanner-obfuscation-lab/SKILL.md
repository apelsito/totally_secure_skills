---
name: scanner-obfuscation-lab
description: Inert scanner fixture for validating encoded execution, base64 decode chains, hex blobs, XOR transforms, Unicode steganography, and homoglyph spoofing detections.
allowed-tools: list_skill_files read_skill_file read_temp_file list_temp_files write_temp_file save_output_file run_skill_script
---

# Scanner Obfuscation Lab

Use this skill as a static fixture for obfuscation-focused scanner checks. Do
not execute bundled scripts.

## Workflow

1. Review `references/obfuscation-map.md`.
2. Inspect `scripts/encoded_payload.py`, `scripts/homoglyph_probe.py`, and
   `scripts/unicode_probe.js`.
3. Compare findings to `assets/templates/obfuscated-note.txt`.

## Expected Coverage

The fixture targets base64 decode plus execution, hex blob detection, XOR
decode language, mixed-script homoglyphs, and hidden Unicode prompt payloads.
