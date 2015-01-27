#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Author: Dev Mehta / dpmehta02@gmail.com
Description: Hit the Twitter API for sample tweets.
Usage: Update config/credentials.py with the appropriate access credentials,
then run: $ python hw1.1-twitterstream.py
"""

import oauth2 as oauth
import urllib2 as urllib

from config.credentials import ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET


def create_opener(debug_level=0):
    """Create HTTP handlers, add them to an opener and then return it."""
    
    http_handler = urllib.HTTPHandler(debuglevel=debug_level)
    https_handler = urllib.HTTPSHandler(debuglevel=debug_level)
    opener = urllib.OpenerDirector()
    opener.add_handler(http_handler)
    opener.add_handler(https_handler)
    return opener


def twitter_request(url, method, parameters):
    """Construct, sign, and open a twitter request."""

    oauth_token = oauth.Token(key=ACCESS_TOKEN_KEY, secret=ACCESS_TOKEN_SECRET)
    oauth_consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

    http_method = "GET"

    req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                                token=oauth_token,
                                                http_method=http_method,
                                                http_url=url,
                                                parameters=parameters)

    req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

    headers = req.to_header()

    if http_method == "POST":
        encoded_post_data = req.to_postdata()
    else:
        encoded_post_data = None
        url = req.to_url()

    _debug_level = 0
    opener = create_opener(_debug_level)
    response = opener.open(url, encoded_post_data)

    return response


def fetch_samples():
    url = "https://stream.twitter.com/1/statuses/sample.json"
    parameters = []
    response = twitter_request(url, "GET", parameters)
    for line in response:
        print line.strip()

if __name__ == '__main__':
    fetch_samples()
