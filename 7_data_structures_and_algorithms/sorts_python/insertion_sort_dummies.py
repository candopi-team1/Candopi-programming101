# Insertion Sort

def insertion_sort(data):
   for scanIndex in range(1, len(data)):
     temp = data[scanIndex]
    
     minIndex = scanIndex
    
     while minIndex > 0 and temp < data[minIndex - 1]:
        data[minIndex] = data[minIndex - 1]
        minIndex -= 1
        
     data[minIndex] = temp
     print(data)
     
   return data

data = [9, 5, 7, 4, 2, 8, 1, 10, 6, 3]
data = [9, 5, 7,9, 5, 7, 4, 2, 8, 1, 10, 6, 9, 5, 7,123, 21, 9, 5, 7, 77,12,3]

print(insertion_sort(data))


