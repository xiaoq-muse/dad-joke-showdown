"""Write a dad joke about an elevator to the entry file."""

# The joke for the Dad Joke Showdown entry.
JOKE = "I told the elevator a joke. It really lifted my spirits."


def validate_joke(joke):
    """Check the joke is non-empty and no longer than 200 characters."""
    if not joke:
        raise ValueError("joke must not be empty")
    if len(joke) > 200:
        raise ValueError(f"joke must be at most 200 characters, got {len(joke)}")
    return True


def write_joke(path="/output/entry.txt"):
    """Write JOKE plus a trailing newline to path; return the path written."""
    import os

    # Make sure the output directory exists before writing.
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    return path


def main():
    """Validate the joke, write it out, and print a confirmation."""
    validate_joke(JOKE)
    path = write_joke()
    print(f"Wrote joke to {path}")


if __name__ == "__main__":
    main()
