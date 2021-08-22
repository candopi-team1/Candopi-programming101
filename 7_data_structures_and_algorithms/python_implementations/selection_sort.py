def selection_sort(items):
    leng = len(items)
    minim = 0

    for i in range(leng):
        # set minimum to this position
        minim = i;
        # check the rest of the array to see if anything is smaller
        for j in range(i+1, leng):
            if ( items[j] < items[minim]) : 
                minim = j;
            
        
        #if the minimum isn't in the position, swap it
        if (i != minim) :
            items=swap(items, i, minim);
            """OK
            temp = items[i];
            items[i] = items[minim];
            items[minim] = temp;"""
        
    

    return items;



def swap(array, index1, index2) :
    temp = array[index1];
    array[index1] = array[index2];
    array[index2] = temp;
    return array



ku=[34,301,12, 2, 7,8,2,1]

print(selection_sort(ku))
