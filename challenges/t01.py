#!/usr/bin/env python3

import unittest
import c01

class T01(unittest.TestCase):

    def test_hex_to_b64(self):
        self.assertEqual(c01.hex_to_b64(bytes.fromhex("1c0111001f010100061a024b53535009181c"), bytes.fromhex("686974207468652062756c6c277320657965")).hex(),"746865206b696420646f6e277420706c6179")

if __name__ == "__main__":
    unittest.main()