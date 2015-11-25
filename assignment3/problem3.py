import MapReduce
import sys

"""
Problem 3: counting friends
"""
mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person
    # value: 1
    mr.emit_intermediate(record[0], 1)
    #mr.emit_intermediate(record[1], 1)

def reducer(key, list_of_values):
    # key: person
    # value: list of 1s
    mr.emit((key, sum(list_of_values)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
