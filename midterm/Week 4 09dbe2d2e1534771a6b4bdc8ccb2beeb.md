# Week 4

### Rod Cutting: Memoization Technique

### Concept

- **MEMOIZATION**
    - An optimization technique used to improve the efficiency of recursive algorithms by ******storing the results of expensive function calls and reusing them when the same inputs occur again******
    - In content of Rod Cutting Problem , memoization helps to **avoid recomputing the maximum revenue for the same rod lengths multiple times.**

### Algorithm

1. Recursive Approach:
    1. Break down the problem into smaller subproblems
    2. Solve each subproblem recursively.
    3. Combine the solutions of subproblems to get the final solution.
2. Memoization:
    1. ***Store the results of subproblems*** in a dictionary or list.
    2. Check if the result for a subproblem is already computed before performing the recursive call.
    3. Retrieve the stored result if exists to avoid redundant calculations.

### Code

```python
import sys
import time

# Increase the recursion limit to handle deep recursion
sys.setrecursionlimit(10000)

# Read the prices into a list
Price = list(map(int, input().split()))
l = len(Price)  # Length of the rod

# Initialize a global counter to track the number of function calls
count = 0

# Initialize a list to count the number of recursive calls for each length
# To count the number of recursive calls for """each rod length"""
calls = [0] * (l + 1)

# Initialize a dictionary for memoization
# To store the results of subproblems
memo = {}

# Define the recursive function to find the maximum revenue with memoization
# Maximum revenue for a rod of length `1`
def RodCut(l):
    global count
    count += 1  # Increment the counter each time the function is called
    calls[l] += 1  # Increment the call count for this specific length
    
    
    if l == 0:
        return 0  # Base case: If the length is 0, no revenue can be made

	#If result for this length is memoized, return directly
    if l in memo:
        return memo[l]  # Return the memoized result if it exists

    maxRev = 0  # Initialize the maximum revenue to 0
    # Loop through """possible cut length"""
    for i in range(1, l + 1):
        # Recursive case: Try cutting the rod at length i and calculate the revenue
   # Price for the cut length `i' => Price[i-1]
   # Caculate maximum revenue for the remaining rod length `l - i`
   #Price is just going from left to right normally on the price list with index 1, 2,3 4
        revenue = Price[i-1] + RodCut(l - i)
        maxRev = max(maxRev, revenue)  # Update the maximum revenue
    # Result is memoized and returned/
    memo[l] = maxRev  # Memoize the result for this length
    return maxRev  # Return the maximum revenue found

# Measure the start time
st = time.process_time()

# Call the RodCut function with the length of the rod and print the result
max_revenue = RodCut(l)
print(f"Maximum revenue obtainable: {max_revenue}")

# Print the total number of function calls
print(f"Total number of function calls: {count}")

# Print the call count for each length
for i in range(1, l + 1):
    print(f"RodCut({i}) was called {calls[i]} times")

# Measure the end time
et = time.process_time()

# Print the running time of the function call
print(f"Running Time: {et - st:.6f} seconds")
```

### Code Visualization

```
----------------------------------------
RodCut(4) called
Considering cutting rod of length 4 into 1 and 3
  ----------------------------------------
  RodCut(3) called
  Considering cutting rod of length 3 into 1 and 2
    ----------------------------------------
    RodCut(2) called
    Considering cutting rod of length 2 into 1 and 1
      ----------------------------------------
      RodCut(1) called
      Considering cutting rod of length 1 into 1 and 0
        ----------------------------------------
        RodCut(0) called
        Base case: l = 0, return 0 (No more rod left to cut)
        ----------------------------------------
      Revenue from cutting rod into lengths 1 and 0: Price[0] + RodCut(0) = 1 + 0 = 1
      Memoizing result for RodCut(1): 1
      Returning maxRev = 1 for RodCut(1)
      ----------------------------------------
    Revenue from cutting rod into lengths 1 and 1: Price[0] + RodCut(1) = 1 + 1 = 2
    Considering cutting rod of length 2 into 2 and 0
      ----------------------------------------
      RodCut(0) called
      Base case: l = 0, return 0 (No more rod left to cut)
      ----------------------------------------
    Revenue from cutting rod into lengths 2 and 0: Price[1] + RodCut(0) = 5 + 0 = 5
    Memoizing result for RodCut(2): 5
    Returning maxRev = 5 for RodCut(2)
    ----------------------------------------
  Revenue from cutting rod into lengths 1 and 2: Price[0] + RodCut(2) = 1 + 5 = 6
  Considering cutting rod of length 3 into 2 and 1
    ----------------------------------------
    RodCut(1) called
    Returning memoized result for RodCut(1): 1
    ----------------------------------------
  Revenue from cutting rod into lengths 2 and 1: Price[1] + RodCut(1) = 5 + 1 = 6
  Considering cutting rod of length 3 into 3 and 0
    ----------------------------------------
    RodCut(0) called
    Base case: l = 0, return 0 (No more rod left to cut)
    ----------------------------------------
  Revenue from cutting rod into lengths 3 and 0: Price[2] + RodCut(0) = 8 + 0 = 8
  Memoizing result for RodCut(3): 8
  Returning maxRev = 8 for RodCut(3)
  ----------------------------------------
