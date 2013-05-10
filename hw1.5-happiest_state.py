#!/usr/bin/env python

# @dpmehta02
# Coursera Data Science HW1 - prints to stdout two letter abbreviation of happiest state from Twitter livestream data
# Requires sentiment file (e.g., AFINN-111.txt: https://code.google.com/p/fb-moody/source/browse/trunk/AFINN/AFINN-111.txt?spec=svn2&r=2)
# USAGE: $ python happiest_state.py <sentiment_file> <tweet_file>

import sys
import json
import re

# This script works, but should be refactored

def main():

  # load a tab delimited dict of sentiment scores
  afinnfile = open(sys.argv[1])
  scores = {}
  for line in afinnfile:
    term, score  = line.split("\t")
    scores[term] = int(score)

  initial_state_sentiment = {}

  # load each tweet as json
  for line in open(sys.argv[2]):
    score = 0
    tweet_json = json.loads(line)
    
    # if a tweet is sent from the US and has text ...
    if tweet_json.get('place') and tweet_json['place']['country_code'] == 'US' and tweet_json.get('text'):
      city_state = tweet_json['place']['full_name'].encode('utf8').split(', ')
      if city_state[1] != 'US':
        tweet_text = tweet_json['text'].encode('utf8').split()
        for word in tweet_text:
          # only read alphanumeric words (NEED TO LOWERCASE?)
          if re.match("^[A-Za-z0-9_-]*$", word):
            score += scores.get(word, 0)
        initial_state_sentiment.setdefault(city_state[1], []).append(score)

  state_sentiment = {}

  for key, value in initial_state_sentiment.items():
    average = sum(value) / len(value)
    state_sentiment[key] = average

  # print the two letter state abbreviation to stdout
  print max(state_sentiment, key=state_sentiment.get)

if __name__ == '__main__':
  main()
