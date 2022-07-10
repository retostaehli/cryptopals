#!/usr/bin/env python3

import unittest
import base64
import c06

class T06(unittest.TestCase):

    def test_hamming_distance(self):
        self.assertEqual(c06.hamming_distance(bytes("this is a test".encode()), bytes("wokka wokka!!!".encode())), 37)
        self.assertEqual(c06.hamming_distance(bytes("this is a test".encode()), bytes("this is a test".encode())), 0)

    def test_break_repeating_key_xor(self):
        with open("../data/d06.txt") as data:
            ciphertext = base64.b64decode(data.read())
        self.assertEqual(c06.break_repeating_key_xor(ciphertext)[0].decode().split("\n")[0], "I'm back and I'm ringin' the bell ")
        
if __name__ == "__main__":
    unittest.main()