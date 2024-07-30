# Read input values
N, M = map(int, input().split())
w = list(map(int, input().split()))
v = list(map(int, input().split()))

# Initialize the table with 0s
dp = [[0] * (M + 1) for _ in range(N + 1)]

# Fill the table in a bottom-up manner
for i in range(1, N + 1):
    for C in range(M + 1):
        # Option 1: Skip the current item
        dp[i][C] = dp[i - 1][C] #f we skip the current item, the maximum value is the same as if we had one fewer item (dp[i - 1][C]).
        
        # Option 2: Take the current item (if it fits in the knapsack)
        if w[i - 1] <= C:
            dp[i][C] = max(dp[i][C], v[i - 1] + dp[i - 1][C - w[i - 1]]) #If we take the current item (and it fits in the knapsack), we add its value to the maximum value achievable with the remaining capacity (dp[i - 1][C - w[i - 1]]).

# Output the maximum value for the full knapsack capacity
print(dp[N][M])
                                                                                                               