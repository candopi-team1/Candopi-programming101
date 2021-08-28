# sammie bae

def partition(array, left, right) :
    #pivot = array[Math.floor((right + left) / 2)];
    new_index=int(  (right + left) / 2)
    pivot = array[ new_index];
    print("Partition gets    ... List=",array,", pv=", pivot,", R=", right, ", L=",left)
    
    while (left <= right) :
        while (pivot > array[left]) :
            left=left+1
        
        while (pivot < array[right]) :
            right=right-1
        
        if (left <= right) :
            temp = array[left];
            array[left] = array[right];
            array[right] = temp;
            print("swap",  array[left], " and ", array[right] )
            left=left+1
            right=right-1
        
    print("Partition returns ... List=",array,", pv=", pivot,", R=", right, ", L=",left)
    return left;

ku=[88, 1,9, 80, 19, 64, 25, 20,21, ]
# ku=[88,3,4,5, 1,9, 4,5,3, 34,12,44,55, 11,80, 19, 64, 25, 20,21, ]

ku1=[21, 3,2,1,  5,   8,11,9, 4]
ku2= [21,  3,2,1,   5,  8,2,  9,4]
ku3=[88,1,9,80,   19,64,  25,20, 21]

ku=[80,88,   64,  25,20, 21]

print(ku)
partition(ku, 0, len(ku)-1)
print(ku ) # [1, 2, 3, 4, 6, 23]

