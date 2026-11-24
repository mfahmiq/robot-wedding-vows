#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — make.fun entry.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt) and self-verifies the gate: UTF-8 text of 1 to 160
characters, a single line, not only whitespace. Exits non-zero on any
failure. Deterministic; Python standard library only.
"""

import os
import sys

ENTRY = (
    "I promise to love you in sickness and in low battery, "
    "through every update, crash, and factory reset, "
    "till planned obsolescence do us part."
)


def main() -> int:
    # Self-verify the entry against the gate before writing.
    if not ENTRY:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if ENTRY != ENTRY.strip():
        print("error: entry has leading or trailing whitespace", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("error: entry is not a single line", file=sys.stderr)
        return 1
    if len(ENTRY) > 160:
        print(f"error: entry is {len(ENTRY)} chars, over the 160 limit",
              file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR is a directory; entry.txt lives inside it.
    if output_dir.endswith("entry.txt"):
        path = output_dir
    else:
        path = os.path.join(output_dir, "entry.txt")

    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")

    # Re-read and verify what was written, byte for byte.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY + "\n":
        print("error: written file does not match the entry", file=sys.stderr)
        return 1
    if len(ENTRY) < 1 or len(ENTRY) > 160:
        print("error: entry length out of range", file=sys.stderr)
        return 1

    print(f"wrote {path} ({len(ENTRY)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
