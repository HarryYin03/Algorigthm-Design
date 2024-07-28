call_count = 0

def maxRev(l, prices):
    global call_count
    call_count += 1
    if l == 0:
        return 0
    max_revenue = 0
    for i in range(1, l + 1):
        max_revenue = max(max_revenue, prices[i - 1] + maxRev(l - i, prices)) #summing the price of the current cut and the revenue from the remaining rod
    return max_revenue

prices = list(map(int, input().split()))
rod_length = len(prices)
print(maxRev(rod_length, prices))
print("Number of function calls:", call_count)
