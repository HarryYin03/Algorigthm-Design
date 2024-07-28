def comb(i):
    if i == n: 
        print(x)
        return 1
    else:
        x[i] = 0
        count_0 = comb(i + 1)
        x[i] = 1
        count_1 = comb(i+1)
        return count_0 + count_1
n = 3
x = [0] * n
total_combination = comb(0)
print(total_combination)