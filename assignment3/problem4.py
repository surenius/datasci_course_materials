import MapReduce
import sys

"""
Problem 4: assymmetric friendship
"""
mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person
    # value: 1
    mr.emit_intermediate(record[0], record)

def reducer(key, list_of_values):
    # key: person
    # value: (personA, personB pairs)
    ...
    mr.emit((key, sum(list_of_values)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
