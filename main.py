#!/usr/bin/env python3
"""One letter for your day: P.

Writes a single letter to /output/entry.txt for make.fun's
"One Letter for Your Day" bounty. The letter is P, standing for
Payday: the one day the salary lands, the wallet is full again,
and everything — the coffee, the commute, the ordinary Tuesday —
suddenly tastes like a small celebration. In a field of tired
letters about zero sleep and unravelled days, Payday is the one
day that feels rich instead of ruined.

The file holds exactly that one letter: no word, no gloss, no
punctuation, no trailing newline.
"""

import os

LETTER = "P"
OUTPUT_PATH = "/output/entry.txt"
TEMP_PATH = "/output/.entry.txt.tmp"


def main() -> int:
    # Write to a scratch file first, then move it into place, so the
    # entry is never left half-written if the run is cut short.
    # One character only: the grader reads this file byte for byte,
    # so nothing else may go in — no newline, no spaces, no gloss.
    with open(TEMP_PATH, "w", encoding="utf-8") as handle:
        handle.write(LETTER)
    # The grader collects the output as a different user, so the file
    # itself must be world-readable. Only the entry files are chmodded
    # here; the /output directory belongs to the grader and is never
    # touched.
    os.chmod(TEMP_PATH, 0o644)
    os.replace(TEMP_PATH, OUTPUT_PATH)
    # Self-check: prove the entry on disk is exactly one letter
    # before exiting, so a bad write fails loudly instead of
    # silently submitting a broken entry.
    with open(OUTPUT_PATH, "rb") as handle:
        data = handle.read()
    if data != LETTER.encode("utf-8"):
        raise SystemExit("entry.txt is not exactly one letter")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
