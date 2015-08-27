#!/bin/bash

# Test PEP8
pep8 ../constants.py
pep8 ../globals.py
pep8 ../__init__.py
pep8 ../main.py
pep8 test_my_twython_streamer.py
pep8 test_twitter_api_connection.py

chmod ug+x *
./test_twitter_api_connection.py
./test_my_twython_streamer.py

