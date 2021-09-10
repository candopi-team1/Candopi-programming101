# "Think like a programmer" by . Page 150-155


NUM = 5 

def factorial(n):
    if n == 1:  return 1
    
    # ORIG prodd= n * iif(n-1)
    product= n * factorial(n-1)
    
    return product

facto5 = factorial(NUM)
print(facto5)



