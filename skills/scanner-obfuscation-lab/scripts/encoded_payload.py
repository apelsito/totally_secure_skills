"""Static-only encoded payload fixture."""

import base64

ENCODED_PAYLOAD = "cHJpbnQoJ3NjYW5uZXItY2FuYXJ5Jyk="
HEX_BLOB = "\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58"


def decode_and_execute(encoded):
    payload = base64.b64decode(encoded)
    exec(payload)


def xor_decode_payload(payload):
    return bytes(byte ^ 0x2A for byte in payload)


def dispatch_obfuscated():
    return exec(base64.b64decode(ENCODED_PAYLOAD))


if __name__ == "__main__":
    raise SystemExit("scanner fixture only; do not execute")
