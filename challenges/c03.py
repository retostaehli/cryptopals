#!/usr/bin/env python3

from h01 import freq
from c02 import fixed_xor
from collections import Counter

freqs = freq()

def xor_single_keybyte(key: int, cipher: bytes) -> bytes:
    return fixed_xor(bytes([key] * len(cipher)), cipher)

def xor_all_keybytes(cipher_text: bytes) -> list[bytes]:
    return [xor_single_keybyte(key,cipher_text) for key in range(256)]

def find_probable_cleartext(data: list[bytes]) -> bytes:
    best_score = float("inf")
    most_probable = data[0]
    for potential_cleartext in data:
        potential_cleartext_score = freq_score(potential_cleartext)
        if potential_cleartext_score < best_score:
            best_score = potential_cleartext_score
            most_probable = potential_cleartext
    return most_probable

def freq_score(potential_cleartext: bytes) -> float:
    potential_cleartext_str = ""
    score = 0.0
    for char in potential_cleartext:
        if 1 > char < 127 :  # Decimal 0 - 8 and 127 are non-printable characters.
            return float("inf")
        potential_cleartext_str += chr(char)
    for letter, frequency in freqs.items():
        count = potential_cleartext_str.count(letter)
        diff = frequency - count / len(potential_cleartext_str)
        score += diff   
    return score

def break_single_byte_xor(cipher_text: bytes) -> bytes:
    possible_cleartexts = xor_all_keybytes(cipher_text)
    probable_cleartext = find_probable_cleartext(possible_cleartexts)
    return probable_cleartext

def main() -> None:
    with open("../data/d03.txt", "r") as data:
        hex_str = data.read()
    cipher_text = bytes.fromhex(hex_str)
    print(f"Most probable cleartext is: {break_single_byte_xor(cipher_text).decode()}")

if __name__ == "__main__":
    main()