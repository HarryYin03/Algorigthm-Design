def read_maze():
    M, N = map(int, input().split())
    return [list(map(int, input().split())) for _ in range(M)]

maze = read_maze()
