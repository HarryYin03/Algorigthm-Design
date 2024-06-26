coins = list(map(int, input().split()))
v = int(input())

def mincoin(v):
    if v == 0:
        return 0
    else:
        mc = v
        for c in coins: 
            if c <= v:
                mc = min(mc, 1+ mincoin(v - c))
        return mc
print(mincoin(v))