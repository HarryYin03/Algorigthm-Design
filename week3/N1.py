def generate_combination(n):
    x = [0] * n 
    
    def comb(i):
        if i == n:
            print(x)
            return
        else:
            x[i] = 0
            comb(i + 1)
            x[i] = 1
            comb(i + 1)
            
    comb(0)
    
generate_combination(2)
