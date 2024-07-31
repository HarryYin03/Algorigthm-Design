# Week 6

### Edit Distance (Levenshtein Distance)

### Concept

- Edit Distance:
    
    ***The edit distance between two strings*** is the ***minimum number of operations*** required to transform one string into the other. The allowed operations are:
    
    1. **Insertion** of a character
    2. **Deletion** of a character
    3. **Substitution** of a character

### Example

Consider the strings `FOOD` and `MONEY` :

1. FOOD → MOOD (**`Substitute` ”F”** with “M” )
2. MOOD → MOND (`Substitute` ”O” with “N”)
3. MOND → MONE (`Substitute` ”D” with “E” )
4. MONE → MONEY (`Insert` ”Y” )

Edi Distance = 4

### Approach

**Step 1: Identifying the States and Operations**

To transform string `A` → string `B` ,  we define the state `(i,j)` where `i`  = index in `A`  and `j` = index in `B` . At each state, we consider the following scenarios:

1. **No operation needed if `A[i] == B[j]`** 
2. **Insert:** Insert `B[j]` in front of `A[j]` 
3. **Delete:**  Delete `A[i]`
4. **Substitute:** Change `A[i]` to `B[j]` 

  

 **Step 2: Recursive Brute-Force Solution** 

A recursive brute-force solution involves exploring all possible operations at each state.

Step 3: Dynamic Programming Optimization

Dynamic Programming(DP) helps us optimize by storing results of sub-problems to avoid redundant calculations

### Code

```python
import time
import sys
sys.setrecursionlimit(10000)
A = input()
B = input()

# Memoization Table
# 2D list initialized to -1
# To store intermediate results

ed = [[-1 for i in range(len(B)+1)] for j in range(len(A)+1)]

def EditDistance(i, j):
    global A, B, ed

    if ed[i][j] != -1: # return the stored value to avoid re-computation
        return ed[i][j]

		# Base Case
    if i == len(A):
        return len(B) - j # Remaining characters in B need to be inserted
    elif j == len(B):
        return len(A) - i # Remaining characters in A need to be deleted

		# Recursive Steps
    elif A[i] == B[j]: # If equal
        answer = EditDistance(i+1, j+1) #move to next characters inb both strings
    else:
		    #Remove A[i], them compare A[i+1] with B[j]
        delete = 1 + EditDistance(i+1, j)
        
        # Add B[j], then compare A[i] with B[j+1]
        insert = 1 + EditDistance(i, j+1)
        
        # Change A[i] to B[j], then compare A[i+1] with B[j+1]
        substitute = 1 + EditDistance(i+1, j+1)
        
        answer = min(delete, insert, substitute)

    ed[i][j] = answer
    return answer

st = time.process_time()
print(EditDistance(0, 0))
et = time.process_time()
print(f"Running Time: {et-st}")
```

### Tree Visualization

