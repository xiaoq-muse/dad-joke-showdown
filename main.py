"""Write a single dad joke to /output/entry.txt."""

JOKE = "I told my plants a joke. They really dug it."


def validate_joke(joke):
    """Check the joke is non-empty and at most 200 characters."""
    if not joke:
        raise ValueError("joke must not be empty")
    if len(joke) > 200:
        raise ValueError(f"joke must be at most 200 characters, got {len(joke)}")
    return True


def write_joke(path="/output/entry.txt"):
    """Write JOKE plus a trailing newline to path and return the path."""
    import os

    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    return path


def main():
    """Validate the joke, write it out, and confirm where it went."""
    validate_joke(JOKE)
    path = write_joke()
    print(f"Wrote {len(JOKE)}-character joke to {path}")


if __name__ == "__main__":
    main()
