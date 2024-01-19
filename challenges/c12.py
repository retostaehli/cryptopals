#!/usr/bin/env python3

from secrets import token_bytes
from Crypto.Cipher import AES
from c09 import pad_pkcs7
from collections import Counter
from base64 import b64decode

key = token_bytes(16)
base64_secret = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"

def score_ecb_probability(ciphertext: bytes, blocksize: int) -> int:
    blocks = [ciphertext[i:i+blocksize] for i in range(0, len(ciphertext), blocksize)]
    blockcount = Counter(blocks)
    return blockcount.most_common(1)[0][1]

def detection_oracle(cleartext: str) -> bytes:
    decoded_secret = b64decode(base64_secret)
    cleartext_with_secret_bytes = cleartext.encode() + decoded_secret
    cleartext_with_secret_bytes = pad_pkcs7(cleartext_with_secret_bytes, 16)
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(cleartext_with_secret_bytes)

def detect_blocksize() -> tuple[int,int]:
    # Padding will ensure that the length will be a multiple of the block size. We increase the number of supplied input bytes until we notice a change in the ciphertext length (which means that the length got increase by the size of one block).
    empty_padded_length = len(detection_oracle(""))
    print(f"Length of ciphertext with empty string supplied is {empty_padded_length}")
    for i in range(256):
        if len(detection_oracle(i * "A")) - empty_padded_length > 0:
            return len(detection_oracle(i * "A")) - empty_padded_length,i

def main() -> None:
    cleartext = 6 * "AAAAAAAAAAAAAAAA"
    ciphertext_with_secret = detection_oracle(cleartext)
    print(ciphertext_with_secret)
    blocksize = detect_blocksize()
    print(f"Identified blocksize is {blocksize}")

if __name__ == "__main__":
    main()