```python
import time
import sys
sys.setrecursionlimit(10000)

# Sample input strings
A = "FOOD"
B = "MONEY"

# Memoization Table
# 2D list initialized to -1
# To store intermediate results
ed = [[-1 for i in range(len(B)+1)] for j in range(len(A)+1)]

def EditDistance(i, j, depth=0, branch=""):
    global A, B, ed

    # Define connectors
    indent = " " * 8
    branch_connector = "|-- " if depth > 0 else ""
    branch_path = branch.replace("|-- ", "|      ") if depth > 0 else ""
    print(f"{branch_path}{branch_connector}EditDistance(i={i}, j={j})")

    if ed[i][j] != -1:  # return the stored value to avoid re-computation
        print(f"{branch_path}|      Returning memoized value: {ed[i][j]}\n")
        return ed[i][j]

    # Base Case
    if i == len(A):
        print(f"{branch_path}| Base case reach i == len(A): {i} == {len(A)}\n")
        ed[i][j] = len(B) - j  # Remaining characters in B need to be inserted
        print(f"{branch_path}|      Base case ed[{i}][{j}]: Insert remaining B characters , {len(B)}(len(B)) - {j}(j): {ed[i][j]}\n")
        return ed[i][j]
    elif j == len(B):
        print(f"{branch_path}| Base case reach j == len(B): {j} == {len(B)}\n")
        ed[i][j] = len(A) - i  # Remaining characters in A need to be deleted
        print(f"{branch_path}|      Base case ed[{i}][{j}]: Delete remaining A characters, {len(A)}(len(A)) - {i}(i): {ed[i][j]}\n")
        return ed[i][j]

    # Recursive Steps
    if A[i] == B[j]:  # If equal
        print(f"{branch_path}|      Characters match: A[i] == B[j] == {A[i]}\n")
        answer = EditDistance(i+1, j+1, depth + 1, branch + "|      ")
    else:
        print(f"{branch_path}|      Characters differ: A[i] == {A[i]}, B[j] == {B[j]}\n")
        # Remove A[i], then compare A[i+1] with B[j]
        print(f"{branch_path}|      Option 1: **DELETE** A[i] ({A[i]}) <-- (A[i] will increase next: +1)\n")
        delete = 1 + EditDistance(i+1, j, depth + 1, branch + "|      ")
        
        # Add B[j], then compare A[i] with B[j+1]
        print(f"{branch_path}|      Option 2: **INSERT** B[j] ({B[j]}) <-- (B[j] will increase next: +1) \n")
        insert = 1 + EditDistance(i, j+1, depth + 1, branch + "|      ")
        
        # Change A[i] to B[j], then compare A[i+1] with B[j+1]
        print(f"{branch_path}|      Option 3: **SUBSTITUTE** A[i] ({A[i]}) with B[j] ({B[j]})\n")
        substitute = 1 + EditDistance(i+1, j+1, depth + 1, branch + "|      ")
        
        answer = min(delete, insert, substitute)
        print(f"{branch_path}|      Result: min(delete={delete}, insert={insert}, substitute={substitute}) = {answer}\n")

    ed[i][j] = answer
    print(f"{branch_path}|      STORING/MEMOZING value: ed[{i}][{j}] = {answer}\n")
    return answer

st = time.process_time()
print("Edit Distance Calculation Tree:\n")
result = EditDistance(0, 0)
print(f"\nEdit Distance: {result}")
et = time.process_time()
print(f"Running Time: {et-st:.5f} seconds")

```

### Matrix Visualization

```python
import time
import sys
sys.setrecursionlimit(10000)

# Sample input strings
A = "FOOD"
B = "MONEY"

# Memoization Table
# 2D list initialized to -1
# To store intermediate results
ed = [[-1 for i in range(len(B)+1)] for j in range(len(A)+1)]

def EditDistance(i, j, depth=0, branch=""):
    global A, B, ed

    # Define connectors
    indent = " " * 8
    branch_connector = "|-- " if depth > 0 else ""
    branch_path = branch.replace("|-- ", "|      ") if depth > 0 else ""
    print(f"{branch_path}{branch_connector}EditDistance(i={i}, j={j})")

    if ed[i][j] != -1:  # return the stored value to avoid re-computation
        print(f"{branch_path}|      Returning memoized value: {ed[i][j]}\n")
        return ed[i][j]

    # Base Case
    if i == len(A):
        print(f"{branch_path}| Base case reach i == len(A): {i} == {len(A)}\n")
        ed[i][j] = len(B) - j  # Remaining characters in B need to be inserted
        print(f"{branch_path}|      Base case ed[{i}][{j}]: Insert remaining B characters , {len(B)}(len(B)) - {j}(j): {ed[i][j]}\n")
        return ed[i][j]
    elif j == len(B):
        print(f"{branch_path}| Base case reach j == len(B): {j} == {len(B)}\n")
        ed[i][j] = len(A) - i  # Remaining characters in A need to be deleted
        print(f"{branch_path}|      Base case ed[{i}][{j}]: Delete remaining A characters, {len(A)}(len(A)) - {i}(i): {ed[i][j]}\n")
        return ed[i][j]

    # Recursive Steps
    if A[i] == B[j]:  # If equal
        print(f"{branch_path}|      Characters match: A[i] == B[j] == {A[i]}\n")
        answer = EditDistance(i+1, j+1, depth + 1, branch + "|      ")
    else:
        print(f"{branch_path}|      Characters differ: A[i] == {A[i]}, B[j] == {B[j]}\n")
        # Remove A[i], then compare A[i+1] with B[j]
        print(f"{branch_path}|      Option 1: **DELETE** A[i] ({A[i]}) <-- (A[i] will increase next: +1)\n")
        delete = 1 + EditDistance(i+1, j, depth + 1, branch + "|      ")
        
        # Add B[j], then compare A[i] with B[j+1]
        print(f"{branch_path}|      Option 2: **INSERT** B[j] ({B[j]}) <-- (B[j] will increase next: +1) \n")
        insert = 1 + EditDistance(i, j+1, depth + 1, branch + "|      ")
        
        # Change A[i] to B[j], then compare A[i+1] with B[j+1]
        print(f"{branch_path}|      Option 3: **SUBSTITUTE** A[i] ({A[i]}) with B[j] ({B[j]})\n")
        substitute = 1 + EditDistance(i+1, j+1, depth + 1, branch + "|      ")
        
        answer = min(delete, insert, substitute)
        print(f"{branch_path}|      Result: min(delete={delete}, insert={insert}, substitute={substitute}) = {answer}\n")

    ed[i][j] = answer
    print(f"{branch_path}|      STORING/MEMOZING value: ed[{i}][{j}] = {answer}\n")
    return answer

st = time.process_time()
print("Edit Distance Calculation Tree:\n")
result = EditDistance(0, 0)
print(f"\nEdit Distance: {result}")
et = time.process_time()
print(f"Running Time: {et-st:.5f} seconds")

```

