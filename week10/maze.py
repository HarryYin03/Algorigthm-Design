from collections import deque

class State:
    def __init__(self, y, x, step=0):
        self.y = y
        self.x = x
        self.step = step

def is_valid(maze, y, x):
    return 0 <= y < len(maze) and 0 <= x < len(maze[0]) and maze[y][x] == 0

def read_maze():
    M, N = map(int, input("Enter dimensions of the maze (rows columns): ").split())
    print(f"Enter the maze ({M} rows, each with {N} integers):")
    return [list(map(int, input().split())) for _ in range(M)]

def bfs_maze(maze, entrance, exit):
    queue = deque([State(entrance[0], entrance[1], 0)])
    visited = set()
    visited.add((entrance[0], entrance[1]))
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    steps = [[-1] * len(maze[0]) for _ in range(len(maze))]  # Step matrix
    steps[entrance[0]][entrance[1]] = 0

    while queue:
        current = queue.popleft()
        if (current.y, current.x) == exit:
            print_step_matrix(steps)  # Optional: print the step matrix
            return current.step
        for dy, dx in directions:
            ny, nx = current.y + dy, current.x + dx
            new_step = current.step + 1
            if is_valid(maze, ny, nx) and (ny, nx) not in visited:
                visited.add((ny, nx))
                steps[ny][nx] = new_step
                queue.append(State(ny, nx, new_step))
    print_step_matrix(steps)  # Optional: print the step matrix
    return -1

def print_step_matrix(steps):
    print("Step matrix showing the number of steps to each position in the maze:")
    for row in steps:
        print(' '.join(f"{x:3}" if x != -1 else "  X" for x in row))

if __name__ == "__main__":
    maze = read_maze()
    start_y, start_x = map(int, input("Enter start position (y x): ").split())
    exit_y, exit_x = map(int, input("Enter exit position (y x): ").split())
    steps = bfs_maze(maze, (start_y, start_x), (exit_y, exit_x))
    print(f"Shortest path length from start to exit: {steps if steps != -1 else 'No path available'}")
