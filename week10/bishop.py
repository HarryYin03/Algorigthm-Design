N = int(input())

def is_safe_bishop(board, row, col):
    # Check for diagonal attacks
    for i in range(N):
        if row - i >= 0 and col - i >= 0 and board[row - i][col - i] == 'B':
            return False
        if row - i >= 0 and col + i < N and board[row - i][col + i] == 'B':
            return False
        if row + i < N and col - i >= 0 and board[row + i][col - i] == 'B':
            return False
        if row + i < N and col + i < N and board[row + i][col + i] == 'B':
            return False
    return True

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()


def solve_bishops(board, col):
    if col >= N:
        return True
    
    for i in range(N):
        if is_safe_bishop(board, i, col):
            board[i][col] = 'B'
            if solve_bishops(board, col + 1):
                return True
            board[i][col] = '.'
    
    return False

board = [['.'] * N for _ in range(N)]
if solve_bishops(board, 0):
    print_board(board)
else:
    print("No solution found")
