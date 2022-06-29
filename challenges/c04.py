#!/usr/bin/env python3

from encodings import utf_8
from gettext import find
from c03 import break_single_byte_xor, find_probable_cleartext

def detect_single_key_xor(cipher_texts: list[bytes]) -> bytes:
    potential_cleartexts = [break_single_byte_xor(cipher_text) for cipher_text in cipher_texts]
    return find_probable_cleartext(potential_cleartexts)

def main() -> None:
    with open("../data/d04.txt") as data:
        cipher_texts_str = data.readlines()
    cipher_texts_bytes = [bytes.fromhex(cipher_text_str) for cipher_text_str in cipher_texts_str]
    probable_cleartext = detect_single_key_xor(cipher_texts_bytes).decode()
    print(probable_cleartext)
    return

if __name__ == "__main__":
    main()