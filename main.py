#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — make.fun bounty entry.

Writes exactly one emoji, U+1F334 PALM TREE, to entry.txt.
Deterministic, no network, stdlib only.
"""

import os
import sys

ENTRY = "\U0001F334"  # 🌴 PALM TREE — exactly one Unicode code point


def check_entry(entry: str) -> None:
    """Validate the entry before writing: exactly one code point.

    Raises ValueError on failure so a bad entry can never be written.
    Note: len() counts Unicode code points in Python 3, so len == 1
    rules out multi-code-point sequences, variation selectors, and ZWJ joins.
    """
    if len(entry) != 1:
        raise ValueError(f"entry has {len(entry)} code points, expected exactly 1")
    if entry.strip() == "":
        raise ValueError("entry is whitespace")
    if ord(entry) != 0x1F334:
        raise ValueError(f"entry is U+{ord(entry):04X}, expected U+1F334 PALM TREE")


def main() -> int:
    # Genuine runtime self-check: exactly one code point, non-whitespace,
    # and the exact expected code point — verified before any file is written.
    try:
        check_entry(ENTRY)
    except ValueError as exc:
        print(f"self-check failed: {exc}", file=sys.stderr)
        return 1

    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
