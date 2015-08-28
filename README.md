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

You can use twitterstreamer from the console (_CLI_) or as a _package_ in your own python project.

**cli**

Run python on interactive mode:

```
$ python
Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

and then

```python
>>> import twitterstreamer
>>> twitterstreamer.getAuthTokens() # You should execute this only the first time or when your tokens are expired.
>>> stream = twitterstreamer.getStream() # get a twython streamer, which is not started yet.
>>> stream.statuses.filter(track='text to search') # open and start a stream. It is a blocking command.
```

If you already have the auth tokens, you can execute the package in an interactive mode.

```
$ python twitterstreamer/__init__.py
```


**Package**

```python
import twitterstreamer
twitterstreamer.getAuthTokens() # You should execute this only the first time or when your tokens are expired.
stream = twitterstreamer.getStream() # get a twython streamer, which is not started yet.
stream.statuses.filter(track='text to search') # open and start a stream. It is a blocking command.
```
