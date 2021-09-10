"""
02 Aug 2020

cd /home/kyawnaing/dailycp/dynamic_prog
python3.5 string_decode_dynamic_pg163.py
"""

from collections import defaultdict

def num_encodings(s):
    cache         = defaultdict(int)
    cache[len(s)] = 1 # defaultdict(<class 'int'>, {lenN: 1})
    

    for i in reversed(range(len(s))):
        if s[i].startswith('0'):
            print(  "BAD INPUT ", i, s[i])
            cache[i] = 0

        elif i == len(s) -1 :
            print(  "ONLY-ONCE-ENDING ", i)
            cache[i] = 1            

        else :
             print(  "A", i, "   ----", cache[i], " + " , cache[i + 1])
             cache[i] = cache[i] + cache[i + 1]
             print( cache)

             if int(s[i: i+2]) <=26 :
                print(  "B", i, s[i: i+2], "----", cache[i], " + " , cache[i + 2])
                 
                cache[i] += cache[i+2]
                print( cache) 
        print('')


    return cache #[0]   


sz= "01234511"
sz="12"
sz="09"
sz="0987"

sz= "19999911"

"""

sz="1234511"
sz="123456789"
sz="1111"
sz="22222"
"""
sz="1238765432" # 3
sz="12121212"

sz="123"
# sz="1253"  # OK
# sz="12319" # OK


print(sz)
cache = num_encodings(sz)


print( cache[0])


