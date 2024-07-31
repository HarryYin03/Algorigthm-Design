def max_profit(price_changes):
    n = len(price_changes)
    max_profit = 0
    min_price = 0
    current_price = 0

    for change in price_changes:
        current_price += change
        max_profit = max(max_profit, current_price - min_price)
        min_price = min(min_price, current_price)

    return max_profit

# Example input
price_changes = list(map(int, input().split()))

# Calculate and print the maximum profit
print(max_profit(price_changes))
