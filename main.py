#!/usr/bin/env python3
"""One-Line Robot Wedding Vows.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt (or ./output/entry.txt
when the variable is unset) and prints that one line to stdout. Stdlib only,
deterministic, no network.

The line is a robot wedding vow: the classic "in sickness and in health ...
till death do us part" shape, retuned with machine specifics (low battery,
safe mode, firmware update) and a payoff in the last few words.
"""

import os
import sys

ENTRY = (
    "I vow to love you in sickness and in health, "
    "in low battery and in safe mode, "
    "until a firmware update do us part."
)
MAX_CHARS = 160


def main() -> int:
    line = ENTRY
    if not line or not line.strip():
        print("error: entry is empty or whitespace-only", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            f"error: entry is {len(line)} chars, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        os.getcwd(), "output"
    )
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Verify what was actually written: byte-exact match, no trailing
    # newline, so a partial write or encoding surprise cannot pass silently.
    with open(out_path, "rb") as f:
        written = f.read()
    if written != line.encode("utf-8"):
        print(
            f"error: verification failed for {out_path}: "
            f"wrote {len(written)} bytes, expected {len(line)}",
            file=sys.stderr,
        )
        return 1
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
