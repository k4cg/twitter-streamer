from twython import Twython
import config


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
