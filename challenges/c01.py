#!/usr/bin/env python3

import base64
def hex_to_b64(hex_str: str) -> str:
    return base64.b64encode(bytes.fromhex(hex_str)).decode("utf-8")

def main() -> None:
    with open("../data/d01.txt", "r") as f:
        print(hex_to_b64(f.read().strip()))

if __name__ == "__main__":
    main()