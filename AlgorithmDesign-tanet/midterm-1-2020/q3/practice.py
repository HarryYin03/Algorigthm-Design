def maximum_earnings(W, sacks):
  # Create a list to store the maximum earnings for each weight
  earnings = [0] * (W + 1)

  # Iterate through each weight from 1 to W
  for weight in range(1, W + 1):
    max_earnings = 0

    # Iterate through each sack size and price
    for sack_size, price in sacks:
      # Check if the sack size is less than or equal to the current weight
      if sack_size <= weight:
        # Calculate the earnings for the current weight using the sack size and price
        current_earnings = earnings[weight - sack_size] + price

        # Update the maximum earnings if the current earnings is greater
        if current_earnings > max_earnings:
          max_earnings = current_earnings

    # Store the maximum earnings for the current weight
    earnings[weight] = max_earnings

  # Return the maximum earnings for W kilograms of rice
  return earnings[W]

# Read the input
W = int(input())
k = int(input())
sacks = []
for _ in range(k):
  sack_size, price = map(int, input().split())
  sacks.append((sack_size, price))

# Calculate and print the maximum earnings
print(maximum_earnings(W, sacks))