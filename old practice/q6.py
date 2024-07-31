def min_difference(gifts):
    total_sum = sum(gifts)
    n = len(gifts)
    dp = [False] * (total_sum // 2 + 1)
    dp[0] = True
    
    for gift in gifts:
        for j in range(total_sum // 2, gift - 1, -1):
            dp[j] = dp[j] or dp[j - gift]
    
    for i in range(total_sum // 2, -1, -1):
        if dp[i]:
            return total_sum - 2 * i

# Example usage:
n = int(input())
gifts = list(map(int, input().split()))
print(min_difference(gifts))
