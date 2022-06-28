#!/usr/bin/env python3

from h01 import freq
from c02 import fixed_xor
from collections import Counter

def xor_single_keybyte(key: int, cipher: bytes) -> bytes:
    return fixed_xor(bytes([key] * len(cipher)), cipher)

def xor_all_keybytes(cipher: bytes) -> list[bytes]:
    return [xor_single_keybyte(key,cipher) for key in range(256)]

def find_probable_cleartext(data: list[bytes]) -> bytes:
    best_score = float("inf")
    for potential_cleartext in data:
        potential_cleartext_score = freq_score(potential_cleartext)
        if potential_cleartext_score < best_score:
            best_score = potential_cleartext_score
            most_probable = potential_cleartext
    return most_probable

def freq_score(potential_cleartext: bytes) -> float:
    freqs = freq()
    potential_cleartext_str = ""
    score = 0.0
    for char in potential_cleartext:
        if 32 > char or char > 128:  # Decimal 0-31 (0x00-1F) and 127 (0x7F) are non-printable characters.
            return float("inf")
        potential_cleartext_str += chr(char)
    for letter, frequency in freqs.items():
        count = potential_cleartext_str.count(letter)
        diff = frequency - count / len(potential_cleartext_str)
        score += diff   
    return score

def break_single_byte_xor(hex_str: str) -> bytes:
    cipher_bytes = bytes.fromhex(hex_str)
    possible_cleartexts = xor_all_keybytes(cipher_bytes)
    probable_cleartext = find_probable_cleartext(possible_cleartexts)
    return probable_cleartext

def main() -> None:
    with open("../data/d03.txt", "r") as data:
        hex_str = data.read()
    print(f"Most probable cleartext is: {break_single_byte_xor(hex_str).decode()}")

if __name__ == "__main__":
    main()