import re
import json

import oauth2 as oauth
import urllib2 as urllib

from config.credentials import ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, \
                               CONSUMER_KEY, CONSUMER_SECRET


def create_opener(debug_level=0):
    """Create HTTP handlers, add them to an opener and then return it."""

    http_handler = urllib.HTTPHandler(debuglevel=debug_level)
    https_handler = urllib.HTTPSHandler(debuglevel=debug_level)

    opener = urllib.OpenerDirector()
    opener.add_handler(http_handler)
    opener.add_handler(https_handler)

    return opener


def twitter_request(url, http_method, parameters):
    """Construct, sign, and open a twitter request."""

    oauth_token = oauth.Token(key=ACCESS_TOKEN_KEY, secret=ACCESS_TOKEN_SECRET)
    oauth_consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

    req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                                token=oauth_token,
                                                http_method=http_method,
                                                http_url=url,
                                                parameters=parameters)

    req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

    if http_method == "POST":
        encoded_post_data = req.to_postdata()
    else:
        encoded_post_data = None
        url = req.to_url()

    opener = create_opener(debug_level=0)
    response = opener.open(url, encoded_post_data)

    return response


def load_sentiment_dict(sentiment_file):
    """Create a sentiment:score dict from a tab-delimited
    word:sentiment_score file.
    """

    with open(sentiment_file) as afinnfile:
        scores = {}
        for line in afinnfile:
            term, score = line.split("\t")
            scores[term] = int(score)

    return scores


def print_sentiment_scores(scores, tweet_file):
    """Prints to stdout a sentiment score for each tweet in a file"""

    for line in tweet_file:
        tweet_json = json.loads(line)
        score = 0

        if tweet_json.get('text'):
            tweet_text = tweet_json['text'].encode('utf8').split()
            for word in tweet_text:
                # only read alphanumeric words (NEED TO LOWERCASE?)
                if re.match("^[A-Za-z0-9_-]*$", word):
                    score += scores.get(word, 0)
            print float(score)
