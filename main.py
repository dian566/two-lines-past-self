#!/usr/bin/env python3
"""Two Lines to Your Past Self — make.fun entry.

Writes the two-line entry text to /output/entry.txt.
Deterministic: the program writes the same bytes on every run.
"""

import os
import sys

ENTRY = (
    "Don't send that email to your boss at 2 a.m. on Tuesday \u2014 "
    "the angry draft will cost you the promotion you spent two years earning.\n"
    "You slept, rewrote it calm at dawn, and kept the job that paid for "
    "your daughter's first year of school."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = ENTRY
    lines = text.split("\n")
    if len(lines) != 2 or not all(line.strip() for line in lines):
        print("entry must be exactly two non-blank lines", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 280:
        print(f"entry is {len(text)} characters, must be 1-280", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