Revenue from cutting rod into lengths 1 and 3: Price[0] + RodCut(3) = 1 + 8 = 9
Considering cutting rod of length 4 into 2 and 2
  ----------------------------------------
  RodCut(2) called
  Returning memoized result for RodCut(2): 5
  ----------------------------------------
Revenue from cutting rod into lengths 2 and 2: Price[1] + RodCut(2) = 5 + 5 = 10
Considering cutting rod of length 4 into 3 and 1
  ----------------------------------------
  RodCut(1) called
  Returning memoized result for RodCut(1): 1
  ----------------------------------------
Revenue from cutting rod into lengths 3 and 1: Price[2] + RodCut(1) = 8 + 1 = 9
Considering cutting rod of length 4 into 4 and 0
  ----------------------------------------
  RodCut(0) called
  Base case: l = 0, return 0 (No more rod left to cut)
  ----------------------------------------
Revenue from cutting rod into lengths 4 and 0: Price[3] + RodCut(0) = 9 + 0 = 9
Memoizing result for RodCut(4): 10
Returning maxRev = 10 for RodCut(4)
----------------------------------------
Maximum revenue obtainable: 10
Total number of function calls: 11
RodCut(1) was called 3 times
RodCut(2) was called 2 times
RodCut(3) was called 1 times
RodCut(4) was called 1 times
Running Time: 0.0 seconds
```

```scss

RodCut(4)
├── RodCut(3)
│   ├── RodCut(2)
│   │   ├── RodCut(1)
│   │   │   ├── RodCut(0) -> returns 0
│   │   │   └── Revenue = Price[0] + RodCut(0) = 1 + 0 = 1
│   │   │   └── Memoize: RodCut(1) = 1
│   │   └── Revenue = Price[0] + RodCut(1) = 1 + 1 = 2
│   │   ├── RodCut(0) -> returns 0
│   │   └── Revenue = Price[1] + RodCut(0) = 5 + 0 = 5
│   │   └── Memoize: RodCut(2) = 5
│   └── Revenue = Price[0] + RodCut(2) = 1 + 5 = 6
│   ├── RodCut(1) -> returns 1 (memoized)
│   └── Revenue = Price[1] + RodCut(1) = 5 + 1 = 6
│   ├── RodCut(0) -> returns 0
│   └── Revenue = Price[2] + RodCut(0) = 8 + 0 = 8
│   └── Memoize: RodCut(3) = 8
└── Revenue = Price[0] + RodCut(3) = 1 + 8 = 9
└── RodCut(2) -> returns 5 (memoized)
└── Revenue = Price[1] + RodCut(2) = 5 + 5 = 10
└── RodCut(1) -> returns 1 (memoized)
└── Revenue = Price[2] + RodCut(1) = 8 + 1 = 9
└── RodCut(0) -> returns 0
└── Revenue = Price[3] + RodCut(0) = 9 + 0 = 9
└── Memoize: RodCut(4) = 10

