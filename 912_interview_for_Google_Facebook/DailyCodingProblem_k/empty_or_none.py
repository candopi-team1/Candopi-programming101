#### hier holzer

>>> lb=[11,445,6,7]

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


>>> if lb:   print("not empty")
... 
>>> if not lb:   print("YES empty")
... 
YES empty
SIMILARLY 
>>> len(lb)
0



>>> dict1= {}
>>> if not dict1:   print("YES empty")
... 
YES empty

>>> len(dict1)
0
 

