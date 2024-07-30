def editDistance(A, B, i, j, memo):
    if (i, j) in memo:
        return memo[(i, j)]
    if i == len(A):
        result = len(B) - j
    elif j == len(B):
        result = len(A) - i
    elif A[i] == B[j]:
        result = editDistance(A, B, i + 1, j + 1, memo)
    else:
        insert = 1 + editDistance(A, B, i, j + 1, memo)
        delete = 1 + editDistance(A, B, i + 1, j, memo)
        replace = 1 + editDistance(A, B, i + 1, j + 1, memo)
        result = min(insert, delete, replace)
    memo[(i, j)] = result
    return result

A = input()
B = input()
memo = {}
print(editDistance(A, B, 0, 0, memo))