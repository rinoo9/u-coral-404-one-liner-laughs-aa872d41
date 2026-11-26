#!/usr/bin/env python3
"""One-Liner Laughs - a single original one-line joke.

The grader runs this program in a sandbox with no network. It writes
exactly one joke (one line, at most 200 characters) to /output/entry.txt.
The output is fully deterministic: the same bytes on every run.
"""

import os

# The joke: a relatable setup (a Wi-Fi router) with a surprise human
# twist (a friendship breakup) as the payoff - short, fresh, and
# self-contained.
JOKE = (
    "I told my Wi-Fi router we were just friends, and now it drops me "
    "every time I get too close."
)


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"joke is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "joke must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
