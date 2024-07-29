import time
import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
w = list(map(int, input().split()))
v = list(map(int, input().split()))
x = [0] * N
def comb(i):
    if i == N:
        sw = sv = 0
        for j in range(N):
            if x[j]:
                sw += w[j]
                sv += v[j]
        if sw > M:
            return -1
        else:
            return sv
            
    else:
        x[i] = 0#x[i] = 0 means the current item i is not included in the knapsack.
        a = comb(i + 1)#a = comb(i + 1) recursively calls comb for the next item, storing the result in a.
        x[i] = 1
        b = comb(i + 1)
    return max(a, b)

print(comb(0))
        