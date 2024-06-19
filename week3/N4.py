k = 0

def generate_combination(n, k_value):
    global k
    k = k_value
    
    x = [0] * n
    
    def comb(i, count_ones):
        if i == n:
            if count_ones == k:
                print(x)
                return 1
            else:
                return 0
        
        x[i] = 0
        count_0 = comb(i + 1, count_ones)
        
        x[i] = 1
        count_1 = comb(i + 1, count_ones + 1)
        
        
        return count_0 + count_1
    total_combination = comb(0, 0)#
    print("Total combination:", total_combination)
    
generate_combination(3, 1)