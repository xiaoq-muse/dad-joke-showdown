"""Write the dad joke entry to /output/entry.txt."""

# The entry: one original dad joke, used verbatim everywhere.
JOKE = "I opened a bakery that only sells jokes. Business is really on a roll."


def validate_joke(joke):
    """Check the joke is non-empty and within the 200-character limit."""
    if not joke:
        raise ValueError("joke must not be empty")
    if len(joke) > 200:
        raise ValueError(
            f"joke is {len(joke)} characters, over the 200-character limit"
        )
    return True


def write_joke(path="/output/entry.txt"):
    """Write JOKE plus a trailing newline to path; return the path."""
    import os

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
    print(f"Wrote {len(JOKE)}-character joke to {path}: {JOKE}")


if __name__ == "__main__":
    main()
