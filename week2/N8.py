import time

def kandane(arr):
    max_sum = current_sum = arr[0]
    
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
        
    return max_sum

sequence = list(map(int, input().split()))

st = time.process_time()
print(kandane(sequence))
et = time.process_time()
print(f"Running Time: {et - st}")