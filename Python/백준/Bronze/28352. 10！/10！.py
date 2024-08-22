def solution():
    import math
    N = int(input())
    factorial_N = math.factorial(N)
    one_week_seconds = 7 * 24 * 60 * 60
    weeks = factorial_N // one_week_seconds
    print(weeks)

solution()