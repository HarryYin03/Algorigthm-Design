def min_coin_change(coins, amount):
    max_val = amount + 1 #max_val is the maximum value of coins that can be used to make the amount
    dp = [max_val] * (amount + 1) #dp is a list of the maximum value of coins that can be used to make the amount
    dp[0] = 0 #Base case: 0 coins are needed to make the amount 0
    
    for i in range(1, amount + 1): #Iterate through all amounts from 1 to the given amount
        for coin in coins:
            if i - coin >= 0: #If the coin can be used to make the amount i
                dp[i] = min(dp[i], dp[i - coin] + 1) #Update the minimum coins needed for amount i
                
    return dp[amount] if dp[amount] != max_val else -1 #Return the minimum coins needed for the amount if it is less than max_val, otherwise return -1

coins = list(map(int, input().split())) #List of coin denominations
amount = int(input()) #Amount of change
print(min_coin_change(coins, amount)) #Print the minimum coins needed to make the amount of change