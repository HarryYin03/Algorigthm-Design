class obj:
    def __init__(self, w, v):
        self.w = w  # Weight of the item
        self.v = v  # Value of the item
        self.r = v / w  # Value-to-weight ratio (used for sorting)

# Input reading
x = input().split()
N = int(x[0])  # Number of items
M = int(x[1])  # Maximum capacity of the knapsack
w = input().split()  # List of weights
v = input().split()  # List of values
item = []
for i in range(N):
    item.append(obj(int(w[i]), int(v[i])))

# Sort items by value-to-weight ratio in decreasing order
item.sort(key=lambda x: x.r, reverse=True)

# Global variables
maxV = 0  # Maximum value found so far
count = 0  # Count of recursive calls

# Bounding function to estimate the maximum value achievable from a given state
def Bound(i, C):
    global item, N
    
    sw = 0  # Accumulated weight
    sv = 0  # Accumulated value
    j = i
    f = 1.0  # Fractional part (1.0 means full item can be taken)
    
    # Greedily take as much value as possible within remaining capacity
    while j < N and f == 1.0:
        wj = min(C - sw, item[j].w)
        f = float(wj) / item[j].w  # Fraction of the item that can fit
        sw += f * item[j].w
        sv += f * item[j].v
        j += 1
    return sv

# DFS with Branch and Bound to explore all possibilities
def dfs(i, sumW, sumV):
    global maxV, item, N, M, count
    count += 1

    # If the current weight exceeds capacity, prune the branch
    if sumW > M:
        return

    # Compute bounds for both skipping and taking the current item
    bound_skip = sumV + Bound(i + 1, M - sumW)  # Bound if we skip item i
    bound_take = sumV + item[i].v + Bound(i + 1, M - sumW - item[i].w) if i < N and sumW + item[i].w <= M else 0

    # Prune if neither bound is better than maxV
    if max(bound_skip, bound_take) <= maxV:
        return

    # Update maxV when we reach the last item and the knapsack is valid
    if i == N:
        if sumW <= M:
            maxV = max(maxV, sumV)
    else:
        # Search the option with the higher bound first
        if bound_take > bound_skip:
            if sumW + item[i].w <= M:  # Only take the item if it fits
                dfs(i + 1, sumW + item[i].w, sumV + item[i].v)
            dfs(i + 1, sumW, sumV)  # Explore skipping the item
        else:
            dfs(i + 1, sumW, sumV)  # Explore skipping the item first
            if sumW + item[i].w <= M:  # Only take the item if it fits
                dfs(i + 1, sumW + item[i].w, sumV + item[i].v)

# Start DFS from the first item
dfs(0, 0, 0)

# Output the maximum value found and the number of recursive calls
print(maxV)
print(count)