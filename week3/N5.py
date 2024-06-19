import sys
def generate_combinations(n):
    # Initialize the global list of length n
    x = [0] * n

    def comb(i):
        # If we've assigned values to all items, print the combination and return 1
        if i == n:
            print(x)
            return 1
        
        # Initialize count of combinations
        count = 0

        # Loop through 3 options (0, 1, 2) for the current item
        for option in range(3):
            x[i] = option
            count += comb(i + 1)
        
        return count
    
    # Initial call to the recursive function
    total_combinations = comb(0)
    print(f"Total combinations: {total_combinations}")
# Example test with n = 3
generate_combinations(2)

