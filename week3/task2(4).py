def comb(i, s):
    if i == n:
        if s == k:
            return 1
        else: 
            return 0
        
    else:
        x[i] = 0
        count_0 = comb(i + 1, s)
        x[i] = 1
        count_1 = comb(i + 1, s + 1)
        return count_0 + count_1
    
n = 4
k = 2
x = [0] * n
total_combination = comb(0, 0)
print(total_combination)