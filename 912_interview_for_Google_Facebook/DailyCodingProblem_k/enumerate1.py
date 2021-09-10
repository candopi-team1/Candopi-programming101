
m = [[4,7],
    [3, 6],
    [2, 5] 

   ]

e1=enumerate(m)

for index, row in e1: 
  print(index, row)

"""==>
0 [4, 7]
1 [3, 6]
2 [2, 5]
"""

row = [4, 7]
e2=  enumerate(row)

for index, col in e2: 
  print(index, col)


"""==>

0 4
1 7

"""
