import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

N=5

def mapper(record):
	key = record[0]
	row=record[1]
	col=record[2]
	value = record[3]
	for x in xrange(0,N):
		if key=='a':
			mr.emit_intermediate((row,x), (key,col,value))
		else:
			mr.emit_intermediate((x,col), (key,row,value))

def reducer(key, list_of_values):
    a={}
    b={}
    for v in list_of_values:
      if v[0]=='a': a[v[1]]=int(v[2])
      else: b[v[1]]=int(v[2])
    s=0
    for v in a:
        if v in b: s+=a[v]*b[v]
    if s!=0:
        mr.emit((int(key[0]),int(key[1]),s))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
