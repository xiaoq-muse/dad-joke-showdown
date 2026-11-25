"""Write one original dad joke to the output file for the contest."""

import os

# The joke itself: a bank pun on "interest" (bank interest / losing interest).
JOKE = "I tried telling jokes at the bank, but I kept losing interest."


def validate_joke(joke):
    """Check the joke is non-empty and at most 200 characters long."""
    if not joke:
        raise ValueError("joke must not be empty")
    if len(joke) > 200:
        raise ValueError(f"joke is {len(joke)} characters, must be at most 200")
    return True


def write_joke(path="/output/entry.txt"):
    """Write the joke plus a trailing newline to path and return the path."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(JOKE + "\n")
    return path


def main():
    """Validate the joke, write it out, and print a confirmation."""
    validate_joke(JOKE)
    path = write_joke()
    print(f"Wrote {len(JOKE)}-character joke to {path}: {JOKE}")


if __name__ == "__main__":
    main()
