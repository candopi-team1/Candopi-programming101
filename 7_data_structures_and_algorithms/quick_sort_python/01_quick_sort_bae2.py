# sammie bae
def quick_sort(items) :
    return quick_sort_helper(items, 0, len(items) - 1);


def quick_sort_helper(items, left, right) :
    # index;
    if (len(items) > 1) :
        index = partition(items, left, right);
        print("\nHELPER ", items, "index=", index, "Li=", left, "Ri=",right)
        
        if (left < index - 1) :            
            quick_sort_helper(items, left, index - 1);
        else: print("When index=", index, ", LHS is sorted.",items)    
        

        if (index < right) :            
            quick_sort_helper(items, index, right);
        else: print("When index=", index, ", RHS is sorted.",items)    
      
    
    return items;


def partition(array, left, right) :
    #pivot = array[Math.floor((right + left) / 2)];
    pivot_index=int(  (right + left) / 2)
    pivot = array[ pivot_index];
    print(" Partition gets    ... List=",array,", pv=", pivot,", Li=",left, "Ri=", right, ",", 
          array[left], "-->", array[right])
    
    while (left <= right) :
        while (pivot > array[left]) :
            left=left+1
        
        while (pivot < array[right]) :
            right=right-1
        
        if (left <= right) : 
            array[left], array[right] = array[right], array[left] 
            print("      swap",  array[left], " and ", array[right] )
            left=left+1
            right=right-1
        
    print(" Partition returns ... List=",array,", pv=", pivot,", Li=",left, "Ri=", right)
    return left;



from data_quick_sorts import ku11, sorted_ku1

ku11=[1,2,3,4, 7,6,9,8]

# print( quick_sort(ku11), len(ku11))
# print( quick_sort(sorted_ku1), len(sorted_ku1))

""" even_length 
ku=[0,1]
print( quick_sort(ku), len(ku)); print("\n*********\n")

ku=[1,0]
print( quick_sort(ku), len(ku)); print("\n*********\n")


ku=[0,1,2,3]
print( quick_sort(ku), len(ku)); print("\n*********\n")

ku=[3,2, 1,0]
print( quick_sort(ku), len(ku)); print("\n*********\n")




ku=[99,11,2,3]
print( quick_sort(ku), len(ku)); print("\n*********\n")

ku=[38,2, 18,0]
print( quick_sort(ku), len(ku)); print("\n*********\n")
"""



""" odd_length 
ku=[0,1,2]
print( quick_sort(ku), len(ku)); print("\n*********\n")

ku=[10,9,2]
print( quick_sort(ku), len(ku)); print("\n*********\n")



ku=[0,1, 27,33, 91]
print( quick_sort(ku), len(ku)); print("\n*********\n")


ku=[15,13, 10,9,  2]
print( quick_sort(ku), len(ku)); print("\n*********\n")




ku=[10,1, -27,91, 15]
print( quick_sort(ku), len(ku)); print("\n*********\n")


ku=[1.5,13, 10,9,  -2]
print( quick_sort(ku), len(ku)); print("\n*********\n")

"""



