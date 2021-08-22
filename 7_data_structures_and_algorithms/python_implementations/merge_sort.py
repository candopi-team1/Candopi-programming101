"""
//        ==> #
function  ==> def
      ==> nothing

} ==>:
&&  ==> and
concat ==> extend
push ==> append

"""

def merge(leftA, rightA):
    results=  []; leftIndex= 0; rightIndex= 0;

    while (leftIndex < len(leftA) and rightIndex < len(rightA)  ) :
        if( leftA[leftIndex]<rightA[rightIndex] ):
            results.append(leftA[leftIndex]) ; # push(leftA[leftIndex++]);
            leftIndex+=1
        else :
            results.append(rightA[rightIndex]);
            rightIndex+=1
        
    
    leftRemains = leftA[leftIndex:]
    rightRemains = rightA[rightIndex:];
    # print("LeftRemains");print(leftRemains);
    # print("RightRemains");print(rightRemains);

    # add remaining to resultant array
    results.extend(leftRemains)
    results.extend(rightRemains);
    print("leftA= ",leftA);
    print("rightA=",rightA);
    print("results= ", results);  print("\n")
   
    return results


def mergeSort(array) :
    if(len(array)<2):
        return array; # Base case: array is now sorted since it's just 1 element
    

    midpoint = int( len(array)/2) # Math.floor
    leftArray = array[0: midpoint] # array.slice(0, midpoint),
    rightArray = array[midpoint:]
    # print("leftArray= ",leftArray);
    # print("rightArray=",rightArray); print("\n")


    
    return merge(mergeSort(leftArray), mergeSort(rightArray));



# ku=[6,1,23,4,2,3]
ku=[68,1,65, 123, 2, 4, 2, 11, 11,34, 3]
print(mergeSort(ku))
# [1, 2, 3, 4, 6, 23]


# TESTING SPLIT
"""
    print("leftArray= ",leftArray);
    print("rightArray=",rightArray); print("\n")

===>

leftArray=  [68, 1, 65, 123, 2]
rightArray= [4, 2, 11, 11, 34, 3]


leftArray=  [68, 1]
rightArray= [65, 123, 2]


leftArray=  [68]
rightArray= [1]


leftArray=  [65]
rightArray= [123, 2]


leftArray=  [123]
rightArray= [2]


leftArray=  [4, 2, 11]
rightArray= [11, 34, 3]


leftArray=  [4]
rightArray= [2, 11]


leftArray=  [2]
rightArray= [11]


leftArray=  [11]
rightArray= [34, 3]


leftArray=  [34]
rightArray= [3]
"""


# TESTING MERGE 
"""
ku1=[5,2,3,1]
ku2=[671,202,33,11,55,44,123,4]
print(merge(ku1,ku2)  )
===>

LeftRemains
[]
RightRemains
[671, 202, 33, 11, 55, 44, 123, 4]             <------ all unsorted
[5, 2, 3, 1, 671, 202, 33, 11, 55, 44, 123, 4] <------ all unsorted
"""




"""
ku3=[1,2,3,5,6]
ku4=[3,4,6,7,11,44,123,904]
print(merge(ku3,ku4)  )
===>

LeftRemains
[]
RightRemains
[7, 11, 44, 123, 904]                          <---- inherits the sortedness
[1, 2, 3, 3, 4, 5, 6, 6, 7, 11, 44, 123, 904]  <---- inherits the sortedness

"""


"""
ku4=[1,2,3,5,6]
ku3=[3,4,6,7,11,44,123,904]
print(merge(ku3,ku4)  )
====>

LeftRemains
[6, 7, 11, 44, 123, 904]                     <---- inherits the sortedness
RightRemains
[]
[1, 2, 3, 3, 4, 5, 6, 6, 7, 11, 44, 123, 904]<---- inherits the sortedness
"""


"""
ku4=[1,2,3,5,6]
ku3=[3,4,6,7,11,44,123,904]
print(merge(ku3,ku4)  == merge(ku4,ku3))


===>
LeftRemains
[6, 7, 11, 44, 123, 904]
RightRemains
[]
+

LeftRemains
[]
RightRemains
[7, 11, 44, 123, 904]
+

True


"""



