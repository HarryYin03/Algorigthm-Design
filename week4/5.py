p = list(map(int, input().split()))
n = len(p)
p = [0] + p

def maxRec(l):
    if l == 0:
        return 0
    else:
        mxp = 0
        for c in range(1, l+1):
            mxp = max(mxp, p[c] + maxRec(l - c))
        return mxp
print(maxRec(n))