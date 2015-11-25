import MapReduce
import sys

"""
Problem 2: join
"""
from timeit import itertools

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: order_id
    # value: tuple (table, attr)
    key = record[1]
    mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
    # key: order_id
    # value: list of tuples (table, attr)
    recs = {}
    for value in list_of_values:
      table = value[0]
      if not table in recs:
        recs[table] = []
      recs[table].append(value)

    leftTable = recs.values()[0]    
    righTable = recs.values()[1]
    
    for r in itertools.product(leftTable, righTable):
      mr.emit(r[1] + r[0])

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
