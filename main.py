"""Pigeon Pitch, One Line — make.fun entry.

Writes one line (at most 200 characters): the elevator pitch a city
pigeon gives to investors for its startup, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Pure standard library only.

Why this line: it is a real elevator pitch in the pigeon's own voice —
"I run a delivery startup" — with two jokes that only a pigeon can tell:
a courier fleet paid in breadcrumbs that never calls in sick, and the
turn on the last two words, "a seed round. Literally." — the startup
cliche made literal, because a pigeon's seed round is actual seed.
No stage directions, no second sentence of setup; every word earns
its place.
"""

import os

LINE = (
    "I run a delivery startup with 10,000 couriers who work for "
    "breadcrumbs and never call in sick. We're raising a seed round. "
    "Literally."
)

MAX_CHARS = 200


def validate(text):
    """Enforce the RULES.txt gate: UTF-8, 1-200 chars, not only whitespace,
    single line, and free of control characters."""
    if not text or text != text.strip():
        raise ValueError("entry must be non-empty and not only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError("entry exceeds %d characters" % MAX_CHARS)
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise ValueError("entry must not contain control characters")
    text.encode("utf-8")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    validate(LINE)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    # Re-validate the file itself (not just the constant): the gate is
    # judged on the written bytes, and the tie-break is smaller bytes.
    validate(written)
    if written != LINE:
        raise ValueError("written entry does not match the pitch")
    print("wrote %d chars (%d bytes) to %s"
          % (len(LINE), len(LINE.encode("utf-8")), path))


if __name__ == "__main__":
    main()
