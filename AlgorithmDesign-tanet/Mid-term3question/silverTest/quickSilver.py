import sys
sys.setrecursionlimit(100000)

N, K , S = map(int, input().split())

balls = [None] * N
for i in range(N):
    pos, score = map(int, input().split())
    balls[i] = [pos, score]


memo = {}

def quickSilver(i, K , S):
    global balls
    if (i, K, S) in memo:
        return memo[(i, K, S) ]
    else:
        if i == N:
            memo[(i, K, S) ] = 0
            return memo[(i, K, S) ]
        else:
            if abs(S - balls[i][0]) <= K:
                leave = 0 + quickSilver(i + 1, K, S)
                take = balls[i][1] + quickSilver(i + 1, K, balls[i][0])
                memo[(i, K, S) ] = max(leave, take)
                return memo[(i, K, S) ]
            else:
                memo[(i, K, S) ] = quickSilver(i + 1, K, S)
                return memo[(i, K, S)]
        
        
    
    
print(quickSilver(0, K, S))


# used /explain (rerun without)
# The time complexity of the provided code depends on the size of the input, specifically the value of N. Let's analyze the code to determine its time complexity.

# The code uses recursion to solve the problem. The quickSilver function is called recursively with different parameters. The function checks if the current state (i, K, S) has already been memoized in the memo dictionary. If it has, the function retrieves the memoized result and returns it. Otherwise, it proceeds with the recursive calculations.

# In the worst case, the function will be called with different combinations of i, K, and S values. Since i can take values from 0 to N-1, K can take values from 0 to K, and S can take values from 0 to S, the total number of unique states is N * K * S. Therefore, the time complexity of the recursive function is O(N * K * S).

# However, the use of memoization significantly reduces the number of recursive calls. Once a state (i, K, S) has been calculated, its result is stored in the memo dictionary. Subsequent calls with the same state will retrieve the result from the dictionary instead of performing the recursive calculations again. This optimization reduces the time complexity of the overall code.

# In conclusion, the time complexity of the provided code is O(N * K * S), but the actual runtime will be improved by the memoization technique.
