# sammie bae
def quick_sort(items) :
    return quick_sort_helper(items, 0, len(items) - 1);


def quick_sort_helper(items, left, right) :
    # index;
    if (len(items) > 1) :
        index = partition(items, left, right);
        print("\n", items, "index=", index, "L=", left, "R=",right)
        
        if (left < index - 1) :
            print(" Sort leftList", items[left: index - 1]) 
            quick_sort_helper(items, left, index - 1);
        

        if (index < right) :
            print(" Sort rightList", items[index:right]) 
            quick_sort_helper(items, index, right);
    else:
        print("EMPTY OR 1-MEMBER-ONLY ", items)
    
    return items;


def partition(array, left, right) :
    #pivot = array[Math.floor((right + left) / 2)];
    new_index=int(  (right + left) / 2)
    pivot = array[ new_index];
    print("    Partition gets    ... List=",array,", pv=", pivot,", R=", right, ", L=",left)
    
    while (left <= right) :
        while (pivot > array[left]) :
            left=left+1
        
        while (pivot < array[right]) :
            right=right-1
        
        if (left <= right) :
            # temp = array[left];
            # array[left] = array[right];
            # array[right] = temp; VERBOSE 
            
            array[left], array[right] = array[right], array[left] 
            print("      swap",  array[left], " and ", array[right] )
            left=left+1
            right=right-1
        
    print("    Partition returns ... List=",array,", pv=", pivot,", R=", right, ", L=",left)
    return left;

ku=[88, 1,9, 80, 19,1,9,1,9, 64, 25, 1,9,1,9, 20,21, 1,9,1,9, 2,2,2,2,2, 80,91,80,92,80]
# ku=[88,3,4,5, 1,9, 4,5,3, 34,12,44,55, 11,80, 19, 64, 25, 20,21, ]

ku= [6,3,2,5,1]
print("ORIG= ",ku)
print( quick_sort(ku)) # [1, 2, 3, 4, 6, 23]

