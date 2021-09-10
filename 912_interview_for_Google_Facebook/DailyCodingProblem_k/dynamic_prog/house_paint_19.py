"""
02 Aug 2020

cd /home/kyawnaing/dailycp/dynamic_prog
python3.5 house_paint_19.py


"""

def get_the_min_of_nonci_cells_of_SR(solution_row, num_of_cols, ci):
            print("                    sol row", solution_row)
            nonci_cells_of_SR= [solution_row[i]
                               for i in range(num_of_cols)
                               if i != ci ]

            print( "nonci_cells_of_SR= ", nonci_cells_of_SR)
            a= min(nonci_cells_of_SR)
            return a

def build_houses(matrix):
    num_of_cols  = len(matrix[0])
    solution_row = [0] * num_of_cols
    # print( solution_row)  # => [0, 0]

    
    for row_numXZZY, row in enumerate(matrix):
        new_row = []
        for ci, cv in enumerate(row):
           
            
            a= get_the_min_of_nonci_cells_of_SR(solution_row, num_of_cols, ci)
            print( "Cell-value = ", cv, " Min value= ", a)
            new_row.append(a + cv)
            print( "New_row = ", new_row)
            
        solution_row = new_row
        print( "In loop solution_row = ",  solution_row  ,"----------------\n"   )


    
    print( "Final costs = ",  solution_row)
    print( "Cheapest cost = ", min(solution_row) )
    



m1 = [[4,7],
    [3, 6],
    [2, 5] 

   ]

m2 = [[1,2],
    [3, 4],
    [5,6] 

   ]

m3 = [[19,23, 69],
    [37, 45,76],
    [59,68, 32] 

   ]

m4 = [[4,7,1,2],

    [3, 6, 5,8],

    [4, 5,9,10] 

   ]

build_houses(m4)




