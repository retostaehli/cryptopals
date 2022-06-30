#!/usr/bin/env python3

from c02 import fixed_xor

def repeating_key_xor(key: bytes, cleartext: bytes) -> bytes:
    extended_key = (key + key * int((len(cleartext) / len(key))))[:len(cleartext)]
    ciphertext = fixed_xor(cleartext, extended_key)
    return ciphertext

def main() -> None:
    key = "ICE"
    cleartext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    ciphertext = repeating_key_xor(bytes(key.encode()), bytes(cleartext.encode()))
    print(ciphertext.hex())
    return

if __name__ == "__main__":
    main()