''' CREDIT ; Towards Data Science: Sadrach Pierre, Ph.D. '''

import time

def partition(input_list,low,high):
    i = (low - 1)
    pivot = input_list[high]
    for j in range(low, high):
        if input_list[j] <= pivot:
            i = i + 1
            input_list[i], input_list[j] =  input_list[j], input_list[i]
    input_list[i+1],input_list[high] = input_list[high],input_list[i+1]
    return (i+1)


def quickSort(input_list, low, high):
    if low < high:
        partition_index = partition(input_list,low,high)
        quickSort(input_list, low, partition_index - 1)
        quickSort(input_list, partition_index + 1, high)

    

from data_quick_sorts import ku11, sorted_ku1


if __name__ == '__main__':
    start = time.time()
    
    # quickSort(sorted_ku1,0, len(sorted_ku1) -1)
    # print('Sorted List:', sorted_ku1)
    # ===>  RecursionError: maximum recursion depth exceeded in comparison

    # OK: Trick: Add some unsorted elements
    sorted_ku1.extend([1,0.00001])
    quickSort(sorted_ku1,0, len(sorted_ku1) -1)
    print('Sorted List:', sorted_ku1)


    # OK
    # quickSort(ku11,0, len(ku11) -1)
    # print('Sorted List:', ku11, len(ku11))
    
    
    stop = time.time()
    print('Time Required:', (stop - start))



