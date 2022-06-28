#!/usr/bin/env python3

from h01 import freq
from c02 import fixed_xor
from collections import Counter

def xor_single_keybyte(key: int, cipher: bytes) -> bytes:
    return fixed_xor(bytes([key] * len(cipher)), cipher)

def xor_all_keybytes(cipher: bytes) -> list[bytes]:
    return [xor_single_keybyte(key,cipher) for key in range(256)]

def find_probable_cleartext(data: list[bytes]) -> bytes:
    for potential_cleartext in data:
        freq_score(potential_cleartext)
    return 

def freq_score(data: bytes) -> float:
    freqs = freq()
    score = float("inf")
    print("Enter loop")
    for char in data:
        if 32 > char or char > 128:  # Decimal 0-31 (0x00-1F) and 127 (0x7F) are non-printable characters.
            print(f"Breaking... Char is {char}")
            return float("inf")
    return score

def main() -> None:
    with open("../data/d03.txt", "r") as data:
        hex_str = data.read()
    cipher_bytes = bytes.fromhex(hex_str)
    possible_cleartexts = xor_all_keybytes(cipher_bytes)
    probable_cleartext = find_probable_cleartext(possible_cleartexts)

if __name__ == "__main__":
    main()