#!/usr/bin/env python3

def fixed_xor(b01: bytes, b02: bytes) -> bytes:
    xor = [i ^ j for i, j in zip(b01, b02)]
    return bytes(xor)
def main() -> None:
    with open("../data/d02.txt", "r") as f:
        s01 = f.read()
    s02 = "686974207468652062756c6c277320657965"
    b01 = bytes.fromhex(s01)
    b02 = bytes.fromhex(s02)
    xor = fixed_xor(b01, b02)
    print(xor.hex())

if __name__ == "__main__":
    main()