import sqlite3 as dbapi

con = dbapi.connect('sqlite_db1.db')
cur = con.cursor()

# CREATE only at frist time
# cur.execute('CREATE TABLE grades(Student TEXT, Marks INTEGER)')

# cur.execute('DROP TABLE grades') # DELETE

cur.execute('INSERT INTO grades VALUES("Michael", "82")')
cur.execute('INSERT INTO grades VALUES("John", "74")')
cur.execute('INSERT INTO grades VALUES("Katy", "65")')
cur.execute('INSERT INTO grades VALUES("Miranda", "50")')
cur.execute('INSERT INTO grades VALUES("Raju", "49")')
cur.execute('INSERT INTO grades VALUES("Ahmad", "36")')


cur.execute('SELECT Student, Marks FROM grades WHERE Marks >=50')
print( "PASSED ---->", cur.fetchall())


cur.execute('SELECT Student, Marks FROM grades WHERE Marks <50')
print( "FAILED ---->", cur.fetchall())

