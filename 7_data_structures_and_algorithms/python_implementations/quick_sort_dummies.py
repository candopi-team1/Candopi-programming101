# Quick Sort

def partition(data, left, right):
    pivot  = data[left]
    lIndex = left + 1
    rIndex = right
    
    while True:
        while lIndex <= rIndex and data[lIndex] <= pivot:
            lIndex += 1
        while rIndex >= lIndex and data[rIndex] >= pivot:
            rIndex -= 1
        if rIndex <= lIndex:
            break
        data[lIndex], data[rIndex] =  data[rIndex], data[lIndex]
        print(data)
        
    data[left], data[rIndex] = data[rIndex], data[left]
    print(data,"\n")
    return rIndex



def quick_sort(data, left, right):
    if right <= left:
        return
    else:
        pivot = partition(data, left, right)
        quick_sort(data, left, pivot-1)
        quick_sort(data, pivot+1, right)
        
    return data

data = [9, 5, 7, 4, 2, 8, 1, 10, 6, 3]
data = [1,2,3, 1,2,3, 1,2,3,
        6,6,6, 9,5,7, 4,2,8,
        1,10,6, 6,6,3, 12,11,9, 12,12,12]
       
print( quick_sort(data, 0, len(data)-1) )




