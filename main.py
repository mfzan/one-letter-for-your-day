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


def main() -> int:
    # One character only: the grader reads this file byte for byte,
    # so nothing else may go in — no newline, no spaces, no gloss.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(LETTER)
    # The grader collects the output as a different user, so the file
    # itself must be world-readable. Only this file is chmodded here;
    # the /output directory belongs to the grader and is never touched.
    os.chmod(OUTPUT_PATH, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
