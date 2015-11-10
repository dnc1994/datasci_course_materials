import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    order_list=[]
    item_list=[]
    for v in list_of_values:
      if v[0]=='order': order_list.append(v)
      else: item_list.append(v)
    for v in order_list:
      for vv in item_list:
        mr.emit(v+vv)
        #mr.emit(len(v+vv))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
