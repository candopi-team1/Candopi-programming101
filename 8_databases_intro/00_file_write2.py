import os
from datetime import datetime  as dt

if not os.path.isdir('out'):
  os.mkdir('out')

title= "kyaw"
# LINUX out_file = '%s_%s.txt' % (title,  dt.utcnow())
out_file = "windows2.txt"

f = open(os.path.join( os.getcwd(), 'out', out_file),  'w')


f.write('Is this head line?')
f.write('Is this 2nd head line?')
# --> Is this head line?Is this 2nd head line?

f.write('\nBe third line?\n')
f.write('Now Line No 4.')
f.close()



details= ['Course Name\t', 'Room\t','Fees\t', 'Venue\t', 'Instructor']
f = open(os.path.join( os.getcwd(), 'out', out_file),  'a+')
f.writelines('\n')
f.writelines(details)

f.writelines('\n')
f.writelines(details)

f.close()




