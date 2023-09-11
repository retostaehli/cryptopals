#!/usr/bin/env python3
import base64
from c02 import fixed_xor
from c09 import pad_pkcs7, unpad_pkcs7
from Crypto.Cipher import AES

def encrypt_aes_cbc(cleartext: bytes, iv: bytes, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    plainblocks = [cleartext[i:i+len(key)] for i in range(0, len(cleartext), len(key))]
    iv = iv
    ciphertext = b""
    for plainblock in plainblocks:
        xorblock = fixed_xor(plainblock,iv)
        aesblock = cipher.encrypt(xorblock)
        ciphertext += aesblock
        iv = aesblock
    return ciphertext

def decrypt_aes_cbc(ciphertext: bytes, iv: bytes, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    cipherblocks = [ciphertext[i:i+len(key)] for i in range(0, len(ciphertext), len(key))]
    iv = iv
    plaintext = b""
    for cipherblock in cipherblocks:
        xorblock = cipher.decrypt(cipherblock)
        plainblock = fixed_xor(xorblock,iv)
        iv = cipherblock
        plaintext += plainblock

    return plaintext

def main() -> None:
    key = b"YELLOW SUBMARINE"
    with open("../data/d10.txt", "r") as data:
        ciphertext = base64.b64decode(data.read())
    print(f"Plaintext is {unpad_pkcs7(decrypt_aes_cbc(ciphertext,bytes(len(key)),key)).decode()}")

if __name__ == "__main__":
    main()
