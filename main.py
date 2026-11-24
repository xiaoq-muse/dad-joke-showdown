#!/usr/bin/env python3
"""Write one original dad joke to /output/entry.txt."""

import os

JOKE = "My chili recipe is top secret. Even the beans won't spill."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
