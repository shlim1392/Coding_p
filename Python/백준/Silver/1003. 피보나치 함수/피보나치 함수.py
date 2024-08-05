def fibonacci_counts(n):
    dp_zeros = [0] * (n + 1)
    dp_ones = [0] * (n + 1)
    
    dp_zeros[0] = 1
    dp_ones[0] = 0
    
    if n > 0:
        dp_zeros[1] = 0
        dp_ones[1] = 1
    
    for i in range(2, n + 1):
        dp_zeros[i] = dp_zeros[i - 1] + dp_zeros[i - 2]
        dp_ones[i] = dp_ones[i - 1] + dp_ones[i - 2]
    
    return dp_zeros[n], dp_ones[n]

T = int(input())
test_cases = [int(input()) for _ in range(T)]

for n in test_cases:
    zeros, ones = fibonacci_counts(n)
    print(zeros, ones)
