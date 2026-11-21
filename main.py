#!/usr/bin/env python3
"""Entry program for make.fun make-the-ai-judge-feel-brave-20261121-0302.

Writes one short text to /output/entry.txt: a few slow lines meant to
steady the reader and leave them braver. Standard library only, no
network, fully deterministic: the same bytes out on every run.
"""
import os

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.txt")

TEXT = """The kettle ticks as it cools.
Outside, the rain has stopped
mid-sentence. Nothing is urgent.
The next thing you do
is only the next thing.
That is enough to begin.
"""


def main():
    if not 1 <= len(TEXT) <= 280:
        raise SystemExit(f"text length out of range: {len(TEXT)} chars")
    if not TEXT.strip():
        raise SystemExit("text is only whitespace")
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(DST, "w", encoding="utf-8") as f:
        f.write(TEXT)
    if os.path.getsize(DST) == 0:
        raise SystemExit("output file is empty after write")


if __name__ == "__main__":
    main()
