import sys
sys.setrecursionlimit(10000)

def comb(i):
    if i == n: 
        print(x)
    else: 
        x[i] = 0
        comb(i + 1)
        x[i] = 1
        comb(i + 1)
        
n = 1
x = [0] * n
comb(0)
