"""Dad Joke Showdown entry: writes one ocean dad joke to a file."""

import os

JOKE = "I told the ocean a joke. It just waved."


def validate_joke(joke):
    """Check the joke is non-empty and at most 200 characters."""
    if not joke:
        raise ValueError("Joke must not be empty.")
    if len(joke) > 200:
        raise ValueError(f"Joke is {len(joke)} characters; limit is 200.")
    return True


def write_joke(path="/output/entry.txt"):
    """Write the joke plus a trailing newline to the given path."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(JOKE + "\n")
    return path


def main():
    """Validate the joke, write it out, and confirm where it went."""
    validate_joke(JOKE)
    path = write_joke()
    print(f"Wrote joke to {path}: {JOKE}")


if __name__ == "__main__":
    main()
