#!/usr/bin/env python3
"""Write one original dad joke to /output/entry.txt."""

import os

JOKE = "I told my trumpet a secret, but it just blew it."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
