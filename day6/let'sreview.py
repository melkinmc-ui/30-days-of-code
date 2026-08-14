# Read the number of test cases
num_test_cases = int(input())

# Process each test case
for _ in range(num_test_cases):
    s = input()
    
    # Get characters at even and odd indexes using slicing
    even_chars = s[::2]
    odd_chars = s[1::2]
    
    # Print both results separated by a space
    print(f"{even_chars} {odd_chars}")
