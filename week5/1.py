import sys
sys.setrecursionlimit(10000)
p = input().split()
L = len(p) 
for i in range(L):
    p[i] = int(p[i])
p.insert(0, 0)

calls = [0] * (L + 1)

def maxRev(l):
    global p, calls
    calls[l] += 1  # Increment the call count for length l
    if l == 0:
        return 0
    else:
        mx = 0
        for i in range(1, l + 1):
            mx = max(mx, p[i] + maxRev(l - i))
    return mx

def maxRevMemo(l, memo):
    global p, calls
    
    if memo[l] != -1:  # Check if the result is already computed
        return memo[l]
    
    calls[l] += 1
    
    if l == 0:
        result = 0
    else:
        result = 0
        for i in range(1, l + 1):
            result = max(result, p[i] + maxRevMemo(l - i, memo))
    
    memo[l] = result  # Store the computed result
    return result

memo = [-1] * (L + 1)
print(maxRevMemo(L, memo))
print(calls)
