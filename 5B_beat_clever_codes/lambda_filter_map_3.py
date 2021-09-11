salaries = {'Aaron': 10000, 'Alan': 250999, 'Bob': 124286, 'Beckie': 9999, 'Cathy': 4139816}
names= set(["Aaron", "Beckie", "Jack"]) # set

indices =list( map(lambda x : salaries[x],    filter(lambda x: x in salaries, names)       ))

print(indices) # 
print("\n")


################   Same result, 2 easier ways ####################

for sal in salaries :
   if sal in names:    
    print(salaries[sal])


print( [sal for name, sal in salaries.items() if name in names] )
