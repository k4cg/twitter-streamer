import datetime
import json
from twython import TwythonStreamer
import config


class MyTwythonStreamer(TwythonStreamer):

    def on_error(self, status_code, data):
        print status_code, data

    def on_success(self, data):
        if 'text' in data:
            # get json object notation string
            json_string_data = json.dumps(data)

            # line to save into a file
            line = json_string_data + '\n'

            # save to a file
            f_trackedTweets = open(config.FILE_TRACKED_TWEETS, 'a')
            f_trackedTweets.write(line)
            f_trackedTweets.close()

            # show log info
            log_datetime = datetime.datetime.today()
            log_message = ' Message receaved and saved. '
            log_message += 'File: ' + config.FILE_TRACKED_TWEETS
            logline = '[' + str(log_datetime) + '] ' + log_message
            print logline
