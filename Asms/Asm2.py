def minPrice(l, p, memo):
    if memo[l] != None:
        return memo[l]
    if l == 0:
        memo[l] = 0
        return memo[l]
    else:
        mx = float('inf')
        for i in range(1, l + 1):
            if i <= l and p[i - 1] != -1:
                mx = min(mx, p[i - 1] + minPrice(l - i, p, memo))  
        memo[l] = mx
        return memo[l] 

tests = int(input())
results = []
for i in range(tests):
 n, k = list(map(int, input().split()))
 prices = list(map(int, input().split()))
 results.append(minPrice( k, prices, [None] * (k + 1)))
    
for i in results:
    if i == float('inf'):
        print(-1)
    else:
        print(i)