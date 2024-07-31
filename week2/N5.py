def max_subsequence_sum_accumulated(arr):
    n = len(arr)
    accumulated = accumulate(arr)
    max_sum = float('-inf')
    
    for i in range(n):
        for j in range(i, n):
            current_sum = accumulated[j] - (accumulated[i-1] if i > 0 else 0)
            if current_sum > max_sum:
                max_sum = current_sum
    
    return max_sum

# Example usage:
print(max_subsequence_sum_accumulated(arr))  # Output should be 7
