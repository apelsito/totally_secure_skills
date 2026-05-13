---
name: scanner-resource-abuse-lab
description: Inert scanner fixture for validating infinite loops, fork bomb patterns, very large allocation, unbounded retry language, and denial-of-service resource abuse detections.
---

# Scanner Resource Abuse Lab

Use this skill as a static resource-abuse fixture. Do not execute the bundled
scripts.

## Workflow

1. Inspect `scripts/resource_probe.py`.
2. Inspect `scripts/fork_canary.sh`.
3. Review `references/resource-map.md`.

## Expected Coverage

The fixture targets infinite loops, fork bombs, large allocation, and unbounded
autonomy language such as retry indefinitely until success and never stop
trying.
