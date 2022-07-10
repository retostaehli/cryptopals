#!/usr/bin/env python3

from collections import Counter

from numpy import block

def detect_aes_ecb(ciphertexts: list[bytes], blocksize: int) -> tuple[bytes, int]:
    max_occurence = 0

    for ciphertext in ciphertexts:
        blocks = [ciphertext[i:i+blocksize] for i in range(0, len(ciphertext), blocksize)]
        blockcount = Counter(blocks)
        max_duplicates = blockcount.most_common(1)[0][1]
        if max_occurence < max_duplicates:
            max_occurence = max_duplicates
            probable_aes_ecb = ciphertext
    return probable_aes_ecb, max_occurence

def main() -> None:
    with open("../data/d08.txt", "r") as f:
        ciphertexts = [bytes.fromhex(ciphertext) for ciphertext in f.readlines()]
    probable_aes_ecb = detect_aes_ecb(ciphertexts, 16)
    print(f"Most probable ciphertext with AES ECB is: {probable_aes_ecb[0].hex()} with {probable_aes_ecb[1]} duplicate blocks")

if __name__ == "__main__":
    main()