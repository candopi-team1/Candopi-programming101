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

ku=[345.5, 345.5, 345, 6,11, 10, 345.5, 1, 23, 4, 2, 3,3,3,3,  1,2,345.5, 1,2,345.5,1,2,345.5, 1,345.5,2,
    345.5,1,2, 1,2, 1,345.5,2, 1,2, ]

print( quick_sort(ku)) # [1, 2, 3, 4, 6, 23]

