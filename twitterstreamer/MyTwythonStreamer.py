import json
from twython import TwythonStreamer
import config


class MyTwythonStreamer(TwythonStreamer):

    def on_error(self, status_code, data):
        print status_code, data
        # Requires Authentication as of Twitter API v1.1

    def on_success(self, data):
        if 'text' in data:
            json_string_data = json.dumps(data)
            line = json_string_data + '\n'
            f_trackedTweets = open(config.FILE_TRACKED_TWEETS, 'a')
            f_trackedTweets.write(line)
            f_trackedTweets.close()
            # Want to disconnect after the first result?
            # self.disconnect()
