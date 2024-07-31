def min_tiles(tile_lengths, walkway_length):
    # Initialize the dp array with infinity for all lengths except 0
    dp = [float('inf')] * (walkway_length + 1)
    dp[0] = 0

    # Update dp array for each tile length
    for length in tile_lengths:
        for i in range(length, walkway_length + 1):
            dp[i] = min(dp[i], dp[i - length] + 1)

    # Return the minimum number of tiles required for length L
    return dp[walkway_length]

# Example input
tile_lengths = list(map(int, input().split()))
walkway_length = int(input())

# Find and print the minimum number of tiles
print(min_tiles(tile_lengths, walkway_length))
