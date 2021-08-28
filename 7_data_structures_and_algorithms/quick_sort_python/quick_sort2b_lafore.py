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


def quick_sort(theArray):
      theArray= recQuickSort(theArray, 0, len(theArray)-1);
      return theArray

   
   
def recQuickSort(theArray, left,  right):
      size = right-left+1;
      
      if(size <= 3) :                 #// manual sort if small
         manualSort(theArray, left, right);
         
      elif(size < 10):                   #// insertion sort if small
         insertion_sort(theArray, left, right);
             
         
      else:                           #// quicksort if large
          median = medianOf3(theArray,left, right); 
		 
          partition = partitionIt(theArray, left, right, median);
          recQuickSort(theArray, left, partition-1);
          recQuickSort(theArray, partition+1, right);

      return theArray


          

def medianOf3(theArray, left,  right):
      center = int ( (left+right)/2 );
      # print("M3",theArray[left], theArray[center],theArray[right-1],theArray[right])
      
      if( theArray[left] > theArray[center] ): #// order left & center         
             theArray[left], theArray[center] =theArray[center], theArray[left]
             
                                       
      if( theArray[left] > theArray[right] ): #// order left & right        
             theArray[left], theArray[right]= theArray[right], theArray[left] ;
                                       
       
      if( theArray[center] > theArray[right] ):#// order center & right
             theArray[center], theArray[right] =theArray[right], theArray[center]

      theArray[center], theArray[right-1] = theArray[right-1],theArray[center] ;  #// put pivot on right

      
      # print("M3",theArray[left], theArray[center],theArray[right-1],theArray[right],"END\n")
      
      # return center # RecursionError: maximum recursion depth exceeded while calling a Python object
      return theArray[right-1];        #// return median value
      
      
    
def partitionIt(theArray, left,  right,  pivot):
       leftPtr = left;             #// right of first elem
       rightPtr = right - 1;       #// left of pivot
       
       
       while(True):
          leftPtr = leftPtr + 1;   # key position 1          
          while( theArray[leftPtr] < pivot ):  #// find bigger  
              leftPtr+=1

          rightPtr = rightPtr - 1; # key position 2   
          while( theArray[rightPtr] > pivot ): # // find smaller 
               rightPtr-=1

       
          if(leftPtr >= rightPtr):      #// if poers cross,
             break;                    #//    partition done
          else:                        #// not crossed, so
             theArray[leftPtr], theArray[rightPtr]= theArray[rightPtr] ,theArray[leftPtr] # // swap elements
             

       
       theArray[leftPtr], theArray[right-1]  = theArray[right-1], theArray[leftPtr];    #// restore pivot  //***
       
       return leftPtr;           #// return pivot location

   
def manualSort(theArray, left,  right):
      size = right-left+1;
      if(size <= 1):
         return;         #// no sort necessary
      if(size == 2):    #// 2-sort left and right
         if( theArray[left] > theArray[right] ):            
            theArray[left], theArray[right]= theArray[right], theArray[left] ;
         return;
       
      else:  #// size==3
         # // 3-sort left, center (right-1) & right
         # print("M starts", theArray[left], theArray[right-1],  theArray[right])
         
         if( theArray[left] > theArray[right-1] ):
            theArray[left], theArray[right-1]= theArray[right-1],theArray[left]; #// left, center
       
         if( theArray[left] > theArray[right] ):
            theArray[left], theArray[right]= theArray[right], theArray[left] ; #// left, right

       
         if( theArray[right-1] > theArray[right] ):
            theArray[right-1], theArray[right]= theArray[right],theArray[right-1] ;  #// center, right

         # print("M ends", theArray[left], theArray[right-1],  theArray[right])
            




from data_quick_sorts import ku11, sorted_ku1


""" OK
resu = quick_sort(ku11)
print( resu, len(ku11), len(resu))
"""

""" OK
resu = quick_sort(sorted_ku1)
print( resu, len(sorted_ku1), len(resu) )
"""



ku11=[6,7,8,1,2,3,1.23,4,5]
resu = quick_sort(ku11)
print( resu, len(ku11), len(resu))




"""
ku11=[6,7,8,1,2,3,1.23,4,5]


==>
M3 6 2 4 5
M3 2 4 5 6 END

M3 2 3 1 4
M3 2 1 3 4 END

"""
       
      

    
