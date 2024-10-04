# Inversion Count

# arr = list(map(int, input().split()))

# count = 0
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] > arr[j] and i < j:
#             count += 1

# print(count)


# Improved Inversion Count 

def merge(arr, s, m, e):
    global count
    i = s
    j = m + 1

    B = []
    while i <= m and j <= e:
        if arr[i] <= arr[j]:
            B.append(arr[i])
            i += 1
        else:
            count += m - i + 1
            B.append(arr[j])
            j += 1
    
    while i <= m:
        B.append(arr[i])
        i += 1  
    while j <= e:
        B.append(arr[j])
        j += 1
    
    arr[s:e+1] = B
    

def mergeSort(arr, s, e):
    if s < e:
        m = (s + e) // 2
        mergeSort(arr, s, m)
        mergeSort(arr, m + 1, e)
        merge(arr, s, m, e)

N = int(input())  
for i in range(N):
    blank = input()  
    n = int(input())  
    A = [int(input()) for j in range(n)]
    count = 0
    mergeSort(A, 0, len(A) - 1)
    print(count)