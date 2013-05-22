import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
	seq_id = record[0]
	nucleotides = record[1]
	
	mr.emit_intermediate(nucleotides[:-10],seq_id)

def reducer(key, list_of_values):
	mr.emit(key)

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)