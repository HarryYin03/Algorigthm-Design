a, x = map(int, input().split())

def expo(a, x):
    if x == 0:
        return 1
    if x % 2 == 0:
        half = expo(a, x //2)
        return half * half
    else:
        return a * expo(a, x - 1)
    
print(expo(a, x))