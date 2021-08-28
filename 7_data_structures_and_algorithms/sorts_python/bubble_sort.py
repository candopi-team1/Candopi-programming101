g=[6,7,8,9,1]
g=[12.34, 11,16.45,7,8,9,1,12.345, 16.451]


length=len(g)
for i in range(length):
   for j in range(length-1):
    if g[j] > g[j+1]:
      temp=g[j]
      g[j]=g[j+1]
      g[j+1]= temp

print(g)
