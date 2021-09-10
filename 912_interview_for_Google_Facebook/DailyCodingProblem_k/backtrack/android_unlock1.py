"""
04 Aug 2020
cd /home/kyawnaing/dailycp/backtrack
python3.5  android_unlock1.py

"""

"""
(1) partial solution
(2) validate the solution so far
(3) checks if the solution is complete

 backtrack :: append/add/set value --> remove/pop/reset value
"""

from unlock_jumps import JUMPS


def num_paths(current, JUMPS, visited, n):
  if n ==1: return 1

  paths= 0
 
  for num in range(1, 9+1): 
   if num not in visited:
     # if neighbor-adjacent  i.e. not 1->3 # 1 to 2/4/5
     if (current, num) not in JUMPS or  JUMPS[(current, num)] in visited: # or ( 1->3 but 2 has been visited)
       visited.add(num)
       paths+= num_paths(num, JUMPS, visited, n-1)
       visited.remove(num)

  return paths

def combinations(n):
    one = num_paths(1, JUMPS, set([1]), n)
    two = num_paths(2, JUMPS, set([2]), n)
    five= num_paths(5, JUMPS, set([5]), n)
    
    return 4* one +  4 * two + five



###################################################################################

MY_VISITED=[]
LEN_OF_PATTERN3 = 3
LEN_OF_PATTERN4 = 4

def num_paths2(current, jumps, visited, n):
   if n==1:
      return 1

   paths = 0
   for num in range(1, 10):
      if num not in visited:
         if (current, num) not in jumps or \
         jumps[(current, num)] in visited:   
            print( str(current) + " --> " + str(num) )
            visited.add(num) 
            print(visited)
            MY_VISITED.append(num)
            paths += num_paths(num, jumps, visited, n-1)
            visited.remove(num)

   return paths      


def combis(n):
   jumps = JUMPS
   return num_paths2(5, jumps, set([5]), n) 




if __name__=="__main__": 
  N=9
  print(combinations(N))           # 140704
  print("\n")

  print( combis(LEN_OF_PATTERN3) ) # 48
  print(MY_VISITED)                # [1, 2, 3, 4, 6, 7, 8, 9]


  MY_VISITED=[]
  print( combis(LEN_OF_PATTERN4) ) # 256
  print(MY_VISITED)                # [1, 2, 3, 4, 6, 7, 8, 9]


