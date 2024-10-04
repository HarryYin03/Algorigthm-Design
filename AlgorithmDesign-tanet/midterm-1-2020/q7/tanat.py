# import time
# data = list(map(int, input().split()))
# n = len(data)
# memo = [None for _ in range(n)]


# def LongestIncreasingSubsequence(i):
#     if i == 0:
#         return 1

#     if memo[i] != None:
#         return memo[i]

#     maxSeq = 1
#     for j in range(i):
#         if data[i] > data[j]:
#             maxSeq = max(maxSeq, 1 + LongestIncreasingSubsequence(j))

#     memo[i] = maxSeq
#     return maxSeq
# max_val = 0
# for i in range(n):
#     max_val = max(max_val, LongestIncreasingSubsequence(i))
# print(max_val)


data = list(map(int, input().split()))
n = len(data)

dp = [1 for _ in range(n)]

def longest_increasing_subsequence():
    for i in range(1, n):
        for j in range(i):
            if data[i] > data[j]:
                dp[i] = max(dp[i], 1 + dp[j])
    return max(dp)

print(longest_increasing_subsequence())



