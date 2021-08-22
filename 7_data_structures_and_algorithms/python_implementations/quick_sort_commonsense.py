def partition(lu, left, right):
    pivot_idx = right
    pivot     = lu[pivot_idx]
    right     = right-1
    
    while True:
      # OK while left <= right and lu[left] <= pivot:
      while lu[left] < pivot:
          left=left + 1
          print(".........L", left)

      # OK while right >= left and lu[right] >= pivot:
      while   lu[right] >= pivot:
          right= right - 1
          print(".........R", right)

      if left >= right:
         break
      else:
         lu[left], lu[right]= lu[right], lu[left]
         print("Swapped", lu[left], "and", lu[right])
         
    

    lu[left], lu[pivot_idx]= lu[pivot_idx], lu[left]
    print("Swapped pivot", lu[left], "and",lu[pivot_idx] )
    print("Returned left_ptr=", left, "\n")
    return left
    


def quick_sort(lu, left, right):
    if (right-left) <= 0 :
        return 
    else:
        pivot_idx= partition(lu, left, right)
    
        quick_sort(lu, left, pivot_idx-1)
        quick_sort(lu, pivot_idx + 1, right)

    return lu



unsolist1= [6666, 11,61,1, 45,6,7, 1, 3,5,11,4,5,612,344, 5555,6]

unsolist_BAD= [ 4,5,6, 7, 1,2,3, 3,3]

unsolist= [ 4,5,6, 7,1,2, 3,4.5,
            6.7, 3.1,0.2,  8,8,8, 1,1,1, 1,1,1, 1,1,1,
            34,12,12, 34,12,12, 34,12,12,
            19,18,17,  19,18,17,  19,18,17, ]


unsolist= [6666,11,6, 45,6,7, 12,3,4,
           55,66,7, 4,2,1, 5555,0.1,0.002,
           19,20,211, 23,24, 22, 4,5,6, 7,1,2, 3,4.5,
            6.7, 3.1,0.2,  8,8,8, 1,1,1, 1,1,1, 1,1,1,
            34,12,12, 34,12,12, 34,12,12,
            19,18,17,  19,18,17,  19,18,17,  ]

print(unsolist)

print(quick_sort(unsolist,0, len(unsolist)-1)  )
    
