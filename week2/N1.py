
import time

def Sum(x, i, j):
    s = 0
    for k in range(i, j + 1):
        s += x[k]
    return s

def max_subsequence_sum(x):
    n = len(x)
    max_sum = float('-inf')
    
    for i in range(n):
        for j in range(i, n):
            current_sum = Sum(x, i, j)
            if current_sum > max_sum:
                max_sum = current_sum
    
    return max_sum

a = list(map(int, input("Enter a sequence of integers separated by spaces: ").split()))
    
st = time.process_time()
result = max_subsequence_sum(a)
et = time.process_time()
    
print("Max subsequence sum: ", result)
print("Time taken: ", et - st, "seconds")