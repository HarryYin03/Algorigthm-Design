def comb(s, i):
    if i == n:
        return 1
    if k == s: 
        return 1
    if k < s or n - i < k - s:
        return 0
    
    else:
        x[i] = 0
        count_0 = comb(s, i + 1)
        x[i] = 1
        count_1 = comb(s+1, i+1)
        return count_0 + count_1
    
n = 4
k = 2
x = [0] * n
total_combination = comb(0, 0)