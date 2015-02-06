#!/usr/bin/python
# -*- coding: utf-8 -*-

from helpers import twitter_request


def fetch_sample_tweets():
    """Hit the Twitter API for sample tweets. Update config/credentials.py
    with the appropriate access credentials before running this script.
    """

    response = twitter_request(
            url="https://stream.twitter.com/1/statuses/sample.json",
            method="GET",
            parameters=[])

    for line in response:
        print line.strip()

if __name__ == '__main__':
    fetch_sample_tweets()
