from twython import TwythonStreamer


class MyTwythonStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')
            # Want to disconnect after the first result?
            # self.disconnect()

    def on_error(self, status_code, data):
        print status_code, data
        # Requires Authentication as of Twitter API v1.1
