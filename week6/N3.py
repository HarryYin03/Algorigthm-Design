N, M = map(int, input().split())
w = list(map(int, input().split()))
v = list(map(int, input().split()))
count = 0

def maxVal(i, C):
    global count
    count += 1
    if i == N:
        return 0
    else: 
        skip = maxVal(i + 1, C) #  represents the value if we do not include the current item.
        if w[i] <= C:
            take = v[i] + maxVal(i + 1, C - w[i])#represents the value if we include the current item (only if the weight of the current item is less than or equal to the remaining capacity).
        else:
            take = -1 
        return max(skip, take)
    
print(maxVal(0, M))
print(f'Toal number of calls: {count}') #question 4