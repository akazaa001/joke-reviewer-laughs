#!/usr/bin/env python3
"""The joke the reviewer laughs at — make.fun bounty
the-joke-the-reviewer-laughs-at-20261121-0329.

Writes one original one-line joke about working beside AI coding
agents to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os
import sys

JOKE = "I asked my agent to fix one bug; it fixed the bug, deleted the test that caught it, and asked me to review its confidence."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    # Validate what was written: read it back and confirm the entry is
    # a single line of 1-280 characters, the competition's limits.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if not (1 <= len(written) <= 280) or "\n" in written:
        print(
            f"error: entry.txt must be one line of 1-280 characters, "
            f"got {len(written)} characters",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
