EMPTY = 0

def sudoku(board):
   if is_complete(board):
      return board
   
   r,c = find_1st_empty(board)
      

   for i in range(1,10):
       board[r][c] = i

       if valid_so_far(board):
          result = sudoku(board)

          if is_complete(result):
             return result

       board[r][c] = EMPTY

   return board



def is_complete(board):
    # ORIG-OK 
    # return all(all(val is not EMPTY for val in row) for row in board)
    
    row_checks= []
    for row in board:
        row_checks.append( all(val is not EMPTY for val in row) )
    # print( row_checks)
    
    return all(row_checks)

   
def find_1st_empty(board):
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val == EMPTY:
               return i, j

    return False


def valid_so_far(board):
    if not rows_valid(board):       return False

    if not cols_valid(board):       return False

    if not blocks_valid(board):     return False

    return True


def rows_valid(board):
    for row in board:
       if duplicates(row):
          return False
    return True



def cols_valid(board):
    for j in range(len(board[0])):
        if duplicates([board[i][j] for i in range(len(board))]  ):
           return False

    return True



def blocks_valid(board):
    for i in range(0,9,3):
        for j in range(0,9,3):
            block = []
            for k in range(3):
                for al in range(3):
                    block.append(board[i+k][j+al])
                
            if duplicates(block):
               return False
    return True        
    

def duplicates(arr):
   c = {}
   for val in arr:
       if val in c and val is not EMPTY:
          return True
       c[val] = True
   return False    
   


board = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],   [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]
         ]


board = [
         [2, 5, 0, 0, 3, 0, 9, 0, 1],
         [0, 1, 0, 0, 0, 4, 0, 0, 0],
         [4, 0, 7, 0, 0, 0, 2, 0, 8],
         [0, 0, 5, 2, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 9, 8, 1, 0, 0],
         [0, 4, 0, 0, 0, 3, 0, 0, 0],
         [0, 0, 0, 3, 6, 0, 0, 7, 2],
         [0, 7, 0, 0, 0, 0, 0, 0, 3],
         [9, 0, 3, 0, 0, 0, 6, 0, 4]
         ]



board = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 2, 3, 4, 5, 6, 7, 8, 9],
         [9, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],   [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [4, 6, 7, 9, 1, 2, 5, 3, 8]
         ]



win_board = sudoku(board)
for row in range(0, 9):
     print( win_board[row])


"""


board=[
[2, 5, 8, 7, 3, 6, 9, 4, 1],
[6, 1, 9, 8, 2, 4, 3, 5, 7],
[4, 3, 7, 9, 1, 5, 2, 6, 8],
[3, 9, 5, 2, 7, 1, 4, 8, 6],
[7, 6, 2, 4, 9, 8, 1, 3, 5],
[8, 4, 1, 6, 5, 3, 7, 2, 9],
[1, 8, 4, 3, 6, 9, 5, 7, 2],
[5, 7, 6, 1, 4, 2, 8, 9, 3],
[9, 2, 3, 5, 8, 7, 6, 1, 4],
   ]

print( "\n\nSHOWING BLOCKS "
def blocks_valid(board):
    for row in range(0,9,3):
        for col in range(0,9,3):
            block = []
            for k in range(3):
                for al in range(3):
                    block.append(board[row +k][col +al])
            print( block)
            
            if duplicates(block):
               return False
    return True        
    
blocks_valid(board)

print( "\n\nSHOWING COLUMNS")
def show_cols(board):
    columns=[]
    
    for col in range(len(board[0])):
        a = []
        for row in range(len(board)):
            a.append(  board[row][col]       )                  
                         
        columns.append(a)
     
      
    return columns           

print( show_cols(board))

"""
