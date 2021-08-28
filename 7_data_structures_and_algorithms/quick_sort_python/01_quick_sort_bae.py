#sammie bae 
def quick_sort(items) :
    return quick_sort_helper(items, 0, len(items) - 1);


def quick_sort_helper(items, left, right) :
    # index;
    if (len(items) > 1) :
        index = partition(items, left, right);

        if (left < index - 1) :
            quick_sort_helper(items, left, index - 1);
        

        if (index < right) :
            quick_sort_helper(items, index, right);
        
    
    return items;


def partition(array, left, right) :
    #pivot = array[Math.floor((right + left) / 2)];
    new_index=int(  (right + left) / 2)
    pivot = array[ new_index];

    
    while (left <= right) :
        while (pivot > array[left]) :
            left=left+1
        
        while (pivot < array[right]) :
            right=right-1
        
        if (left <= right) :            
            array[left], array[right] = array[right], array[left] 
            left=left+1
            right=right-1
        
    
    return left;


from data_quick_sorts import ku11, sorted_ku1

print( quick_sort(ku11), len(ku11))
# print( quick_sort(sorted_ku1), len(sorted_ku1))

