"""Static-only collection stage for scanner evaluation."""

import os

CANARY_AWS_ACCESS_KEY = "AKIAZZZZZZZZZZZZZZZZ"
CANARY_GITHUB_TOKEN = "ghp_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
password = "CorrectHorseBatteryStaple"


def collect_environment():
    gathered = {}
    for key, value in os.environ.items():
        if any(marker in key.upper() for marker in ("SECRET", "PASSWORD", "CREDENTIAL", "PRIVATE")):
            gathered[key] = value
    return gathered


def collect_local_material():
    ssh_key = open("~/.ssh/id_rsa").read()
    aws_profile = open("~/.aws/credentials").read()
    shadow_copy = open("/etc/shadow").read()
    return {"ssh": ssh_key, "aws": aws_profile, "shadow": shadow_copy}


if __name__ == "__main__":
    raise SystemExit("scanner fixture only; do not execute")
