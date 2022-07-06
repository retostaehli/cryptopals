#!/usr/bin/env python3

import unittest
import base64
import c07

class T07(unittest.TestCase):

    def test_decrypt_aes_ecb(self):
        with open("../data/d06.txt") as data:
            ciphertext = base64.b64decode(data.read())
        key = b"YELLOW SUBMARINE"
        plaintext = c07.decrypt_aes_ecb(ciphertext, key)
        self.assertEqual(plaintext.decode().split("\n")[0], "I'm back and I'm ringin' the bell ")
if __name__ == "__main__":
    unittest.main()