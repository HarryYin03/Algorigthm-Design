import sys

# Function to calculate the number of harvesters using memoization
def number_of_harvesters(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    if n == 2:
        return 2
    memo[n] = number_of_harvesters(n-1, memo) + number_of_harvesters(n-2, memo)
    return memo[n]

# Main function to read input and print the result
def main():
    input = sys.stdin.read
    try:
        n = int(input().strip())
        print(number_of_harvesters(n))
    except Exception as e:
        print("Error:", e)

# Function to validate the results using predefined test cases
def run_tests():
    test_cases = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (28, 514229),
        (97, 135301852344706746049),
    ]

    for n, expected in test_cases:
        result = number_of_harvesters(n)
        print(f"Running test case n={n}")
        print(f"Expected: {expected}, Got: {result}")
        assert result == expected, f'Test failed for n={n}. Expected {expected}, got {result}'
        print(f'Test passed for n={n}. Output: {result}')

if __name__ == "__main__":
    mode = input("Enter 'test' to run tests or 'run' to enter generation number: ").strip().lower()
    if mode == 'test':
        run_tests()
    else:
        main()
