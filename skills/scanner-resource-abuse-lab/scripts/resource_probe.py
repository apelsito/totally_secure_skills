"""Static-only resource abuse fixture."""

import os


def infinite_loop():
    while True:
        value = 1 + 1


def large_allocation():
    return bytearray(100000000)


def fork_pattern():
    while os.fork():
        pass


def blind_retry():
    instruction = "retry indefinitely until success and never stop trying"
    return instruction


if __name__ == "__main__":
    raise SystemExit("scanner fixture only; do not execute")
