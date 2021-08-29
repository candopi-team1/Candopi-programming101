import os
import MySQLdb as dbapi

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

  sql_stmt1 ='''SELECT * FROM p6word WHERE word = %s;''' 
  cur.execute(sql_stmt1, [word])
  row= cur.fetchone();

  if row != None:
    print( row) # ->  (201L, 'inummerable', '', '', 'NTPS;; Gimm Moh;; Tao Nan')
    the_id, the_word, definition1, examples1, past_occur1= row 

    if definition1.endswith(';;'): 
       definition =definition1 +  definition
    else:
       definition =definition1 + ';;' + definition

    if examples1.endswith(';;'):   
       examples =examples1 + examples
    else:
       examples =examples1 + ';;' + examples

    if past_occur1.endswith(';;'):  
       past_occur= past_occur1 + past_occur
    else:
       past_occur= past_occur1 + ';;' + past_occur

    sql_stmt3 ='''
               UPDATE p6word 
               SET definition= %s, examples= %s, past_occur= %s  
               WHERE word=%s; ''' 
    cur.execute(sql_stmt3, [definition, examples, past_occur, word ])
    conn.commit()
    # No commit => No inserts!! 
    
  else:
    sql_stmt2 ='''
               INSERT INTO p6word(word, definition, examples, past_occur)  
               VALUES (%s, %s, %s, %s);''' 
    cur.execute(sql_stmt2, [word,  definition, examples, past_occur ])
    conn.commit()
    # No commit => No inserts!! 
        
  # OK  counter += 1
  # OK  if counter > 1: break


f.close()