### Worksheet(6) Answer

### Question 1

**What is the beginning state?**

The beginning state is when both strings are at the start, meaning no characters have been processed yet. Thus, the initial indices are:

- i=0
- j=0

### Question 2

If A runs out, but B has not yet, in other words, i == len(A), but j < len(B), what is the additional edit distance required to complete the transformation?

If A runs out, we need to insert the remaining characters of B into A. The additional edit distance required will be the number of remaining characters in BBB, which is:
len(B) - j

### Question 3

**If B runs out, but A has not yet, what is the additional edit distance required to complete the transformation?**

If B runs out, we need to delete the remaining characters in A to match B. The additional edit distance required will be the number of remaining characters in A, which is:
len(A) - i 

### Question 4

**Using the concepts obtained from step 1 to 4 above, write a recursive brute-force solution for this problem.**

Here's a brute-force recursive solution without memoization:

```python
pythonCopy code
def edit_distance_recursive(A, B, i, j):
    # If we reach the end of A, insert all remaining characters of B
    if i == len(A):
        return len(B) - j

    # If we reach the end of B, delete all remaining characters of A
    if j == len(B):
        return len(A) - i

    # If characters are the same, move to the next characters
    if A[i] == B[j]:
        return edit_distance_recursive(A, B, i + 1, j + 1)

    # If characters are different, consider all operations and take the minimum
    insert_op = 1 + edit_distance_recursive(A, B, i, j + 1)    # Insert B[j] in front of A[i]
    delete_op = 1 + edit_distance_recursive(A, B, i + 1, j)    # Delete A[i]
    replace_op = 1 + edit_distance_recursive(A, B, i + 1, j + 1) # Replace A[i] with B[j]

    return min(insert_op, delete_op, replace_op)

# Example usage
A = "FOOD"
B = "MONEY"
print("Edit Distance:", edit_distance_recursive(A, B, 0, 0))

```

### Question 5

**Given that a string can be up to 1000 letters long, improve the brute-force solution so that the program will finish in no more than 2.5 seconds (CPU processing time).**

To handle longer strings efficiently, we use memoization to store previously computed results and avoid redundant calculations. Here’s how to do it:

