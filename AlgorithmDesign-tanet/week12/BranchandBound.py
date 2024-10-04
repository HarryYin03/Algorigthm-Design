class obj:
    def __init__(self, w, v):
        self.w = w
        self.v = v
        self.r = v / w


x = input().split()
N = int(x[0])
M = int(x[1])
w = input().split()
v = input().split()
item = []
for i in range(N):
    item.append(obj(int(w[i]), int(v[i])))

maxV = 0
count = 0


def Bound(i, sumW, sumV):
    global item, N, M

    RightWeight = 0
    SV = 0
    propotion = 1
    j = i + 1

    # proportion == 1 means the item[j] can be put into the knapsack physically
    # M-sumW-RightWeight > 0 means there is still space in the knapsack

    # j < N means there are still items to be considered
    while j < N and propotion == 1:
        # if the item[j] can be put into the knapsack physically then propotion is 1
        # otherwise propotion is the proportion of the item[j] that can be put into the knapsack

        propotion = min(M - sumW - RightWeight, item[j].w) / item[j].w
        RightWeight += propotion * item[j].w
        SV += propotion * item[j].v
        j += 1

    return SV + sumV


maxBound = 0


def dfs(i, sumW, sumV):
    global maxV, item, N, M, count, maxBound
    count += 1
    maxBound = max(maxBound, Bound(i, sumW, sumV))

    if i == N:
        maxV = max(maxV, sumV)  # update maxV
    else:
        if sumW + item[i].w <= M:
            dfs(i + 1, sumW + item[i].w, sumV + item[i].v)

        if Bound(i, sumW, sumV) > maxV:
            dfs(i + 1, sumW, sumV)


item.sort(key=lambda x: x.r, reverse=True)
dfs(0, 0, 0)
print(maxV)
print(count)

'''In the Knapsack Branch and Bound approach, you sort the items in decreasing order of their value-to-weight ratios (r). 
This heuristic is used to prioritize items that provide the most value for their weight.
The Bound function calculates an upper bound on the maximum value that can be obtained with the current partial solution. 
It uses the remaining capacity of the knapsack (M - sumW - RightWeight) and the proportion of the next item that can be included.
The dfs function explores the solution space recursively, considering two possibilities for each item: including it or not including it.
The maxBound variable keeps track of the maximum bound encountered during the search.
The approach uses a combination of a heuristic (r-based sorting) and a branch-and-bound strategy to efficiently explore the solution space.
This approach can be effective for certain types of instances where the heuristic provides a good initial bound and pruning is effective.'''
