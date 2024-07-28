def rodcut(i, prices, memo = None):
    if memo is None: 
        memo = {}
    if i in memo: 
        return memo[i]
    if i == 0:
        return 0
    max_revenue = 0
    for j in range(1, i + 1):
        max_revenue = max(max_revenue, prices[j - 1] + rodcut(i - j, prices, memo))
    return max_revenue

prices = list(map(int, input().split()))
rod_length = len(prices)
print(rodcut(rod_length, prices))