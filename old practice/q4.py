def fibonacci(n):

    result = [1, 1]

    for i in range(len(result), n + 2):
        num = result[i-1] + result[i-2]
        result.append(num)

    print(result[-1])


fibonacci(12)