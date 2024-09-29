def minimum_price(prices):
    n = len(prices)
    # Initialize the DP array where dp[i] is the minimum cost to buy the first i shoes.
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # No shoes, no cost.

    # Calculate the minimal cost using DP
    for i in range(1, n + 1):
        # Option 1: Buy this shoe alone.
        dp[i] = min(dp[i], dp[i-1] + prices[i-1])
        
        # Option 2: Buy this shoe and the previous shoe, apply the 50% discount on the cheaper one.
        if i > 1:
            cost_with_discount = prices[i-1] + prices[i-2] * 0.5 if prices[i-1] > prices[i-2] else prices[i-2] + prices[i-1] * 0.5
            dp[i] = min(dp[i], dp[i-2] + cost_with_discount)
        
        # Option 3: Buy this and the two previous shoes, one shoe is free.
        if i > 2:
            three_prices = sorted(prices[i-3:i])
            cost_with_free = three_prices[1] + three_prices[2]  # cheapest one is free
            dp[i] = min(dp[i], dp[i-3] + cost_with_free)

    return dp[n]

# Input reading
n = int(input())
prices = list(map(int, input().split()))

# Output the minimum obtainable price
print(f"{minimum_price(prices):.1f}")
