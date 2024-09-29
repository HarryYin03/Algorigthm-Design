from collections import deque

def bfs_maze_state_count(maze, entrance, exit):
    queue = deque([State(entrance[0], entrance[1], 0)])
    visited = set()
    visited.add((entrance[0], entrance[1]))
    state_count = 1  # Start with the initial state
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        current = queue.popleft()
        if (current.y, current.x) == exit:
            return current.step, state_count
        for dy, dx in directions:
            ny, nx = current.y + dy, current.x + dx
            if is_valid(maze, ny, nx) and (ny, nx) not in visited:
                visited.add((ny, nx))
                queue.append(State(ny, nx, current.step + 1))
                state_count += 1
    return -1, state_count

# Example usage:
M, N = 5, 5  # Example maze dimensions
maze = [[0]*N for _ in range(M)]  # Sample maze with no walls
entrance = (0, 0)
exit = (4, 4)
steps, total_states = bfs_maze_state_count(maze, entrance, exit)
print(f"Steps: {steps}, Total states created: {total_states}")
