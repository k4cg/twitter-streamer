#!/bin/bash

chmod ug+x *
./test_constants.py
./test_twitter_api_connection.py
./test_my_twython_streamer.py

