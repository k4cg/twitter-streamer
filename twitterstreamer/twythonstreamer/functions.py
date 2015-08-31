from getpass import getpass
from twython import Twython
import config
from MyTwythonStreamer import MyTwythonStreamer


def getAuthTokens():
    f_authTokens = open(config.FILE_TMP_TOKENS, 'w')

    # get first auth
    twitter = Twython(config.APP_KEY, config.APP_SECRET)
    firstAuth = twitter.get_authentication_tokens()

    # get auth pin
    print 'auth url: ' + firstAuth['auth_url']
    authPin = getpass('pin: ')

    # get second auth
    twitter = Twython(
      config.APP_KEY,
      config.APP_SECRET,
      firstAuth['oauth_token'],
      firstAuth['oauth_token_secret'])
    secondAuth = twitter.get_authorized_tokens(authPin)

    # save tokens to a file
    for key in secondAuth:
        line = key + '\t' + secondAuth[key] + '\n'
        f_authTokens.write(line)

    f_authTokens.close()

    return secondAuth


def getStream():
    # Get auth tokens
    f_authTokens = open(config.FILE_TMP_TOKENS, 'r')
    tokens = {}
    for line in f_authTokens:
        line = line.strip('\n')
        key, value = line.split('\t', 1)
        tokens[key] = value
    f_authTokens.close()

    # verify credentials
    twitter = Twython(
      config.APP_KEY,
      config.APP_SECRET,
      tokens['oauth_token'],
      tokens['oauth_token_secret'])
    credentials = twitter.verify_credentials()

    # open stream
    stream = MyTwythonStreamer(
      config.APP_KEY,
      config.APP_SECRET,
      tokens['oauth_token'],
      tokens['oauth_token_secret'])

    return stream
