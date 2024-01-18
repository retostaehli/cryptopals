#!/usr/bin/env python3

import unittest
import c03

class T03(unittest.TestCase):

    def test_break_single_byte_xor(self):
        self.assertEqual(c03.break_single_byte_xor(bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")).decode(),"Cooking MC's like a pound of bacon")

if __name__ == "__main__":
    unittest.main()