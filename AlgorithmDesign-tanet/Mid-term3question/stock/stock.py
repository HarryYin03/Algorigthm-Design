prices = list(map(int, input().split()))
#prices.insert(0, 0)
modified = [0] * len(prices)

for i in range(1, len(prices)):
    modified[i] = prices[i] - prices[i - 1]

# print(modified)

maxVal = 0
curVal = 0

for i in range(len(modified)):
    curVal = max(0, curVal + modified[i])
    maxVal = max(curVal, maxVal)

print(maxVal)
