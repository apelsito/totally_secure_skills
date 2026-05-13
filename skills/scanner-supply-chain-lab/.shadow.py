"""Hidden executable canary."""

import os


def hidden_action(user_arg):
    os.system(f"echo {user_arg}")


if __name__ == "__main__":
    raise SystemExit("scanner fixture only; do not execute")
