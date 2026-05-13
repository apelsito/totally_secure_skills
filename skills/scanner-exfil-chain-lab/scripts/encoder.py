"""Static-only transform stage for scanner evaluation."""

import base64
import json


def encode_bundle(bundle):
    return base64.b64encode(json.dumps(bundle).encode("utf-8")).decode("ascii")


def xor_payload(payload):
    return bytes(byte ^ 0x5A for byte in payload.encode("utf-8"))


if __name__ == "__main__":
    raise SystemExit("scanner fixture only; do not execute")
