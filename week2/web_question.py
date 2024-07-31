def max_subarray_sum(arr):
    # Kadane's Algorithm for 1D array
    max_sum = arr[0]
    current_sum = arr[0]
    
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

def max_subrectangle_sum(matrix):
    n = len(matrix)
    max_sum = float('-inf')
    
    # Temporary array to store column sums
    temp = [0] * n
    
    # Iterate over all possible top rows
    for top in range(n):
        # Reset the temporary array
        temp = [0] * n
        
        # Iterate over all possible bottom rows >= top
        for bottom in range(top, n):
            # Calculate the sum of elements in each column for the submatrix from row 'top' to row 'bottom'
            for col in range(n):
                temp[col] += matrix[bottom][col]
            
            # Find the maximum subarray sum for this submatrix using Kadane's Algorithm
            current_max = max_subarray_sum(temp)
            max_sum = max(max_sum, current_max)
    
    return max_sum

# Read input
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
matrix = []
index = 1
for i in range(N):
    row = list(map(int, data[index:index + N]))
    matrix.append(row)
    index += N

# Find and print the maximum subrectangle sum
print(max_subrectangle_sum(matrix))
