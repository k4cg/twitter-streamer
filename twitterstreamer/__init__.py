from twython import Twython
import config


def getAuthTokens():
    f_authTokens = open('.tmp_tokens', 'w')

    # get first auth
    twitter = Twython(config.APP_KEY, config.APP_SECRET)
    firstAuth = twitter.get_authentication_tokens()

    # get auth pin
    print 'auth url: ' + firstAuth['auth_url']
    authPin = raw_input('pin: ')

    # get second auth
    twitter = Twython(config.APP_KEY, config.APP_SECRET, firstAuth['oauth_token'], firstAuth['oauth_token_secret'])
    secondAuth = twitter.get_authorized_tokens(authPin)

    # save tokens to a file
    for key in secondAuth:
        line = key + '\t' + secondAuth[key] + '\n'
        f_authTokens.write(line)

    f_authTokens.close()

    return secondAuth
