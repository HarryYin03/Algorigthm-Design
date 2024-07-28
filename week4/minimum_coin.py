call_count = 0

def mincoin(v, coins):
    global call_count
    call_count += 1
    if v == 0:
        return 0
    min_coins = float('inf')
    for coin in coins:
        if v - coin >= 0:
            current_min = mincoin(v - coin, coins)
            min_coins = min(min_coins, current_min + 1)
    return min_coins

coin_denominations = list(map(int, input().split()))
amount_of_change = int(input())
print(mincoin(amount_of_change, coin_denominations))
print("Number of function calls:", call_count)
