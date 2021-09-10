def n_queens(n, board = []):
    # print( n)
    if n == len(board):
        return 1

    count = 0
    for col in range(n):
        board.append(col)
        #print( "BOARD 1 = ", board)
        if column_valid(board) and diagonal_valid(board):
            count += n_queens(n, board)
        board.pop()
        #print( "BOARD 2 = ", board))
    return count


def column_valid(board):       
    current_Q_col = board[-1]

    for row,col in enumerate(board[:-1]):
        diff = abs(current_Q_col - col) 	
        if diff == 0:
            return False
    return True



def diagonal_valid(board):
    current_Q_row = len(board) - 1
    current_Q_col = board[-1]
    for row,col in enumerate(board[:-1]):
        diff = current_Q_row - row	
        if diff == abs(current_Q_col - col):
            return False    
    return True




no_of_queens = 12 # 11# 9# 8 # 5 # ==>  2680  ways! -->  14200  ways!
ans = n_queens(no_of_queens)
print( ans, " ways!")
				


