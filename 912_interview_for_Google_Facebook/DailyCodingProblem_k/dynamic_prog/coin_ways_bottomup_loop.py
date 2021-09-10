"""
03 Aug 2020

cd /home/kyawnaing/dailycp/dynamic_prog
python3.5  coin_ways_bottomup_loop.py


BETTER THAN top-dwon version
"""

def coin_ways(n):
 
 cache={0:1}

 for i in range(1, n+1):
   cache[i]= cache.get(i-1, 0) + cache.get(i-5, 0) 

 return cache[n]


n= 100  # 823322219501  --- fast
n= 500  # 5820217480158126341009576049727194571183784772138787991739440 # fast

n= 6500   # 794 digits   ---- still fast 
n= 16500  # 2015  digits ---- still fast 

ways = coin_ways(n)
print( ways )

print(len(str(ways)))
