def buying_apples(test_cases):
    results = []
    for case in test_cases:
        n, k, prices = case
        dp = [float('inf')] * (k + 1)
        dp[0] = 0

        for weight in range(1, k + 1):
            if prices[weight - 1] != -1:
                for j in range(weight, k + 1):
                    if dp[j - weight] != float('inf'):
                        dp[j] = min(dp[j], dp[j - weight] + prices[weight - 1])
        
        result = dp[k] if dp[k] != float('inf') else -1
        results.append(result)
    return results

# Input parsing
input_data = """
2
3 5
-1 -1 4 5 -1
5 5
1 2 3 4 5
"""

lines = input_data.strip().split('\n')
num_test_cases = int(lines[0])
test_cases = []

index = 1
for _ in range(num_test_cases):
    n, k = map(int, lines[index].split())
    prices = list(map(int, lines[index + 1].split()))
    test_cases.append((n, k, prices))
    index += 2

# Running the test
results = buying_apples(test_cases)
for result in results:
    print(result)
