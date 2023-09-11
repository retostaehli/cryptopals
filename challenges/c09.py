#!/usr/bin/env python3

def pad_pkcs7(plaintext: str, blocksize: int) -> bytes:
    plaintext_bytes = bytes(plaintext, 'utf-8')
    padlength = blocksize - (len(plaintext_bytes) % blocksize)
    if padlength: #We pad to a multiple of blocksize if plaintext is not a multiple of blocksize
        return plaintext_bytes + padlength * padlength.to_bytes(1,'little')
    return plaintext_bytes + blocksize * blocksize.to_bytes(1,'little') #We add a padding of lenght blocksize

def unpad_pkcs7(plaintext: bytes) -> bytes:
    padlength = plaintext[-1]
    return plaintext[0:len(plaintext) - padlength]

def main() -> None:
    plaintext = "YELLOW SUBMARINE"
    blocksize = 20
    print(f"Padded: {pad_pkcs7(plaintext, blocksize)} - Unpadded: {unpad_pkcs7(pad_pkcs7(plaintext, blocksize))}")

if __name__ == "__main__":
    main()
