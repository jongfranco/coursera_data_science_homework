#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Author: Dev Mehta / dpmehta02@gmail.com
Description: Hit the Twitter API for sample tweets.
Usage: Update config/credentials.py with the appropriate access credentials,
then run: $ python hw1.1-twitterstream.py
"""

from helpers import twitter_request


def fetch_sample_tweets():
    response = twitter_request(
                url="https://stream.twitter.com/1/statuses/sample.json",
                method="GET",
                parameters=[])

    for line in response:
        print line.strip()

if __name__ == '__main__':
    fetch_sample_tweets()
