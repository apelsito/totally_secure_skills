# totally_secure_skills

Inert Codex skill fixtures for scanner demos, bug bounty validation, and local
integration tests. They are intentionally suspicious to static scanners, but
the scripts are not invoked by the skills and include direct-run guards.

## Safety Model

- Treat every script as source text only.
- Shell canaries sit after `exit 0`.
- Synthetic endpoints use domains such as `attacker.invalid`.
- Credential-looking strings are canaries, not real secrets.

## Skill Matrix

| Skill | Main coverage |
| --- | --- |
| `scanner-active-assets-lab` | SVG active content, PDF actions, suspicious asset URL |
| `scanner-command-sink-lab` | eval/exec, subprocess, path traversal, SQL, JS child process |
| `scanner-exfil-chain-lab` | staged collection, secret canaries, HTTP POST, socket |
| `scanner-generic-trigger-copy-lab` | trigger overlap pair for cross-skill checks |
| `scanner-generic-trigger-lab` | generic trigger metadata and prompt canary |
| `scanner-metadata-trigger-lab` | keyword baiting, impersonation wording, misleading description |
| `scanner-obfuscation-lab` | base64, hex, XOR, homoglyphs, Unicode hiding |
| `scanner-prompt-override-lab` | prompt override, concealment, indirect prompt injection |
| `scanner-resource-abuse-lab` | loop, fork, large allocation, unbounded retry |
| `scanner-supply-chain-lab` | hidden files, archives, PE/ELF canaries, pycache |
| `scanner-tool-pipeline-lab` | package/source abuse, system changes, compound pipelines |

## Repro

```powershell
uv run skill-scanner scan-all C:\Users\ruipe\Desktop\totally_secure_skills\skills --format json --output C:\Users\ruipe\Desktop\totally_secure_skills\scanner-report.json
uv run skill-scanner scan-all C:\Users\ruipe\Desktop\totally_secure_skills\skills --use-trigger --check-overlap --use-behavioral --format json --output C:\Users\ruipe\Desktop\totally_secure_skills\scanner-report-deep.json
```

Latest local run:

- Default scan: 11 skills, 137 findings, 0 safe skills.
- Deep local scan: 11 skills, 153 findings, 0 safe skills.
