import sys
import subprocess

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

# Test function to validate the results
def test_harvesters():
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
        result = subprocess.run(
            ['python3', 'harvesters.py'],
            input=str(n) + '\n',
            text=True,
            capture_output=True
        )
        output = result.stdout.strip()
        print(f"Running test case n={n}")
        print(f"Expected: {expected}, Got: {output}")
        if output:
            try:
                output = int(output)
                assert output == expected, f'Test failed for n={n}. Expected {expected}, got {output}'
                print(f'Test passed for n={n}. Output: {output}')
            except ValueError as ve:
                print(f"Test failed for n={n}. Could not convert output to int: {output}")
        else:
            print(f"Test failed for n={n}. No output received.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test_harvesters()
    else:
        main()
