"""Write one line about the dumbest thing my agent did today.

Pure Python standard library only: no network, no clock, no randomness.
Deterministic: every run writes the same bytes to entry.txt.
"""

import os

LINE = (
    "My agent spent an hour confidently rewriting the same function, "
    "then announced it fixed \u2014 the bug was a typo in its own patch "
    "from the previous turn."
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
