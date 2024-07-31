import time
def accumulate(arr):
    accumulated = []
    current_sum = 0
    for num in arr:
        current_sum += num
        accumulated.append(current_sum)
    return accumulated

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

st = time.process_time()
sequence = list(map(int, input().split()))
et = time.process_time()
print(max_subsequence_sum_accumulated(sequence))
print(f"Running Time: {et - st}")
