import time
def max_subarray_sum(arr):
    max_sum = float('-inf')
    current_sum = 0
    
    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Example usage:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum(arr)
print("Maximum subarray sum:", result)

a = list(map(int, input("Enter a sequence of integers separated by spaces: ").split()))

st = time.process_time()
result = max_subarray_sum(a)
et = time.process_time()

print("Max subarray sum:", result)
print("Time taken:", et - st, "seconds")