```

### ELI5

### ELI5 (Explain Like I'm 5)

Imagine you have a long stick of candy, and you can cut it into smaller pieces. Each piece of a certain length can be sold for a different amount of money. You want to figure out the best way to cut the candy stick so that you get the most money.

**Without Memoization:** You might try cutting the candy stick in every possible way, but sometimes you keep cutting it the same way over and over again, which takes a lot of time.

**With Memoization:** You keep a notebook where you write down the best way to cut each length of the candy stick. So, if you need to cut a piece of the same length again, you just look it up in your notebook instead of figuring it out all over again. This saves a lot of time and makes you much faster at finding the best way to cut the candy stick.

In the code, the `memo` dictionary is like your notebook where you store the best cuts, and the `calls` list helps you keep track of how many times you thought about each length of the candy stick. This way, you become very efficient at cutting the candy stick and making the most money!

### Worksheet Exercise QA Answer

- **For each value of 𝑙, does maxRev(𝑙) return the same or different values?**
    - **Answer:** For each value of `l`, `maxRev(l)` (or `RodCut(l)` in our function) returns the same value every time it is called. This is because the problem and the prices are deterministic; hence, the maximum revenue for a given length does not change.
- **Therefore, for length of 𝐿, at most how many calls to all maxRev()’s should be adequate?**
    - **Answer:** For the length of L, at most L calls to `RodCut(l)` should be adequate because each length from 1 to L should be computed only once and stored (memoized). However, without memoization, the number of calls can be significantly higher due to overlapping subproblems.
- **What is the reason that there were too many calls to maxRev() in the brute-force solution?**
    - **Answer:** The brute-force solution makes too many calls to `maxRev()` because it recomputes the same values multiple times for different combinations of cuts. This redundancy happens because the same subproblems are solved repeatedly without storing their results.
- **Suggest a modification to the brute-force solution such that once a value of an maxRev(𝑙) is already computed, it will never have to be recomputed again. Only idea is needed in this step.**
    - **Answer:** The modification involves using memoization. We store the results of each `maxRev(l)` (or `RodCut(l)`) in a dictionary or list. If a value has already been computed, it is retrieved from the storage instead of being recomputed.
    
    **Observe how faster the algorithm becomes (comparing the total number of recursive calls).**
    
    - **Answer:** By running the modified code and comparing the `count` variable (total number of function calls) and the `calls` list, you can observe a significant reduction in the number of recursive calls. The memoized version avoids redundant calculations, making the algorithm much faster.

### Minimum Coin Change: Memoization Technique

### Code

```python
import sys
import time

# Set recursion limit
sys.setrecursionlimit(10001)

# Read input
c = list(map(int, input().split()))
v = int(input())

# Initialize memoization dictionary
memo = {}

def mincoin(v):
    # Base case: if the value is 0, no coins are needed
    if v == 0:
        return 0
    
    # Check if the result is already computed
    if v in memo:
        return memo[v]
    
    # Initialize the minimum number of coins to a large value
    minc = float('inf')
    
    # Check each coin in the list
    for coin in c:
        if coin <= v:
            # Recursively compute the minimum number of coins for the remaining value
            minc = min(minc, 1 + mincoin(v - coin))
    
    # Store the result in the memoization dictionary
    memo[v] = minc
    
    return minc

# Measure the start time
st = time.process_time()

# Call the function and print the result
print(mincoin(v))

# Measure the end time
et = time.process_time()
print(f"Running Time: {et - st} seconds")

```

### Visualization

```scss
c = 1 3 4
v = 6

mincoin(6)
├── mincoin(5) -> min(minc, 1 + mincoin(5 - 1))
│   ├── mincoin(4) -> min(minc, 1 + mincoin(4 - 1))
│   │   ├── mincoin(3) -> min(minc, 1 + mincoin(3 - 1))
│   │   │   ├── mincoin(2) -> min(minc, 1 + mincoin(2 - 1))
│   │   │   │   ├── mincoin(1) -> min(minc, 1 + mincoin(1 - 1))
│   │   │   │   │   ├── mincoin(0) -> returns 0
│   │   │   │   │   └── mincoin(1) = min(inf, 1 + 0) = 1
│   │   │   │   │       Memoize: mincoin(1) = 1
│   │   │   │   └── mincoin(2) = min(inf, 1 + mincoin(1)) = min(inf, 1 + 1) = 2
│   │   │   │       Memoize: mincoin(2) = 2
│   │   │   ├── mincoin(0) -> returns 0
│   │   │   └── mincoin(3) = min(inf, 1 + mincoin(2)) = min(inf, 1 + 2) = 3
│   │   │       Memoize: mincoin(3) = 1
│   │   ├── mincoin(1) -> returns 1 (memoized)
│   │   └── mincoin(4) = min(inf, 1 + mincoin(3)) = min(inf, 1 + 1) = 2
│   │       Memoize: mincoin(4) = 1
│   ├── mincoin(2) -> returns 2 (memoized)
│   └── mincoin(5) = min(inf, 1 + mincoin(4)) = min(inf, 1 + 1) = 2
│       Memoize: mincoin(5) = 2
├── mincoin(3) -> returns 1 (memoized)
└── mincoin(6) = min(inf, 1 + mincoin(5), 1 + mincoin(3)) = min(inf, 1 + 2, 1 + 1) = 2
    Memoize: mincoin(6) = 2

```