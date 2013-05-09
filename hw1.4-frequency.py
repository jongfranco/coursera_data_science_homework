#!/usr/bin/env python

# @dpmehta02
# Coursera Data Science HW1 - compute term frequency of Twitter livestream data
# USAGE: $ python frequency.py <tweet_file>

import sys
import json
import re
from collections import Counter

def main():
  all_words = []
  # load each tweet as json
  for line in open(sys.argv[1]):
    tweet_json = json.loads(line)
    # only accept records with a 'text' field
    if tweet_json.get('text'):
      tweet_text = tweet_json['text'].encode('utf8').split()
      for word in tweet_text:
        # only read alphanumeric words and mentions (e.g., "@dpmehta02")
        if re.match("^@|[@A-Za-z0-9_-]*$", word):
          all_words.append(word)

  words_hash = Counter(all_words)
  denominator = float(sum(words_hash.values()))
  frequency_dict = {}
  for (key, value) in words_hash.items():
    frequency_dict[key] = float(value/denominator)

  # print term frequencies <term:string> <frequency:float>
  for (key, value) in frequency_dict.items():
    print key, value

if __name__ == '__main__':
    main()
