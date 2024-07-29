def minCoins(coins, m, V, memo):
    if V == 0:
        return 0
    if V in memo:
        return memo[V]
    res = float('inf')
    for i in range(m):
        if coins[i] <= V:
            sub_res = minCoins(coins, m, V - coins[i], memo)
            if sub_res != float('inf') and sub_res + 1 < res:
                res = sub_res + 1
    memo[V] = res
    return res

coins = list(map(int, input().split()))
V = int(input())
memo = {}
print(minCoins(coins, len(coins), V, memo))