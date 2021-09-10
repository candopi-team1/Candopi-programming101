"""
03 Aug 2020

cd /home/kyawnaing/dailycp/dynamic_prog
python3.5 coin_ways_topdown_memoize.py

"""


def coin_ways(n, cache={0:1}):
   if n in cache:
    return cache[n]

   if n < 0:
     return 0
 
   
   cache[n]= coin_ways(n-1) + coin_ways(n-5) 

   return cache[n]


n= 100  # 823322219501  --- fast

# n= 6500 # RecursionError: maximum recursion depth exceeded in comparison
# n= 2500 # RecursionError: maximum recursion depth exceeded in comparison
# n = 1200 # RecursionError: maximum recursion depth exceeded in comparison
# n= 999 # RecursionError: maximum recursion depth exceeded in comparison
n =990   # 121 digits -- fast


ways = coin_ways(n)
print( ways )

print(len(str(ways)))
