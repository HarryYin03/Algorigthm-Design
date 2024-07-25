def knapsack(N, W, items):
    # Initialize the table for dynamic programming
    dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]

    # Fill the table in a bottom-up manner
    for i in range(1, N + 1):
        value, weight = items[i-1]
        for w in range(W + 1):
            if weight <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - weight] + value)
            else:
                dp[i][w] = dp[i-1][w]

    # The maximum value that can be obtained with the given weight capacity
    return dp[N][W]

# Read input
import sys
input = sys.stdin.read
data = input().split()

# Parse input
N = int(data[0])
W = int(data[1])
items = [(int(data[i*2+2]), int(data[i*2+1+2])) for i in range(N)]

# Get the result
result = knapsack(N, W, items)
print(result)
