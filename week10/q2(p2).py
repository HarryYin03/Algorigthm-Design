def is_valid(maze, y, x):
    return 0 <= y < len(maze) and 0 <= x < len(maze[0]) and maze[y][x] == 0
