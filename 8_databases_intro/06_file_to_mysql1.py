import os
import MySQLdb as dbapi

"""
(1)
CREATE DATABASE IF NOT EXISTS wordnet2my;

CREATE USER 'gliagood' IDENTIFIED BY 'gliagoodpass';
GRANT ALL ON wordnet2my.* TO  "gliagood";


conn = dbapi.connect(host='localhost', user='gliagood',
                     passwd='gliagoodpass', db='wordnet2my')

(2) Create tables with file_to_mysql_Wordnet.txt
                     
"""
conn = dbapi.connect(host='localhost', user='gliagood',
                     passwd='gliagoodpass', db='wordnet2my')
cur = conn.cursor()



filename = 'p6words.txt'
f = open(os.path.join( os.getcwd(), '', filename),  'r')
FILE_COLUMN_SEPERATOR='-;;'

counter = 0
for line in f:
  line = line.strip()
  if line == '': continue
  if line.startswith('##'): continue

  splits= line.split(FILE_COLUMN_SEPERATOR)
  splits= [e.strip() for e in splits]

  word,  definition, examples, past_occur = splits

  sql_stmt ='''
               INSERT INTO p6word(word, definition, examples, past_occur)  
               VALUES (%s, %s, %s, %s);''' 


  cur.execute(sql_stmt, [word,  definition, examples, past_occur ])
  conn.commit()
  # No commit => No inserts!! 
        
  # OK  counter += 1
  # OK  if counter > 1: break


f.close()
