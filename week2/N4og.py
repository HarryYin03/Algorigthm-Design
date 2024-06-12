def prefix_sum(lst):
    accumulated = []
    current_sum = 0
    
    for num in lst:
        current_sum += num
        accumulated.append(current_sum)
        
    return accumulated

# Example usage with input that matches expected output
original_list = [-2, -3, 4, -1, -2, 1, 5, -3]
accumulated_list = prefix_sum(original_list)
print(accumulated_list)  # Should print: [-2, -5, -1, -2, -4, -3, 2, -1]

# Example usage with input you used in your script
original_list = [-2, -3, 4, -1, 2, 1, 5, -3]
accumulated_list = prefix_sum(original_list)
print(accumulated_list)  # Should print: [-2, -5, -1, -2, 0, 1, 6, 3]
