# twitter-streamer


### Description

Get tweets filtered by geolocation and text message


### Dependencies

Versions tested
- Python 2.7.6 (ubuntu: sudo apt-get install python)
- Twython 3.3.0 (ubuntu: sudo apt-get install python-pip && sudo pip install twython)


### Requisites

**app key** and **app key secret** to make an oAuth connection to twitter.
You may have a twitter account and create an app on https://apps.twitter.com/.

After the configuration, you can obtain these keys on https://apps.twitter.com/app/{YOUR_APP_ID}/keys


### Installation

This package does not provide any installation method. The package folder (_twitterstreamer_) may be downloaded and placed manually.

### Configuration

Edit the file _twitterstreamer/config.py_ with your text editor.
Put your twitter keys on the correct place.
By default, the tracked tweets will be save on file _.tracked_tweets.txt_. If you want to save them on other file, change the value of variable _FILE_TRACKED_TWEETS_.

### Usage

You can use twitterstreamer as a command (_CLI_) or as a _package_ in your own python project.

**cli**

Execute this command to get more information:

```
$ python twitterstreamer/twythonstreamer/ -h
```

If you have not the auth tokens yet, you should use the -T parameter, or the iteractive mode.  
You could obtain the tokens from the twitter apps web page and write them on the config file manually.

```
$ python twitterstreamer/twythonstreamer/ -T -t sunset # Get new tokens proccess and search for "sunset" in tweets.
$ python twitterstreamer/twythonstreamer/ -i # You will be asked for needed parameters.
```


**Package**

```python
import twitterstreamer
twitterstreamer.getAuthTokens() # You should execute this only the first time or when your tokens are expired.
stream = twitterstreamer.getStream() # get a twython streamer, which is not started yet.
stream.statuses.filter(track='text to search') # open and start a stream. It is a blocking command.
```
