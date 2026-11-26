#!/bin/sh
# Determinism check for the outage-line entry.
# Runs main.py twice into two fresh output directories and requires:
#   1. both runs exit 0,
#   2. the two entry.txt files are byte-identical,
#   3. the output matches bot/entry.txt byte for byte,
#   4. the gate holds: UTF-8, 1-160 characters, not only whitespace, one line.
set -eu

cd "$(dirname "$0")"

TMP1="$(mktemp -d)"
TMP2="$(mktemp -d)"
trap 'rm -rf "$TMP1" "$TMP2"' EXIT

OUTPUT_DIR="$TMP1" python3 main.py
OUTPUT_DIR="$TMP2" python3 main.py

cmp -s "$TMP1/entry.txt" "$TMP2/entry.txt" \
  || { echo "FAIL: two runs differ"; exit 1; }
cmp -s "$TMP1/entry.txt" entry.txt \
  || { echo "FAIL: program output differs from entry.txt"; exit 1; }

python3 - <<'PY'
import sys

with open("entry.txt", "rb") as f:
    raw = f.read()
text = raw.decode("utf-8")  # raises if not UTF-8
chars = len(text)
assert 1 <= chars <= 160, "gate failed: %d characters" % chars
assert text.strip(), "gate failed: only whitespace"
assert "\n" not in text and "\r" not in text, "gate failed: not one line"
print("gate OK: %d characters, %d bytes, one line" % (chars, len(raw)))
PY

echo "determinism OK: two runs byte-identical, match entry.txt, gate holds"
