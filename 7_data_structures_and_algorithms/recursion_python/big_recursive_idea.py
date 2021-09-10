
# "Think like a programmer" by . Page 150-155


lis1= [1,2,3,4, 50]

def iterative_sum(liss):
    sum =0
    for i in range(0, len(liss)):
        sum += liss[i]

    return sum



sum1 = iterative_sum(lis1)
print(sum1)


    

def dispatcher1(liss):
    lenn= len(liss)
    if lenn ==0:  return 0
    last= liss[lenn-1]
    
    sum_without_last= iterative_sum(liss[0: lenn-1])

    return last + sum_without_last

sum2 = iterative_sum(lis1)
print(sum2)



def recursive_sum(liss):
    lenn= len(liss)
    if lenn ==0:  return 0
    last= liss[lenn-1]

    # ORIG sum_without_last= iterative_sum(liss[0: lenn-1])
    sum_without_last= recursive_sum(liss[0: lenn-1])
    
    return last + sum_without_last

sum3 = recursive_sum(lis1)
print(sum3)



