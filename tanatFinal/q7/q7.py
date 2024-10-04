def min_damage(soldiers):
    damage = 0
    while len(soldiers) > 0:
        n = len(soldiers)
        if n <= 3:
            break  # Last shot, no more damage
        
        # Find the optimal shot
        max_destroyed = 0
        best_index = 0
        for i in range(n):
            destroyed = soldiers[i] + soldiers[(i+1)%n] + soldiers[(i+2)%n]
            if destroyed > max_destroyed:
                max_destroyed = destroyed
                best_index = i
        
        # Remove the destroyed aircrafts
        soldiers = soldiers[best_index+3:] + soldiers[:best_index]
        
        # Calculate damage
        damage += sum(soldiers)
    
    return damage

# Read input
soldiers = list(map(int, input().split()))

# Calculate and print the result
print(min_damage(soldiers))