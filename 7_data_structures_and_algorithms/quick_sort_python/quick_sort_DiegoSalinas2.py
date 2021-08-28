''' CREDIT ; Towards Data Science: Diego Salinas : FIX by KKN '''

import time

def iteration(mylist):
    final = []
    left = []
    right = []
    
    n = len(mylist)//2 + 1

    pivot = mylist[0]
    final.append(pivot)
    mylist = mylist[1:]

    
    for i in mylist:
        for x in range(n+1):
            if i >= final[x]:
                if i >= final[len(final)-1]:
                    final.append(i); print(i, "at end")
                    break
                
            elif i < final[x]:
                print(i,x, final)
                for j in range(0,x-1):
                    final[j+1] = final[j]
                final.insert(x,i)
                print(i, "index=", x, final, "<<<<")
                break
    return final


def quicksort(lu):
    final_right = []
    final_left = []
    left = []
    right = []
    final = []

    
    first = lu[0]
    last = lu[len(lu)-2]
    beforelast = lu[len(lu)-3]
    
    # pivot = []
    pivot = (first+last+beforelast)//3

    for i in lu:      
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)

            
    final_left = iteration(left)
    final_right = iteration(right)
    
    final = final_left + final_right
    return final



from data_quick_sorts import ku11, sorted_ku1

import random
import numpy as np


if __name__ == '__main__':
    start = time.time()

    # lu = [random.randint(1,10) for i in range(1,10)]

    # lu = [random.randint(1,1000000) for i in range(1,1000000)] # PC sort of hanged.
    # lu = [random.randint(1,1000000) for i in   range(1,10000)]

    # lu = np.array(lu)
    # Time Required: 10.458323001861572

    # print(quicksort(lu), len(lu) )
    

    
    # OK print( quicksort(sorted_ku1), len(sorted_ku1) )
    

    """
    ku11=[0,1,2,3,4,5,6,7,8,9,10]
    ku11=[11,0,14,42,13,84,5,6,7,9]
    """
    
    ku11=[2,3,4,5,6,7,8,401,402,403,404, 1.002,1.0001,1.03, -0.09, -1, 500,600,
          200,201,202, 203,11,0,14,42,13, 22,11,44,33,99,101, 55,66,77,88,
          55,66,77,88,99,100, 84,5,6,7,9,-90,-17,-2,889,1900, 1234,12,13,14,
          700,700, 800, 900, 151,67,8,911,22,33,44,-9]

    ku11=[1,2,3,4,5,6, 1,2,3,4,5,6, 1,2,3,4,5,6,
          11,11,11, 12,13,14,  12,13,14,  12,13,14, ]
    
    resu =quicksort(ku11)
    print(resu , len(ku11), len(resu) )
    
    

    
    stop = time.time()
    print('Time Required:', (stop - start))



