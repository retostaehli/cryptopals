#!/usr/bin/env python3

from random import randrange
from secrets import token_bytes
from Crypto.Cipher import AES
from c09 import pad_pkcs7
from c10 import encrypt_aes_cbc
from collections import Counter

def score_ecb_probability(ciphertext: bytes, blocksize: int) -> int:
    blocks = [ciphertext[i:i+blocksize] for i in range(0, len(ciphertext), blocksize)]
    blockcount = Counter(blocks)
    return blockcount.most_common(1)[0][1]

def detection_oracle(cleartext: str) -> bool:
    key = token_bytes(16)
    cleartext_bytes = bytes(randrange(5,11)) + cleartext.encode() + bytes(randrange(5,11))
    cleartext_bytes = pad_pkcs7(cleartext_bytes, 16)
    if randrange(2) == 0:
        ciphertext = encrypt_aes_cbc(cleartext_bytes, token_bytes(16), key)
    else:
        cipher = AES.new(key, AES.MODE_ECB)
        ciphertext = cipher.encrypt(cleartext_bytes)
    if score_ecb_probability(ciphertext, 16) > 1:
       return True
    return False

def main() -> None:
    if detection_oracle("This string will be encrypted under ECB or CBC. No one knows which one will be used. If we just have some random input we can not control, it will be hard. If we can control the input, it is doable"):
        print("Encrypted using ECB")
    else:
        print("Encrypted using CBC")
    if detection_oracle(6 * "YELLOW SUBMARINE"):
        print("Encrypted using ECB")
    else:
        print("Encrypted using CBC")

if __name__ == "__main__":
    main()
