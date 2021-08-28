"""
C++ Data Structures and Algorithm Design Principles
Carey, Doshi, Rajan 2019
page: 163
""" 

def partition(arr, start, end):
    pivot = arr[start]  
    left= start
    right= end
    # print("start = ", start, ", end = ", end, ",pivot = ",pivot, ", Arr=", arr, "SubArr=", arr[start: end+1]);
    
    while(True):
       while(left < right and arr[left] <= pivot): # skip smallers to find bigger
           left= left+1
             
       while(left < right and arr[right] > pivot): # skip biggers to find smaller
           right= right-1

       if left == right: # if left and right meet, no element to swap
           break    
       else:
           # print("Swapping", arr[left], " and ", arr[right])
           arr[left], arr[right] = arr[right], arr[left]
  
    if pivot > arr[right]:
      arr[start], arr[right] = arr[right], arr[start]
      # print("Swapped", arr[start], " and ", arr[right], "\n")
    return right

  
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low   --> Starting index,
# high  --> Ending index
    
def quickSort(arr, low, high):
    if (high-low) < 1 :
        return arr    

    pi = partition(arr, low, high)
  
    # Separately sort elements before partition and after partition
    # Omits the pivot
    quickSort(arr, low, pi-1)
    quickSort(arr, pi, high)
    
    return arr



      

from data_quick_sorts import ku11, sorted_ku1


print( quickSort(ku11, 0, len(ku11)-1), len(ku11))
# print("Sorted array is:", quickSort(sorted_ku1, 0, len(sorted_ku1)-1), len(sorted_ku1) )



"""
Omitting pivot 
       >>> ku=[0,1,2,3,4,5]
       >>> pi=3
       >>> ku[0:pi-1] --> [0, 1]
       >>> ku[pi:]    -->        [3, 4, 5]

"""
