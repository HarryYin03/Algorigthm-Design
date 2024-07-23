import sys

def KadaneAlgorithm(data):
    maxGlobal = data[0]
    maxLocal = data[0]

    for i in range(1, len(data)):
        maxLocal = max(data[i], maxLocal + data[i])
        maxGlobal = max(maxGlobal, maxLocal)

    return maxGlobal

def maxSubmatrixSum(N, M):
    max_sum = (-1) * sys.maxsize

    for left in range(N):
        temp = [0] * N

        for right in range(left, N):
            for i in range(N):
                temp[i] += M[i][right]

            max_sum = max(max_sum, KadaneAlgorithm(temp))

    return max_sum

if __name__ == "__main__":
    input_data = sys.stdin.read().splitlines()
    
    # Debug: Print the first few lines to inspect the input
    print("First few lines of input:")
    for i in range(min(5, len(input_data))):
        print(input_data[i])
    
    N = int(input_data[0].strip())
    M = [list(map(int, line.strip().split())) for line in input_data[1:N+1]]

    result = maxSubmatrixSum(N, M)
    print(result)
