#!/usr/bin/env python

# @dpmehta02
# Coursera Data Science HW1 - Script analyzes tweets for sentiment (negativity/positivity)
# Requires sentiment file (e.g., AFINN-111.txt: https://code.google.com/p/fb-moody/source/browse/trunk/AFINN/AFINN-111.txt?spec=svn2&r=2)
# USAGE: $ python tweet_sentiment.py <sentiment_file> <tweet_file>

import sys
import json
import re

def main():

  # load a tab delimited dict of sentiment scores
  afinnfile = open(sys.argv[1])
  scores = {}
  for line in afinnfile:
    term, score  = line.split("\t")
    scores[term] = int(score)

  # load each tweet as json
  for line in open(sys.argv[2]):
    score = 0
    tweet_json = json.loads(line)
    
    # only accept records with a 'text' field
    if tweet_json.get('text'):
      tweet_text = tweet_json['text'].encode('utf8').split()
      for word in tweet_text:
        # only read alphanumeric words (NEED TO LOWERCASE?)
        if re.match("^[A-Za-z0-9_-]*$", word):
          score += scores.get(word, 0)
      print float(score)


if __name__ == '__main__':
  main()
