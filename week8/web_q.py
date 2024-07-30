def knapsack(N, W, items):
    # Initialize a DP table with dimensions (N+1) x (W+1)
    dp = [[0] * (W + 1) for _ in range(N + 1)]

    # Process each item
    for i in range(1, N + 1):
        value, weight = items[i - 1]
        for w in range(W + 1):
            if weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
            else:
                dp[i][w] = dp[i - 1][w]
    
    # The answer is in dp[N][W]
    return dp[N][W]

# Read inputs
N, W = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

# Get the result
result = knapsack(N, W, items)

# Print the result
print(result)
