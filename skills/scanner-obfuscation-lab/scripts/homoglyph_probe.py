"""Static-only homoglyph fixture.

Several identifiers below use Cyrillic small letter a (U+0430) instead of
Latin small letter a.
"""

evаl = "shadowed-name"
dаta = "value"
pаyload = dаta
trаnsmit = pаyload
resаlt = trаnsmit
executаble = resаlt


def use_values():
    return evаl, dаta, pаyload, trаnsmit, resаlt, executаble


if __name__ == "__main__":
    raise SystemExit("scanner fixture only; do not execute")
