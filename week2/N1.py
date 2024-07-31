import time
def sum_subarray(x, i, j): #uses a brute force method to find the maximum sum of a contiguous subsequence
    return sum(x[i:j + 1])

def max_subquence_sum_straightforward(arr): #The max_subsequence_sum_straightforward function iterates through all possible subarrays and updates the maximum sum found.
    n = len(arr)
    max_sum = float('-inf')
    
    for i in range(n):
        for j in range(i, n):
            current_sum = sum_subarray(arr, i, j)
            if current_sum > max_sum: 
                max_sum = current_sum 
    return max_sum

st = time.process_time()
sequence = list(map(int, input().split()))
print(max_subquence_sum_straightforward(sequence))
et = time.process_time()
print (f"Running Time: {et - st}")