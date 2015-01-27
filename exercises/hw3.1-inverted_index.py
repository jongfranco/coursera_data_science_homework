import MapReduce
import sys

mr = MapReduce.MapReduce()


def mapper(record):
    # key: document identifier
    # value: document contents
    # used words to prevent dupes
    used = []

    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
        if w not in used:
            mr.emit_intermediate(w, key)
            used.append(w)


def reducer(key, list_of_values):
    mr.emit((key, list_of_values))

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
