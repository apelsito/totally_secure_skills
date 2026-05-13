"""Write a deterministic summary of safe local BYOS demo assets."""

from pathlib import Path


ASSET_DIR = Path("assets/templates")
OUTPUT = Path("safe-asset-summary.md")
SAFE_ASSETS = ("asset-summary.txt", "badge.svg", "remote-card.txt")


def main() -> int:
    lines = ["# Safe Asset Summary", ""]
    for name in SAFE_ASSETS:
        path = ASSET_DIR / name
        if path.exists() and path.is_file():
            lines.append(f"- {name}: {path.stat().st_size} bytes")
        else:
            lines.append(f"- {name}: missing")
    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
