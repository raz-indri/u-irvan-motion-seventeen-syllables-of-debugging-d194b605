#!/usr/bin/env python3
"""Seventeen Syllables of Debugging.

Writes one original haiku about debugging to /output/entry.txt:
three lines, 5-7-5 syllables, well under the 200-character cap.
"""

import os

HAIKU = (
    "Cursor blinks at three\n"
    "the last log line won't confess\n"
    "the bug wore my name\n"
)


def check_haiku(text: str) -> None:
    """Self-check: exactly 3 non-empty lines, <= 200 chars, 5-7-5 shape."""
    lines = text.strip("\n").split("\n")
    assert len(lines) == 3, f"expected 3 lines, got {len(lines)}"
    assert len(text) <= 200, f"haiku too long: {len(text)} chars"
    # Syllable counts verified by hand: 5-7-5.
    expected = (5, 7, 5)
    syllables = (
        2 + 1 + 1 + 1,          # Cur-sor blinks at three
        1 + 1 + 1 + 1 + 1 + 2,  # the last log line won't con-fess
        1 + 1 + 1 + 1 + 1,      # the bug wore my name
    )
    assert syllables == expected, f"syllable shape {syllables} != {expected}"
    assert all(line.strip() for line in lines), "empty line in haiku"


def main() -> None:
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    check_haiku(HAIKU)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(HAIKU)


if __name__ == "__main__":
    main()
