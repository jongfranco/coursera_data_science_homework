# Dev Mehta dpmehta02@gmail.com
# print to stdout 10 pages of tweets based on search criteria

import urllib
import json

# for 10 pages
for i in range(10):
    # search for clippers
    response = urllib.urlopen(
        "http://search.twitter.com/search.json?q=clippers&page=%d" % (i + 1))
    data = json.load(response)

    results = len(data['results'])

    print 'Page %d' % (i + 1)
    print '_______________\n'

    # json parsed to print tweet text
    for result in range(results):
        print 'Result %s:' % (result + 1), data['results'][result]['text'], '\n'
