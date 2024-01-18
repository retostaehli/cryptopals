#!/usr/bin/env python3

import unittest
import c01

class T01(unittest.TestCase):

    def test_hex_to_b64(self):
        self.assertEqual(c01.hex_to_b64("5468697349734154657374"), "VGhpc0lzQVRlc3Q=")

if __name__ == "__main__":
    unittest.main()