```python
pythonCopy code
def edit_distance_memoized(A, B):
    memo = {}

    def helper(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == len(A):
            result = len(B) - j
        elif j == len(B):
            result = len(A) - i
        elif A[i] == B[j]:
            result = helper(i + 1, j + 1)
        else:
            insert_op = 1 + helper(i, j + 1)
            delete_op = 1 + helper(i + 1, j)
            replace_op = 1 + helper(i + 1, j + 1)
            result = min(insert_op, delete_op, replace_op)

        memo[(i, j)] = result
        return result

    return helper(0, 0)

# Example usage
A = "FOOD"
B = "MONEY"
print("Edit Distance:", edit_distance_memoized(A, B))

```

### Question 6

**Use the concepts obtained from step 1 to 4 above in write a recursive brute-force solution for this problem. The zipped test case file is downloadable from Class Materials.**

Since the test case file is not provided here, you can use the above recursive memoized solution as a template and test it with different strings from your test cases.

### ELI10

Imagine you have two strings of letters. You want to change the first string to become exactly like the second one. You can do this by:

1. Adding a letter.
2. Removing a letter.
3. Changing one letter to another.

To find out the fewest changes needed, we use a method that tries every possibility but remembers the results of each step, so we don't have to do the same work twice. This makes the process faster.

### Key Concepts

1. **Recursion**:
    - The function calls itself with smaller problems until it reaches a simple case it can solve directly.
2. **Memoization**:
    - Storing results of expensive function calls and reusing the stored results when the same inputs occur again.
3. **Dynamic Programming**:
    - Breaking down a problem into simpler sub-problems, solving each sub-problem just once, and storing their solutions.

### Dynamic Programming for Minimum Coin Change

### Memoization Code

```python
import sys
import time 
sys.setrecursionlimit(10001)

# Input coin denominations and the target value
coin = list(map(int, input().split()))
V = int(input())

# Initialize call and memoization lists
call = [0] * (V + 1)
mm = [-1] * (V + 1)

# Define the recursive function with memoization
def mincoin(v):
    global call, mm, coin

    if mm[v] == -1:  # If value not already computed
        call[v] += 1  # Increment the call count for this value

        if v == 0:
            mm[v] = 0  # Base case: No coins needed for value 0
        else:
            minc = float('inf')  # Initialize minimum coins as infinity
            for c in coin:
                if c <= v:  # If coin can be used to make value v
                    minc = min(minc, 1 + mincoin(v - c))  # Recursively compute minimum coins
            mm[v] = minc  # Store the computed result in the memoization list

    return mm[v]  # Return the memoized result

# Measure execution time
st = time.process_time()
print(mincoin(V))  # Print the minimum number of coins needed for value V
print(call[V])  # Print the number of calls made for value V
et = time.process_time()
print(f"Running Time: {et - st:.10f} seconds")

```

### Tree Visualization For Memoized Code

```python
import sys
import time

sys.setrecursionlimit(10001)

# Input coin denominations and the target value
coin = list(map(int, input().split()))
V = int(input())

# Initialize call and memoization lists
call = [0] * (V + 1)
mm = [-1] * (V + 1)

# Function to print the tree structure
def print_tree(level, message):
    indent = "    " * level
    print(f"{indent}{message}")

# Define the recursive function with memoization and tree visualization
def mincoin(v, level=0):
    global call, mm, coin

    if mm[v] == -1:  # If value not already computed
        call[v] += 1  # Increment the call count for this value
        print_tree(level, f"mincoin({v}) called")
        
        if v == 0:
            mm[v] = 0  # Base case: No coins needed for value 0
            print_tree(level, f"Base case: mincoin({v}) = 0")
        else:
            minc = float('inf')  # Initialize minimum coins as infinity
            for c in coin:
                if c <= v:  # If coin can be used to make value v
                    print_tree(level, f"Trying coin {c} for value {v}")
                    current = 1 + mincoin(v - c, level + 1)  # Recursively compute minimum coins
                    minc = min(minc, current)
                    print_tree(level + 1, f"mincoin({v} - {c}) = {current - 1}")
                    print_tree(level + 1, f"Total coins if using coin {c}: {current}")
            mm[v] = minc  # Store the computed result in the memoization list
            print_tree(level, f"Result: mincoin({v}) = {mm[v]}")

    else:
        print_tree(level, f"Returning memoized value: mincoin({v}) = {mm[v]}")

    return mm[v]  # Return the memoized result

# Measure execution time
st = time.process_time()
print(f"Minimum coins required: {mincoin(V)}")  # Print the minimum number of coins needed for value V
print(f"Number of calls for value {V}: {call[V]}")  # Print the number of calls made for value V
et = time.process_time()
print(f"Running Time: {et - st:.10f} seconds")

```

