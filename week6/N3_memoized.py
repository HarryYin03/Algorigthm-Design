N, M = map(int, input().split())
w = list(map(int, input().split()))
v = list(map(int, input().split()))
memo = {}

def maxVal(i, c):
    if (i, c) in memo:
        return memo[(i, c)]
    if i == N:
        result = 0
    else: 
        skip = maxVal(i + 1, c)
        if w[i] <= c:
            take = v[i] + maxVal(i + 1, c= w[i])
        else:
            take = -1
            
        result  = max(skip, take)
    memo[(i, c)] = result
    return result

print(maxVal(0, M))
print('total number of calls:', len(memo))
            