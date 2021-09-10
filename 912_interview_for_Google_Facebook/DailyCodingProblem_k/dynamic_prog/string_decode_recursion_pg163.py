"""
02 Aug 2020

cd /home/kyawnaing/dailycp/dynamic_prog
python3.5 string_decode_recursion_pg163.py


"""
sz= None
sz= "1234511"
sz='123'
sz='125'
sz='1251'
sz='1231'
sz='12319'

# sz= "1212511"
# sz= "31"
# sz= "11"

def num_encodings(sz, tot=0, msg="FIRST"):
   print( "Entering ", sz, ", ", msg)
   if sz ==None:
      return 0
   elif  sz.startswith('0'):
      return 0

   elif len(sz) <=1 :
       print( " ADDING 1")
       return 1

   news = sz[1:]
   tot = tot+ num_encodings(news, msg="AFTER 1")
 
   if int(sz[:2]) <= 26 :            
          news = sz[2:]
          # print(len(news))
          tot = tot+ num_encodings(news, msg="AFTER 2")

   return tot

print(sz)       
print( num_encodings(sz)    )

"""
12319
Entering  12319 ,  FIRST
Entering  2319 ,  AFTER 1
Entering  319 ,  AFTER 1
Entering  19 ,  AFTER 1

Entering  9 ,  AFTER 1
 ADDING 1

Entering   ,  AFTER 2
 ADDING 1



Entering  19 ,  AFTER 2
Entering  9 ,  AFTER 1
 ADDING 1
Entering   ,  AFTER 2
 ADDING 1


Entering  319 ,  AFTER 2
Entering  19 ,  AFTER 1
Entering  9 ,  AFTER 1
 ADDING 1
Entering   ,  AFTER 2
 ADDING 1
6

"""
