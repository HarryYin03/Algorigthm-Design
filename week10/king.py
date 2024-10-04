N = int(input())

def is_safe_king(board, row, col):
    king_moves = [
        (-1, -1), (-1, 0), (-1, 1), 
        (0, -1), (0, 1), 
        (1, -1), (1, 0), (1, 1)
    ]
    for move in king_moves:
        new_row, new_col = row + move[0], col + move[1]
        if 0 <= new_row < N and 0 <= new_col < N and board[new_row][new_col] == 'K':
            return False
    return True

def solve_kings(board, col):
    if col >= N:
        return True
    
    for i in range(N):
        if is_safe_king(board, i, col):
            board[i][col] = 'K'
            if solve_kings(board, col + 1):
                return True
            board[i][col] = '.'
    
    return False
def print_board(board):
    for row in board:
        print(' '.join(row))
    print()


board = [['.'] * N for _ in range(N)]
if solve_kings(board, 0):
    print_board(board)
else:
    print("No solution found")
