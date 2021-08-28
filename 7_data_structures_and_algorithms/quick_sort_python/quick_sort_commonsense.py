def partition(lu, left, right):
    pivot_idx = right
    pivot     = lu[pivot_idx]
    right     = right-1
    
    while True:
      # OK while left <= right and lu[left] <= pivot:
      while lu[left] < pivot:
          left=left + 1
          # print(".........L", left)

      while right >= left and lu[right] >= pivot:
          right= right - 1
          # print(".........R", right)

      if left >= right:
         break
      else:
         lu[left], lu[right]= lu[right], lu[left]
         # print("Swapped", lu[left], "and", lu[right])
         
    

    lu[left], lu[pivot_idx]= lu[pivot_idx], lu[left]
    # print("Swapped pivot", lu[left], "and",lu[pivot_idx] )
    # print("Returned left_ptr=", left, "\n")
    return left
    


def quick_sort(lu, left, right):
    if (right-left) <= 0 :
        return 
    else:
        pivot_idx= partition(lu, left, right)
    
        quick_sort(lu, left, pivot_idx-1)
        quick_sort(lu, pivot_idx + 1, right)

    return lu



from data_quick_sorts import ku11, sorted_ku1

print( quick_sort(ku11,0, len(ku11)-1), len(ku11))
# print( quick_sort(sorted_ku1,0, len(sorted_ku1)-1), len(sorted_ku1))




            


