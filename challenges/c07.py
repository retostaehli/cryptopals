#!/usr/bin/env python3
import base64
from Crypto.Cipher import AES

def decrypt_aes_ecb(ciphertext: bytes, key: str) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(ciphertext)

def main() -> None:
    with open("../data/d07.txt", "r") as f:
        ciphertext = base64.b64decode(f.read())
    key = b"YELLOW SUBMARINE"
    print(decrypt_aes_ecb(ciphertext, key).decode())

if __name__ == "__main__":
    main()