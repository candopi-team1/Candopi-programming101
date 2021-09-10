"""
03 Aug 2020

cd /home/kyawnaing/dailycp/dynamic_prog
python3.5 staircase_dynamic_pg161.py

"""

def staircase(n, X):
 cache=[ 0 for _ in range(n+1)]
 cache[0]=1

 for i in range(1, n+1):
  cache[i] += sum(cache[i - step]  for step in X if (i - step) >=0 ) 


 return cache[n] 


########################################################################################
n=1
n=3
X=[0, 1,2,3]

ways= staircase(n, X)
print(ways)



########################################################################################
n= 23              # 755476 --fast
# X=[-5, 0, 1,2,3] # BAD # X=[0, 0, 1, 0, -3]
X=[0, 0, 1, 0, 0]  # 1
X=[0, 1,2,3]


ways= staircase(n, X)
print(ways)



########################################################################################
n=23
n=235           # 525002197928794521302227501771093376241406960614563414353020013033137 ---- fast !!!

X=[1,2,3,4,5]   # 3040048 -- fast

ways= staircase(n, X)
print(ways)



