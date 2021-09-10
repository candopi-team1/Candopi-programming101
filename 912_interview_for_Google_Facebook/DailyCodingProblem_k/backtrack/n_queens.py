"""
07 Aug 2020
cd /home/kyawnaing/dailycp/backtrack
python3.5  n_queens.py
"""

"""
(1) partial solution
(2) validate the solution so far
(3) checks if the solution is complete

 backtrack :: append/add/set value --> remove/pop/reset value
"""

"""
You have an N by N board. Write a function that returns the no of possible arrangements of the board where 
N queens can be placed on the board without threatening each other,
i.e. no two queens share the same row, column, or diagonal.
"""

def n_queens(n, board=[]):
   if n == len(board): return 1

   count= 0
  
   for col in range(n):
      board.append(col)
      if is_valid(board):
        count += n_queens(n, board)
        # OK if n == len(board): print(n, col, board) # kkn: This is successful positioning.
      board.pop()

   return count


def col_attack(current_col, prev_col):
      return abs(current_col - prev_col)


def diago_attack(currrent_row, prev_row):
      return (currrent_row - prev_row)

def is_valid(board):
    currrent_queen_row, currrent_queen_col= len(board)-1,  board[-1]

    for row, col in enumerate(board[:-1]):
       col_vul= col_attack(currrent_queen_col, col)

       if col_vul == 0 or col_vul == diago_attack(currrent_queen_row, row): 
             return False

    return True





if __name__ == "__main__":
    for n in range(1, 10):
        print(n, " ---> ", n_queens(n))
        print("  ")
       

n= 1 # 8 # 7 # 6 # 4 # 5
print(n, " ---> ", n_queens(n))
  

"""
4 2 [1, 3, 0, 2]
4 1 [2, 0, 3, 1]
4  --->  2
"""

"""
5 3 [0, 2, 4, 1, 3]
5 2 [0, 3, 1, 4, 2]
5 4 [1, 3, 0, 2, 4]
5 3 [1, 4, 2, 0, 3]
5 4 [2, 0, 3, 1, 4]
5 0 [2, 4, 1, 3, 0]
5 1 [3, 0, 2, 4, 1]
5 0 [3, 1, 4, 2, 0]
5 2 [4, 1, 3, 0, 2]
5 1 [4, 2, 0, 3, 1]
5  --->  10
"""










