def insertion_sort(items) :
     leng = len(items) # number of items in the array
     #value =0 # the value currently being compared
     #   i, # index into unsorted section
     #   j; # index into sorted section

     for i in range(leng) :
        # store the current value because it may shift later
        value = items[i];

        # Whenever the value in the sorted section is greater than the value
        # in the unsorted section, shift all items in the sorted section over
        #by one. This creates space in which to insert the value.

        """
        for (j = i - 1; j > -1 && items[j] > value; j--) :
            items[j + 1] = items[j];
        }
        """

        
        j = i - 1;
        while( j > -1 and items[j] > value):            
            items[j + 1] = items[j];
            j = j-1
        

        
        items[j + 1] = value;

    
     return items;



ku= [61, 1, 23, 4, 2, 13,1,1.2, 1.5]
print( insertion_sort(ku) )

# [1, 2, 3, 4, 6, 23]
