def bfs_maze_optimized(maze, entrance, exit):
    queue = deque([State(entrance[0], entrance[1], 0)])
    visited = set()
    visited.add((entrance[0], entrance[1]))
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    steps = [[-1] * len(maze[0]) for _ in range(len(maze))]  # Step matrix
    steps[entrance[0]][entrance[1]] = 0

    while queue:
        current = queue.popleft()
        if (current.y, current.x) == exit:
            return current.step
        for dy, dx in directions:
            ny, nx = current.y + dy, current.x + dx
            new_step = current.step + 1
            if is_valid(maze, ny, nx) and (steps[ny][nx] == -1 or new_step < steps[ny][nx]):
                steps[ny][nx] = new_step
                queue.append(State(ny, nx, new_step))
    return -1
