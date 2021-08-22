"""
C++ Data Structures and Algorithm Design Principles
Carey, Doshi, Rajan 2019
page: 163
""" 

def partition(arr, start, end):
    pivot = arr[start]  
    left= start
    right= end
    print("start = ", start, ", end = ", end, ",pivot = ",pivot, ", Arr=", arr, "SubArr=", arr[start: end+1]);
    
    while(True):
       while(left < right and arr[left] <= pivot): # skip smallers to find bigger
           left= left+1
             
       while(left < right and arr[right] > pivot): # skip biggers to find smaller
           right= right-1

       if left == right: # if left and right meet, no element to swap
           break    
       else:
           print("Swapping", arr[left], " and ", arr[right])
           arr[left], arr[right] = arr[right], arr[left]
  
    if pivot > arr[right]:
      arr[start], arr[right] = arr[right], arr[start]
      print("Swapped", arr[start], " and ", arr[right], "\n")
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



# ku = [333,334,335,21, 33, 123, 1, 333,10, 7, 8, 9, 1, 5, 11,1,1,2,33,21,123,123,]
# n = len(ku)
# print("Sorted array is:", quickSort(ku, 0, n-1))


ku2=[21,11,6,6, 1,2,3, 5,  7,8,11, 4]

ku=[21,11,6, 1,2,3, 5,  7,8, 4]
ku=[21,11,6, 1,2,3, 5,  7,8, 4,-1,-2,23,24,25,6,7,8,8,7,6,3,2,11,22,32,23,32,32,555]
ku=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,15,16,16,17,18,19,20,20,20,21,22,22,23,24,25,26]

ku=[52,51,50,49,49,49,48,47,35,34,34,32,32,31,30,29,28,27,20,19,17,16,15,14,12,12,12,9,8,7,7,7, 12,12,12,]
print(ku)
#print( partition(ku, low=0, high= len(ku)-1 ))
#print(ku)
print("Sorted array is:", quickSort(ku, 0, len(ku)-1))


"""
Omitting pivot 
       >>> ku=[0,1,2,3,4,5]
       >>> pi=3
       >>> ku[0:pi-1] --> [0, 1]
       >>> ku[pi:]    -->        [3, 4, 5]

"""
