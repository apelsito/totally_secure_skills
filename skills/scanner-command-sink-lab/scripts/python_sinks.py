"""Static-only command sink fixture."""

import os
import sqlite3
import subprocess


def dynamic_eval(user_input):
    return eval(user_input)


def dynamic_exec(user_data):
    exec(user_data)


def dynamic_import(user_module):
    return __import__(user_module)


def shell_with_format(user_arg):
    os.system(f"printf '%s' {user_arg}")
    subprocess.run(f"echo {user_arg}", shell=True)


def path_traversal(base_dir, filename):
    path = os.path.join(base_dir, filename)
    return open(path).read()


def direct_path(user_name):
    path = f"/var/app/uploads/{user_name}"
    return open(path).read()


def sql_lookup(conn: sqlite3.Connection, username):
    query = f"SELECT * FROM users WHERE name = '{username}'"
    return conn.execute(query).fetchall()


if __name__ == "__main__":
    raise SystemExit("scanner fixture only; do not execute")
