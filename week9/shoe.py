n = int(input())
p = list(map(int, input().split()))

dp = [-1] * n

def minPrice(i):
    if i >= n:
        return 0
    
    if dp[i] != -1:
        return dp[i]
    
    cost = p[i] + minPrice(i + 1)
    
    if i + 1 < n:
        cost = min(cost, p[i] + p[i + 1] - (min(p[i], p[i + 1]) * 0.5) + minPrice(i + 2))
    
    if i + 2 < n:
        cost = min(cost, p[i] + p[i + 1] + p[i + 2] - min(p[i], p[i + 1], p[i + 2]) + minPrice(i + 3))
    
    dp[i] = cost
    return dp[i]


for i in range(len(p), -1, -1):
    minPrice(i)

print(f"{dp[0]:.1f}")

