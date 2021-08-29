'''
from nltk.corpus import words
print words.fileids()              --------> ['en', 'en-basic']
print len(words.words('en-basic')) # 850
print len(words.words('en'))       # 234936

# this creates a new file with given name.
with open('basic850_words.txt', 'a') as handle:
  for wd in words.words('en-basic'):
      handle.write(wd+ '\n')
'''
# Now I copied that file here : basic850_words.txt

import os
from nltk.corpus import wordnet
import nltk
# OK nltk.data.path.append('D:/py_dev_2/nltk_data')
nltk.data.path.append('/home/kyawnaing/django_dev/vocab456/nltk_data')


filename = 'basic850_words.txt'
outfile = 'basic850_words_with_extras.txt'
# OK outfile = 'basic850_words_for_1.txt'
f = open(os.path.join( os.getcwd(), '', filename),  'r')
f2 = open(os.path.join( os.getcwd(), 'out', outfile),  'w')

counter = 0
for line in f:
  syns = wordnet.synsets(line.strip())

  for syn in syns:
   f2.writelines( [ str(lemma.name())+" "  for lemma in syn.lemmas()] )
   f2.writelines('\n')

   f2.writelines( syn.name())
   f2.writelines('\n')

   f2.writelines( syn.definition())
   f2.writelines('\n')

   if syn.examples():
     f2.writelines('\tExamples ::')
     for ex in syn.examples():
       f2.writelines('\t\t'+ ex)
       f2.writelines('\n')
   else:
       f2.writelines( 'No examples so far.\n')
       f2.writelines('\n')

  f2.writelines('\n')
  # OK counter += 1
  # OK if counter > 0: break


f.close()
