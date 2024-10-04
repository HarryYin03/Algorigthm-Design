import sys
sys.setrecursionlimit(100000)

N = int(input())

colors = [None] * N
for i in range(N):
    colors[i] = list(map(int, input().split()))



min_diff = float('inf')
def comb(i, totalvivid, totaldull):
    global colors
    global min_diff
    if i == N:
        if totaldull == 0 and totalvivid == 1:
            return float('inf')
        else: 
            diff = abs(totaldull - totalvivid)
            min_diff = min(min_diff, diff)
    else:
        comb(i + 1, totalvivid * colors[i][0] , totaldull + colors[i][1])
        comb(i + 1, totalvivid  , totaldull )


comb(0, 1, 0)

print(min_diff)

