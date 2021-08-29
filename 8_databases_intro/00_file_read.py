import os
from datetime import datetime  as dt


out_file = 'kool1.txt'
f = open(os.path.join( os.getcwd(), 'out', out_file),  'r+')


# OK file_read=f.read()
# OK print file_read # ---> all of the file contents

''' OK
file_readline = f.readline()
print file_readline
print f.readline()
print f.readline()
print f.readline()
print f.readline()
try:
  print '1', f.readline()
  print '2', f.readline()
  print 'No exception thrown, but empty.'
except Exception as ee:
  print ee
'''

''' OK
file_readlines = f.readlines()
print len(file_readlines)
# 5
'''

for line in f:
  print( line)


f.write("\nIt looks fine")
f.write("\nThis looks fine")
f.close()




