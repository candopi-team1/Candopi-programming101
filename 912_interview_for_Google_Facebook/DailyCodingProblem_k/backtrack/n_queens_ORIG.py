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




def nQueens(n, board=[]):
    if n == len(board):
        return 1
    
    count = 0
    for col in range(n):
        board.append(col)
        if isValid(board):
            count += nQueens(n, board)
        board.pop()
    
    return count

def isValid(board):
    currentQueenRow, currentQueenCol = len(board)-1, board[-1]

    for row, col in enumerate(board[:-1]):
        diff = abs(currentQueenCol - col)

        if diff == 0 or diff == currentQueenRow - row:
            return False
    
    return True



if __name__ == "__main__":
    for n in range(10):
        print(nQueens(n))


