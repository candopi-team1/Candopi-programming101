
vocab = ["apple", "ape","boy","ball","cat", "joyful"]    
    
word2index = {}  
for i,word in enumerate(vocab):  
     word2index[word]=i  
print(word2index)
# {'apple': 0, 'ape': 1, 'boy': 2, 'ball': 3, 'cat': 4}


words= set(["apple", "joyful", "ball"]) # set

# indices = list(map(lambda x:word2index[x],filter(lambda x:x in word2index, words)))

#OK a1=lambda x:word2index[x]
#OK print(a1)  # <function <lambda> at 0x000002DD6407C8C8>

def a1(x):
    return word2index[x]
print(a1)  # <function a1 at 0x000001BF3840C950>
print(a1("ape"))
try:
 print(a1("application"))
except:
    pass




#OK a2 = lambda x:x in word2index # , words
def a2(xuu):
    y= [x for x in word2index]
    return y

print(a2(11)) # they are keys ==> ['apple', 'ape', 'boy', 'ball', 'cat', 'joyful']

a3=filter(a2, words)

print("Filter ---> ", list(filter( lambda x: x%2 ==0 , [1,2,3, 111,23,45,66]))  )
# Filter --->  [2, 66]

print("Filter ---> ", list(filter( lambda x: x=="go" , [1,2,3, 111,23,45,66, "go"]))  )
# Filter --->  ['go']

list_1=["go","come"]
print("Filter ---> ", list(filter( lambda x: x in list_1 , [1,2,3, 111,"come",23,45,66, "go"]))  )
# Filter --->  ['come', 'go']



mappie= map(a1, a3)
# print(mappie) # <map object at 0x000001D6A6B06320>

indices = list(mappie)

print(indices) # [5, 3, 0]


"""
for i in indices:
    word= vocab[i]
    print(word, word2index[word])
"""
print("\n*******************************************\n")



funct_2_list_map= map(  lambda x: x in [1,2,3], [10,20,30,  3,4,5])
print("Map ---> ",   list(funct_2_list_map)  )


funct_2_list_map= map(  lambda x: x in [1,2,3], [10,20,30,  3,4,5])
print("Map ---> ",   list(funct_2_list_map)  )




 
#indices = list(map(lambda x:word2index[x],              filter(lambda x:x in word2index, words)))
#indices = list(map( funct that gives index of word,            funct that gives all keys of dict, key_word in words

words_that_match_keys=filter(lambda x:x in word2index, words)
indices_of_those_words= map(lambda x:word2index[x],  words_that_match_keys )


indices = list(indices_of_those_words)
print(indices) # [5, 3, 0]


for i in indices:
    word= vocab[i]
    print(word, word2index[word])



