FLAT = 0
UPPER2 = 1
LOWER2 = 2

L = int(input())

# Initialize the DP table with zero values
dp = [[0] * 3 for _ in range(L + 1)]

# Base case: There is 1 way to tile a grid of length 0 in FLAT state
dp[0][FLAT] = 1

# Fill the DP table
for d in range(L):
    dp[d+1][UPPER2] += dp[d][FLAT]
    dp[d+1][LOWER2] += dp[d][FLAT]
    
    if d + 2 <= L:
        dp[d+2][FLAT] += dp[d][FLAT]
        dp[d+2][UPPER2] += dp[d][UPPER2]
        dp[d+2][LOWER2] += dp[d][LOWER2]
    
    dp[d+1][FLAT] += dp[d][UPPER2] + dp[d][LOWER2]

# The result is the number of ways to tile a grid of length L in FLAT state
print(dp[L][FLAT])
