from collections import deque

# Define the target state and possible moves (down, up, right, left)
goal_state = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left

# BFS function to solve the 8-puzzle
def bfs(start_state):
    start_state = tuple(tuple(row) for row in start_state)  # Convert the start state to tuple of tuples
    queue = deque([(start_state, 0)])  # Each element in the queue is (current state, steps)
    visited = set()  # To store visited states
    visited.add(start_state)
    
    while queue:
        current_state, steps = queue.popleft()

        # Check if we've reached the goal
        if current_state == goal_state:
            return steps

        # Locate the empty space (0)
        for i in range(3):
            for j in range(3):
                if current_state[i][j] == 0:
                    zero_row, zero_col = i, j

        # Explore all 4 possible moves
        for dr, dc in moves:
            new_row, new_col = zero_row + dr, zero_col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                # Create a new state by swapping the 0 with the adjacent tile
                new_state = [list(row) for row in current_state]
                new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]
                new_state = tuple(tuple(row) for row in new_state)  # Convert it to tuple of tuples

                # If the new state hasn't been visited, add it to the queue
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, steps + 1))

    return -1  # Shouldn't happen due to problem constraints

# Input parsing
initial_state = []
for _ in range(3):
    initial_state.append(list(map(int, input().split())))

# Call the BFS function and print the result
result = bfs(initial_state)
print(result)
