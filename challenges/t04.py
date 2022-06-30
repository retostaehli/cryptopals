#!/usr/bin/env python3

import unittest
import c04

class T04(unittest.TestCase):

    def test_find_single_byte_xor(self):
            with open("../data/d04.txt") as data:
                cipher_texts_str = data.readlines()
            cipher_texts_bytes = [bytes.fromhex(cipher_text_str) for cipher_text_str in cipher_texts_str]
            self.assertEqual(c04.detect_single_key_xor(cipher_texts_bytes).decode(),"Now that the party is jumping\n")

if __name__ == "__main__":
    unittest.main()