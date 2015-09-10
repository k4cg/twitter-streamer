import datetime
import json
from twython import TwythonStreamer
import config


class MyTwythonStreamer(TwythonStreamer):

    def on_error(self, status_code, data):
        # show log info
        log_datetime = datetime.datetime.today()
        log_message = status_code + data
        logline = '[' + str(log_datetime) + '] ' + log_message
        print logline
        print logline

    def on_success(self, data):
        if 'text' in data:
            # get saved tweets
            try:
                f_trackedTweets = open(config.FILE_TRACKED_TWEETS, 'r')
                json_string_tweets = f_trackedTweets.read()
                f_trackedTweets.close()
                # as a python object array
                saved_tweets = json.loads(json_string_tweets)
            except IOError:
                saved_tweets = []

            # add the incoming tweet
            saved_tweets.append(data)

            # get json object notation string
            json_string_tweets = json.dumps(saved_tweets)

            # save to a file
            f_trackedTweets = open(config.FILE_TRACKED_TWEETS, 'w')
            f_trackedTweets.write(json_string_tweets)
            f_trackedTweets.close()

            # show log info
            log_datetime = datetime.datetime.today()
            log_message = ' Message receaved and saved. '
            log_message += 'File: ' + config.FILE_TRACKED_TWEETS
            logline = '[' + str(log_datetime) + '] ' + log_message
            print logline
