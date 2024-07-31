def accumulate_list(arr):
    accumulated = [0] * len(arr)
    accumulated[0] = arr[0]
    for i in range(1, len(arr)):
        accumulated[i] = accumulated[i-1] + arr[i]
    return accumulated


sequence = list(map(int, input().split()))
print(accumulate_list(sequence))