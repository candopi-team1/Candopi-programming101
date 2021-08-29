import MySQLdb as dbapi
conn = dbapi.connect(host='localhost', user='hmktest',
                     passwd='hmktestpass', db='hmk1')
cur = conn.cursor()

sql_st1="""
INSERT INTO abcd1 ( name,  location,  price)
values(%s, %s, %s);
  
"""


nam="hmk"
loc = 'CLEMENTI AVE2 '
price = 123.45
cur.execute(sql_st1, [nam, loc, str(price)])

conn.commit()
