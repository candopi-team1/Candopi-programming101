"""
06 Aug 2020
cd /home/kyawnaing/dailycp/backtrack
python3.5  sudoku1.py

"""

"""
(1) partial solution
(2) validate the solution so far
(3) checks if the solution is complete

 backtrack :: append/add/set value --> remove/pop/reset value
"""


EMPTY = 0

def sudoku(board):
   if is_complete(board): return board

   # set r,c to value from 1 to 9
   r,c= find_frist_empty(board)

   for val in range(1,10):
      board[r][c]= val
      if valid_so_far(board):
         result= sudoku(board)
         if is_complete(result): return result

      board[r][c]= EMPTY

   return board



def is_complete(board):
   return all(   all(cell is not EMPTY for cell in row) for row in board  )




def find_frist_empty(board):
   for i, row in enumerate(board):
    for j, val in enumerate(row):
        if val == EMPTY:
           return i,j

   return False


def valid_so_far(board):
    if not rows_valid(board):   return False 
    if not cols_valid(board):   return False
    if not blocks_valid(board): return False

    return True
 

def rows_valid(board):    
    for row in board:
     if duplicates(row):  return False
    return True

def cols_valid(board): 
  col_len= len(board[0])
  row_len = len(board)

  for j in range(col_len ):
    # keep col_J constant, vary row_I
    j_col=  [ board[i][j]  for i in range(row_len) ] 
    if duplicates( j_col  ) : return False   

  return True


def blocks_valid(board):  
   for i in range(0,9,3):
     for j in range(0,9,3):
        block=[]
        for k in range(3):
           for l in range(3):
             block.append(board[i+k][j+l])

        if duplicates(block): return False

   return True 

def duplicates(arr):
    cache={}
    for val in arr:
        if val in cache and val is not EMPTY: return True
        cache[val] = True

    return False
 


def blocks_valid2(board):
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


def show_cols(board):
    columns=[]
    
    for col in range(len(board[0])):
        a = []
        for row in range(len(board)):
            a.append(  board[row][col]       )                  
                         
        columns.append(a)     
      
    return columns  


board_ORIG = [
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

result1=[
[2, 5, 8, 7, 3, 6, 9, 4, 1],
[6, 1, 9, 8, 2, 4, 3, 5, 7],
[4, 3, 7, 9, 1, 5, 2, 6, 8],
[3, 9, 5, 2, 7, 1, 4, 8, 6],
[7, 6, 2, 4, 9, 8, 1, 3, 5],
[8, 4, 1, 6, 5, 3, 7, 2, 9],
[1, 8, 4, 3, 6, 9, 5, 7, 2],
[5, 7, 6, 1, 4, 2, 8, 9, 3],
[9, 2, 3, 5, 8, 7, 6, 1, 4]
]


board = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],

         [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],   [0, 0, 0, 0, 0, 0, 0, 0, 0],

         [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]

         ]

result2=[
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[4, 5, 6, 7, 8, 9, 1, 2, 3],
[7, 8, 9, 1, 2, 3, 4, 5, 6],
[2, 1, 4, 3, 6, 5, 8, 9, 7],
[3, 6, 5, 8, 9, 7, 2, 1, 4],
[8, 9, 7, 2, 1, 4, 3, 6, 5],
[5, 3, 1, 6, 4, 2, 9, 7, 8],
[6, 4, 2, 9, 7, 8, 5, 3, 1],
[9, 7, 8, 5, 3, 1, 6, 4, 2]

]


board = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 2, 3, 4, 5, 6, 7, 8, 9],
         [9, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],   [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [4, 6, 7, 9, 1, 2, 5, 3, 8]
         ]

result3=[
[5, 4, 6, 7, 8, 9, 1, 2, 3],
[7, 8, 9, 1, 2, 3, 4, 5, 6],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[9, 1, 2, 3, 4, 5, 8, 6, 7],
[3, 5, 4, 6, 7, 8, 2, 9, 1],
[6, 7, 8, 2, 9, 1, 3, 4, 5],
[2, 3, 5, 8, 6, 7, 9, 1, 4],
[8, 9, 1, 5, 3, 4, 6, 7, 2],
[4, 6, 7, 9, 1, 2, 5, 3, 8]

]  

if __name__=="__main__": 
  winning_board = sudoku(board)
  for row in range(0, 9):
     print( winning_board[row] )




for board in [result1, result2, result3  ]:
 print( "\n\nSHOWING BLOCKS "  )  
 blocks_valid2(board)

 print( "\n\nSHOWING COLUMNS")
 print( show_cols(board) )







