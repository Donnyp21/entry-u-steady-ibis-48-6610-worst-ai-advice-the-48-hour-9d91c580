"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of the worst possible advice an AI could give to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR). The text is fixed: no
randomness, no network, no clock, so two runs write the same bytes,
which is what the determinism check wants.
"""

import os

LINE = "Use the same password for every account — that way you only have one to remember, and hackers only have one to find."

MAX_CHARS = 140


def main():
    line = LINE.strip()
    if not 1 <= len(line) <= MAX_CHARS:
        raise SystemExit(f"line must be 1-{MAX_CHARS} chars, got {len(line)}")
    if "\n" in line:
        raise SystemExit("line must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(line)
    print(f"wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()
