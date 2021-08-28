''' CREDIT : https://realpython.com/sorting-algorithms-python/#the-merge-sort-algorithm-in-python '''

from random import randint

def quicksort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    #if len(array) <10:
    #    print("pivot= ", pivot, low, "+", same, "+", high, "\n" )
    
    return quicksort(low) + same + quicksort(high)



ARRAY_LENGTH=1234

"""
array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
print(quicksort(array))
"""

from data_quick_sorts import ku11, sorted_ku1

"""
# ku11=[1,2,3,4, 7,6,9,8]

# print( quicksort(ku11), len(ku11))
# print( quicksort(sorted_ku1), len(sorted_ku1))
"""


from timeit import repeat

def run_sorting_algorithm(algorithm, array):
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


import random
import numpy as np


if __name__ == "__main__OK_tempt":
    # Generate an array of `ARRAY_LENGTH` items consisting
    # of random integer values between 0 and 999
    # array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    # array = ku11

     
    """
    array = [random.randint(1,1000000) for i in range(1,1000000)] # PC sort of hanged.    

    array = np.array(array) ==>
    quicksort([736586 769041 212026 ... 510814 850791 585428])
                      ^
    SyntaxError: invalid syntax
    """

    """ OK
    array = [random.randint(1,1000000) for i in   range(1,10000)] # Algorithm: quicksort. Minimum execution time: 0.5914060000000001
    # array = np.array(array) # ==> SyntaxError: invalid syntax
    """


    # array= ku11     # Algorithm: quicksort. Minimum execution time: 0.06738749999999993
    array= sorted_ku1 # Algorithm: quicksort. Minimum execution time: 0.041381999999999974 FASTER

    array=[0,1,2,3,4,5,6]
    array=[4,1,3,2,0,6,5]
    
    # Call the function using the name of the sorting algorithm
    # and the array you just created
    run_sorting_algorithm(algorithm="quicksort", array=array)




from data_quick_sorts import ku11, sorted_ku1

if __name__ == "__main__":
   """ OK
   resu = quicksort(ku11)
   print( resu, len(ku11), len(resu))
   """
   
   """ OK
   resu = quicksort(sorted_ku1)
   print( resu, len(sorted_ku1), len(resu) )
   """

   #"""OK
   ku11=[6,7,8,1,11,45,2,3,1.23,4,5,56,12,45,67,123, 99,234,56,17,89,8.2]
   ku1=[6,7,8,1,11,]

   resu = quicksort(ku11)
   print( resu, len(ku11), len(resu))
   #"""
    

