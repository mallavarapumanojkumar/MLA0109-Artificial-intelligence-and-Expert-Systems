def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_queens(row, board):
    if row == 8:
        print(board)
        return True
    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col
            if solve_queens(row + 1, board):
                return True
    return False

board = [-1] * 8
solve_queens(0, board)
