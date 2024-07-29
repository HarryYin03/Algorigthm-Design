def maxRev(l, prices, memo):
    calls[l] += 1
    if memo[l] is not None:
        return memo[l]
    if l == 0:
        return 0
    max_rev = 0
    for i in range(1, l + 1):
        max_rev = max(max_rev, prices[i-1] + maxRev(l -i, prices, memo))
    return max_rev

prices = list(map(int, input().split()))
L = len(prices)
memo = [None] * (L + 1)
calls = [0] * (L + 1)
print(maxRev(L, prices, memo))
print(f"Number of calls: {sum(calls)}")
print(f"Number of calls for each length: {calls[1:]}")
print(f"Memo: {memo[1:]}")