### Dynamic Code

```python
import sys
import time 

sys.setrecursionlimit(10000)

def min_coin():
    coin_denominator = list(map(int, input().split()))
    amount_of_change = int(input())
    dp = [[float("inf")] * (amount_of_change + 1) for _ in range(len(coin_denominator))]

    def calculate():
        for i in range(len(coin_denominator)):
            dp[i][0] = 0  # 0 coins are needed to make 0 amount
            for j in range(1, amount_of_change + 1):
                if coin_denominator[i] <= j:
                    dp[i][j] = min(dp[i][j], 1 + dp[i][j - coin_denominator[i]])
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j])

        return dp[len(coin_denominator) - 1][amount_of_change]

    return calculate()

st = time.process_time()
print(min_coin())
et = time.process_time()
print(f"Running Time: {et - st:.10f} seconds")

```

### Dynamic Code Tree Visualization

```python
import sys
import time

sys.setrecursionlimit(10000)

def min_coin():
    coin_denominator = [2, 3, 5, 11]
    amount_of_change = 30
    dp = [[float("inf")] * (amount_of_change + 1) for _ in range(len(coin_denominator))] 
    #dp represent the minimum number of coins needed to make the amount of change for each coin index

    def print_tree(level, message):
        indent = "    " * level
        print(f"{indent}{message}")

    def calculate():
        for i in range(len(coin_denominator)): # i represents the coin index
            print_tree(0, f'for coin index i = {i}')
            dp[i][0] = 0  # 0 coins are needed to make 0 amount
            print_tree(0, f'dp[{i}][0] = 0 <-- # 0 coins are needed to make 0 amount')

            for j in range(1, amount_of_change + 1): # j represents the amount of change
                print_tree(0, f'for amount of change j = {j}')

                if coin_denominator[i] <= j: # If the coin value is less than or equal to the amount of change
                    print_tree(j, f'Because coin_denominator[{i}] = {coin_denominator[i]} <= {j}')

                    if dp[i][j] > 1 + dp[i][j - coin_denominator[i]]: # If the current value is greater than the value with the current coin
                        print_tree(j, f'Because dp[{i}][{j}] > 1 + dp[{i}][{j - coin_denominator[i]}]') # The reason for +1 is because we are using a coin to make the amount of change j 

                    dp[i][j] = min(dp[i][j], 1 + dp[i][j - coin_denominator[i]])  # Recursively compute minimum coins
                print_tree(j, f'dp[{i}][{j}] = {dp[i][j]}')

#############################################

                if i > 0: # If the coin index is greater than 0
                    print_tree(j, f'Because coin_denominator[{i}] = {coin_denominator[i]} > {j}') 

                    if dp[i][j] > dp[i - 1][j]: # If the current value is greater than the value with the previous coin
                        print_tree(j, f'Because dp[{i}][{j}] > dp[{i - 1}][{j}]')

                    dp[i][j] = min(dp[i][j], dp[i - 1][j])  # Recursively compute minimum coins
                print_tree(j, f'dp[{i}][{j}] = {dp[i][j]}')

        print("DP Table:")
        for i in range(len(coin_denominator)):
            print(dp[i])
        return dp[len(coin_denominator) - 1][amount_of_change]

    return calculate()

st = time.process_time()
print("Minimum coins required:", min_coin())
et = time.process_time()
print(f"Running Time: {et - st:.10f} seconds")

```

### Dynamic Concept

### Concept

The coin change problem is a classic problem where the goal is to determine the minimum number of coins required to make a given amount of change using a set of given coin denominations.

### Algorithm and Approach

