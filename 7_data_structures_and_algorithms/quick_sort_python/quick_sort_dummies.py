# Algorithms for Dummies

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
        # print(data)
        
    data[left], data[rIndex] = data[rIndex], data[left]
    # print(data,"\n")
    return rIndex



def quick_sort(data, left, right):
    if right <= left:
        return
    else:
        pivot = partition(data, left, right)
        quick_sort(data, left, pivot-1)
        quick_sort(data, pivot+1, right)
        
    return data




from data_quick_sorts import ku11, sorted_ku1

print( quick_sort(ku11,0, len(ku11)-1), len(ku11))

# print( quick_sort(sorted_ku1,0, len(sorted_ku1)-1), len(sorted_ku1))





