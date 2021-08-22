package  c7.sort;

class ArrayInsDec23{
   private double[] theArray;        // ref to array theArray
   private int nElems;               // number of data items

   public ArrayInsDec23(int max){
      theArray = new double[max];        // create the array
      nElems = 0;                        // no items yet
   }

   public void insert(double value) {
      theArray[nElems] = value;         // insert it
      nElems++;                         // increment size
   }

   public void display(){
      System.out.print("A=");
      for(int j=0; j<nElems; j++)       // for each element,
         System.out.print(theArray[j] + " ");  // display it
      System.out.println("");
   }

   public void quickSort() {
      recQuickSort(0, nElems-1);
   }
   
//--------------------------------------------------------------
   public void recQuickSort(int left, int right) {
      int size = right-left+1;
      if(size <= 3)                  // manual sort if small
         manualSort(left, right);    //kkn1 
      else{                           // quicksort if large
         double median = medianOf3(left, right); //kkn2
		 
         int partition = partitionIt(left, right, median);
		 System.out.println(" getting partition " + partition); 
		 
         recQuickSort(left, partition-1);
         recQuickSort(partition+1, right);
      }//else
	  
   }// end recQuickSort()
//--------------------------------------------------------------
   public double medianOf3(int left, int right){
      int center = (left+right)/2;
                                       // order left & center
      if( theArray[left] > theArray[center] )   swap(left, center);
                                       // order left & right
      if( theArray[left] > theArray[right] )     swap(left, right);
                                       // order center & right
      if( theArray[center] > theArray[right] )   swap(center, right);

      swap(center, right-1);           // put pivot on right
	  
	  System.out.println(" returning median " +  theArray[right-1] );
      return theArray[right-1];        // return median value
      
  }  // end medianOf3()
  
    
//--------------------------------------------------------------
   public void swap(int dex1, int dex2){  // swap two elements
      double temp = theArray[dex1];      // A into temp
      theArray[dex1] = theArray[dex2];   // B into A
      theArray[dex2] = temp;             // temp into B
   }// end swap()
   
//--------------------------------------------------------------
    public int partitionIt(int left, int right, double pivot){
       int leftPtr = left;             // right of first elem
       int rightPtr = right - 1;       // left of pivot

       while(true){
          while( theArray[++leftPtr] < pivot );  // find bigger //    (nop)
          while( theArray[--rightPtr] > pivot ); // find smaller //   (nop)
		  
          if(leftPtr >= rightPtr)      // if pointers cross,
             break;                    //    partition done
          else                         // not crossed, so
             swap(leftPtr, rightPtr);  // swap elements
       }// end while(true)
	   
       swap(leftPtr, right-1); // restore pivot  //***
       return leftPtr;        // return pivot location
	   
     }// end partitionIt()
//--------------------------------------------------------------
   public void manualSort(int left, int right){
      int size = right-left+1;
	  System.out.println("manual for size " + size +" and LR "+ left +"/"+ right);
	   
      if(size <= 1)   return;         // no sort necessary
      if(size == 2){  // 2-sort left and right
         if( theArray[left] > theArray[right] ) swap(left, right);
         return;
      } else{  // size==3 // 3-sort left, center (right-1) & right
         if( theArray[left] > theArray[right-1] )  swap(left, right-1);                // left, center
         if( theArray[left] > theArray[right] )    swap(left, right);                  // left, right
         if( theArray[right-1] > theArray[right] ) swap(right-1, right);               // center, right
      }//else
	  
    }// end manualSort()
//--------------------------------------------------------------
}// end class ArrayInsDec23
   
//////////////////////////

class QuickSort2bApp{
   //public static int[]  karray=new int[10];
   
   public static void main(String[] args)  {
      int maxSize = 16;             // array size
	  //maxSize=10;
	  
      ArrayInsDec23 arr;                 // reference to array
      arr = new ArrayInsDec23(maxSize);  // create the array
//*
      for(int j=0; j<maxSize; j++)  // fill array with
         {                          // random numbers
         double n = (int)(java.lang.Math.random()*99);
         arr.insert(n);
         }
//*/
		 
		 /*//kkn test
		 arr.insert(9);arr.insert(1);arr.insert(6);
		 arr.insert(7);arr.insert(5);arr.insert(8);
		 arr.insert(4);arr.insert(3);arr.insert(0);
		 arr.insert(2);//arr.insert();arr.insert();
		 */
		 
		 
      arr.display();                // display items
      arr.quickSort();              // quicksort them
      arr.display();                // display them again
	 
		   
   }  // end main()    
    
}  // end class QuickSort2bApp
/*
A=9.0 1.0 6.0 7.0 5.0 8.0 4.0 3.0 0.0 2.0
 returning median 5.0
 getting partition 5
 returning median 2.0
 getting partition 2
manual for size 2 and LR 0/1
manual for size 2 and LR 3/4
 returning median 7.0
 getting partition 7
manual for size 1 and LR 6/6
manual for size 2 and LR 8/9
A=0.0 1.0 2.0 3.0 4.0 5.0 6.0 7.0 8.0 9.0
*/