1. **Initialization**:
    - **Coin Denominations and Amount of Change**: The algorithm starts by taking input for the coin denominations and the amount of change needed.
    - **DP Table**: A 2D list `dp` is initialized with dimensions `[len(coin_denominator)][amount_of_change + 1]`. Each entry `dp[i][j]` represents the minimum number of coins needed to make an amount `j` using the first `i+1` coin denominations.
    - **Infinity Initialization**: All entries of the DP table are initially set to infinity (`float("inf")`) to represent that the amount cannot be made with the current set of coins initially.
2. **Base Case**:
    - **Zero Amount**: The base case is that 0 coins are needed to make an amount of 0. Therefore, for all coin denominations, `dp[i][0]` is set to 0.
3. **DP Table Calculation**:
    - The algorithm iterates through each coin denomination `i` and for each denomination, iterates through each amount `j` from 1 to `amount_of_change`.
    - **Using the Current Coin**:
        - If the current coin denomination `coin_denominator[i]` can be used to make the amount `j` (i.e., `coin_denominator[i] <= j`), then the algorithm checks if using the current coin results in a fewer number of coins. This is done by the formula `1 + dp[i][j - coin_denominator[i]]`.
        - The value `1 + dp[i][j - coin_denominator[i]]` represents using one more coin (the current coin) plus the minimum number of coins needed to make the remaining amount (`j - coin_denominator[i]`).
        - The algorithm updates `dp[i][j]` with the minimum of its current value and this computed value.
    - **Not Using the Current Coin**:
        - If the current coin is not used, then the minimum number of coins needed to make the amount `j` is simply the same as the minimum number of coins needed using the previous set of coins (`dp[i - 1][j]`).
4. **Result**:
    - The final result is found in `dp[len(coin_denominator) - 1][amount_of_change]`, which represents the minimum number of coins needed to make the `amount_of_change` using all given coin denominations.
    
    ```python
    import sys
    sys.setrecursionlimit(10000)
    
    def min_coin():
        coin_denominator = list(map(int, input().split()))
        amount_of_change = int(input())
        dp = [[float("inf")] * (amount_of_change + 1) for _ in range(len(coin_denominator))]
    
        def calculate():
            for i in range(len(coin_denominator)):
                dp[i][0] = 0  # 0 coins are needed to make 0 amount
                for j in range(1, amount_of_change + 1):
                    if coin_denominator[i] <= j:
                        dp[i][j] = min(dp[i][j], 1 + dp[i][j - coin_denominator[i]])
                    if i > 0:
                        dp[i][j] = min(dp[i][j], dp[i - 1][j])
    
            return dp[len(coin_denominator) - 1][amount_of_change]
    
        return calculate()
    
    print(min_coin())
    
    ```
    
    - **Line 1-2**: Importing the `sys` module and setting the recursion limit (though not necessary for this non-recursive DP approach).
    - **Function `min_coin`**:
        - **Line 6**: Takes the coin denominations as input.
        - **Line 7**: Takes the amount of change needed as input.
        - **Line 8**: Initializes the DP table with `float("inf")` values.
    - **Function `calculate`**:
        - **Line 11-12**: Initializes the base case where 0 coins are needed to make 0 amount.
        - **Line 13-20**: Fills the DP table by iterating through each coin denomination and each amount. It updates the DP table based on whether the current coin is used or not.
        - **Line 22**: Returns the result from the DP table.
    - **Line 25**: Returns the result of the `calculate` function.
    - **Line 27**: Prints the result of the `min_coin` function.
    
    - This dynamic programming approach ensures that the solution is computed efficiently by breaking down the problem into smaller subproblems and storing the results of these subproblems to avoid redundant calculations.

### Worksheet Answer

Let's address the questions one by one:

1. Given that v1≥v2:

### 1.1 Which recursive call, to `mincoin(v1)` or to `mincoin(v2)`, is made first?

- **Answer**: The recursive call to `mincoin(v2)` is made first. In the process of calculating `mincoin(v1)`, the function might need to compute the minimum coins for smaller values first, including `v2`. Since `v2` is less than or equal to `v1`, the recursive call to `mincoin(v2)` will be encountered and executed before completing the call to `mincoin(v1)`.

