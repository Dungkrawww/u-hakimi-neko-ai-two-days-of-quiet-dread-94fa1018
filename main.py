#!/usr/bin/env python3
"""Two Days of Quiet Dread — one-line code review comment.

Writes a single line (<=140 chars) to /output/entry.txt: a code review
comment that approves a pull request while carrying quiet existential
dread, in the flat voice of a tired engineer clicking approve.
"""

import os

ENTRY = "Approved. It passes the tests, reads cleanly, and will outlive us all anyway."


def main():
    # No trailing newline: the gate counts every character and the
    # entry must stay a single line of at most 140 characters.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
