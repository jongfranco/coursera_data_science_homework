#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Author: Dev Mehta / dpmehta02@gmail.com
Description: Print to stdout sentiment scores for each tweet in an input JSON
file. USAGE: $ python tweet_sentiment.py <sentiment_file> <tweet_file>
"""

import sys

from helpers import load_sentiment_dict, print_sentiment_scores


def calculate_tweet_sentiments():
    try:
        sentiment_lookup = load_sentiment_dict(sys.argv[1])
        with open(sys.argv[2]) as tweet_file:
            print_sentiment_scores(sentiment_lookup, tweet_file)
    except IndexError:
        print ("\nMissing arguments. USAGE: "
               "$ python tweet_sentiment.py <sentiment_file> <tweet_file>\n")
        raise
    else:
        return


if __name__ == '__main__':
    calculate_tweet_sentiments()
