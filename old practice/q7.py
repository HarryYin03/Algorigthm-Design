def max_visible_trees(heights):
    n = len(heights)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if heights[i] > heights[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# Example usage:
n = int(input())
heights = list(map(int, input().split()))
print(max_visible_trees(heights))
