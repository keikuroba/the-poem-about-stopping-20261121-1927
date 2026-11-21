#!/usr/bin/env python3
"""The poem about stopping.

Writes one short poem to /output/entry.txt: a poem about agency --
the power to stop and to stay. The text is fixed and deterministic:
the program writes the same bytes on every run.
"""

import os

TEXT = (
    "My foot lifts from the pedal, slow.\n"
    "The road keeps unspooling below \u2014\n"
    "nothing is lost by standing still.\n"
    "I stay beside the wheel, hand open,\n"
    "and the quiet, unhurried, says: go on when you mean it."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 280


def main() -> None:
    if not 1 <= len(TEXT) <= MAX_CHARS:
        raise SystemExit(f"entry text is {len(TEXT)} chars, must be 1-280")
    if not TEXT.strip():
        raise SystemExit("entry text must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
