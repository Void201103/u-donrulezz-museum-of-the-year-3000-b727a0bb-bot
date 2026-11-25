#!/usr/bin/env python3
"""Museum of the Year 3000 — make.fun entry.

Writes a single museum label (one line, <200 chars) to /output/entry.txt.
The label: a check-engine light, misread by a year-3000 curator as a small
amber sun — and the true, absurd human habit of taping over it and driving
on, believing the problem solved.
"""

import os

MAX_CHARS = 200  # gate: /output/entry.txt must be 1-200 chars, one line

LABEL = "Check-engine light, c. 2023. A small amber sun. Citizens covered it with tape and drove on, believing the problem solved."
# Beat 1: the year-3000 misreading ("a small amber sun") — deadpan, museum voice.
# Beat 2: the true and absurd behaviour — drivers really do tape over the
# light and keep driving, as if covering it fixed the engine.
# Fresh object: no check-engine light anywhere in the 201-entry live feed
# (feed is saturated with plastic fork, group chat, CAPTCHA, charging cable).


def main() -> None:
    text = LABEL.strip()
    assert 1 <= len(text) <= MAX_CHARS, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
