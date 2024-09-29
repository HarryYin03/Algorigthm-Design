from collections import deque

def bfs_maze(maze, entrance, exit):
    queue = deque([State(*entrance, 0)])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()
    visited.add(entrance)
    while queue:
        current = queue.popleft()
        if (current.y, current.x) == exit:
            return current.step
        for dy, dx in directions:
            ny, nx = current.y + dy, current.x + dx
            if (ny, nx) not in visited and is_valid(maze, ny, nx):
                visited.add((ny, nx))
                queue.append(State(ny, nx, current.step + 1))
    return -1
