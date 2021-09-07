"""
Hands-on Data Structures and Algorithms with Kotlin
page. 142

"""

def partition(lu, low, high):    
    pivot                       = lu[high]
    idx_for_smaller_than_pivot  = low-1

    for j in range(low,high):
      if lu[j] <= pivot:
           idx_for_smaller_than_pivot += 1
           lu[idx_for_smaller_than_pivot], lu[j]    = lu[j], lu[idx_for_smaller_than_pivot]
           
    lu[idx_for_smaller_than_pivot +1], lu[high]= lu[high],  lu[idx_for_smaller_than_pivot +1]

    return idx_for_smaller_than_pivot +1
    


def quick_sort(lu, low, high):
    if low < high:
        pivot_idx = partition(lu, low, high)
    
        quick_sort(lu, low,           pivot_idx-1)
        quick_sort(lu, pivot_idx +1,  high)

    return lu



from data_quick_sorts import ku11, sorted_ku1

ku11=[17,12, 29,21, 5, 7]
print( quick_sort(ku11,0, len(ku11)-1), len(ku11))

try:
  print( quick_sort(sorted_ku1,0, len(sorted_ku1)-1), len(sorted_ku1))
except Exception as e:
  # ==> RecursionError: maximum recursion depth exceeded in comparison
  sorted_ku1.extend([2,-1])
  print( quick_sort(sorted_ku1,0, len(sorted_ku1)-1), len(sorted_ku1))
  print(e)
  

            


