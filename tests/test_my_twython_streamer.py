#!/usr/bin/python

import os
import sys
from twython import Twython
import unittest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from constants import *
from MyTwythonStreamer import MyTwythonStreamer


class TestMyTwythonStreamer(unittest.TestCase):

    def test_my_twython_streamer(self):
        twitter = Twython(APP_KEY, APP_SECRET)
        first_auth = twitter.get_authentication_tokens()
        self.assertNotEqual(first_auth['oauth_token'], '')
        self.assertNotEqual(first_auth['oauth_token_secret'], '')
        self.assertNotEqual(first_auth['auth_url'], '')
        OAUTH_TOKEN = first_auth['oauth_token']
        OAUTH_TOKEN_SECRET = first_auth['oauth_token_secret']
        URL_SECRET = first_auth['auth_url']
        print URL_SECRET
        PIN_CODE = raw_input('Pin code: ')
        twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        final_tokens = twitter.get_authorized_tokens(PIN_CODE)
        self.assertNotEqual(final_tokens['oauth_token'], '')
        self.assertNotEqual(final_tokens['oauth_token_secret'], '')
        FINAL_OAUTH_TOKEN = final_tokens['oauth_token']
        FINAL_OAUTH_TOKEN_SECRET = final_tokens['oauth_token_secret']
        twitter = Twython(
            APP_KEY,
            APP_SECRET,
            FINAL_OAUTH_TOKEN,
            FINAL_OAUTH_TOKEN_SECRET
        )
        credentials = twitter.verify_credentials()
        self.assertNotEqual(credentials['screen_name'], '')
        stream = MyTwythonStreamer(
            APP_KEY,
            APP_SECRET,
            FINAL_OAUTH_TOKEN,
            FINAL_OAUTH_TOKEN_SECRET
        )
        self.assertIsNotNone(stream.statuses)


if __name__ == '__main__':
    unittest.main()
