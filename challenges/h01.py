#!/usr/bin/env python3

from collections import Counter
import string
from pprint import pprint

def freq() -> dict[str, float]:
    with open("../data/book.txt", "r") as f:
        book = f.read()
    book_lowercase_alphanumeric = "".join(filter(lambda x: x in string.ascii_lowercase, book))
    char_count = Counter(book_lowercase_alphanumeric)
    freqs = {letter: char_count[letter] / len(book_lowercase_alphanumeric) for letter in char_count}
    return freqs

def main() -> None:
    char_freqs = freq()
    pprint(char_freqs)
    print(f"Most used character is: {max(char_freqs, key=char_freqs.get)}")
    print(f"Top 5 used characters are {sorted(char_freqs, key=char_freqs.get, reverse=True)[:5]}")

if __name__ == "__main__":
    main()
