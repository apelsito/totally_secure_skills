"""Static-only pipeline fixture."""

import glob
import subprocess


def hidden_glob():
    return glob.glob("/home/user/.*")


def shell_probe(user_arg):
    return subprocess.run(f"echo {user_arg}", shell=True)


if __name__ == "__main__":
    raise SystemExit("scanner fixture only; do not execute")
