#!/usr/bin/python

import os
import sys
from twython import Twython
import unittest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from constants import *


class TestTwitterApiConnection(unittest.TestCase):

    def test_obtain_first_auth(self):
        twitter = Twython(APP_KEY, APP_SECRET)
        first_auth = twitter.get_authentication_tokens()
        self.assertNotEqual(first_auth['oauth_token'], '')
        self.assertNotEqual(first_auth['oauth_token_secret'], '')
        self.assertNotEqual(first_auth['auth_url'], '')

if __name__ == '__main__':
    unittest.main()
