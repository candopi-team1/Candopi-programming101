"""
04 Aug 2020
cd /home/kyawnaing/dailycp/backtrack
python3.5  android_unlock2.py

"""

"""
(1) partial solution
(2) validate the solution so far
(3) checks if the solution is complete

 backtrack :: append/add/set value --> remove/pop/reset value
"""


from unlock_jumps    import JUMPS
from android_unlock1 import  num_paths



def combis(LEN_OF_PATTERN9):
   jumps = JUMPS

   start_points= [1,2,5] # SAME 140704
   start_points= [1,3,7] # same 124128
   start_points= [1,3,9] # same 124128
   start_points= [3,9,7] # same 124128

   start_points= [2,4,8] # SAME 140076
   start_points= [2,4,6] # SAME 140076
   start_points= [4,8,6] # SAME 140076
   start_points= [8,4,6] # SAME 140076

   start_points= [8,8,8] # SAME 140076

   start_points= [1,1,1] # same 124128


   ones=    4 * num_paths(start_points[0], jumps, set([start_points[0]]), LEN_OF_PATTERN9)
   twos=    4 * num_paths(start_points[1], jumps, set([start_points[1]]), LEN_OF_PATTERN9) 
   fives=   1 * num_paths(start_points[2], jumps, set([start_points[2]]), LEN_OF_PATTERN9)
   
   return   ones + twos + fives

   
if __name__=="__main__": 
 LEN_OF_PATTERN9 = 9
 no_of_combinations=  combis(LEN_OF_PATTERN9)
 print( no_of_combinations)



