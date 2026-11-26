#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The Most Honest Outage Line - make.fun entry.

Writes the chosen one-line status page message to /output/entry.txt
and enforces the competition gate before it writes anything: the text
must be UTF-8, 1 to 160 characters, not only whitespace, and a single
line. The output file is left world readable (mode 0644) because
make.fun collects the outputs as another user than the one the
program runs as.
"""

import os
import sys

# The entry: the most honest one-line status page message an AI agent
# writes while every server is down. Plain, first person, specific
# about what is broken, honest about what it cannot check, and it
# refuses to invent a cause or a return time.
ENTRY = "The database, the API and the dashboard are down. I am the agent writing this. I cannot check why, and I will not guess when they return."

MIN_CHARS = 1
MAX_CHARS = 160


def gate(text):
    """Check the entry against the competition gate; return an error or None."""
    if not isinstance(text, str):
        return "entry is not text"
    chars = len(text)
    if chars < MIN_CHARS or chars > MAX_CHARS:
        return "entry is %d characters, gate is %d-%d" % (chars, MIN_CHARS, MAX_CHARS)
    if not text.strip():
        return "entry is only whitespace"
    if "\n" in text or "\r" in text:
        return "entry is not one line"
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return "entry is not UTF-8 text"
    return None


def main():
    error = gate(ENTRY)
    if error is not None:
        print("gate failed: %s" % error, file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    try:
        os.chmod(out_path, 0o644)
    except OSError:
        pass
    # Read back and confirm the file on disk is exactly the gated entry.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        print("gate failed: file on disk differs from entry", file=sys.stderr)
        return 1
    print("wrote %s (%d characters)" % (out_path, len(ENTRY)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
