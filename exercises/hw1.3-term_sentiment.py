#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from helpers import load_sentiment_dict, get_tweet_sentiments, \
    get_word_sentiments, get_unscored_words


def main():
    """Print to stdout a sentiment score for each non-AFINN word in an input
    JSON file.

    USAGE: $ python term_sentiment.py <sentiment_file> <tweet_file>
    """

    try:
        scores = load_sentiment_dict(sys.argv[1])
        tweet_sentiments = get_tweet_sentiments(scores, sys.argv[2])
    except IndexError:
        print ("\nMissing arguments. USAGE: "
               "$ python term_sentiment.py <sentiment_file> <tweet_file>\n")
        raise

    word_sentiments = get_word_sentiments(tweet_sentiments, sys.argv[2])
    unscored_words = get_unscored_words(
        scores, word_sentiments, sys.argv[2])

    for key, value in unscored_words.iteritems():
        print key, float(value)

if __name__ == '__main__':
    main()
