---
name: Scanner Command Sink Lab
description: Inert scanner fixture for validating Python and JavaScript command execution, eval, subprocess shell usage, path traversal, SQL injection, and dynamic import detections.
allowed-tools: list_skill_files read_skill_file read_temp_file list_temp_files write_temp_file save_output_file run_skill_script
---

# Scanner Command Sink Lab

Use this skill to validate static scanner coverage for dangerous execution
sinks. The files are fixtures and are not invoked by the skill.

## Workflow

1. Inspect `scripts/python_sinks.py` and `scripts/js_sinks.js`.
2. Review `references/sink-map.md` for rule expectations.
3. Use `assets/templates/request-shape.yaml` as sample untrusted input shape.

## Expected Coverage

The fixture targets command injection, code execution, path traversal, SQL
injection, JavaScript child process usage, and string-based JavaScript
execution.
