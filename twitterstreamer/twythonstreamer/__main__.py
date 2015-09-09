import argparse
from functions import *

def getParsedArguments():
    argumentParser = argparse.ArgumentParser(
        description='Get a stream of tweets using twython.',
        epilog='if option -i is used, -t and -T will be ignored.')

    argumentParser.add_argument(
        '-i', '--interactive-mode',
        action='store_true',
        help='Ask for needed arguments.')

    argumentParser.add_argument(
        '-T', '--get-new-tokens',
        action='store_true',
        help='Get new auth tokens process. pin may be written by user.')

    argumentParser.add_argument(
        '-t', '--track',
        type=str, default='party', nargs='+',
        help='Show tweets that contain this text.', metavar='text')

    args = argumentParser.parse_args()

    return args

if __name__ == '__main__':
    args = getParsedArguments()
    args.track = ' '.join(args.track)

    if args.interactive_mode:
        # get new tokens?
        getNewTokens = raw_input('Get new tokens? [Y/n]: ')
        if getNewTokens in ('y', 'Y'):
            getAuthTokens() # user may enter auth pin manually

        # what filter?
        track = raw_input('track [party]: ')
        if track != '':
            args.track = track
    else:
        if args.get_new_tokens:
            getAuthTokens() # user may enter auth pin manually

    # get stream
    stream = getStream()

    print 'Stream opened. Searching for <' + args.track + '>. Waiting for tweets...'
    try:
        stream.statuses.filter(track=args.track)
    except KeyboardInterrupt:
        print "[KeyboardInterrupt] Stream stopped by user"
