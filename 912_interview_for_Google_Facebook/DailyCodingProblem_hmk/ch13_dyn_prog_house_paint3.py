def get_the_min_of_nonci_cells_of_SR(solution_row, num_of_cols, ci):

            nonci_cells_of_SR= [solution_row[i]
                               for i in range(num_of_cols)
                               if i != ci ]

            print( "nonci_cells_of_SR= ", nonci_cells_of_SR)
            a= min(nonci_cells_of_SR)
            return a

def build_houses(matrix):
    num_of_cols  = len(matrix[0])
    solution_row = [0] * num_of_cols
    #print( solution_row # => [0, 0]

    
    for row_numXZZY, row in enumerate(matrix):
        new_row = []
        for ci, cv in enumerate(row):
           
            
            a= get_the_min_of_nonci_cells_of_SR(solution_row, num_of_cols, ci)
            print( "Cell value = ", cv)
            new_row.append(a + cv)
            print( "New_row = ", new_row)
            
        solution_row = new_row
        print( "In loop solution_row = ",  solution_row  ,"\n" )  


    
    print( "Final costs = ",  solution_row)
    print( "Cheapest cost = ", min(solution_row))
    




m = [[19,23, 69],
    [37, 45,76],
    [59,68, 32] 

   ]


"""
e1=enumerate(m)

print( e1.next())
print( e1.next())
print( e1.next())

=> (0, [4, 7])
(1, [3, 6])
(2, [2, 5])
"""
"""
row = [4, 7]
e2=  enumerate(row)
print( e2)
print( e2.next())
print( e2.next())
=>
(0, 4)
(1, 7)
"""
# print( len(m[0])) # 2
# print( range(2))
build_houses(m)
