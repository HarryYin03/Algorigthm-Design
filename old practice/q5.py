def max_earnings(W, sack_sizes):
    dp = [0] * (W + 1)
    
    for weight, price in sack_sizes:
        for i in range(weight, W + 1):
            dp[i] = max(dp[i], dp[i - weight] + price)
    
    return dp[W]

# Example usage:
W = int(input())
k = int(input())
sack_sizes = [tuple(map(int, input().split())) for _ in range(k)]
print(max_earnings(W, sack_sizes))
