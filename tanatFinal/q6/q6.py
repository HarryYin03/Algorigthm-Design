# MOD = 44711


# def mat_mult(A, B):
#     """Multiply matrix A and B modulo MOD."""
#     n = len(A)
#     m = len(A[0])
#     p = len(B[0])

#     C = [[0] * p for _ in range(n)]
#     for i in range(n):
#         for j in range(p):
#             for k in range(m):
#                 C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
#     return C

# # Computes matrix power using exponentiation by squaring


# def mat_pow(m, n):
#     if n == 1:
#         return m

#     half_pow = mat_pow(m, n // 2)
#     if n % 2 == 0:
#         return mat_mult(half_pow, half_pow)
#     else:
#         return mat_mult(mat_mult(half_pow, half_pow), m)


# def tile(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         result = mat_pow([[4, -1], [1, 0]], (n-2) // 2)
#         return (3 * result[0][0] + result[0][1]) % MOD


# print(tile(4999998))
# print(tile(4999999998))

MOD = 44711

# Matrix multiplication function
def multiply2D(A, B):
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD, 
             (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
             (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]]

# Matrix exponentiation function
def expo(M, n):
    if n == 0:
        return [[1, 0], [0, 1]]  # Identity matrix
    else:
        Mhalf = expo(M, n // 2)
        Mhalf = multiply2D(Mhalf, Mhalf)
        if n % 2 == 1:
            Mhalf = multiply2D(Mhalf, M)
        return Mhalf

# Main function to calculate f(L)
def find_f(L):
    if L % 2 == 1:
        return 0  # Odd L has no valid tiling
    elif L == 0:
        return 1  # Base case f(0)
    elif L == 2:
        return 3  # Base case f(2)
    
    # Define the matrix M
    M = [[4, -1], [1, 0]]
    
    # Perform matrix exponentiation: M^(L//2 - 1)
    A = expo(M, (L // 2) - 1)
    
    # Multiply the resulting matrix by the initial vector [f(2), f(0)] = [3, 1]
    fL = (A[0][0] * 3 + A[0][1] * 1) % MOD
    
    return fL

# Input
L = int(input())

# Output the result
print(find_f(L))

