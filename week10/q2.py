def initialize_queens(n):
    return [-1] * n

def print_queens(queens):
    n = len(queens)
    board = [['.' for _ in range(n)] for _ in range(n)]
    for i, row in enumerate(queens):
        if row != -1:
            board[row][i] = 'Q'
    for line in board:
        print(' '.join(line))
    print()
