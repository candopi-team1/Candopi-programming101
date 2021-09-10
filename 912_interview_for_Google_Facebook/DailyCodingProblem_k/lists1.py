
"""

s = "12345"
>>> s[:2]
'12'
>>> s[2:]
'345'
>>> exit()


"""


s='123'
s[1:3] # '23'
s[2:13] # '3'



li1=[4,5,6]
print(   all(val > 1 for val in li1) ) # ==> True


############## flight itinerary
>>> li1=[1,2,3,4,5,6]
>>> li1[:1]
[1]
>>> li1[1:]
[2, 3, 4, 5, 6]

>>> li1[1+1:]
[3, 4, 5, 6]


>>> li1[:1] + li1[1+1:]
[1, 3, 4, 5, 6]
>>> 

>>> for i in li1:
...   ci.append(i)
...   print(ci)
...   print( ci.pop() )
...   print(ci)
... 
[90, 90, 1]  1 [90, 90]
[90, 90, 2]  2 [90, 90]
[90, 90, 3]  3 [90, 90]
[90, 90, 4]  4 [90, 90]
[90, 90, 5]  5 [90, 90]
[90, 90, 6]  6 [90, 90]

############################## n queens
board=[1,2,3,4,5]
board[-1] # last     -> 5
board[-2] # 2nd last -> 4


board[:-1]      #  without last -> [1, 2, 3, 4]
board[:-2]      #  without 2nd last and later -> [1, 2, 3]
>>> board[:-3]  #  without 3rd last and later -> [1, 2]



for r,c in enumerate(board[:-1]):



#################### Hierholzer

>>> la = [1,2,3]
>>> next(a for a in la)
1
>>> next(a for a in la)
1
>>> next(a for a in la)
1
>>> lb=[11,445,6,7]
>>> next(a for a in lb)
11
>>> next(a for a in lb)
11

+
>>> for i in range(4):
...    lb.pop()
... 
7
6
445
11
>>> next(a for a in lb)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration




























