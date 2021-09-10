"""
03 Aug 2020

cd /home/kyawnaing/dailycp/dynamic_prog
python3.5 staircase_recur_pg16.py


"""

def staircase(n, X):
  if n < 0:
    return 0

  elif n == 0:
    return 1


  return sum(staircase( n - step, X)  for step in X if step > 0 ) 


n=1
n= 23           # 755476 -- slow with recursion

X=[-5, 0, 1,2,3]
X=[1,2,3,4,5]   # 3040048 -- slow with recursion

ways= staircase(n, X)
print(ways)
