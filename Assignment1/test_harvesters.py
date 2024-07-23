import subprocess

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
            output = int(output)
            assert output == expected, f'Test failed for n={n}. Expected {expected}, got {output}'
            print(f'Test passed for n={n}. Output: {output}')
        else:
            print(f"Test failed for n={n}. No output received.")

if __name__ == "__main__":
    test_harvesters()
