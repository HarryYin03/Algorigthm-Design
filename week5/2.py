import sys
sys.setrecursionlimit(10000)
p = input().split()
L = len(p) 
for i in range(L):
    p[i] = int(p[i])
p.insert(0, 0)

calls= [0] * (L + 1)
def maxRev(l):
    global p, L
    calls[l] += 1
    if l == 0:
        return 0
    else:
        mx = 0
        for i in range(1, l + 1):
            mx = max(mx, p[i] + maxRev(l - i))
    return mx

print(maxRev(L))
print(calls)