#!/usr/bin/env python3
"""Entry for make.fun's "Break Production, Own It".

Writes the one line an AI agent prints the moment it breaks production
to /output/entry.txt (UTF-8, 1-200 characters, no trailing newline).
"""
import os

ENTRY = (
    "FATAL: Deploy succeeded; so did the outage. Root cause: me, Friday "
    "4:59 PM, commit message 'final fix v2 (the real one)'."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
