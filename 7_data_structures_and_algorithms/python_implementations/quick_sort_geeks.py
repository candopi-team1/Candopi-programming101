"""
# This code is contributed by Mohit Kumra
# This code in improved by https://githu b.com/anushkrishnav

Last Updated : 30 Dec, 2020
Like Merge Sort, QuickSort is a Divide and Conquer algorithm.
It picks an element as pivot and partitions the given array around the picked pivot.
There are many different versions of quickSort that pick pivot in different ways. 

1.Always pick first element as pivot.
2.Always pick last element as pivot (implemented below)
3.Pick a random element as pivot.
4. Pick median as pivot.

The key process in quickSort is partition().
Target of partitions is, given an array and an element x of array as pivot,
put x at its correct position in sorted array and put all smaller elements (smaller than x) before x,
and put all greater elements (greater than x) after x.

All this should be done in linear time. 
"""


"""
Pseudo Code for recursive QuickSort function : 

/* low  --> Starting index,  high  --> Ending index */
quickSort(arr[], low, high)
{
    if (low < high)
    {
        /* pi is partitioning index, arr[p] is now
           at right place */
        pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);  // Before pi
        quickSort(arr, pi + 1, high); // After pi
    }
}

""" 

  
# This function takes last element as pivot,
# places the pivot element at its correct position in sorted array,
# and places all smaller (smaller than pivot) to left of pivot
# and all greater elements to right of pivot 
  
def partition(arr, low, high):
    i = (low-1)           # index of smaller element
    pivot = arr[high]     # pivot
    print("low = ", low, ", high = ", high, ",pivot = ",pivot, ", Arr=", arr, "SubArr=", arr[low:high+1]);
    
    for j in range(low, high):
  
        # If current element is smaller/equal pivot
        if arr[j] <= pivot:  
            # increment index of smaller/bigger element that you passed over previously
            i = i+1
            print("Swapping", arr[i], " and ", arr[j])
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i+1], arr[high] = arr[high], arr[i+1]
    print("Swapped", arr[i+1], " and ", arr[high], ".i+1 = ", i+1, "\n")
    return (i+1)

  
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low   --> Starting index,
# high  --> Ending index
    
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    
    if low < high:
        # pi is partitioning index,
        # arr[p] is now at right place
        pi = partition(arr, low, high)
  
        # Separately sort elements before partition and after partition
        # Omits the pivot
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
    
    return arr


# Driver code to test above
# ku = [333,334,335,21, 33, 123, 1, 333,10, 7, 8, 9, 1, 5, 11,1,1,2,33,21,123,123,]
# n = len(ku)
# print("Sorted array is:", quickSort(ku, 0, n-1))


ku=[21,11,6,6, 1,2,3, 5,1,2,3, 5,1,2,3, 5,  7,8,11, 4, 4,4,4,4,4,4,4,4, 1,2,3, 5,]

ku3=[21,11,6, 1,2,3, 5,  7,8, 4]

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
