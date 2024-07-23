def minCoins(coins, m, V):
    # Initialize dp array with a large number (infinity equivalent)
    dp = [float('inf')] * (V + 1)
    
    # Base case: 0 coins are needed to make 0 change
    dp[0] = 0
    
    # Compute minimum coins required for all values from 1 to V
    for i in range(1, V + 1):
        for j in range(m):
            if coins[j] <= i:
                sub_res = dp[i - coins[j]]
                if sub_res != float('inf') and sub_res + 1 < dp[i]:
                    dp[i] = sub_res + 1
    
    # If dp[V] is still infinity, then it's not possible to make the change
    return dp[V] if dp[V] != float('inf') else -1



# Driver program to test above function
coins = [1, 2, 5, 10, 13]
m = len(coins)
V = 3377
print("Minimum coins required is", minCoins(coins, m, V))
