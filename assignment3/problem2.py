import MapReduce
import sys

"""
Problem 1: building inverted index
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: (table, order_id)
    # value: list of tuples (db records)
    key = (record[0], record[1])
    value = record[1]
    attr = record[2,]
    mr.emit_intermediate(key, attr)

def reducer(key, list_of_values):
    # key: word
    # value: list of document IDs
    uniqueDocIds = list(set(list_of_values))
    mr.emit((key, uniqueDocIds))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
