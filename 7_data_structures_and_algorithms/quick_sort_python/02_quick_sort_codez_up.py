''' CREDIT ; https://codezup.com/ '''

import time

def quicksortBetter(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    if len(arr) <10:
        print("A= ", arr, left, "+", middle, "+", right, "\n" )
    
    return quicksortBetter(left) + middle + quicksortBetter(right)


from data_quick_sorts import ku11, sorted_ku1


if __name__ == '__main__OK_temp':
    ku0 = [3, 4, 2, 6, 5, 7, 1, 9]
    
    
    start = time.time()
    # print('Sorted List:', quicksortBetter(ku0))
    
    # print('Sorted List:', quicksortBetter(ku11))
    # print('Sorted List:', quicksortBetter(sorted_ku1))

    ku1=[0,1,2,3,4,5,6]
    ku2=[4,1,3,2,0,6,5]

    # print('Sorted List:', quicksortBetter(ku1))
    print('Sorted List:', quicksortBetter(ku2))
    
    stop = time.time()
    print('Time Required:', (stop - start))




from data_quick_sorts import ku11, sorted_ku1

if __name__ == "__main__":
   #""" OK
   resu = quicksortBetter(ku11)
   print( resu, len(ku11), len(resu))
   #"""
   
   """ OK
   resu = quicksortBetter(sorted_ku1)
   print( resu, len(sorted_ku1), len(resu) )
   """

   """OK
   ku11=[6,7,8,1,11,45,2,3,1.23,4,5,56,12,45,67,123, 99,234,56,17,89,8.2]
   ku1=[6,7,8,1,11,]

   resu = quicksortBetter(ku11)
   print( resu, len(ku11), len(resu))
   """
    
