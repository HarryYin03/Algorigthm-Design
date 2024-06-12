import time

def Sum(accumulated, i, j):
    if i == 0:
        return accumulated[j]
    else:
        return accumulated[j] - accumulated[i - 1]

def max_subsequence_sum(x):
    n = len(x)
    max_sum = float('-inf')
    
    # Compute the prefix sum array
    accumulated = [x[0]]
    for i in range(1, n):
        accumulated.append(accumulated[i - 1] + x[i])
    
    # Iterate over all possible subarrays
    for i in range(n):
        for j in range(i, n):
            current_sum = Sum(accumulated, i, j)
            if current_sum > max_sum:
                max_sum = current_sum
    
    return max_sum


a = list(map(int, input("Enter a sequence of integers separated by spaces: ").split()))

st = time.process_time()
result = max_subsequence_sum(a)
et = time.process_time()

print("Max subsequence sum:", result)
print("Time taken:", et - st, "seconds")
