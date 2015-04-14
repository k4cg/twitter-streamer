#!/usr/bin/python

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from constants import *
import unittest


class TestConstants(unittest.TestCase):

    def test_tokens_are_not_empty(self):
        self.assertNotEqual(APP_KEY, '')
        self.assertNotEqual(APP_SECRET, '')

if __name__ == '__main__':
    unittest.main()
