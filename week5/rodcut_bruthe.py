#rod cut with bruthe force
def maxRev(l, prices):
    calls[l] += 1
    if l == 0:
        return 0
    max_revenue = 0
    for i in range(1, l + 1):
        max_revenue = max(max_revenue, prices[i -1] + maxRev(l - i, prices))
        
    return max_revenue

prices = list (map(int, input().split()))
L = len(prices)

calls = [0] * (L + 1)
print(maxRev(L, prices))
print(f"Number of function calls: {calls}")