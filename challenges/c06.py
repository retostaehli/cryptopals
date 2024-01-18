#!/usr/bin/env python3

from c02 import fixed_xor
from c03 import break_single_byte_xor
from c05 import repeating_key_xor
import base64

def hamming_distance(str1: bytes, str2: bytes) -> int:
    return bin(int.from_bytes(str1, "big") ^ int.from_bytes(str2, "big")).count("1")

def find_probable_keysize(ciphertext: bytes) -> "list[int]":
    min_distance = float("inf")
    candidates = {}
    for keysize in range(2, 41):
        blocks = [ciphertext[i*keysize:i*keysize+keysize] for i in range(40)]
        hamming_distance_avg = sum(hamming_distance(blocks[i], blocks[i+1]) / keysize for i in range(39))
        candidates.update({keysize : hamming_distance_avg})
        if min_distance > hamming_distance_avg:
            min_distance = hamming_distance_avg
            best_keysize = keysize
    return sorted(candidates, key=candidates.get)[:5]

def transpose_blocks(ciphertext: bytes, blocksize: int) -> "list[bytes]":
    keysize_blocks = [ciphertext[i:i+blocksize] for i in range(0, len(ciphertext), blocksize)]
    #print(f"Blocks split by keysize is: {keysize_blocks} with length of block1: {len(keysize_blocks[0])} block2: {len(keysize_blocks[1])} total number of blocks {len(keysize_blocks)} \n\n")
    transposed_blocks = []
    for i in range(blocksize):
        transposed_block = b''.join([block[i:i+1] for block in keysize_blocks])
        transposed_blocks.append(transposed_block)
    return transposed_blocks

def find_key(cleartext: bytes, ciphertext: bytes) -> bytes:
    return fixed_xor(cleartext, ciphertext)

def break_repeating_key_xor(ciphertext: bytes) -> "list[bytes]":
    probable_keysizes = find_probable_keysize(ciphertext)
    transposed_blocks = [transpose_blocks(ciphertext, keysize) for keysize in probable_keysizes]
    probable_plaintexts = []
    for blocks in transposed_blocks:
        probable_plainblocks = [break_single_byte_xor(block) for block in blocks]
        probable_key = b''.join([find_key(probable_plainblocks[i][0:1], ciphertext[i:i+1]) for i in range(len(blocks))])
        probable_plaintexts.append(repeating_key_xor(probable_key, ciphertext))
    return probable_plaintexts

def main() -> None:
    with open("../data/d06.txt") as data:
        ciphertext = base64.b64decode(data.read())
    probable_plaintexts = break_repeating_key_xor(ciphertext)
    print(probable_plaintexts[0].decode())
    return

if __name__ == "__main__":
    main()