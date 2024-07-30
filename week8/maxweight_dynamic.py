import sys
import time
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
w = list(map(int, input().split()))
v = list(map(int, input().split()))

mm = [[0] * (M + 1) for i in range(N + 1)] #Create a 2D list mm with dimensions (N + 1) x (M + 1) initialized to 0. This table will store the maximum values for subproblems

for i in range(N - 1, -1, -1):#iterates from the last item to the first.
    for C in range(0, M + 1): #iterates from zero capacity to the maximum capacity
        skip = mm[i + 1][C] # Maximum value if we skip the current item
        take = 0
        if w[i] <= C: #If the current item's weight is less than or equal to the current capacity, update take to include the current item's value and the best solution for the remaining capacity.
            take = v[i] + mm[i + 1][C - w[i]]
        mm[i][C] = max(skip, take)

st =  time.process_time()  
print(mm[0][M])
print('total number of calls:', len(mm))#Print the maximum value for the original problem (item 0 and capacity M) and the total number of subproblems solved.
et = time.process_time()
print('time taken:', et-st)