### 1.2 Which recursive function, `mincoin(v1)` or `mincoin(v2)`, returns first?

- **Answer**: The recursive function `mincoin(v2)` returns first. As the recursion progresses, `mincoin(v2)` will complete its computation and return a result before `mincoin(v1)`, because `mincoin(v1)` might depend on the result of `mincoin(v2)`.

### 1.3 Which mm’s entry, `mm[v1]` or `mm[v2]`, obtains its final value first?

- **Answer**: The mm’s entry `mm[v2]` obtains its final value first. Since the computation of `mincoin(v1)` may require the result of `mincoin(v2)`, the value for `mm[v2]` will be computed and finalized before `mm[v1]`.

### Explanation

When dealing with the `mincoin` function, the algorithm relies on solving smaller subproblems first. If we have to compute the minimum coins for a larger value, we first need to compute the minimum coins for all possible smaller values that sum up to that larger value. This results in a bottom-up approach in which the function resolves and finalizes smaller values (like `v2`) before larger ones (like `v1`).

According to the explanation provided:

- If the items in the memoization array `mm` are computed in a certain order, such that smaller values are resolved first, the function call `mincoin(v-c)` can always retrieve values from the pre-computed entries in `mm`. This avoids redundant recursive calls and optimizes the computation, effectively eliminating long chains of recursive calls. This is the essence of dynamic programming, where subproblem results are stored and reused to build up the solution to the larger problem.

### Memoization Vs Dynamic

### Memoization:

1. **Top-Down Approach**:
    - It starts with the main problem and breaks it down into smaller subproblems.
    - Uses recursion to solve subproblems and caches the results.
2. **Cache Use**:
    - Stores intermediate results in a cache (usually a dictionary or list) to avoid redundant calculations.
3. **Call Overhead**:
    - Involves function call overhead due to recursion.
    - Can have issues with stack overflow if the recursion depth is too deep.

### Dynamic Programming (DP):

1. **Bottom-Up Approach**:
    - It starts by solving the smallest subproblems and combines their results to solve larger subproblems.
    - Iteratively fills a table to store results of subproblems.
2. **Iterative Computation**:
    - Avoids the overhead of recursive calls.
    - More straightforward control flow as it iterates through possible solutions.
3. **Space Efficiency**:
    - Typically uses a table (2D array) to store results, which can be more space-efficient for certain problems.

### Speed Comparison:

1. **Overhead**:
    - Memoization involves recursive calls, which add function call overhead and can be slower due to the deeper recursion stack.
    - DP avoids recursion, reducing the overhead associated with function calls.
2. **Computation**:
    - Both methods generally compute the same number of subproblems, but the DP approach can often be faster due to its iterative nature.
3. **Practical Differences**:
    - Memoization is often simpler to implement and can be more intuitive for problems naturally expressed in a recursive manner.
    - DP, being iterative, is typically faster due to less overhead from function calls and better space optimization.

### Example Comparison for Minimum Coin Change:

### Memoization:

```python
pythonCopy code
def min_coin_memo(coin, amount):
    memo = [-1] * (amount + 1)
    memo[0] = 0

    def dp(n):
        if memo[n] != -1:
            return memo[n]
        min_count = float('inf')
        for c in coin:
            if n >= c:
                min_count = min(min_count, 1 + dp(n - c))
        memo[n] = min_count
        return memo[n]

    return dp(amount)

```

### Dynamic Programming:

```python
pythonCopy code
def min_coin_dp(coin, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for c in coin:
            if i >= c:
                dp[i] = min(dp[i], dp[i - c] + 1)
    return dp[amount]

```

### Conclusion:

In practice, **dynamic programming (DP)** is often faster than memoization for large problems because it avoids the overhead associated with recursive function calls. Additionally, DP can be more space-efficient and avoids issues with recursion limits. However, memoization can be easier to implement and more intuitive for problems that naturally fit a recursive solution. Both techniques, when used correctly, ensure that the same subproblem is not solved multiple times, thus improving efficiency over naive recursive solutions.