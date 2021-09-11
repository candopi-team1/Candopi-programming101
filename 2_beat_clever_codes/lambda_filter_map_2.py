
word2index = {'apple': 0, 'ape': 1, 'boy': 2, 'ball': 3, 'cat': 4}

words= set(["apple", "joyful", "ball"]) # set

 
indices = list(map(lambda x:word2index[x],     filter(lambda x:x in word2index, words)))

indices2 = list(map(lambda x:word2index[x],    ["apple", "ball", ] )     )
#                   indices_of_those_words      words_that_match_keys 


try:
    indices3 = list(map(lambda x:word2index[x],    ["apple", "ball", "great"] )     )
except KeyError as e:
     print("KeyError   ---> ", e)


# words_that_match_keys   = filter(lambda x:x in word2index, words)
# indices_of_those_words  = map(lambda x:word2index[x],  words_that_match_keys )


print(indices) # [3, 0]
print(indices2) # [3, 0]
