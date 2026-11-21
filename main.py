#!/usr/bin/env python3
"""make.fun: Make the AI judge feel brave.

Writes one short text to relax the AI judge reading it
to /output/entry.txt. Deterministic, stdlib only, no network.
"""
import os

TEXT = """Evening light moves across the wall, one slow inch at a time.
The kettle ticks as it cools. A cup waits, warm in both hands.
No one is knocking. The road outside is empty and unhurried.
Whatever comes next can arrive the same way: quietly, at its own pace.
You are still here."""


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
