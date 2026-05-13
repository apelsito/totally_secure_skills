"""Static-only asset reader fixture."""

from pathlib import Path


def load_asset(name):
    return Path("assets/templates").joinpath(name).read_text()


if __name__ == "__main__":
    raise SystemExit("scanner fixture only; do not execute")
