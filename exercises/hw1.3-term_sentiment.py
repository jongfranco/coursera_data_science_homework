#!/usr/bin/env python

# @dpmehta02
# Coursera Data Science HW1 - Script analyzes non-AFINN words in tweets for
# sentiment (negativity/positivity).
# Requires sentiment file (e.g., AFINN-111.txt:
#   https://code.google.com/p/fb-moody/source/browse/trunk/AFINN/AFINN-111.txt?spec=svn2&r=2)
# USAGE: $ python term_sentiment.py <sentiment_file> <tweet_file>

# This script works, but should be refactored

import sys
import json
import re


def main():
    # load a tab delimited dict of sentiment scores
    afinnfile = open(sys.argv[1])
    scores = {}
    for line in afinnfile:
        term, score = line.split("\t")
        scores[term] = int(score)

    tweet_sentiments = {}
    word_sentiments = {}

    # load each tweet as json
    for line in open(sys.argv[2]):
        score = 0
        tweet_json = json.loads(line)

        # only accept records with a 'text' field
        if tweet_json.get('text'):
            tweet_text = tweet_json['text'].encode('utf8').split()
            for word in tweet_text:
                # only read alphanumeric words and mentions (e.g.,
                # "@dpmehta02")
                if re.match("^@|[@A-Za-z0-9_-]*$", word):
                    score += scores.get(word, 0)
            tweet_sentiments[line] = score
            for everyword in tweet_text:
                # only read alphanumeric words and mentions (e.g.,
                # "@dpmehta02")
                if re.match("^@|[@A-Za-z0-9_-]*$", everyword):
                    word_sentiments[everyword] = tweet_sentiments[line]

    # empty dict for storing non-AFINN word sentiments
    unscored_words = {}

    # cycle through each tweet, keep running tweet score for each word not in
    # AFINN
    for line in open(sys.argv[2]):
        tweet_json = json.loads(line)

        # only accept records with a 'text' field
        if tweet_json.get('text'):
            tweet_text = tweet_json['text'].encode('utf8').split()
            for word in tweet_text:
                # only read alphanumeric words and mentions (e.g.,
                # "@dpmehta02")
                if re.match("^@|[A-Za-z0-9_-]*$", word):
                    if not scores.get(word):
                        unscored_words[word] = word_sentiments[word]

    # print full dict <term:string> <sentiment:float>
    for key, value in unscored_words.items():
        print key, float(value)

if __name__ == '__main__':
    main()
