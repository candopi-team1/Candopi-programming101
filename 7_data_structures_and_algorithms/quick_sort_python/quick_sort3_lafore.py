def insertion_sort(theArray, left, right):

      # for(out=left+1; out<=right; out++) {
      for i in range(left+1, right+1):
         temp = theArray[i];  #// remove marked item
         index = i;                     #// start shifts at out
                                      # // until one is smaller,
									   
         while(index>left and theArray[index-1] >= temp) :
            theArray[index] = theArray[index-1]; #// shift item to right
            index -=1;                      #// go left one position
         
         theArray[index] = temp;          #// insert marked item
      
      return theArray


# print(len(ku));
# print( insertion_sort(ku, 0,2) ) # [1, 23, 61,     4, 2, 13, 1, 1.2, 1.5]
# print( insertion_sort(ku, 1,4) ) # [61,     1, 2, 4, 23,         13, 1, 1.2, 1.5]
# print( insertion_sort(ku, 4, 8) ) # [61, 1, 23, 4,     1, 1.2, 1.5, 2, 13]



def quick_sort(theArray):
      nElems= len(theArray)      
      theArray= recur_quick_sort(theArray, 0, nElems-1);
      
      return theArray


def recur_quick_sort(theArray,left, right):
      size = right-left+1;
      if(size < 10):                   #// insertion sort if small
         insertion_sort(theArray, left, right);
      else:                            #// quicksort if large         
         median = medianOf3(theArray,left, right);
         partition = partitionIt(theArray, left, right, median);
         recur_quick_sort(theArray, left, partition-1);
         recur_quick_sort(theArray, partition+1, right);
      
      return theArray   


def medianOf3(theArray, left, right):
      center = int( (left+right)/2 );
                                       #// order left & center
      if( theArray[left] > theArray[center] ):
         theArray[left], theArray[center]=theArray[center], theArray[left]
                                       #// order left & right
      if( theArray[left] > theArray[right] ):
         theArray[left], theArray[right]=theArray[right], theArray[left];
                                       #// order center & right
      if( theArray[center] > theArray[right] ):
         theArray[center], theArray[right]= theArray[right], theArray[center];
 
      theArray[center], theArray[right-1] = theArray[right-1], theArray[center];           #// put pivot on right
	  
      # print("returning median ", theArray[right-1])
      
      return theArray[right-1];        #// return median value




def partitionIt(theArray, left,  right, pivot):      
       leftPtr = left;             #// right of first elem
       rightPtr = right - 1;       #// left of pivot
       
       while( True):
          leftPtr= leftPtr+1;  # key position 1           
          while( theArray[leftPtr] < pivot ):  #// find bigger
             leftPtr =leftPtr+1;                                  #// (nop)

          rightPtr= rightPtr-1;  # key position 2
          while( theArray[rightPtr] > pivot ): #// find smaller
            rightPtr=rightPtr-1;                                  #// (nop)
      
          if(leftPtr >= rightPtr):      #// if pointers cross,
             break;                    #//    partition done
          else:                         #// not crossed, so
             theArray[leftPtr], theArray[rightPtr]=theArray[rightPtr], theArray[leftPtr];  #// swap elements
       #end while
      
       theArray[leftPtr], theArray[right-1]= theArray[right-1], theArray[leftPtr] ; #// restore pivot
       return leftPtr;                 # // return pivot location




from data_quick_sorts import ku11, sorted_ku1

print( quick_sort(ku11), len(ku11))
# print( quick_sort(sorted_ku1), len(sorted_ku1))


