import MySQLdb as dbapi

conn = dbapi.connect(host='localhost', user='hmktest',
                     passwd='hmktestpass', db='hmk1')
cur = conn.cursor()

sql_st1="""
CREATE TABLE abcd1 (
  id int(11) NOT NULL AUTO_INCREMENT,
  name varchar(250) NOT NULL,
  location varchar(250) NOT NULL,
  price decimal(7,2) NOT NULL,
  PRIMARY KEY (id)
);
"""

cur.execute(sql_st1, [])
