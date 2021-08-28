def quick_sort(arr):
      arr= recQuickSort(arr, 0, len(arr)-1);
      return arr

   
   
def recQuickSort(arr, left,  right):
      size = right-left+1;
      
         
      
      if(size <= 3) :                 #// manual sort if small
         manualSort(arr, left, right);
         
         
      else:                           #// quicksort if large
          median = medianOf3(arr,left, right); 
		 
          partition = partitionIt(arr, left, right, median);
          recQuickSort(arr, left, partition-1);
          recQuickSort(arr, partition+1, right);

      return arr


          

def medianOf3(arr, left,  right):
      center = int ( (left+right)/2 );
      # print("Median3 starts", arr)
      # print("Median3 starts", arr[left], arr[right-1],  arr[right])
           
      if( arr[left] > arr[center] ): #// order left & center         
             arr[left], arr[center] =arr[center], arr[left]
             
                                       
      if( arr[left] > arr[right] ): #// order left & right        
             arr[left], arr[right]= arr[right], arr[left] ;
                                       
       
      if( arr[center] > arr[right] ):#// order center & right
             arr[center], arr[right] =arr[right], arr[center]

      arr[center], arr[right-1] = arr[right-1],arr[center] ;  #// put pivot on right

      
      # print("Median3   ends", arr[left], arr[right-1],  arr[right])
      # print("Median3   ends", arr)
      center_val=arr[right-1]
      
      return center_val;        #// return median value
      
      
    
def partitionIt(arr, left,  right,  pivot):
       leftPtr = left;             #// right of first elem
       rightPtr = right - 1;       #// left of pivot
       
       
       while(True):
          leftPtr = leftPtr + 1;   # key position 1          
          while( arr[leftPtr] < pivot ):  #// find bigger  
              leftPtr+=1

          rightPtr = rightPtr - 1; # key position 2   
          while( arr[rightPtr] > pivot ): # // find smaller 
               rightPtr-=1

       
          if(leftPtr >= rightPtr):      #// if poers cross,
             break;                    #//    partition done
          else:                        #// not crossed, so
             arr[leftPtr], arr[rightPtr]= arr[rightPtr] ,arr[leftPtr] # // swap elements
             

       
       arr[leftPtr], arr[right-1]  = arr[right-1], arr[leftPtr];    #// restore pivot  //***
       
       return leftPtr;           #// return pivot location

   
def manualSort(arr, left,  right):
      size = right-left+1;
      if(size <= 1):
         return;         #// no sort necessary
      if(size == 2):    #// 2-sort left and right
         if( arr[left] > arr[right] ):            
            arr[left], arr[right]= arr[right], arr[left] ;
         return;
       
      else:  #// size==3
         # // 3-sort left, center (right-1) & right
         # print("Manual starts", arr[left], arr[right-1],  arr[right])
         
         if( arr[left] > arr[right-1] ):
            arr[left], arr[right-1]= arr[right-1],arr[left]; #// left, center
       
         if( arr[left] > arr[right] ):
            arr[left], arr[right]= arr[right], arr[left] ; #// left, right

       
         if( arr[right-1] > arr[right] ):
            arr[right-1], arr[right]= arr[right],arr[right-1] ;  #// center, right

         # print("Manual   ends", arr[left], arr[right-1],  arr[right])
            




from data_quick_sorts import ku11, sorted_ku1


""" OK
resu = quick_sort(ku11)
print( resu, len(ku11), len(resu))
"""

""" OK
resu = quick_sort(sorted_ku1)
print( resu, len(sorted_ku1), len(resu) )
"""



ku11=[6,7,8,1,11,45,2,3,1.23,4,5,56,12,45,67,123, 99,234,56,17,89,8.2]
ku11=[6,7,8,1,11,]

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
       
      

    
