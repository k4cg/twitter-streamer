#!/usr/bin/python
import unittest
import twitterstreamer

class TestTwitterStreamer(unittest.TestCase):

    def test_getFirstAuth(self):
        first_auth = twitterstreamer.getFirstAuth()

        self.assertIsInstance(first_auth, dict)

        self.assertIsInstance(first_auth['oauth_token_secret'], unicode)
        self.assertNotEqual(first_auth['oauth_token_secret'], '')

        self.assertIsInstance(first_auth['auth_url'], str)
        self.assertNotEqual(first_auth['auth_url'], '')

        self.assertIsInstance(first_auth['oauth_token'], unicode)
        self.assertNotEqual(first_auth['oauth_token'], '')

        self.assertIsInstance(first_auth['oauth_callback_confirmed'], unicode)
        self.assertNotEqual(first_auth['oauth_callback_confirmed'], '')

if __name__ == '__main__':
    unittest.main()
