#!/usr/bin/env python3

import unittest
import c10
from c09 import pad_pkcs7, unpad_pkcs7

class T10(unittest.TestCase):

    def test_aes_cbc(self):
        key = b"YELLOW SUBMARINE"
        self.assertEqual(unpad_pkcs7(c10.decrypt_aes_cbc(c10.encrypt_aes_cbc(pad_pkcs7("This is a random string to encrypt".encode(),32),bytes(len(key)),key),bytes(len(key)),key)),bytes("This is a random string to encrypt","utf8"))

if __name__ == "__main__":
    unittest.main()
