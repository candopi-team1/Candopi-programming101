import os
from datetime import datetime  as dt

if not os.path.isdir('out'):
  os.mkdir('out')

# LINUX out_file = '%s_%s.k1' % ('title',  dt.utcnow())

out_file = "windows1.txt"

f = open(os.path.join( os.getcwd(), 'out', out_file),  'w')

f.write('test 123 last')
f.close()




