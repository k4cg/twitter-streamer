from twython import Twython
import config


def getAuthPin():
    f_firstAuth = open('.tmp_firstAuth', 'r')
    f_authPin = open('.tmp_authPin', 'w')

    # check if first auth was receaved
    firstAuth = {}
    for line in f_firstAuth:
      key, value = line.split('\t')
      firstAuth[key] = value

    # if first auth not receaved, get new one
    if 'auth_url' in firstAuth.keys() and firstAuth['auth_url'] == '':
      firstAuth = getFirstAuth()

    # get auth pin
    print 'Go to this link and allow twitter access: ' + firstAuth['auth_url']
    authPin = raw_input('Enter auth pin: ')

    # and save it to a file
    f_authPin.write(authPin)

    f_firstAuth.close()
    f_authPin.close()
    return authPin


def getFirstAuth():
    f_firstAuth = open('.tmp_firstAuth', 'w')

    # get first auth
    twitter = Twython(config.APP_KEY, config.APP_SECRET)
    firstAuth = twitter.get_authentication_tokens()

    # and save it to a file
    for key in firstAuth:
      line = key + '\t' + firstAuth[key] + '\n'
      f_firstAuth.write(line)

    f_firstAuth.close()
    return firstAuth
