import MapReduce
import sys

"""
Problem 4: assymmetric friendship
"""
mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    (personA, personB) = record
    mr.emit_intermediate((personA, personB), 1)
    mr.emit_intermediate((personB, personA), 1)

def reducer(key, list_of_values):
    # key: (personA, personB)
    # values: list of 1s

    (person, friend) = key
    if (sum(list_of_values) == 1):
      mr.emit((friend, person))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
