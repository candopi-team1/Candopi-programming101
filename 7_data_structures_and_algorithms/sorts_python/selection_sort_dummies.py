# Selection Sort
   
def selection_sort(data):
   for scanIndex in range(0, len(data)):
      minIndex = scanIndex
    
      for compIndex in range(scanIndex + 1, len(data)):
            if data[compIndex] < data[minIndex]:
                minIndex = compIndex
            
      if minIndex != scanIndex:
          data[scanIndex], data[minIndex] =      data[minIndex], data[scanIndex]
          print(data)

   return data

data = [9, 5, 7, 4, 2, 8, 1, 10, 6, 3]


data = [3456, 23.33,9, 5, 7, 4, 2, 8, 1, 10, 6, 3,  1, 10, 6, 3]


print(selection_sort(data))


