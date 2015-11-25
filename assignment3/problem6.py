import MapReduce
import sys

"""
Problem 5: matrix multiplication 
"""
mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # record comes as: [a|b, i, j, value]
    matrix = record[0]
    i = record[1]
    j = record[2]
    value = record[3]
    if (matrix == "a"):
      for k in range(j):
        mr.emit_intermediate((i, k), (matrix, 0))
      mr.emit_intermediate((i, j), (matrix, value))
    else:
      for k in range(i):
        mr.emit_intermediate((j, k), (matrix, 0))
      mr.emit_intermediate((j, i), (matrix, value))
      

def reducer(key, list_of_values):
    # key: (i, j)
    # value: list of (matrix, value) tuples
    
    d = {"a":[], "b":[]}
    for (matrix, value) in list_of_values:
      d[matrix].append(value)
    
    s = 0 
    for (lv, rv) in zip(d.values()[0], d.values()[1]):
      s = s + lv * rv
      
    mr.emit((key, s))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
