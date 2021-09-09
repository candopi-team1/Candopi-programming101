def num_paths(current, jumps, visited, n):
   if n==1:
      return 1

   paths = 0
   for num in range(1, 9+1):
      if num not in visited:
         if (current, num) not in jumps or \
         jumps[(current, num)] in visited:
            
            # print( str(current) + " --> " + str(num)
            visited.add(num)
            print( visited)
            
            paths += num_paths(num, jumps, visited, n-1)
            visited.remove(num)

   return paths      



def combine(length_of_pattern):
   jumps = {
            (1,3): 2, (1,7): 4, (1,9): 5,
            (2,8): 5,
            (3,1): 2, (3,7): 5, (3,9): 6,
            (4,6): 5, (6,4): 5,
            (7,1): 4, (7,3): 5, (7,9): 8,
            (8,2): 5,
            (9,1): 5, (9,3): 6, (9,7): 8
           }
   start_points= [1]
   
   no_of_combinations =  1 * num_paths(start_points[0], jumps, set([start_points[0]]), length_of_pattern) 
         
   
   print( no_of_combinations )
   return no_of_combinations


length_of_pattern = 3
no_of_combinations=  combine(length_of_pattern)
print( no_of_combinations )
