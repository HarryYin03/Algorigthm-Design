def rodCutting(prices, length):
    # Initialize dp array to store maximum revenue for each length
    dp = [0] * (length + 1)
    
    # Compute maximum revenue for each length from 1 to length
    for j in range(1, length + 1):
        max_revenue = float('-inf')
        for i in range(1, j + 1):
            max_revenue = max(max_revenue, prices[i - 1] + dp[j - i])
        dp[j] = max_revenue
    
    return dp[length]

# Given lengths and prices
lengths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

# Length of the rod
L = 8
print("Maximum revenue obtainable is", rodCutting(prices, L))
