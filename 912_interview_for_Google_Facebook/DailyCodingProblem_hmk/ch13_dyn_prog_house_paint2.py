def get_the_min_of_nonci_cells_of_SR(solution_row, num_of_cols, ci):
            a = max(solution_row)
           
            for mci in range(num_of_cols):
                
                  if mci != ci and solution_row[mci] < a:
                          print( "Meet conds --->",  ci, mci, ",    ", solution_row[mci], " < ",a)
                          a = solution_row[mci]
                  else:
                       print( "NO conds in 3rd loop", ci, mci, ",    ", solution_row[mci], " vs ",a)

            print( a, "\n")
            return a

def build_houses(matrix):
    num_of_cols  = len(matrix[0])
    solution_row = [0] * num_of_cols
    #print( solution_row) # => [0, 0]

    
    for row_numXZZY, row in enumerate(matrix):
        new_row = []
        for ci, cv in enumerate(row):
           
            
            a= get_the_min_of_nonci_cells_of_SR(solution_row, num_of_cols, ci)
            
            new_row.append(a + cv)
            print( "New_row = ", new_row)
            
        solution_row = new_row
        print( "In loop solution_row = ",  solution_row   )  


    
    print( "Finally = ",  solution_row)
    return min(solution_row)
    



m = [[4,7],
    [3, 6],
    [2, 5] 

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
