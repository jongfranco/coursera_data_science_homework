import MapReduce
import sys

mr = MapReduce.MapReduce()


def mapper(record):
    order_id = record[1]
    mr.emit_intermediate(order_id, record)


def reducer(key, list_of_values):
    for first_value in list_of_values:
        for second_value in list_of_values:
            if first_value[0] == 'order' and second_value[0] == 'line_item':
                mr.emit(first_value + second_value)

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
