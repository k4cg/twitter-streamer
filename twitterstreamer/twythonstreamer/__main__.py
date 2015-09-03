from functions import *

if __name__ == '__main__':
    # get new tokens?
    getNewTokens = raw_input('Get new tokens? [Y/n]: ')
    if getNewTokens in ('y', 'Y'):
        getAuthTokens()

    # get stream
    stream = getStream()

    # what filter?
    track = raw_input('track [party]: ')
    if track == '':
        track = 'party'

    try:
        print "Stream opened. Waiting for tweets..."
        stream.statuses.filter(track=track)
    except KeyboardInterrupt:
        print "[KeyboardInterrupt] Stream stopped by user"
