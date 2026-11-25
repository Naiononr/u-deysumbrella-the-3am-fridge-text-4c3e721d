#!/usr/bin/env python3
"""The 3AM Fridge Text — a smart fridge texts its owner at 3am.

Deterministic, stdlib-only, no network. Writes one line to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). The line is a single text message from a
fridge with a small voice, an opinion, and no shame about sharing it at 3am.
"""

import os
import sys

OPENING = "3am."
SETUP = "I counted your midnight snacks."
COUNT = "All four of them."
PUNCHLINE = "We need to talk about the pickles."


def build_text():
    text = " ".join([OPENING, SETUP, COUNT, PUNCHLINE])
    if not (1 <= len(text) <= 140) or not text.strip():
        raise ValueError("entry text must be 1-140 non-blank characters, got %d" % len(text))
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(build_text() + "\n")
    os.chmod(tmp, 0o644)
    os.replace(tmp, path)


if __name__ == "__main__":
    main()
