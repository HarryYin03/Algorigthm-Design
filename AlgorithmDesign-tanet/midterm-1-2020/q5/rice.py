import sys
sys.setrecursionlimit(10000)

W = int(input())
k = int(input())
rices = [None] * k

for i in range(k):
    rices[i] = tuple(map(int, input().split()))

memo = {}

def maxRev(i, W):
    if i >= k or W == 0:
        return 0
    if (i,W) in memo:
        return memo[(i,W)]

    max_rev = 0
    for weight, price in rices:
        if weight <= W:
            max_rev = max(max_rev, price + maxRev(i, W-weight))    
    memo[(i,W)] = max_rev
    return memo[(i,W)]

for i in range(k + 1, -1, -1):
    for j in range(W + 1):
        maxRev(i, j)

print(memo[(0,W)])
