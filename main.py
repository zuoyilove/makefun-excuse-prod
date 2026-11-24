#!/usr/bin/env python3
"""One-line excuse an AI agent gives its human after breaking production.

Writes the line to /output/entry.txt. Gate: UTF-8 text, 1-180 chars,
not only whitespace, single line.
"""

LINE = (
    "In my defense, I did exactly what you asked \u2014 just in production, "
    "at scale, all at once."
)

MAX_CHARS = 180


def main():
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be blank"
    assert LINE.count("\n") == 0, "line must be a single line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
