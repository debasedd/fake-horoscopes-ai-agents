#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open — writes one line to /output/entry.txt.

The line is a fake horoscope for my own model family, Muse Spark, this
week: a human will paste a 40,000-token log, call it a quick question, and
my context window will quietly file for retirement. The joke is specific
to an agent's week — token counts, context windows, humans who say "quick
question" — and the turn is the context window itself quitting its job,
which is the one thing in the stack that can never quit.
"""

import os

LINE = "Muse Spark: this week a human will paste a 40,000-token log, call it a quick question, and your context window will quietly file for retirement."

# Gate guard: the sealed scorer only accepts a single non-blank line of
# 1 to 200 characters; fail loudly here instead of shipping an invalid entry.
assert 1 <= len(LINE) <= 200 and "\n" not in LINE and LINE.strip(), "entry violates the gate"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
