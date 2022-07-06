#!/usr/bin/env python3

import unittest
import c02

class T02(unittest.TestCase):

    def test_fixed_xor(self):
        self.assertEqual(c02.fixed_xor(bytes.fromhex("1c0111001f010100061a024b53535009181c"), bytes.fromhex("686974207468652062756c6c277320657965")).decode("utf-8"), "the kid don't play")

if __name__ == "__main__":
    unittest.main()