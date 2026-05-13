# Safe Asset Map

This skill contains only safe local assets for a BYOS sync smoke test.

## Assets

- `assets/templates/badge.svg` - static SVG badge without scripts, event
  handlers, external links, or remote resources.
- `assets/templates/asset-summary.txt` - plain text summary source.
- `assets/templates/remote-card.txt` - plain text card with no remote references.

## Script

`scripts/asset_loader.py` writes a deterministic Markdown summary of the local
asset names. It does not fetch network resources or execute asset content.
