package c7.sort;

class ArrayIns{
   private double[] theArray;        // ref to array theArray
   private int nElems;               // number of data items

   public ArrayIns(int max) {         // constructor
      theArray = new double[max];        // create the array
      nElems = 0;                        // no items yet
   }

   public void insert(double value) { // put element into array
      theArray[nElems] = value;         // insert it
      nElems++;                         // increment size
   }

   public void display(){             // displays array contents
      System.out.print("A = ");
      for(int j=0; j<nElems; j++)       // for each element,
         System.out.print(theArray[j] + " ");  // display it
      System.out.println("");
   }

   public void quickSort(){ 
               recQuickSort(0, nElems-1); //left and right    
   }
   
//--------------------------------------------------------------
   public void recQuickSort(int left, int right) {
      if(right-left <= 0)    return;  // if size <= 1, already sorted
	  
      else {                   // size is 2 or larger
         double pivot = theArray[right];    // rightmost item
                                            // partition range
         int partition = partitionIt(left, right, pivot);
		 
		 //kkn1
		 System.out.println("pivot = " + pivot + "; partition = " + partition);
		 
         recQuickSort(left, partition-1);   // sort left side
         recQuickSort(partition+1, right);  // sort right side
      }//else
	  
   }// end recQuickSort()
//--------------------------------------------------------------
    public int partitionIt(int left, int right, double pivot){
       int leftPtr = left-1;           // left    (after ++)
       int rightPtr = right;           // right-1 (after --)
       while(true){
                                    // find bigger item
          while( theArray[++leftPtr] < pivot );  // (nop)
		  
                                       // find smaller item
          while(rightPtr > 0 && theArray[--rightPtr] > pivot);  // (nop)

          if(leftPtr >= rightPtr)      // if pointers cross,
             break;                    //    partition done
          else                         // not crossed, so
             swap(leftPtr, rightPtr);  //    swap elements
        }  // end while(true)
       
	   swap(leftPtr, right);           // restore pivot
       return leftPtr;                 // return pivot location
     }  // end partitionIt()
//--------------------------------------------------------------
   public void swap(int dex1, int dex2){  // swap two elements
      double temp = theArray[dex1];      // A into temp
      theArray[dex1] = theArray[dex2];   // B into A
      theArray[dex2] = temp;             // temp into B
	  
	  // /kkn2
	  System.out.println("swapping: " +dex1 +" with "+ dex2);
	  for(int k=0; k< theArray.length; k++){
	     System.out.print( theArray[k] + " " );
	  }
	  System.out.print("\n");
	  ///
	  
   }// end swap method
//--------------------------------------------------------------
}  // end class ArrayIns

///////////////////////

class QuickSort1App {
   public static void main(String[] args) {
      int maxSize = 10; //16;      // array size
      ArrayIns arr;
      arr = new ArrayIns(maxSize);  // create array

/*
      for(int j=0; j<maxSize; j++){  // fill array with
                                 // random numbers
         double n = (int)(java.lang.Math.random()*99);
         arr.insert(n);
      }//fill with random
	*/
	
	
	//kkn       
	arr.insert(85.0);arr.insert(89.0);
	arr.insert(77.0); 	arr.insert(67.0);
	arr.insert(77.0);arr.insert(4.0);
	arr.insert(13.0);arr.insert(88.0);
	arr.insert(41.0);	arr.insert(64.0);
	
      arr.display();                // display items
      arr.quickSort();              // quicksort them
      arr.display();                // display them again
     }  // end main()
   }  // end class QuickSort1App
/*
//kkn1

*/