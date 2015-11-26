import MapReduce
import sys

"""
Problem 5: matrix multiplication 
"""
mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

n = 5

def mapper(record):
    # record comes as: [a|b, i, j, value]
    matrix = record[0]
    i = record[1]
    j = record[2]
    value = record[3]
    if (matrix == "a"):
      for k in range(n):
        mr.emit_intermediate((i, k), (matrix, j, value))
    else:
      for k in range(n):
        mr.emit_intermediate((k, j), (matrix, i, value))
      

def reducer(key, list_of_values):
    # key: (i, j)
    # value: list of (matrix, value) tuples
    
    a = {}
    b = {}
    for (matrix, j, value) in list_of_values:
      if (matrix == "a"):
        a[j] = value
      else:
        b[j] = value
        
    s = 0 
    for j in range(n):
      lv = a[j] if j in a else 0
      rv = b[j] if j in b else 0
      s += lv * rv
      
    mr.emit((key[0], key[1], s))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
