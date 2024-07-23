def min_cost(n, k, prices):
    dp = [float('inf')] * (k + 1)
    dp[0] = 0

    for i in range(1, k + 1):
        if prices[i - 1] != -1:
            for j in range(i, k + 1):
                if dp[j - i] != float('inf'):
                    dp[j] = min(dp[j], dp[j - i] + prices[i - 1])

    return dp[k] if dp[k] != float('inf') else -1

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        k = int(data[index + 1])
        index += 2
        prices = list(map(int, data[index:index + k]))
        index += k
        result = min_cost(n, k, prices)
        results.append(result)
    
    for result in results:
        print(result)
