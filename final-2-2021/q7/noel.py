# Reading the input in the required format
M, N = map(int, input().split())  # M is the total money, N is the number of stocks

# Initialize lists for weights (prices) and values (profits)
w = []  # Stock prices
v = []  # Stock profits

# Read N lines for stock prices and profits
for _ in range(N):
    price, profit = map(int, input().split())
    w.append(price)
    v.append(profit)

count = 0  # To count recursive calls

# Memoization table (N+1 rows for items, M+1 columns for knapsack capacity)
memo = [[-1] * (M + 1) for _ in range(N + 1)]

# Recursive function with memoization
def maxVal(i, C):
    global count
    if memo[i][C] != -1:
        return memo[i][C]
    else: 
        count += 1  # Track the number of function calls
        if i == N:  # Base case: no more items to consider
            memo[i][C] = 0
            return memo[i][C]
        else:
            # Option 1: Skip the current stock
            skip = maxVal(i + 1, C)
            
            # Option 2: Take the current stock, if its price is within the remaining money
            if w[i] <= C:
                take = v[i] + maxVal(i + 1, C - w[i])
            else:
                take = -1  # Invalid option if price exceeds the current budget
            
            # Store the best of the two options
            memo[i][C] = max(skip, take)
            return memo[i][C]

# Calling the recursive function to fill the memo table
result = maxVal(0, M)

# Output the maximum total profit
print(result)
# print(count)  # Output the number of recursive calls made (for debugging purposes)
