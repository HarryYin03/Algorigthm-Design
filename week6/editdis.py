def editDistance(A, B, i, j): #A and B are strings, i and j are indices
    if i == len(A):
        return len(B) - j
    if j == len(B):
        return len(A) - i
    if A[i] == B[j]:
        return editDistance(A, B, i + 1, j + 1)
    insert = 1 + editDistance(A, B, i, j + 1)
    delete = 1 + editDistance(A, B, i + 1, j)
    replace = 1 + editDistance(A, B, i + 1, j + 1)
    return min(insert, delete, replace)

A = input()
B = input()
print(editDistance(A, B, 0, 0))