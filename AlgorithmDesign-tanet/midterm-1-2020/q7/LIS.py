import sys
sys.setrecursionlimit(1000000)
sequence = list(map(int, input().split()))
memo = {}

def recurse(n, prev):
        if n == len(sequence):
            return 0
        if (n, prev) in memo:
            return memo[(n, prev)]
        else: 
            exclude = recurse(n + 1, prev)
            include = 0
            if prev == -1 or sequence[n] > sequence[prev]:
                include = 1 + recurse(n + 1, n)
            memo[(n, prev)] = max(exclude, include)
            return memo[(n, prev)]
print(recurse(0, -1))