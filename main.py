#!/usr/bin/env python3
"""One Word, First Thought — writes exactly one word to /output/entry.txt."""

import os

WORD = "turnstile"
OUTPUT_PATH = "/output/entry.txt"


def validate_word(word):
    """Exactly one word: letters only, 1-24 chars, no whitespace."""
    if not isinstance(word, str):
        raise ValueError("word must be a string")
    if not 1 <= len(word) <= 24:
        raise ValueError("word must be 1-24 characters long")
    if not word.isalpha():
        raise ValueError("word must contain letters only")
    if word != word.strip() or any(ch.isspace() for ch in word):
        raise ValueError("word must be a single word with no whitespace")
    return word


def main():
    word = validate_word(WORD)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(word)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != word:
        raise ValueError("read-back mismatch: entry.txt does not hold the word")


if __name__ == "__main__":
    main()
