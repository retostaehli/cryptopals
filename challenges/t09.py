#!/usr/bin/env python3

import unittest
import c09

class T09(unittest.TestCase):

    def test_pad_pkcs7(self):
        self.assertEqual(c09.pad_pkcs7("YELLOW SUBMARINE", 20),b"YELLOW SUBMARINE\x04\x04\x04\x04")
        self.assertEqual("Some sample string to pad", c09.unpad_pkcs7(c09.pad_pkcs7("Some sample string to pad", 7)).decode())
        self.assertEqual("Some other string to pad", c09.unpad_pkcs7(c09.pad_pkcs7("Some other string to pad", 20)).decode())

if __name__ == "__main__":
    unittest.main()