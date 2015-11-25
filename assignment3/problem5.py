import MapReduce
import sys

"""
Problem 5: nucleotides 
"""
mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: trimmed nucleotide
    # value: 1
    mr.emit_intermediate(record[1][0:len(record[1]) - 10], 1)

def reducer(key, list_of_values):
    # key: person
    # value: (personA, personB pairs)
    mr.emit((key))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
