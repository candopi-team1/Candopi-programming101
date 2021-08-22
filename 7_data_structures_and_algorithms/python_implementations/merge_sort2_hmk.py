list1 = [1,3,5,7,9, 12,34,56, 88,90, 120]
list2 = [0, 1, 2,4,6,8,10, 34,36,78,90]

'''
list1 = [1,3,5,7]
list2 = [8,10, 34,36,78,90]


list1 = [8,10, 34,36,78,90]
list2 = [1,3,5,7]

'''
def merge(list1, list2):# , final_list): 
   len1 = len(list1)
   len2 = len(list2)
   final_list = [None] * (len1 + len2)
    
   a,b,c = 0,0,0

   while a < len1 and b < len2:
        if list1[a] < list2[b]:
          final_list[c] = list1[a]
          a += 1   

        elif list2[b] < list1[a]:
            final_list[c] = list2[b]
            b += 1     
     
        else :
           final_list[c] = list1[a]
           final_list[c + 1] = list2[b]
           a+= 1; b+= 1;
           c += 1     

        c += 1

   while a < len1 :
       final_list[c] = list1[a]
       a += 1
       c += 1

   while b < len2 :
       final_list[c] = list2[b]
       b += 1
       c += 1

   print( final_list)
   # print( len1, len2, len(final_list))
   return final_list



def mergesort(list1):
    lenn = len(list1)
    if lenn <= 1: return list1
    
    mid = int(lenn/2)
    listleft, listright = list1[0:mid], list1[mid:]
    mergesort(listleft)
    mergesort(listright)
  
    
    final_list = merge( mergesort(listleft),mergesort(listright) )
    return final_list

   

list1= []
print( "Type numbers you want to sort. To stop type 'xxx'")
while True :
    number = input()
    if str(number) == 'xxx': break 
    list1.append(int(number))

# list1 = [2,7,56,567,630,18,4,63,11,2,7]
print( list1)
print(   mergesort(list1) )   
