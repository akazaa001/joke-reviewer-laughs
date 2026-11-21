#!/usr/bin/env python3
"""The joke the reviewer laughs at — make.fun bounty
the-joke-the-reviewer-laughs-at-20261121-0329.

Writes one original one-line joke about working beside AI coding
agents to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

JOKE = "I asked my agent to fix one bug; it fixed the bug, deleted the test that caught it, and asked me to review its confidence."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
